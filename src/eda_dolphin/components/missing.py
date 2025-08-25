import pandas as pd
import numpy as np
from src.eda_dolphin.logger import logger

def check_missing(df: pd.DataFrame, 
                 columns: str = 'null', 
                 sort_by: str = 'percentage', 
                 ascending: bool = False,
                 include_dtypes: list = None,
                 exclude_dtypes: list = None,
                 threshold: float = None,
                 show_total: bool = True,
                 show_datatype: bool = True,
                 show_summary: bool = False) -> pd.DataFrame:
    """
    Comprehensive function to check for missing values in the DataFrame with detailed statistics.

    Parameters:
    df (pd.DataFrame): The input DataFrame to check for missing values.
    columns (str): Which columns to include. Options: 'all', 'null'. Default 'null'.
    sort_by (str): Column to sort results by. Options: 'column', 'count', 'percentage', 'dtype'. Default 'percentage'.
    ascending (bool): Sort order. Default False (descending).
    include_dtypes (list): List of specific data types to include (e.g., ['int64', 'float64']).
    exclude_dtypes (list): List of specific data types to exclude.
    threshold (float): Only show columns with missing percentage above this threshold (0-100).
    show_total (bool): Whether to show total values column. Default True.
    show_datatype (bool): Whether to show data type column. Default True.
    show_summary (bool): Whether to print a summary of missing values. Default False.

    Returns:
    pd.DataFrame: A DataFrame containing columns with their missing values statistics.
    """
    try:
        # Calculate missing values statistics
        missing_count = df.isnull().sum()
        missing_percentage = (df.isnull().sum() / len(df)) * 100
        non_missing_count = len(df) - missing_count
        
        # Get data types for each column
        dtypes = df.dtypes
        
        # Create a comprehensive DataFrame
        missing_df = pd.DataFrame({
            'Column': missing_count.index,
            'Data_Type': dtypes.values,
            'Total_Values': len(df),
            'Non_Missing_Count': non_missing_count.values,
            'Missing_Count': missing_count.values,
            'Missing_Percentage': missing_percentage.values.round(2)
        })
        
        # Filter columns based on the 'columns' parameter
        if columns == 'null':
            missing_df = missing_df[missing_df['Missing_Count'] > 0]
        
        # Filter by data types
        if include_dtypes:
            missing_df = missing_df[missing_df['Data_Type'].isin(include_dtypes)]
        
        if exclude_dtypes:
            missing_df = missing_df[~missing_df['Data_Type'].isin(exclude_dtypes)]
        
        # Filter by threshold
        if threshold is not None:
            missing_df = missing_df[missing_df['Missing_Percentage'] >= threshold]
        
        # Sort the results
        sort_columns = {
            'column': 'Column',
            'count': 'Missing_Count',
            'percentage': 'Missing_Percentage',
            'dtype': 'Data_Type'
        }
        
        sort_column = sort_columns.get(sort_by.lower(), 'Missing_Percentage')
        missing_df = missing_df.sort_values(sort_column, ascending=ascending)
        
        # Customize output columns
        output_columns = ['Column']
        if show_datatype:
            output_columns.append('Data_Type')
        if show_total:
            output_columns.extend(['Total_Values', 'Non_Missing_Count'])
        output_columns.extend(['Missing_Count', 'Missing_Percentage'])
        
        missing_df = missing_df[output_columns]
        
        # Print summary if requested
        if show_summary:
            print_missing_summary(missing_df, df)
        
        return missing_df.reset_index(drop=True)
        
    except Exception as e:
        logger.error(f"Error in check_missing: {e}")
        raise

def print_missing_summary(missing_df: pd.DataFrame, original_df: pd.DataFrame) -> None:
    """Print a comprehensive summary of missing values."""
    try:
        total_missing = missing_df['Missing_Count'].sum()
        total_cells = len(original_df) * len(original_df.columns)
        overall_missing_percentage = (total_missing / total_cells) * 100
        
        print("=" * 60)
        print("MISSING VALUES SUMMARY")
        print("=" * 60)
        print(f"Total dataset rows: {len(original_df):,}")
        print(f"Total dataset columns: {len(original_df.columns):,}")
        print(f"Total cells: {total_cells:,}")
        print(f"Total missing values: {total_missing:,}")
        print(f"Overall missing percentage: {overall_missing_percentage:.2f}%")
        print(f"Columns with missing values: {len(missing_df):,} out of {len(original_df.columns):,}")
        
        if len(missing_df) > 0:
            print("\nColumns with highest missing percentages:")
            top_missing = missing_df.nlargest(5, 'Missing_Percentage')
            for _, row in top_missing.iterrows():
                print(f"  - {row['Column']}: {row['Missing_Percentage']}%")
        
        print("=" * 60)
    
    except KeyError as e:
        logger.error(f"KeyError in print_missing_summary: Required column not found - {e}")
        print("Error: Required columns not found in the missing DataFrame.")
    
    except Exception as e:
        logger.error(f"Unexpected error in print_missing_summary: {e}")
        print(f"An unexpected error occurred while generating the summary: {e}")

