from flask import Flask

app = Flask(__name__)

# Main route — returns a simple HTML page
@app.route("/")
def home():
    return """
    <h1>CI/CD Pipeline — Stephen Cotton</h1>
    <p>Deployed automatically via GitHub Actions to AWS ECS Fargate</p>
    <p>Every push to main triggers a new build and deployment</p>
    """

# Health check route — ECS uses this to confirm the container is running
@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
