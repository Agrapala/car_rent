from flask import Flask
import requests

app = Flask(__name__)
BACKEND_URL = "http://backend:8000"

@app.route("/")
def home():
    try:
        response = requests.get(f"{BACKEND_URL}/cars", timeout=3)
        cars = response.json()
    except Exception as e:
        return f"<h2>Backend not reachable</h2><p>{e}</p>", 500

    html = "<h1>Car Rental Shop</h1><ul>"
    for car in cars:
        status = "Available" if car["available"] else "Rented"
        html += f"<li>{car['name']} - {status}</li>"
    html += "</ul>"
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
