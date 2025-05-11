from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated broker login logic
def angelone_login(user_data):
    return {"message": f"AngelOne login successful for {user_data['username']}"}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
    elif request.method == 'GET':
        data = request.args

    username = data.get("username")
    broker = data.get("broker")

    if not username or not broker:
        return jsonify({"error": "Missing required parameters"}), 400

    if broker == "angelone":
        return jsonify(angelone_login(data))
    else:
        return jsonify({"error": "Unsupported broker"}), 400

if __name__ == '__main__':
    app.run(debug=True)
