from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os
import requests


# class PushNotificationInput(BaseModel):
#     # THis is message to be send to the user
#     """Input schema for PushNotificationTool."""
#     message: str = Field(..., description="The message to be sent to the user")

# class PushNotificationTool(BaseTool):
#     name: str = "Send a Push Notification Tool"
#     description: str = (
#         "This tool is used to send a push notification to the user"
#     )
#     args_schema: Type[BaseModel] = PushNotificationInput

#     def _run(self, message: str) -> str:
#         pushover_user = os.getenv("PUSHOVER_USER")
#         pushover_token = os.getenv("PUSHOVER_TOKEN")
#         pushover_url = "https://api.pushover.net/1/messages.json"

#         print(f"Push: {message}")
#         payload = {"user" : pushover_user, 
#                    "token": pushover_token,
#                    "message": message}
#         requests.post(pushover_url, data=payload)
#         return '{"notification": "ok"}'


class TelegramNotificationInput(BaseModel):
    message: str = Field(..., description="Message to send via Telegram")


class TelegramNotificationTool(BaseTool):
    name: str = "Send Telegram Notification Tool"
    description: str = "Sends a Telegram message to the User"
    args_schema: Type[BaseModel] = TelegramNotificationInput

    def _run(self, message: str) -> str:
        token = os.getenv("TELEGRAM_BOT_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID")

        if not token or not chat_id:
            return "Telegram credientails not set"

        url = f"https://api.telegram.org/bot{token}/sendMessage"

        payload = {
            "chat_id": chat_id,
            "text": message
        }

        try:
            response = requests.post(url, json=payload, timeout=10)
            print("Telegram response: ", response.status_code, response.text)
            return '{"Notification":"sent"}'

        except Exception as e:
            print("Telegram error:",e)
            return '{"notification": "failed"}'