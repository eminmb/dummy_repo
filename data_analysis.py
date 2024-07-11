import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """
    Load CSV data into a pandas DataFrame.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: Loaded data.
    """
    return pd.read_csv(file_path)

def clean_data(df):
    """
    Clean the data by handling missing values and removing duplicates.
    
    Args:
        df (pd.DataFrame): Input data.
    
    Returns:
        pd.DataFrame: Cleaned data.
    """
    df = df.drop_duplicates()
    df = df.dropna()
    return df

def summary_statistics(df):
    """
    Generate summary statistics for the DataFrame.
    
    Args:
        df (pd.DataFrame): Input data.
    
    Returns:
        pd.DataFrame: Summary statistics.
    """
    return df.describe()

def plot_histogram(df, column, bins=10):
    """
    Plot a histogram of a specified column.
    
    Args:
        df (pd.DataFrame): Input data.
        column (str): Column name for the histogram.
        bins (int): Number of bins for the histogram.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], bins=bins, kde=True)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

def plot_scatter(df, column1, column2):
    """
    Plot a scatter plot between two specified columns.
    
    Args:
        df (pd.DataFrame): Input data.
        column1 (str): First column for the scatter plot.
        column2 (str): Second column for the scatter plot.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=column1, y=column2)
    plt.title(f'Scatter Plot of {column1} vs {column2}')
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.show()

def plot_correlation_matrix(df):
    """
    Plot a correlation matrix heatmap for the DataFrame.
    
    Args:
        df (pd.DataFrame): Input data.
    """
    plt.figure(figsize=(12, 10))
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix Heatmap')
    plt.show()

def save_clean_data(df, file_path):
    """
    Save the cleaned data to a CSV file.
    
    Args:
        df (pd.DataFrame): Cleaned data.
        file_path (str): Path to save the cleaned data.
    """
    df.to_csv(file_path, index=False)
    print(f'Cleaned data saved to {file_path}')

# Example usage
if __name__ == "__main__":
    data_file = 'data.csv'
    clean_file = 'clean_data.csv'

    # Load and clean data
    data = load_data(data_file)
    clean_data = clean_data(data)

    # Summary statistics
    stats = summary_statistics(clean_data)
    print(stats)

    # Plot histograms
    plot_histogram(clean_data, 'column_name1')
    plot_histogram(clean_data, 'column_name2')

    # Plot scatter plots
    plot_scatter(clean_data, 'column_name1', 'column_name2')
    plot_scatter(clean_data, 'column_name3', 'column_name4')

    # Plot correlation matrix
    plot_correlation_matrix(clean_data)

    # Save cleaned data
    save_clean_data(clean_data, clean_file)
