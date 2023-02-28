from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route('/',methods = ['GET','POST'])
def index_page():
    
    if request.method == 'POST':
        #Capturing the data from the frontend
        reg_exp = request.form['reg_exp']  
        txt = request.form['txt']

       # Finding matches and total no. of matches 
        result = re.findall(reg_exp, txt)
        count = len(result)   

        #returning the variables from the backend so that we can display it back to the frontend
        return render_template('index.html', c=count,r=result,t=txt,reg=reg_exp)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)




    