def quick_missing_report(df: pd.DataFrame, top_n: int = 10) -> None:
    """
    Quick missing values report for rapid EDA.
    
    Parameters:
    df (pd.DataFrame): Input DataFrame
    top_n (int): Number of top columns to show. Default 10.
    """
    try:
        missing_df = check_missing(df, columns='null', sort_by='percentage', 
                                  show_total=False, show_datatype=True)
        
        if len(missing_df) == 0:
            print("✅ No missing values found in the dataset!")
            return
        
        print(f"🔍 Missing Values Report (Top {top_n} columns):")
        print("-" * 50)
        
        display_count = min(top_n, len(missing_df))
        
        for _, row in missing_df.head(display_count).iterrows():
            print(f"{row['Column']} ({row['Data_Type']}): {row['Missing_Count']} missing ({row['Missing_Percentage']}%)")
        
        total_missing = missing_df['Missing_Count'].sum()
        print(f"\n📊 Total missing values: {total_missing:,}")
        print(f"🏆 Worst column: {missing_df.iloc[0]['Column']} ({missing_df.iloc[0]['Missing_Percentage']}% missing)")
    
    except Exception as e:
        logger.error(f"Error in quick_missing_report: {e}")
        print(f"An error occurred while generating the quick report: {e}")

def safe_check_missing(df: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    Safe wrapper for check_missing that returns an empty DataFrame on error.
    
    Parameters:
    df (pd.DataFrame): Input DataFrame
    **kwargs: Additional arguments to pass to check_missing
    
    Returns:
    pd.DataFrame: Result DataFrame or empty DataFrame on error
    """
    try:
        return check_missing(df, **kwargs)
    except Exception as e:
        logger.error(f"Error in safe_check_missing: {e}")
        print(f"Error occurred while checking missing values: {e}")
        return pd.DataFrame()

# NEW: Simplified functions that work with just DataFrame
def analyze_missing(df: pd.DataFrame) -> pd.DataFrame:
    """
    Simple analysis of missing values - just pass the DataFrame!
    
    Parameters:
    df (pd.DataFrame): Input DataFrame
    
    Returns:
    pd.DataFrame: Missing values analysis
    """
    return check_missing(df, show_summary=True)

def quick_analysis(df: pd.DataFrame) -> None:
    """
    Quick analysis with visual output - just pass the DataFrame!
    
    Parameters:
    df (pd.DataFrame): Input DataFrame
    """
    quick_missing_report(df)

def comprehensive_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """
    Comprehensive missing values analysis - just pass the DataFrame!
    
    Parameters:
    df (pd.DataFrame): Input DataFrame
    
    Returns:
    pd.DataFrame: Detailed missing values analysis
    """
    result = check_missing(df, columns='all', show_summary=True, show_total=True, show_datatype=True)
    print("\n" + "="*60)
    print("COMPREHENSIVE MISSING VALUES ANALYSIS")
    print("="*60)
    return result

# NEW: One-function solution for all needs
def missing_analysis(df: pd.DataFrame, 
                    mode: str = 'quick',
                    **kwargs) -> pd.DataFrame:
    """
    Unified function for missing values analysis with different modes.
    
    Parameters:
    df (pd.DataFrame): Input DataFrame
    mode (str): Analysis mode - 'quick', 'detailed', 'comprehensive'
    **kwargs: Additional arguments for advanced customization
    
    Returns:
    pd.DataFrame: Analysis results (varies by mode)
    """
    modes = {
        'quick': lambda: quick_missing_report(df),
        'detailed': lambda: check_missing(df, show_summary=True, **kwargs),
        'comprehensive': lambda: check_missing(df, columns='all', show_summary=True, 
                                              show_total=True, show_datatype=True, **kwargs)
    }
    
    if mode not in modes:
        raise ValueError(f"Mode must be one of: {list(modes.keys())}")
    
    if mode == 'quick':
        modes[mode]()
        return pd.DataFrame()  # quick mode doesn't return DataFrame
    else:
        return modes[mode]()

# NEW: Default export for easy importing
__all__ = [
    'check_missing',
    'print_missing_summary',
    'quick_missing_report',
    'safe_check_missing',
    'analyze_missing',      # Simple one-parameter function
    'quick_analysis',       # Simple one-parameter function
    'comprehensive_analysis', # Simple one-parameter function
    'missing_analysis'      # Unified function
]