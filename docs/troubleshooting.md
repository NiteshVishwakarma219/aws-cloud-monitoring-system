# 🚨 Troubleshooting Guide - AWS Monitoring System

## ⚠️ 1. EC2 Instance Not Showing Status

### Problem:
Instance status returns empty or null.

### Fix:
- Check correct Instance ID
- Ensure EC2 is in running state
- Verify IAM permissions:
  - ec2:DescribeInstanceStatus

---

## ⚠️ 2. CloudWatch Metrics Not Appearing

### Problem:
No CPU or system metrics visible.

### Fix:
- Enable **Detailed Monitoring** in EC2
- Wait 5–10 minutes for data
- Check correct region selection

---

## ⚠️ 3. SNS Alerts Not Received

### Problem:
No email/SMS alerts triggered.

### Fix:
- Confirm email subscription in SNS
- Check spam folder
- Ensure CloudWatch alarm is "In Alarm" state
- Verify SNS topic ARN in alarm action

---

## ⚠️ 4. Python boto3 Errors

### Problem:
`NoCredentialsError` or `AccessDenied`

### Fix:
```bash
aws configure

Or set IAM role if using EC2 instance.

⚠️ 5. CloudWatch Logs Not Fetching
Problem:

No logs returned from log_fetcher.py

Fix:

Ensure log group exists:

/aws/ec2/system-logs
Check IAM permissions:
logs:DescribeLogStreams
logs:GetLogEvents
⚠️ 6. Auto Recovery Not Triggering
Problem:

Instance not restarting automatically.

Fix:
Check CPU threshold (>80%)
Verify CloudWatch metric namespace
Ensure correct Instance ID in script
Validate boto3 permissions:
ec2:RebootInstances