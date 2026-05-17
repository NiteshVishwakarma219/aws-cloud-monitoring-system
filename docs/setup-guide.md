# 🚀 Setup Guide - Advanced Cloud Monitoring & Incident Response System

## 📌 Prerequisites

Before starting, ensure you have:

- AWS Account (Free Tier or Paid)
- AWS CLI installed and configured
- Python 3.8+
- `boto3` installed
- IAM user with permissions:
  - CloudWatchFullAccess
  - EC2FullAccess
  - SNSFullAccess

---

## ⚙️ Step 1: Configure AWS CLI

```bash
aws configure

Enter:

AWS Access Key
AWS Secret Key
Region: ap-south-1 (or your region)
Output format: json

---

## 🖥️ Step 2: Launch EC2 Instance

1. Go to AWS Console
2. Launch EC2 (Amazon Linux 2 / Ubuntu)
3. Enable:
   - Detailed monitoring
   - Security group (allow SSH)
4. Note Instance ID

---

## 📊 Step 3: Enable CloudWatch Monitoring

- Go to CloudWatch
- Enable metrics for EC2
- Create custom dashboard:
  - CPU Utilization
  - Status Checks
  - Network In/Out

---

## 🚨 Step 4: Create SNS Topic

1. Go to SNS service
2. Create topic:

cloud-alerts-topic

3. Subscribe email/SMS
4. Confirm subscription

---

## 📉 Step 5: Create CloudWatch Alarm

Example:
- Metric: CPU Utilization
- Threshold: > 80%
- Action: SNS Topic alert

---

## 🐍 Step 6: Install Python Dependencies

```bash
pip install boto3
▶️ Step 7: Run Scripts
python scripts/ec2_monitor.py
python scripts/log_fetcher.py
python scripts/auto_recovery.py