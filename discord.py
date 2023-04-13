#!/usr/bin/env python3
import json
import subprocess
import requests

# Replace this with the path to your govstat binary
govstat_binary_path = "./govstat"

# Replace this with your Discord webhook URL
webhook_url = "https://discord.com/api/webhooks/your-webhook-id/your-webhook-token"

# Run the govstat binary and capture its output
govstat_output = subprocess.check_output(govstat_binary_path).decode("utf-8")

# Convert the output to JSON format
payload = {"content": govstat_output}
json_payload = json.dumps(payload)

# Send the JSON payload to Discord webhook
headers = {"Content-Type": "application/json"}
response = requests.post(webhook_url, data=json_payload, headers=headers)

# Check if the request was successful
if response.status_code == 204:
    print("Message sent to Discord successfully.")
else:
    print(f"Failed to send message to Discord. Status code: {response.status_code}")
