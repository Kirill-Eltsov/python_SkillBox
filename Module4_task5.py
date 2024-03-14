from flask import Flask, request, jsonify
import subprocess
import shlex

app = Flask(__name__)

@app.route('/ps')
def execute_ps_command():
    args = request.args.getlist('arg')
    clean_args = [shlex.quote(arg) for arg in args]
    command = ['ps'] + clean_args
    result = subprocess.run(command, capture_output=True, text=True)
    return f"<pre>{result.stdout}</pre>"


if __name__ == '__main__':
    app.run(debug=True)
