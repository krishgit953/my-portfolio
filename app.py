from flask import Flask, render_template, request
app= Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/location')
def location():
    return render_template("location.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    message_sent=False
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        message=request.form['message']
        print(f"message from {name} ({email}): {message}")
        message_sent=True
    return render_template("contact.html", message_sent=message_sent)

@app.route('/Our_Branch')
def Our_Branch():
    return render_template("Our_Branch.html")

if __name__ == '__main__':
    app.run(debug=True)