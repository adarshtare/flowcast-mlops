import pandas as pd
import numpy as np


def create_features(df):
    df = df.copy()

    # ===== SORT =====
    df = df.sort_values("date_time")

    # ===== TIME FEATURES =====
    df["hour"] = df["date_time"].dt.hour
    df["day_of_week"] = df["date_time"].dt.dayofweek
    df["month"] = df["date_time"].dt.month
    df["day"] = df["date_time"].dt.day

    # Cyclical encoding (VERY IMPORTANT)
    df["hour_sin"] = np.sin(2 * np.pi * df["hour"] / 24)
    df["hour_cos"] = np.cos(2 * np.pi * df["hour"] / 24)

    df["dow_sin"] = np.sin(2 * np.pi * df["day_of_week"] / 7)
    df["dow_cos"] = np.cos(2 * np.pi * df["day_of_week"] / 7)

    df["month_sin"] = np.sin(2 * np.pi * df["month"] / 12)
    df["month_cos"] = np.cos(2 * np.pi * df["month"] / 12)

    # ===== FLAGS =====
    df["is_weekend"] = df["day_of_week"].isin([5, 6]).astype(int)
    df["is_rush_hour"] = df["hour"].isin([7, 8, 9, 16, 17, 18]).astype(int)

    # ===== ROLLING FEATURES =====
    df["rolling_mean_6"] = df["traffic_volume"].rolling(6).mean()
    df["rolling_std_6"] = df["traffic_volume"].rolling(6).std()

    df["rolling_mean_24"] = df["traffic_volume"].rolling(24).mean()
    df["rolling_std_24"] = df["traffic_volume"].rolling(24).std()

    # ===== LAG FEATURES =====
    df["lag_1"] = df["traffic_volume"].shift(1)
    df["lag_24"] = df["traffic_volume"].shift(24)
    df["lag_168"] = df["traffic_volume"].shift(168)

    # ===== CATEGORICAL =====
    df = pd.get_dummies(df, columns=["weather_main", "holiday"], drop_first=True)

    # Clean column names
    df.columns = df.columns.str.replace(" ", "_")

    # Drop NaN rows
    df = df.dropna()

    return df