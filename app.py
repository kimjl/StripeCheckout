from flask import Flask, render_template, request, redirect, url_for
import stripe

app = Flask(__name__)

pub_key = 'YOURKEY'
secret_key = 'YOURSECRET'
stripe.api_key = secret_key

@app.route('/')
def index():
    return render_template('index.html', pub_key=pub_key)

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/pay', methods=['POST'])
def pay():
    # print(request.form)
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])
    charge = stripe.Charge.create(customer=customer.id, amount=1999, currency='usd', description='The Product')
    return redirect(url_for('thanks'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)