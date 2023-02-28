# Step-1: import
from flask import Flask

# Step-2: Create the object
app = Flask(__name__)

users = ['dhruv-dixit', 'azhaku', 'soham-jondhale', 'gaikwadpallavi']

##############################################################
# Step-3: Define the Routes and bind it with functions
@app.route('/')
def index():
    return 'Welcome to this Application!'
    
@app.route('/about')
def about_us():
    return 'This is About us Page'

@app.route('/user/<user_name>')
def user_profile(user_name):
    if user_name in users:
        return 'Welcome {}!'.format(user_name)

    return 'Please Register'
##############################################################

# Step-4: Run the app

if __name__ == '__main__':
    app.run(debug=True)
