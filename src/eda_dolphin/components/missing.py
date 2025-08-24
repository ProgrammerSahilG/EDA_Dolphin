import pandas as pd 

def check_missing(df: pd.DataFrame, show_all: bool = False) -> pd.DataFrame:
    """
    Check for missing values in the DataFrame and provide detailed statistics.

    Parameters:
    df (pd.DataFrame): The input DataFrame to check for missing values.
    show_all (bool): If True, show all columns including those with no missing values.
                    If False, show only columns with missing values. Default is False.

    Returns:
    pd.DataFrame: A DataFrame containing columns with their missing values statistics.
    """
    # Calculate missing values count and percentage
    missing_count = df.isnull().sum()
    missing_percentage = (df.isnull().sum() / len(df)) * 100
    
    # Get data types for each column
    dtypes = df.dtypes
    
    # Create a comprehensive DataFrame
    missing_df = pd.DataFrame({
        'Column': missing_count.index,
        'Data_Type': dtypes.values,
        'Total_Values': len(df),
        'Missing_Count': missing_count.values,
        'Missing_Percentage': missing_percentage.values.round(2)
    })
    
    
    # Sort by missing percentage in descending order
    missing_df = missing_df.sort_values('Missing_Percentage', ascending=False)
    
    return missing_df.reset_index(drop=True)