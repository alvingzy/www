import requests
from stat_updater.py import total_count
import time

webhook_url = "https://discord.com/api/webhooks/1165613802222518353/lvf4jR1H2kptM2GdKVtiSZFCH5h7bLAwibF8lsxQ5MUuIoobT4fG0xsypzY-VTalZFFl"
rotation_value = 12421

while True:
    # Update your rotating value here, for example, increment it by 1 each time.
    rotation_value += 1

    # Create a dictionary with the data you want to send to the webhook.
    data = {
        "value": rotation_value
    }

    try:
        # Send a POST request to the webhook URL with the data.
        response = requests.post(webhook_url, json=data)

        # Check the response status code to ensure the request was successful.
        if response.status_code == 200:
            print(f"Value {rotation_value} sent successfully to the webhook.")
        else:
            print(f"Failed to send value {rotation_value} to the webhook. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

    # Wait for 1 second before the next update.
    time.sleep(1)