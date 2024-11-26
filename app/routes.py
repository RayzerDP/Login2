from flask import render_template, redirect, session, request, flash, url_for
from app import app, mysql
from app.forms import RegisterForm
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = RegisterForm()
    if form.validate_on_submit():
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id FROM users WHERE email = %s', (form.email.data,))
        user = cursor.fetchone()
        if user:
            flash('El correo ya está registrado.', 'danger')
            return redirect(url_for('index'))

        password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        cursor.execute(
            'INSERT INTO users (first_name, last_name, email, password_hash) VALUES (%s, %s, %s, %s)',
            (form.first_name.data, form.last_name.data, form.email.data, password_hash)
        )
        mysql.connection.commit()
        cursor.close()
        flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id, password_hash FROM users WHERE email = %s', (email,))
        user = cursor.fetchone()
        if user and bcrypt.check_password_hash(user[1], password):
            session['user_id'] = user[0]
            return redirect(url_for('success'))
        flash('Correo o contraseña incorrectos.', 'danger')
    return render_template('login.html')

@app.route('/success')
def success():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('success.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))
