from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/success/<name>')
def success(name):
    return f'Welcome, {name}!'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']  # Ambil data dari form (POST)
        return redirect(url_for('success', name=user))
    else:
        return render_template('login.html')  # Render login.html

if __name__ == '__main__':
    app.run(debug=True)
