from flask import *
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'
mysql = MySQL(app)
@app.route("/")
def home():
   
    return render_template("index.html")

@app.route("/post", methods=["POST","GET"])
def postValues():
    
    if request.method == "POST":
        flash("Data Inserted Successfully")
        contact = request.form['number']
        message = request.form['msg']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO test1 (name, message) VALUES (%s, %s)", (contact, message))
        mysql.connection.commit()
        cur.close()
        
    return redirect(url_for('getValues'))
    

    

@app.route("/get", methods=["POST","GET"])
def getValues():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM test1")
    fetchdata = cur.fetchall()
    cur.close()
    return render_template("index.html",data = fetchdata)
app.run(debug=True)

