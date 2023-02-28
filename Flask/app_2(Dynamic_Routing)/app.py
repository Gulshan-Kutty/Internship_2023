# Step-1: import
from flask import Flask

# Step-2: Create the object
app = Flask(__name__)

##############################################################
# Step-3: Define the Routes and bind it with functions
@app.route('/')
def index():
    return 'Welcome to this Application!'
    
@app.route('/about')
def about_us():
    return 'This is About us Page'

@app.route('/user/<user_name>') # ex: 127.0.0.1:5000/user/gulshan-kutty-----> Output: Welcome gulshan-kutty!
def user_profile(user_name):
    return 'Welcome {}!'.format(user_name)

##############################################################


# Step-4: Run the app

if __name__ == '__main__':
    app.run(debug=True)
