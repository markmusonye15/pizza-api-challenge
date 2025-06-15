from flask import Flask


app = Flask(__name__)

@app.route('/')
def welcome():
    print( "Welcome to the Flask app!")

    
    return"<p>Welcome to the Flask app!</p>"

@app.route('/users')
def fetch_all_users():
    print( "Fetching all users...")
    return "<p>Fetching all users...</p>"

@app.route('/meals')
def fetch_all_meals():
    print("Fetching all meals...")
    return "<p>Fetching all meals...</p>"

if __name__ == '__main__':
    app.run()
