import requests
from datetime import datetime


# ==========================================
# TELEGRAM CONFIG
# ==========================================

import os

TOKEN = os.getenv("TOKEN")

CHAT_ID = os.getenv("CHAT_ID")


# ==========================================
# DAILY CODE GENERATOR
# ==========================================

def generate_daily_code():

    today = datetime.now().strftime("%Y%m%d")

    secret = "HGX9_AutoSecure_2026"

    raw = today + secret

    total = 0

    for i, ch in enumerate(raw, start=1):

        total += ord(ch) * i

    total ^= 7381

    total = (total * 13) % 99999999

    return str(total).zfill(8)


# ==========================================
# SEND TELEGRAM MESSAGE
# ==========================================

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


# ==========================================
# MAIN
# ==========================================

code = generate_daily_code()

message = (
    "HGsons Daily Security Key\n\n"
    f"{code}"
)

send_message(message)

print("Daily code sent successfully.")
