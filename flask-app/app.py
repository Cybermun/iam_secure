from flask import Flask, request, jsonify
import requests, jwt

app = Flask(__name__)

def get_public_key():
    oidc_cfg = requests.get("http://keycloak:8080/realms/demo/.well-known/openid-configuration").json()
    jwks = requests.get(oidc_cfg["jwks_uri"]).json()
    cert = jwks["keys"][0]["x5c"][0]
    return "-----BEGIN CERTIFICATE-----\n" + cert + "\n-----END CERTIFICATE-----"

@app.route("/public")
def public():
    return jsonify({"message": "This is a public endpoint"})

@app.route("/protected")
def protected():
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return jsonify({"error": "Missing token"}), 401
    token = auth.split(" ")[1]
    try:
        decoded = jwt.decode(token, get_public_key(), algorithms=["RS256"], audience="flask-client")
        return jsonify({"message": "Welcome!", "user": decoded.get("preferred_username")})
    except Exception as e:
        return jsonify({"error": "Invalid token", "details": str(e)}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
