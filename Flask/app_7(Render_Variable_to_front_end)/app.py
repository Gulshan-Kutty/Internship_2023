from flask import Flask, render_template,request

app = Flask(__name__)
##########################################################

@app.route('/')
def index_function():
    return render_template('index.html')

@app.route('/thankyou',methods=['post'])
def thankyou_function():
    name = request.form['in_1'] # we captured the data from frontend to backend
    age = request.form['in_2'] # we captured the data from frontend to backend
    return render_template('thank_you.html',n=name, a=age) # here we also need to return these 2 variables to render to frontend(i.e to any other page)

@app.route('/contact_us')
def contact_function():
    return render_template('contact.html')


##########################################################
if __name__ == '__main__':
    app.run(debug=True)


