from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('my-site.html')

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    binary = 0
    if request.method == 'GET':
        binary = 0

    elif request.method == 'POST':
        email = request.form['email']
        message = request.form['message']
        my_email = 'pyt.gusmao@gmail.com'
        password = 'htkklcfotsfxjvyi'
        connection = smtplib.SMTP('smtp.gmail.com', 587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        body = f"Subject: {email}\n" \
        f"Content-Type: text/plain; charset=utf-8\n" \
        f"Content-Transfer-Encoding: 8bit\n\n" \
        f"{message}"
        connection.sendmail(from_addr=my_email, to_addrs='maitrijoshi6.mj@gmail.com', msg=body.encode('utf-8'))
        binary = 1

    return render_template('contact-me.html', binary = binary)





if __name__ == "__main__":
    app.run(debug=True)