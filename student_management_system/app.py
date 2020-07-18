from flask import Flask, render_template

app = Flask(__name__)

@app.route('/first_page')
def first_page():
    return render_template('first_page.html')

if __name__ == '__main__':
    app.run()