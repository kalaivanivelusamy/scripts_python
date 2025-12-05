import pywhatkit

phone_number = "+91xxxxxxxxxx"
message = "message to be sent"
hour = 00
minute = 00

try:
    pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
except Exception as e:
    print(f"An error occurred: {e}")


