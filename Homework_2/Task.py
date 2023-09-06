from flask import Flask, request, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = '5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username', 'email')
        return redirect(url_for('hello', username=session['username']))
    return render_template('login.html')


@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
