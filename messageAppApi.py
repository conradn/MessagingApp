from flask import *


app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/post", methods=["POST","GET"])
def getValues():
    contact = request.args.get('number')
    message = request.args.get('msg')
    return 'new message '+message+' from '+contact

app.run(debug=True)

