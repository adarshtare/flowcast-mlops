from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator
import pandas as pd
import xgboost as xgb
import math
import logging

# ---------------------------------
# Structured Logging
# ---------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
logger = logging.getLogger("flowcast_api")


# ---------------------------------
# Load model
# ---------------------------------
logger.info("Loading XGBoost model...")

model = xgb.XGBRegressor()
model.load_model("models/model.ubj")

logger.info("Model loaded successfully")


app = FastAPI(
    title="FlowCast Traffic Predictor",
    version="1.0"
)

# Prometheus metrics endpoint
Instrumentator().instrument(app).expose(app)


# ---------------------------------
# Input Schema
# ---------------------------------
class TrafficInput(BaseModel):
    temp: float
    rain_1h: float
    snow_1h: float
    clouds_all: int
    hour: int
    day_of_week: int
    month: int
    day: int
    weather_main: str


# ---------------------------------
# Health Endpoints
# ---------------------------------
@app.get("/")
def home():
    logger.info("Home endpoint called")
    return {"status": "running"}


@app.get("/health")
def health():
    logger.info("Health endpoint called")
    return {
        "status": "healthy",
        "model_loaded": True
    }


@app.get("/ready")
def ready():
    logger.info("Readiness endpoint called")
    return {"status": "ready"}


# ---------------------------------
# Prediction Endpoint
# ---------------------------------
@app.post("/predict")
def predict(data: TrafficInput):

    try:
        logger.info(
            f"Prediction request received | "
            f"hour={data.hour}, temp={data.temp}, weather={data.weather_main}"
        )

        row = {
            "temp": data.temp,
            "rain_1h": data.rain_1h,
            "snow_1h": data.snow_1h,
            "clouds_all": data.clouds_all,

            "hour": data.hour,
            "day_of_week": data.day_of_week,
            "month": data.month,
            "day": data.day,

            # engineered features
            "is_weekend": int(data.day_of_week in [5,6]),
            "is_rush_hour": int(data.hour in [7,8,9,16,17,18]),

            # lag features
            "lag_1": 3000,
            "lag_24": 3200,
            "lag_168": 3100,

            # rolling stats
            "rolling_mean_6": 3150,
            "rolling_std_6": 150,
            "rolling_mean_24": 3200,
            "rolling_std_24": 200,

            # cyclical hour
            "hour_sin": math.sin(2*math.pi*data.hour/24),
            "hour_cos": math.cos(2*math.pi*data.hour/24),

            # cyclical day-of-week
            "dow_sin": math.sin(2*math.pi*data.day_of_week/7),
            "dow_cos": math.cos(2*math.pi*data.day_of_week/7),

            # cyclical month
            "month_sin": math.sin(2*math.pi*data.month/12),
            "month_cos": math.cos(2*math.pi*data.month/12),
        }

        # ---------------------------------
        # Weather One-Hot Encoding
        # ---------------------------------
        weather_cols = [
            "weather_main_Clouds",
            "weather_main_Drizzle",
            "weather_main_Fog",
            "weather_main_Haze",
            "weather_main_Mist",
            "weather_main_Rain",
            "weather_main_Smoke",
            "weather_main_Snow",
            "weather_main_Squall",
            "weather_main_Thunderstorm"
        ]

        for c in weather_cols:
            row[c] = 0

        chosen = f"weather_main_{data.weather_main}"

        if chosen in row:
            row[chosen] = 1
        else:
            logger.warning(
                f"Unknown weather category '{data.weather_main}', using defaults"
            )


        # ---------------------------------
        # Holiday placeholders
        # ---------------------------------
        holiday_cols = [
            "holiday_Columbus_Day",
            "holiday_Independence_Day",
            "holiday_Labor_Day",
            "holiday_Martin_Luther_King_Jr_Day",
            "holiday_Memorial_Day",
            "holiday_New_Years_Day",
            "holiday_State_Fair",
            "holiday_Thanksgiving_Day",
            "holiday_Veterans_Day",
            "holiday_Washingtons_Birthday"
        ]

        for h in holiday_cols:
            row[h] = 0


        expected_cols = [
            "temp","rain_1h","snow_1h","clouds_all",
            "hour","day_of_week","month","day",

            "hour_sin","hour_cos",
            "dow_sin","dow_cos",
            "month_sin","month_cos",

            "is_weekend","is_rush_hour",

            "rolling_mean_6","rolling_std_6",
            "rolling_mean_24","rolling_std_24",

            "lag_1","lag_24","lag_168",

            "weather_main_Clouds",
            "weather_main_Drizzle",
            "weather_main_Fog",
            "weather_main_Haze",
            "weather_main_Mist",
            "weather_main_Rain",
            "weather_main_Smoke",
            "weather_main_Snow",
            "weather_main_Squall",
            "weather_main_Thunderstorm",

            "holiday_Columbus_Day",
            "holiday_Independence_Day",
            "holiday_Labor_Day",
            "holiday_Martin_Luther_King_Jr_Day",
            "holiday_Memorial_Day",
            "holiday_New_Years_Day",
            "holiday_State_Fair",
            "holiday_Thanksgiving_Day",
            "holiday_Veterans_Day",
            "holiday_Washingtons_Birthday"
        ]

        df = pd.DataFrame([row])

        for c in expected_cols:
            if c not in df.columns:
                df[c] = 0

        df = df[expected_cols]

        pred = model.predict(df)[0]

        logger.info(f"Prediction successful | traffic_volume={int(pred)}")

        return {
            "predicted_traffic_volume": int(pred)
        }

    except Exception as e:
        logger.exception("Inference failed with exception")
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )