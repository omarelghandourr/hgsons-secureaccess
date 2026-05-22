# HGsons SecureAccess

A lightweight automated security system designed to protect Microsoft Access-based business applications using dynamically generated daily authentication keys and scheduled secure delivery through Telegram.

This project was developed mainly for startup and family businesses that rely on local Microsoft Access systems and require an additional operational security layer without deploying complex cloud infrastructure.

The system combines Microsoft Access VBA, Python automation, scheduled execution, and Telegram Bot integration into a unified workflow.

---

# Project Overview

The project is composed of 3 main parts:

1. Microsoft Access Lockdown System
2. Daily Encryption Key Generator
3. Automated Scheduled Delivery Agent

The overall idea is simple:

- The Microsoft Access application remains locked.
- A new authentication key is generated every day.
- The key is automatically sent to authorized users through Telegram.
- The user enters the daily key to unlock and access the system.

This creates an additional operational security layer for local business software.

---

# System Architecture

```text
+------------------------+
| GitHub Actions /       |
| Local Scheduler        |
+-----------+------------+
            |
            v
+------------------------+
| Python Key Generator   |
+-----------+------------+
            |
            v
+------------------------+
| Telegram Bot Delivery  |
+-----------+------------+
            |
            v
+------------------------+
| Microsoft Access App   |
| (VBA Validation)       |
+------------------------+
```

---

# Main Features

## Microsoft Access Security

- Lock/unlock protection for the Access database
- VBA-based daily key validation
- Startup security verification
- Unauthorized access shutdown
- Dynamic navigation locking
- Local-only verification logic
- Compatible with `.accdb` and deployment-ready `.accde`

---

## Daily Encryption Key Generator

The encryption key is generated dynamically based on:

- Current date
- Internal authentication secret
- Character position weighting
- Integer mixing operations
- Chaotic transformation parameters

The same algorithm exists in:

- Python
- VBA (Microsoft Access)

This ensures synchronized validation between both environments.

---

## Telegram Automated Delivery

The system automatically sends the generated daily code to a private Telegram group using:

- Telegram Bot API
- Python requests library
- Scheduled automation

Features include:

- Fully automated daily messages
- Arabic and English formatted messages
- Private group support
- Centralized distribution
- Lightweight deployment

---

# Technologies Used

## Backend & Automation

- Python 3.11
- VBA (Microsoft Access)
- GitHub Actions
- Telegram Bot API

---

## Libraries

### Python

- requests
- datetime
- zoneinfo
- os
- json

---

## Microsoft Access

- VBA Modules
- Forms
- Startup Validation Logic
- ACCDE Deployment

---

# Scheduled Automation

The project currently supports multiple scheduling methods:

## 1. GitHub Actions

Used for cloud-based scheduled execution.

Example:

```yaml
schedule:
  - cron: '0 4 * * *'
```

---

## 2. Android Local Automation

Using:

- Pydroid
- MacroDroid

This method allows fully local execution directly from a mobile device.

---

# Telegram Message Example

```text
============================
HGsons Security Verification System
نظام التحقق الأمني - شركه اولاد حسنى الغندور
============================

Daily Verification Code
الشفره اليومية

Date / التاريخ :
21-05-2026

Security Code / الشفره :
48372615

Please do not share this code.
يرجى عدم مشاركة هذه الشفره.

============================
```

---

# Repository Structure

```text
hgsons-secureaccess/
│
├── access_vba/
│   ├── security_modules/
│   ├── startup_validation/
│   └── encryption_logic/
│
├── python_bot/
│   ├── send_daily_code.py
│   ├── send_daily_code_v2.py
│   └── requirements.txt
│
├── github_actions/
│   └── workflows/
│
├── docs/
│   └── screenshots/
│
├── .env.example
├── .gitignore
├── README.md
│
└── LICENSE
```

---

# Secure Configuration

Sensitive production parameters are managed using GitHub Actions Secrets and environment variables.

This includes:

- Telegram Bot Token
- Telegram Chat ID
- Internal Authentication Secret
- Chaotic Mixing Parameters

No production secrets are stored directly inside the public repository.

---

# Security Notes

- The secret key should never be uploaded publicly.
- Production security parameters are injected at runtime using GitHub Secrets.
- Sensitive cryptographic configuration values are intentionally excluded from the public repository.
- Avoid hardcoding sensitive information inside scripts.
- ACCDE deployment is recommended for production use.

---

# Deployment

The system can be deployed using:

- GitHub Actions (cloud scheduler)
- Local Windows Task Scheduler
- Android automation tools (Pydroid + MacroDroid)

Production deployments should use GitHub Secrets or local environment variables for sensitive configuration.

---

# Environment Configuration Example

```text
TOKEN=YOUR_TELEGRAM_TOKEN
CHAT_ID=YOUR_CHAT_ID
SECRET_KEY=YOUR_SECRET_KEY
CHAOS_MULTIPLIER=YOUR_SECRET_VALUE
```

---

# Current Status

Current implemented capabilities:

- Daily synchronized encryption generation
- Telegram automated delivery
- Microsoft Access validation
- Scheduled automation
- Arabic/English notification formatting
- Mobile-based local execution
- GitHub Actions cloud execution

---

# Planned Future Improvements

- Multi-user authorization levels
- Hardware-based validation
- Machine fingerprint verification
- Database activity logging
- Encrypted local configuration files
- Admin dashboard
- Remote revoke system
- Time-limited session keys
- AES-based advanced encryption layer
- Web monitoring interface

---

# Use Case

This project is primarily intended for:

- Family businesses
- Small local businesses
- Offline operational systems
- Microsoft Access-based ERP tools
- Inventory systems
- Lightweight internal management systems

---

# Disclaimer

This project is designed as a lightweight operational security layer and should not be considered a replacement for enterprise-grade cybersecurity systems.

It is intended for operational security enhancement in local business environments.

---

# Author

Omar Elghandour

- Applied AI Engineer
- MSc ICE – Autonomous Systems & Robotics
- B.Sc. Mechatronics Engineering

LinkedIn:
https://www.linkedin.com/in/omar-elghandour/
