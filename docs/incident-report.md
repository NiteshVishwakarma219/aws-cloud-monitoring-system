# Incident Report

## Incident Title

High CPU Utilization on EC2 Monitoring Server

---

# Date

2026-05-23

---

# Severity

Medium

---

# Affected Resource

- EC2 Instance: Monitoring-Server

---

# Incident Description

A simulated CPU overload incident was created to test the monitoring and alerting capabilities of the cloud monitoring system.

The system detected abnormal CPU usage through CloudWatch metrics and triggered automated SNS email alerts.

---

# Detection Method

- AWS CloudWatch Alarm
- CPUUtilization > 70%
- SNS Email Notification

---

# Root Cause

The following command intentionally generated high CPU usage:

```bash
yes > /dev/null
```

This continuously consumed CPU resources.

---

# Impact

- Increased CPU utilization
- Performance degradation
- Alarm triggered successfully

---

# Response Actions

- Reviewed CloudWatch metrics
- Verified SNS notifications
- Investigated logs
- Stopped CPU stress process

---

# Resolution

CPU stress process terminated successfully using:

```bash
CTRL + C
```

CPU usage returned to normal.

---

# Lessons Learned

- CloudWatch alarms functioned correctly
- SNS alerts delivered instantly
- Monitoring scripts successfully retrieved metrics
- Incident response process validated

---

# Recommendations

- Add auto-remediation using AWS Lambda
- Integrate Slack alerts
- Enable centralized logging
- Add Grafana dashboards