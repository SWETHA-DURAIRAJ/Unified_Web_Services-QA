# ReqRes Load Test Report

## Tool Used
Postman Performance Testing

## API Details
- Base URL: https://reqres.in/api
- Endpoint: /users?page=1
- Method: GET

---

## Load Configuration
- Virtual Users: 50
- Duration: 2 minutes

---

## Performance Metrics

| Metric | Value |
|---|---|
| Total Requests Sent | 4,427 |
| Requests per Second | 34.88 req/s |
| Average Response Time | 146 ms |
| Minimum Response Time | 12 ms |
| Maximum Response Time | 5,947 ms |
| P90 Response Time | 401 ms |
| P95 Response Time | 789 ms |
| P99 Response Time | 1,900 ms |
| Error Rate | 0.00% |

---

## Final Observation

- The API handled 50 concurrent virtual users successfully.
- Total of 4,427 requests were processed during the 2-minute execution.
- Average response time remained low at 146 ms.
- No failed requests or errors were observed.
- Overall API performance was stable under moderate load.
