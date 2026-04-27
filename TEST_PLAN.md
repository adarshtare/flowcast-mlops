# Test Plan and Test Report — FlowCast

# 1. Test Objective
Validate correctness, reliability, API behavior, deployment, and user workflow.

---

# 2. Test Scope
Components tested:

- Streamlit frontend
- FastAPI backend
- Model inference
- Docker containers
- Monitoring endpoints
- REST integration

---

# 3. Test Environment

OS:
Ubuntu WSL

Language:
Python 3.11

Containers:
Docker + Docker Compose

Frameworks:
FastAPI
Streamlit
XGBoost

---

# 4. Test Cases

| ID | Test Case | Input | Expected Result | Status |
|----|-----------|-------|----------------|--------|
| TC01 | Health endpoint | GET /health | Healthy response | Pass |
| TC02 | Readiness endpoint | GET /ready | Ready response | Pass |
| TC03 | Prediction API | Valid payload | Traffic prediction returned | Pass |
| TC04 | Invalid request | Missing field | Validation error | Pass |
| TC05 | Metrics endpoint | GET /metrics | Prometheus metrics visible | Pass |
| TC06 | Frontend prediction flow | User submits form | Prediction displayed | Pass |
| TC07 | Docker startup | docker-compose up | Both containers run | Pass |
| TC08 | Model loading | startup | model loads successfully | Pass |

---

# 5. Test Report Summary

Total Test Cases:
8

Passed:
8

Failed:
0

Pass Rate:
100%

---

# 6. Acceptance Criteria

System accepted if:

- All endpoints return expected output
- Prediction works from frontend
- Containers deploy successfully
- Metrics exposed successfully
- No critical runtime errors
- Inference latency below 200 ms

Result:
Acceptance Criteria Met

---

# 7. Negative Testing

Case:
Invalid payload

Example:

{
 "temp":"abc"
}

Expected:
Validation failure

Observed:
Pass

---

# 8. Performance Testing

Inference latency:
~150 ms

Container startup:
~5 seconds

Throughput:
Real-time online prediction

Status:
Pass

---

# 9. Reliability Testing

Repeated prediction requests:
Stable

Container restarts:
Stable

Health probes:
Pass

---

# 10. Defects Encountered and Resolved

Issue:
Feature mismatch during inference

Resolution:
Added missing engineered features

---

Issue:
Container model path failure

Resolution:
Loaded serialized model directly

---

Issue:
Frontend API communication issue

Resolution:
Fixed docker service hostname routing

---

# 11. Conclusion
All defined test cases passed and system meets acceptance criteria.