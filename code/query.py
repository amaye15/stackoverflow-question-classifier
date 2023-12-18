import requests

# URL of your FastAPI endpoint
url = "http://127.0.0.1:8000/classify"

# Data to be sent (modify this with your actual text and labels)
data = {
    "text": "Sample text to classify",
    "labels": ["label1", "label2", "label3"]
}

# Sending a POST request
response = requests.post(url, json=data)

# Checking the response
if response.status_code == 200:
    print("Classification successful!")
    print(response.json())
else:
    print("Error:", response.status_code)
    print(response.text)
