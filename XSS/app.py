from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # reflected XSS demo: read 'q' and render it unsafely in the template
    q = request.args.get('q', '')
    return render_template('index.html', q=q)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
