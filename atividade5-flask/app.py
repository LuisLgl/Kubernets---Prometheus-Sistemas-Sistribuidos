from flask import Flask
import socket, time
app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello from Flask! Hostname: {socket.gethostname()} - {time.time()}"

@app.route("/healthz")
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
