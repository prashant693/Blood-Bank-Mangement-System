from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bloodbank'
 
mysql = MySQL(app)
 
@app.route('/')
def form():
    return render_template('page1.html')
 
@app.route('/search', methods = ['POST', 'GET'])
def login():     
    if request.method == 'POST':
        name = request.form.get('district')
        cursor = mysql.connection.cursor()
        cursor.execute('''SELECT * FROM bloodbankinfo INNER JOIN available ON bloodbankinfo.Name=available.name and District=%s''',[name])
        fetchdata = cursor.fetchall()
        cursor.close()
        return render_template("page1.html",fetchdata=fetchdata)
 
if __name__ == "__main__":
    app.run(debug=True) 