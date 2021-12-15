from flask import Flask
from endpoints import simple_endpoints

app = Flask(__name__)
app.register_blueprint(simple_endpoints)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


