import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.
    Prints the dimensions of the dataset.
    """
    try:
        if not path.endswith('.csv'):
            raise ValueError("The file must be a CSV.")
        if not pd.io.common.file_exists(path):
            raise FileNotFoundError("The file does not exist.")
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except (ValueError, FileNotFoundError) as e:
        print(f"An error occurred: {e}")
        return None
