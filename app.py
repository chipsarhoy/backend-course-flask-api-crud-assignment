import os
from flask import Flask

import routes 

flask_host = os.environ.get("FLASK_HOST")
flask_port = os.environ.get("FLASK_PORT")

app = Flask(__name__)
app.register_blueprint(routes.products)

if __name__ == "__main__":
    app.run(host=flask_host, port=flask_port)