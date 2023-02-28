from flask import Flask, render_template,request

app = Flask(__name__)
##########################################################

@app.route('/')
def index_function():
    return render_template('index.html')

@app.route('/thankyou',methods=['post'])
def thankyou_function():
    return render_template('thank_you.html')

@app.route('/contact_us')
def contact_function():
    return render_template('contact.html')


##########################################################
if __name__ == '__main__':
    app.run(debug=True)


