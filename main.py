import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv() 

OWM_Endpoint = os.getenv("OWM_Endpoint")
api_key = os.getenv("API_KEY")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")


weather_params = {
    "lat": 17.802280,
    "lon": 83.385147,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        break

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid="MG3401916e257045a5244ad629ca621ec2",
        body="It will rain today ☔",
        from_="+1234567890",  # Replace with your Twilio verified number if not using Messaging Service SID
        to="+918871716969"
    )
    print(message.sid)
else:
    print("No rain expected in the next few hours ☀️")
