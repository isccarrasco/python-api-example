from flask import Flask
from apis import blueprint as api

# Create Flask instance
app = Flask(__name__)

# Register Blueprint
app.register_blueprint(api)

# Not needed when using Blueprint
# Blueprint manages the initialization of the endpoints
# api.init_app(app)

# Run app
app.run(debug=True)