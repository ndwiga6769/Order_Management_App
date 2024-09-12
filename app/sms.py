import africastalking
from config import Config

# Africa's Talking API setup
africastalking.initialize(Config.AFRICAS_TALKING_USERNAME, Config.AFRICAS_TALKING_API_KEY)
sms = africastalking.SMS

def send_sms_alert(message):
    try:
        # Placeholder for recipient number
        response = sms.send(message, ['+254700000000'])  # Replace with actual phone number
        print(f"SMS sent: {response}")
    except Exception as e:
        print(f"Error sending SMS: {e}")
