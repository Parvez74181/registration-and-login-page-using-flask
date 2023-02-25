from flask import Flask, request, render_template

app = Flask(__name__)

users = {}  # this set is for database alternative


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        user_name = request.form.get('user-name')
        user_address = request.form.get('user-address')
        user_email = request.form.get('user-email')
        user_password = request.form.get('user-password')
        user_confirm_password = request.form.get('user-confirm-password')

    try:
        if user_password == user_confirm_password:
            for i in users:
                if users[i]['email'] == user_email:
                    return render_template('index.html', err_msg='Email already exist!', user_name=user_email, user_address=user_address, user_email=user_email)

            users[user_name] = {
                'address': user_address,
                'email': user_email,
                'password': user_password
            }

            return render_template('login.html')
        else:
            error = "password dosen't matched"
            return render_template('index.html', error=error, user_name=user_email, user_address=user_address, user_email=user_email)

    except Exception as e:
        print('error - ', e)
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == "POST":
            user_email = request.form.get('user-email')
            user_password = request.form.get('user-password')
            for i in users:
                if (users[i]['email']) == user_email and (users[i]['password']) == user_password:
                    return render_template('login.html', succ_msg='Login Successfull...')
                else:
                    return render_template('login.html', err_msg='Invalid login details!', user_email=user_email, user_password=user_password)

    except Exception as e:
        print(e)

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
