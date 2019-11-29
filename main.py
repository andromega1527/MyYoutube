from flask import Flask, request, render_template

app = Flask('youtube')


@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)