from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return "No file part", 400

    file = request.files['image']
    # You can save the file if needed
    # file.save(f"./uploads/{file.filename}")

    # Send a WhatsApp message using an alternative service
    send_whatsapp_message("You are violating the traffic rules and thus an amount of 100$ has been deducted from your bank account 😈😈😈😈")
    
    return "Image uploaded and message sent", 200

def send_whatsapp_message(message):
    # Use a free WhatsApp API alternative like WhatsApp Business API through a service like "Chat-API" or "WATI"
    # Note: You need to sign up for one of these services to get an API key.
    
    # Example for Chat-API (this is just a placeholder, you'll need to replace it with actual implementation)
    url = "https://api.chat-api.com/instanceXXXX/sendMessage"
    payload = {
        "phone": "1234567890",  # Replace with the recipient's phone number
        "body": message
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_API_KEY"  # Replace with your API key
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.json())

if __name__ == '__main__':
    app.run(debug=True)
