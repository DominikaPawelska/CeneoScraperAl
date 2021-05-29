



from flask import Flask

app = Flask(__name__)
from app import routes



# import of routings (routes module) form app package

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8081)
