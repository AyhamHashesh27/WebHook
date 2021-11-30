# WebHook: Way for APIs to communicate when even occurs.
# Simply, it's automated HTTP messages sent from apps (Server to Server) when something happens.
# They contain payload message and are sent to unique URL.

# Sending the HTTP request
import requests
# Formatting the payload
import json

# Destination URL we send the webhook to
webhook_url = 'https://webhook.site/531d28bb-3a90-4bd4-a3a1-4c6fc5aa5ce0'

payload_data = {
    'reporter': 'Ayham Hashesh'
}

# Convert python dict to JSON
json_payload_data = json.dumps(payload_data)

# Header
http_header = {
    'Content-Type': 'application/json'
}

# Send request
r = requests.post(webhook_url, data=json_payload_data, headers=http_header)
# WebHook: Way for APIs to communicate when even occurs.
# Simply, it's automated HTTP messages sent from apps (Server to Server) when something happens.
# They contain payload message and are sent to unique URL.

# Sending the HTTP request
import requests
# Formatting the payload
import json

# Destination URL we send the webhook to
# webhook_url = 'https://webhook.site/531d28bb-3a90-4bd4-a3a1-4c6fc5aa5ce0'
webhook_url = 'http://127.0.0.1:5000/webhook'

payload_data = {
    'reporter': 'Ayham Hashesh'
}

# Convert python dict to JSON
json_payload_data = json.dumps(payload_data)

# Header
http_header = {
    'Content-Type': 'application/json'
}

# Send request
r = requests.post(webhook_url, data=json_payload_data, headers=http_header)
