from flask import Flask, render_template, request

app = Flask(__name__)

available_pages = [
    ('Home', '/'),
    ('About', '/about'),
    ('Contact', '/contact')
]


@app.errorhandler(404)
def page_not_found(e):
    requested_url = request.url
    return render_template('404.html', requested_url=requested_url, available_pages=available_pages), 404


@app.route('/')
def home():
    return 'Welcome to the Home page!'


@app.route('/about')
def about():
    return 'This is the About page.'


@app.route('/contact')
def contact():
    return 'You can contact us here.'


if __name__ == '__main__':
    app.run()
