from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return "No file part", 400

    file = request.files['image']
    # Process the image if needed (e.g., save it, analyze it, etc.)

    # Send WhatsApp message
    send_whatsapp_message("+1234567890",
                          "You are violating the traffic rules and thus an amount of 100$ has been deducted from your bank account 😈😈😈😈")

    return "Image uploaded and message sent", 200


def send_whatsapp_message(phone_number, message):
    # Twilio API credentials
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    client.messages.create(
        body=message,
        from_='whatsapp:+your_twilio_whatsapp_number',
        to=f'whatsapp:{phone_number}'
    )


if __name__ == '__main__':
    app.run(debug=True)
