# hgsons-security-bot

A lightweight automated security system designed to protect a Microsoft Access-based business application using dynamically generated daily encryption keys and scheduled secure delivery through Telegram.

This project was developed mainly for small and startup businesses that rely on local Microsoft Access systems and require an additional security layer without deploying complex cloud infrastructure.

The system combines Microsoft Access VBA, Python automation, scheduled execution, and Telegram Bot integration into a unified workflow.

---

# Project Overview

The project is composed of 3 main parts:

1. Microsoft Access Lockdown System  
2. Daily Encryption Key Generator  
3. Automated Scheduled Delivery Agent  

The overall idea is simple:

- The Microsoft Access application remains locked.
- A new encryption key is generated every day.
- The key is automatically sent to authorized users through Telegram.
- The user enters the daily key to unlock and access the system.

This creates an additional layer of operational security for local business software.

---


# System Architecture

```text

+------------------------+
|  GitHub Actions /      |
|  Local Scheduler       |
+-----------+------------+
            |
            v
+------------------------+
|  Python Key Generator  |
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
- Secret internal key
- Character position weighting
- XOR operation
- Mathematical transformations

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
- hashlib (future extension)
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

schedule:
  - cron: '0 4 * * *'

---

## 2. Android Local Automation

Using:

- Pydroid
- MacroDroid

This method allows fully local execution directly from a mobile device.

---

# Telegram Message Example

HGsons Security System

Daily Access Code / الشفرة اليومية

Date:
2026-05-21

Today's Security Code:
48372615

Please use this code to access the system.

يرجى استخدام هذه الشفرة للدخول إلى النظام

---

# Repository Structure
```text

hgsons-security-bot/
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
├── README.md
│
└── LICENSE
```
---

# Security Notes

- The secret key should never be uploaded publicly.
- Use GitHub Secrets for:
  - Telegram Bot Token
  - Chat ID
  - Future API credentials
- Avoid hardcoding sensitive information inside scripts.
- ACCDE deployment is recommended for production use.

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

This project is mainly intended for:

- Family businesses
- Small local businesses
- Offline operational systems
- Microsoft Access-based ERP tools
- Inventory systems
- Lightweight internal management systems

---

# Disclaimer

This project is designed as a lightweight practical protection layer and should not be considered a replacement for enterprise-grade cybersecurity systems.

It is intended for operational security enhancement in local business environments.

---

# Author

Omar Elghandour

- Applied AI Engineer
- MSc ICE – Autonomous Systems & Robotics
- B.Sc. Mechatronics Engineering

LinkedIn:
https://www.linkedin.com/in/omar-elghandour/
