from flask import Flask
from flask import render_template
import pusher

app = Flask(__name__)

# Configure Pusher with your Pusher credentials
pusher_client = pusher.Pusher(
    app_id='1638415',
    key='96b3f7a5a54517450f0d',
    secret='963323e048f9027c3355',
    cluster='us2',
    ssl=True
)

@app.route("/")
def hello_world():
    return render_template("index.html")
