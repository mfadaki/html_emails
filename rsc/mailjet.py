from mailjet_rest import Client
import os
api_key = 'db5e6be12436d156deb7ad9b6034bfce'
api_secret = '02f63a6dd7f80d2deaef34915be83583'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
data = {
    'Messages': [
        {
            "From": {
                "Email": "mfadaki@icloud.com",
                "Name": "Masih"
            },
            "To": [
                {
                    "Email": "mfadaki@icloud.com",
                    "Name": "Masih"
                }
            ],
            "Subject": "Greetings from Mailjet.",
            "TextPart": "My first Mailjet email",
            "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
            "CustomID": "AppGettingStartedTest"
        }
    ]
}
result = mailjet.send.create(data=data)
print(result.status_code)
print(result.json())
