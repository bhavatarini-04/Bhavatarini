from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login', methods = ['POST','GET'])
def loginpage():
    if request.method=='POST':
        return render_template('login.html')    
    return render_template('login.html')
    
if __name__ == '__main__':
    app.run(debug=True)