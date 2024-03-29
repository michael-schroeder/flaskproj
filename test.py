# import all the libraries we will be using
from flask import Flask, request
from flask_ngrok import run_with_ngrok
from twilio import twiml

# set up Flask to connect this code to the local host, which will
# later be connected to the internet through Ngrok
app = Flask(__name__)
# run_ngrok(app) -- add to run with ngrok
    
# Main method. When a POST request is sent to our local host through Ngrok 
# (which creates a tunnel to the web), this code will run. The Twilio service # sends the POST request - we will set this up on the Twilio website. So when # a message is sent over SMS to our Twilio number, this code will run
@app.route('/', methods=['POST'])
def sms():
    # Get the text in the message sent
    message_body = request.form['Body']
    
    # Create a Twilio response object to be able to send a reply back (as per         # Twilio docs)
    resp = twiml.Response()
    
    # Send the message body to the getReply message, where 
    # we will query the String and formulate a response
    replyText = getReply(message_body)

	# Text back our response!
    resp.message('Hi\n\n' + replyText )
    return str(resp)
	
# when you run the code through terminal, this will allow Flask to work
if __name__ == '__main__':
    app.run()
