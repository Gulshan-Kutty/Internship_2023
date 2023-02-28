from flask import Flask, render_template, request

app = Flask(__name__)

###############################################

@app.route('/')
def fun_1():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def fun_2():
    return 'Post Request Page'
#OR
'''
@app.route('/', methods=['GET','POST'])
def fun_1():
    if request.method == 'POST':
        return 'Post Request page'
    return render_template('index.html')
'''
###############################################

if __name__ == '__main__':
    app.run(debug=True)