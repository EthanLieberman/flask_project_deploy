# controller.py
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.article import Article
from flask_app.models.user import User


@app.route('/')
@app.route('/<none>')
@app.errorhandler(404)
@app.errorhandler(400)
@app.errorhandler(500)
def index(none=None):
    return render_template('index.html',session=session)



@app.route('/register')
def register_page():
    if 'id' in session:
        return redirect('/')
    return render_template('register.html')


@app.route('/register_submit', methods=['post'])
def register_submit():
    if not User.validate_register(request.form):
        return redirect('/register')

    User.save_account(request.form)

    session['id'] = User.get_one_user(request.form).id
    session['username'] = User.get_one_user(request.form).username
    session['admin'] = User.get_one_user(request.form).admin

    return redirect('/')


@app.route('/login')
def login_page():
    if 'id' in session:
        return redirect('/')
    return render_template('login.html')


@app.route('/login_submit', methods=['post'])
def login_submit():
    if not User.login_submit(request.form):
        return redirect('/login')

    session['id'] = User.get_one_user(request.form).id
    session['username'] = User.get_one_user(request.form).username
    session['admin'] = User.get_one_user(request.form).admin

    return redirect('/')


@app.route('/account')
def profile():
    if 'id' not in session:
        redirect('/')

    user_id = {
        'id': session['id']
    }

    total = User.get_total_written(user_id)[0]['total']

    return render_template('profile.html', total=total)

@app.route('/profile_update', methods=['post'])
def profile_update():
    data ={
        'id': session['id'],
        'username': request.form['username']
    }
    if not User.validate_username(data):
        return redirect('/account')

    User.profile_update(data)
    session['username'] = request.form['username']

    return redirect('/account')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')