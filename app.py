from flask import Flask , request
from twilio.twiml.messaging_response import MessagingResponse
app = Flask(__name__)

@app.route("/", methods=["get","post"])

def reply():
    text = request.form.get("Body")
    number = request.form.get("From")
    response = MessagingResponse()
    ##msg = response.message(f"hello. You sent '{text}' from {number}")
    if "handsome" in text:
        response.message("Baobao is the most handsome boy in the world💜!")
    elif "night" in text:
        response.message("Gute Nacht mein baby Baobao!Traume etwas schönes!")
    elif "morning" in text:
        response.message("Guten Morgen, mein lieber kapitän baobao😊.Habe einen schönen Tag!")    
    else:
        response.message("Hallo, was kann ich für Sie tun?")
    return str(response)

if __name__ == "__main__":
    app.run()


