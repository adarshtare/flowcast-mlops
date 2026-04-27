# User Manual — FlowCast Traffic Predictor

# 1. Introduction
FlowCast predicts traffic volume using weather and time conditions through an interactive web application.

This application is designed for non-technical users.

---

# 2. System Access

Start application:

docker-compose up

Open browser:

Frontend:
http://localhost:8501

API documentation:
http://localhost:8001/docs

---

# 3. How To Use

Step 1
Open FlowCast web interface.

---

Step 2
Enter input values:

- Temperature
- Cloud cover
- Rain
- Snow
- Hour
- Day of week
- Month
- Day
- Weather condition

Example:

Temperature: 290

Clouds: 75

Hour: 8

Weather:
Clouds

---

Step 3
Click:

Predict Traffic

---

Step 4
View prediction result:

Predicted Traffic Volume

Example:
4832

Traffic category:

- Low Traffic
- Moderate Traffic
- Heavy Traffic

---

# 4. Understanding Output

Traffic volume < 2000
Low Traffic

Traffic volume 2000–4000
Moderate Traffic

Traffic volume > 4000
Heavy Traffic

---

# 5. MLOps Pipeline Dashboard

Open:

MLOps Pipeline Dashboard tab

View:

- Data Pipeline
- Model Pipeline
- Experiment Tracking
- Deployment Architecture
- Monitoring Metrics

---

# 6. Health Checks

System health:

http://localhost:8001/health

Readiness:

http://localhost:8001/ready

Metrics:

http://localhost:8001/metrics

---

# 7. Troubleshooting

Problem:
Prediction not returned

Action:
Verify API container running

---

Problem:
Frontend unavailable

Action:
Restart docker compose

docker-compose down
docker-compose up

---

# 8. User Workflow

Launch App

↓

Enter Conditions

↓

Predict Traffic

↓

Interpret Traffic Level

---

# 9. Intended Users

- Traffic planners
- Commuters
- Students
- Demonstration users

---

# 10. Support
For issues:
Restart application containers and verify API health endpoint.