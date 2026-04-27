import pandas as pd
from sklearn.metrics import mean_squared_error
import xgboost as xgb
import lightgbm as lgb
import mlflow
import mlflow.xgboost

DATA_PATH = "data/processed/traffic_processed.csv"


def load_data():
    df = pd.read_csv(DATA_PATH)
    df = df.drop(columns=["date_time", "weather_description"], errors="ignore")
    return df


def split_data(df):
    train_size = int(len(df) * 0.8)

    train = df[:train_size]
    test = df[train_size:]

    X_train = train.drop("traffic_volume", axis=1)
    y_train = train["traffic_volume"]

    X_test = test.drop("traffic_volume", axis=1)
    y_test = test["traffic_volume"]

    return X_train, X_test, y_train, y_test


# ----------- XGBOOST (OPTIMIZED) -----------
def train_xgb(X_train, y_train):
    model = xgb.XGBRegressor(
        n_estimators=500,
        max_depth=10,
        learning_rate=0.03,
        subsample=0.85,
        colsample_bytree=0.85,
        gamma=0.1,
        reg_alpha=0.1,
        reg_lambda=1,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)
    return model


# ----------- LIGHTGBM -----------
def train_lgb(X_train, y_train):
    model = lgb.LGBMRegressor(
        n_estimators=500,
        learning_rate=0.03,
        num_leaves=31,
        subsample=0.85,
        colsample_bytree=0.85,
        random_state=42
    )
    model.fit(X_train, y_train)
    return model


def evaluate(model, X_test, y_test):
    preds = model.predict(X_test)
    rmse = mean_squared_error(y_test, preds) ** 0.5
    return rmse


def main():
    df = load_data()
    X_train, X_test, y_train, y_test = split_data(df)

    mlflow.set_experiment("flowcast-traffic")

    # -------- XGBOOST --------
    with mlflow.start_run(run_name="xgboost_final"):
        model = train_xgb(X_train, y_train)
        rmse = evaluate(model, X_test, y_test)

        print(f"XGBoost RMSE: {rmse}")

        mlflow.log_param("model", "xgboost")
        mlflow.log_metric("rmse", rmse)

        mlflow.xgboost.log_model(model, name="model")

    # -------- LIGHTGBM --------
    with mlflow.start_run(run_name="lightgbm_final"):
        model = train_lgb(X_train, y_train)
        rmse = evaluate(model, X_test, y_test)

        print(f"LightGBM RMSE: {rmse}")

        mlflow.log_param("model", "lightgbm")
        mlflow.log_metric("rmse", rmse)


if __name__ == "__main__":
    main()