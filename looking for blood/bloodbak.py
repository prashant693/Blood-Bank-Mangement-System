from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bloodbank'
 
mysql = MySQL(app)
 
@app.route('/sea')
def form():
    return render_template('page2.html')
 
@app.route('/search', methods = ['POST', 'GET'])
def login():     
    if request.method == 'POST':
        name = request.form.get('district')
        cursor = mysql.connection.cursor()
        cursor.execute('''SELECT * FROM bloodbankinfo WHERE District=%s''',[name])
        fetchdata = cursor.fetchall()
        cursor.close()
        return render_template("lal.html",fetchdata=fetchdata)
 
if __name__ == "__main__":
    app.run(debug=True) 