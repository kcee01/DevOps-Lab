# Import the Flask framework
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define the route for the home page ("/")
@app.route("/")
def home():
    # Return a simple HTML page when the root URL is accessed
    return """
    <h1>DevOps Phase 0</h1>
    <p>Application is running successfully!</p>
    """

# Define a health check endpoint
@app.route("/health")
def health():
    # Return a JSON response indicating that the application is healthy
    return {
        "status": "healthy"
    }

# Start the Flask development server only when this file is run directly
if __name__ == "__main__":
    # Listen on all network interfaces (0.0.0.0) using port 5000
    app.run(host="0.0.0.0", port=5000)
