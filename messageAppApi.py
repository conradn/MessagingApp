from flask import *


app = Flask(__name__)
@app.route("/")
def home():
    return render_template("page2.html")

@app.route("/post", methods=["POST","GET"])
def getValues():
    contact = request.args.get('receipient')
    message = request.args.get('message')
    return 'new message '+str(message)+' from '+str(contact)

app.run(debug=True)

