import os
import time
import requests
from datetime import datetime

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def send_alert():
    message = (
        "🛡️ SecGuard Alerts\n\n"
        "⚠️ تنبيه أمني تجريبي\n"
        "الحالة: النظام يعمل بشكل طبيعي\n"
        f"الوقت: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    response = requests.post(
        url,
        data={"chat_id": CHAT_ID, "text": message},
        timeout=15
    )

    response.raise_for_status()
    print("تم إرسال التنبيه بنجاح")

if __name__ == "__main__":
    if not TOKEN or not CHAT_ID:
        raise SystemExit("أضف TELEGRAM_BOT_TOKEN و TELEGRAM_CHAT_ID أولاً")

    while True:
        try:
            send_alert()
        except Exception as error:
            print(f"فشل الإرسال: {error}")

        time.sleep(300)
