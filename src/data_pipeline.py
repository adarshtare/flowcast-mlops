import pandas as pd
import os
from src.features import create_features

# Paths
RAW_DATA_PATH = "data/raw/traffic.csv"
PROCESSED_DATA_PATH = "data/processed/traffic_processed.csv"


def load_data(path):
    try:
        df = pd.read_csv(path)
        print("Data loaded successfully")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None


def preprocess_data(df):
    try:
        df = df.copy()

        # Convert date_time column
        df["date_time"] = pd.to_datetime(df["date_time"])

        # Extract time features
        df["hour"] = df["date_time"].dt.hour
        df["day_of_week"] = df["date_time"].dt.dayofweek

        # Handle missing values
        df = df.ffill()

        print("Preprocessing done")
        return df

    except Exception as e:
        print(f"Error in preprocessing: {e}")
        return None


def save_data(df, path):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        df.to_csv(path, index=False)
        print(f"Data saved at {path}")
    except Exception as e:
        print(f"Error saving data: {e}")


def run_pipeline():
    df = load_data(RAW_DATA_PATH)

    if df is not None:
        df_processed = preprocess_data(df)

        if df_processed is not None:
            df_features = create_features(df_processed)   
            save_data(df_features, PROCESSED_DATA_PATH)


if __name__ == "__main__":
    run_pipeline()