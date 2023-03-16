
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
    return render_template('registration.html')
 
@app.route('/login', methods = ['POST', 'GET'])
def login():     
    if request.method == 'POST':
        bloodbankname = request.form.get('bloodbankname')
        category = request.form.get('category')
        phone = request.form.get('phone')
        district = request.form.get('district')
        state = request.form.get('state')
        email = request.form.get('email')
        #mysql.connection.commit()
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO bloodbankinfo (`Name`, `Category`, `District`, `State`, `Phone`, `Email`) VALUES (%s,%s,%s,%s,%s,%s)''',[bloodbankname,category,district,state,phone,email]) 
        mysql.connection.commit()
        cursor.close()
        return "added"
 
if __name__ == "__main__":
    app.run(debug=True) 