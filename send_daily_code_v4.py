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
3) After 58 days from the activation date,
   sends the permanent password

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

SECRET_KEY = os.getenv("SECRET_KEY")
CHAOS_MULTIPLIER = int(os.getenv("CHAOS_MULTIPLIER"))

ACTIVATION_DATE = os.getenv("ACTIVATION_DATE")
PERMANENT_PASSWORD = os.getenv("PERMANENT_PASSWORD")


# =========================================================
# DAILY CODE GENERATOR
# =========================================================

def generate_daily_code(
    date_input,
    secret
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
                (seed * CHAOS_MULTIPLIER)
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

def send_message(message, chat_id):

    url = (
        f"https://api.telegram.org/bot"
        f"{TOKEN}/sendMessage"
    )

    data = {
        "chat_id": chat_id,
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


# =========================================================
# CHECK ACTIVATION DATE
# =========================================================

activation_date = datetime.strptime(
    ACTIVATION_DATE,
    "%Y-%m-%d"
).date()

today_date = today.date()

days_since_activation = (
    today_date - activation_date
).days


# =========================================================
# PRINT ACTIVATION INFORMATION
# =========================================================

print("===========================")
print("HGsons Daily Security System")
print("===========================")

print("Activation Date :", activation_date)
print("Today's Date    :", today_date)
print("Days Since Activation :", days_since_activation)

print("===========================")


# =========================================================
# AFTER 58 DAYS
# =========================================================

if days_since_activation > 58:

    message = (
        "========================================\n"
        "HGSONS SECURITY SYSTEM\n"
        "========================================\n\n"

        "PERMANENT ACCESS CREDENTIAL\n\n"

        "The activation period for this system has expired.\n\n"

        "Your permanent access password is:\n\n"

        f"{PERMANENT_PASSWORD}\n\n"

        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"

        "IMPORTANT NOTICE\n\n"

        "Please SAVE this message immediately.\n\n"

        "This message will be automatically deleted "
        "after 24 hours.\n\n"

        "Once deleted, this password will NOT be "
        "available from this message again.\n\n"

        "Please store the password in a secure location.\n\n"

        f"Activation Date: "
        f"{activation_date.strftime('%d-%m-%Y')}\n"

        f"Days Since Activation: "
        f"{days_since_activation}\n\n"

        "AUTHORIZED PERMANENT ACCESS\n\n"

        "----------------------------------------\n"
        "العربية\n"
        "----------------------------------------\n\n"

        "نظام الأمان والتحقق\n"
        "شركه اولاد حسنى الغندور\n\n"

        "بيانات الدخول الدائمة\n\n"

        "انتهت فترة التفعيل الخاصة بهذا النظام.\n\n"

        "كلمة المرور الدائمة الخاصة بك هي:\n\n"

        f"{PERMANENT_PASSWORD}\n\n"

        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"

        "تنبيه هام جدًا\n\n"

        "يرجى حفظ هذه الرسالة فورًا.\n\n"

        "سيتم حذف هذه الرسالة تلقائيًا بعد 24 ساعة.\n\n"

        "بعد حذف الرسالة، لن تكون كلمة المرور متاحة "
        "مرة أخرى من خلال هذه الرسالة.\n\n"

        "يرجى الاحتفاظ بكلمة المرور في مكان آمن.\n\n"

        f"تاريخ التفعيل: "
        f"{activation_date.strftime('%d-%m-%Y')}\n"

        f"عدد الأيام منذ التفعيل: "
        f"{days_since_activation}\n\n"

        "دخول دائم مصرح به\n\n"

        "V4.0\n"

        "========================================"
    )

    # =====================================================
    # SEND PERMANENT PASSWORD
    # =====================================================

    send_message(
        message,
        CHAT_ID
    )

    print("58-day period has expired.")
    print("Permanent password sent.")


# =========================================================
# NORMAL DAILY CODE
# =========================================================

else:

    daily_code = generate_daily_code(
        today,
        SECRET_KEY
    )

    message = (
        "========================================\n"
        "HGSONS SECURITY VERIFICATION SYSTEM\n"
        "========================================\n\n"

        "DAILY VERIFICATION CODE\n\n"

        f"Date: "
        f"{today.strftime('%d-%m-%Y')}\n\n"

        "Security Code:\n\n"

        f"{daily_code}\n\n"

        "Please do not share this code.\n\n"

        "----------------------------------------\n"
        "العربية\n"
        "----------------------------------------\n\n"

        "نظام الأمان والتحقق\n"
        "شركه اولاد حسنى الغندور\n\n"

        "الشفره اليومية\n\n"

        f"التاريخ: "
        f"{today.strftime('%d-%m-%Y')}\n\n"

        "الشفره الأمنية:\n\n"

        f"{daily_code}\n\n"

        "يرجى عدم مشاركة هذه الشفره.\n\n"

        "V4.0\n"

        "========================================"
    )

    send_message(
        message,
        CHAT_ID
    )

    print("Today's Code :", daily_code)
    print("Daily code sent successfully.")


# =========================================================
# END
# =========================================================

print("===========================")
print("HGsons Security Bot Finished")
print("===========================")
