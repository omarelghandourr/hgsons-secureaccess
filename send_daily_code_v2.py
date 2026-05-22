"""

008 6 digit daily code + Telegram (Arabic).py


=========================================================
HGsons Daily Telegram Verification System
=========================================================

Author:
Omar Elghandour

Purpose:
--------
This script:

1) Generates a secure daily verification code
2) Sends the code automatically to a Telegram group

Designed for:
- Microsoft Access protection
- Daily authentication systems
- Offline business verification systems

=========================================================
"""

import requests
from datetime import datetime
from zoneinfo import ZoneInfo
import os

# =========================================================
# TELEGRAM CONFIG
# =========================================================


TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


# =========================================================
# DAILY CODE GENERATOR
# =========================================================

def generate_daily_code(
    date_input,
    secret="HGsons2026"
):

    # =====================================================
    # STEP 1 — FORMAT DATE
    # =====================================================

    raw_date = date_input.strftime("%Y%m%d")


    # =====================================================
    # STEP 2 — BUILD RAW STRING
    # =====================================================

    raw_string = raw_date + secret


    # =====================================================
    # STEP 3 — TEXT TO NUMERIC CONVERSION
    # =====================================================

    total = 0

    for i, ch in enumerate(raw_string):

        total += ord(ch) * (i + 1)


    # =====================================================
    # STEP 4 — INITIAL SEED EXTRACTION
    # =====================================================

    seed = total % 1000


    # =====================================================
    # STEP 5 — INTEGER MIXING ALGORITHM
    # =====================================================

    for _ in range(80):

        seed = (
            (
                (seed * 399)
                ^ (seed // 7)
            )
            + 12345
        ) % 1000000


    # =====================================================
    # STEP 6 — FINAL CODE EXTRACTION
    # =====================================================

    code = str(seed).zfill(6)

    return code


# =========================================================
# TELEGRAM MESSAGE SENDER
# =========================================================

def send_message(message):

    url = (
        f"https://api.telegram.org/bot"
        f"{TOKEN}/sendMessage"
    )

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(
        url,
        data=data
    )

    print(response.text)


# =========================================================
# MAIN
# =========================================================


today = datetime.now(
    ZoneInfo("Africa/Cairo")
)


daily_code = generate_daily_code(today)

message = (
    "============================\n"
    "HGsons Security Verification System\n"
    "نظام التحقق الأمني - شركه اولاد حسنى الغندور\n"
    "============================\n\n"

    "Daily Verification Code\n"
    "الشفره اليومية\n\n"

    f"Date / التاريخ : "
    f"{today.strftime('%d-%m-%Y')}\n\n"

    f"Security Code / الشفره :\n"
    f"{daily_code}\n\n"

    "Please do not share this code.\n"
    "يرجى عدم مشاركة هذه الشفره.\n\n"

    "============================"
)

send_message(message)

print("===========================")
print("HGsons Daily Verification System")
print("===========================")

print("Today's Date :", today.strftime("%d-%m-%Y"))
print("Today's Code :", daily_code)

print("===========================")

print("Daily code sent successfully.")
