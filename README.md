# 🚀 Production-Grade Cloud Observability & Auto-Healing System (AWS + Python)

## 📌 Overview

This project implements a production-style cloud observability and incident response system that continuously monitors AWS infrastructure, detects anomalies in real time, and performs automated recovery actions using Python (boto3).

It simulates a real-world Site Reliability Engineering (SRE) system used in modern cloud-native production environments.

---

## 🎯 Problem Statement

Modern cloud systems face:
- Sudden infrastructure failures
- CPU spikes and resource exhaustion
- Delayed incident detection
- Manual recovery delays

This system solves these issues by building an **automated observability + alerting + self-healing pipeline** to reduce downtime and improve reliability.

---

## 🏗️ Architecture Flow

EC2 / S3 / IAM Events  
→ Amazon CloudWatch (Metrics + Logs)  
→ CloudWatch Alarms (Threshold Detection)  
→ Amazon SNS (Real-Time Alerts)  
→ Python Automation Layer (boto3)  
→ Auto-Healing Actions (Restart / Log Analysis / Recovery)

---

## ☁️ AWS Services Used

- Amazon EC2 – Compute monitoring  
- Amazon S3 – Storage activity tracking  
- AWS IAM – Security event monitoring  
- Amazon CloudWatch – Metrics, logs, alarms, dashboards  
- Amazon SNS – Event-driven notifications  

---

## 🧠 Core Features

### 📊 Observability Layer
- Real-time EC2 CPU monitoring  
- Instance health checks  
- CloudWatch log stream tracking  
- Continuous infrastructure visibility  

### 🚨 Alerting Layer
- CPU threshold alerts (>80%)  
- Instance failure detection  
- Log-based anomaly detection  
- Instant SNS notifications (Email/SMS)  

### 🐍 Automation Layer (Python + boto3)
- EC2 health monitoring scripts  
- CloudWatch log retrieval system  
- Auto restart (self-healing) mechanism  
- Continuous monitoring loop  

### 🔥 Incident Simulation
- High CPU stress testing  
- Instance crash simulation  
- Log anomaly generation  
- Real-time debugging validation  

---

## 🔁 Incident Lifecycle

1. AWS services generate metrics/logs  
2. CloudWatch continuously monitors system health  
3. Anomaly detected (CPU spike / failure)  
4. Alarm is triggered automatically  
5. SNS sends real-time alert  
6. Python automation executes recovery  
7. System stabilizes (self-healed)

---

## 📁 Project Structure

cloud-monitoring-system/
├── scripts/
│   ├── ec2_monitor.py
│   ├── log_fetcher.py
│   └── auto_recovery.py
│
├── docs/
│   ├── setup-guide.md
│   ├── troubleshooting.md
│
├── architecture/
│   └── architecture.png
│
└── README.md

---

## ⚙️ Setup Instructions

aws configure  
pip install boto3  

python scripts/ec2_monitor.py  
python scripts/log_fetcher.py  
python scripts/auto_recovery.py  

---

## 🧠 Engineering Decisions

- CloudWatch → Central observability engine  
- SNS → Event-driven alert system  
- boto3 → Infrastructure automation layer  
- Event-driven design → Scalable and production-aligned architecture  

---

## 🔥 Skills Demonstrated

- Cloud Observability (AWS CloudWatch)  
- Incident Response Engineering (SRE Concepts)  
- Python Automation (boto3)  
- Event-Driven Architecture  
- Cloud Debugging & Troubleshooting  
- Production System Design Thinking  

---

## 💼 Real-World Relevance

This system mirrors production-grade cloud environments where:
- Infrastructure is continuously monitored  
- Failures are detected instantly  
- Alerts are automated  
- Recovery is self-healing  

---

## 🚀 Future Enhancements

- AWS Lambda serverless automation  
- AI-based anomaly detection  
- Slack / Teams integration  
- Multi-region monitoring  
- Centralized logging (ELK stack)  

---

## 👨‍💻 Author

Nitesh Vishwakarma  
Cloud & DevOps Enthusiast  
