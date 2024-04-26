from flask import Flask, request, jsonify, config

app = Flask(__name__)

# Existing user data (replace with your data storage logic)
users = {}

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/images", methods=["GET"])
def get_images():
    user_id = request.args.get("userId")
    if not user_id:
        return jsonify({"error": "Missing userId parameter"}), 400
    # Assuming image path is always "good-selfie.jpg" for this user
    image_path = "good-selfie.jpg"

    # Set STATIC_URL based on environment (adjust as needed)
    if config.get("ENV") == "development":
        # Use an empty string for dev (assuming static at app root)
        image_url = f"static/{image_path}"
    else:
        # Replace with the actual production URL for static files
        image_url = f"https://cvardi-bi-back.onrender.com/static/{image_path}"

    return jsonify({"imageUrl": image_url})

@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing data in request body"}), 400
    required_fields = {"image", "id", "username"}
    missing_fields = required_fields - set(data.keys())
    if missing_fields:
        return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400
    # Replace this with logic to store user data
    # (e.g., database insert, file system storage)
    users[data["id"]] = data
    return jsonify({"success": True})

if __name__ == "__main__":
    # Configure the static folder location (adjust as needed)
    app.config['STATIC_FOLDER'] = 'static'

    # Set a default environment variable for development
    if not config.get("ENV"):
        app.config["ENV"] = "development"

    app.run(debug=True)

