from .data_loader import DataLoader

# python -m src.data_cleaner

class DataCleaner:
    """
    
    """
    def __init__(self):
        """
        
        """
    
    def find_missing_values(self):
        """
        Finds and shows missing values (NaN) in DataFrame.
        """


    def remove_duplicates(self, dfs):
        """
        
        """
        dfs_cleaned = {}
        for data_name, df in dfs.items():
            if "timestamp" not in df.columns:
                raise ValueError(f"'timestamp'-column missing in {data_name}")
            df_cleaned = df.drop_duplicates(subset=["timestamp"])
            dfs_cleaned[data_name] = df_cleaned
        return dfs_cleaned

    def convert_to_datetime(self):
        """
        
        """

    def convert_to_float(self):
        """
        
        """

    def fill_missing_with_forward(self):
        """
        
        """
    
    def fill_missing_with_backward(self):
        """
        
        """

    def fill_missing_with_interpolation(self):
        """
        
        """

    def fill_missing_with_mean(self):
        """
        
        """

    def fill_missing_with_median(self):
        """
        
        """

    def correct_extrem_peaks(self):
        """

        """
    
    def normalise_data(self):
        """
        
        """

    def standardise_data(self):
        """
        
        """

    def sort_data(self):
        """
        
        """
