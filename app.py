from flask import Flask, request, jsonify

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
    # Replace this with logic to retrieve images based on user_id
    # (e.g., database lookup, file system access)
    images = []  # Replace with actual image data
    return jsonify({"images": images})

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
    app.run(debug=True)

