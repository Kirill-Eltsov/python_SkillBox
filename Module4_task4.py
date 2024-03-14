from datetime import *

from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/uptime')
def get_uptime():
    uptime_seconds = psutil.boot_time()
    uptime_string = str(datetime.now() - datetime.fromtimestamp(uptime_seconds))
    return jsonify(f"Current uptime is {uptime_string}")


if __name__ == "__main__":
    app.run(debug=True)