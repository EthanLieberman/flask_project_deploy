from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.article import Article
from datetime import datetime

from flask_app.models.user import User

date_format = "%I:%M %p %m/%d/%Y"



@app.route('/create_article')
def create_new():
    return render_template('new_article.html')


@app.route('/create_submit', methods=['post'])
def create_submit():
    
    if not Article.validate_article(request.form):
        return redirect('/create_article')

    # incoming_url = request.form['video']
    # print(incoming_url)

    # if 'youtube' in incoming_url:
    #     sliced_text = slice(32, 62)

    # if 'youtu.be' in incoming_url:
    #     sliced_text = slice(17, 47)

    # yt_format = 'https://www.youtube.com/embed/'
    # print(yt_format + incoming_url[sliced_text])

    save_data = {
        'program': request.form['program'],
        'title': request.form['title'],
        'video': request.form['video'],
        'comment': request.form['comment'],
        # 'comment': yt_format + incoming_url[sliced_text],
        'user_id': session['id'],
    }

    Article.create_article(save_data)
    session['last_article'] = save_data


    return redirect('/')

@app.route('/edit/<int:id>')
def edit_article(id):
    if 'id' not in session:
        return redirect('/')
    article_edit = {
        'id': id
    }
    article = Article.get_one_article_id(article_edit)

    if article:
        if article.creator != session['username'] and session['admin'] == 0:
            return redirect('/')
    else:
        return redirect('/')

    return render_template('edit_article.html', article=article)


@app.route('/edit_submit',methods=['post'])
def edit_submit():
    print("*******")
    print(Article.validate_article(request.form))
    print("*******")
    if not Article.validate_article(request.form):
        print("fasle")
        print(request.form['id'])
        return redirect(f'/edit/{request.form["id"]}')

    Article.update(request.form)
    print(request.form['id'])
    
    return redirect(f'/{request.form["program"]}')


@app.route('/delete/<int:id>')
def delete(id):
    program_id = {
        'id': id,
    }

    Article.delete(program_id)


    return redirect('/')
    
# ****************Directories******************************

@app.route('/photoshop')
def photoshop():
    program_name = {
        'program': 'photoshop'
    }

    programs = Article.get_all_articles(program_name)

    return render_template('articles.html', programs=programs, name=program_name['program'], date_format=date_format)

@app.route('/illustrator')
def illustrator():
    program_name = {
        'program': 'illustrator'
    }

    programs = Article.get_all_articles(program_name)

    return render_template('articles.html', programs=programs, name=program_name['program'], date_format=date_format)

@app.route('/blender')
def blender():
    program_name = {
        'program': 'blender'
    }

    programs = Article.get_all_articles(program_name)

    return render_template('articles.html', programs=programs, name=program_name['program'], date_format=date_format)

@app.route('/substancepainter')
def substancepainter():
    program_name = {
        'program': 'substancepainter'
    }

    programs = Article.get_all_articles(program_name)

    return render_template('articles.html', programs=programs, name=program_name['program'], date_format=date_format)

@app.route('/solidworks')
def solidworks():
    program_name = {
        'program': 'solidworks'
    }

    programs = Article.get_all_articles(program_name)

    return render_template('articles.html', programs=programs, name=program_name['program'], date_format=date_format)

@app.route('/unity')
def unity():
    program_name = {
        'program': 'unity'
    }

    programs = Article.get_all_articles(program_name)

    return render_template('articles.html', programs=programs, name=program_name['program'], date_format=date_format)

@app.route('/premierpro')
def premierpro():
    program_name = {
        'program': 'premierpro'
    }

    programs = Article.get_all_articles(program_name)

    return render_template('articles.html', programs=programs, name=program_name['program'], date_format=date_format)

@app.route('/python')
def python():
    program_name = {
        'program': 'python'
    }

    programs = Article.get_all_articles(program_name)

    return render_template('articles.html', programs=programs, name=program_name['program'], date_format=date_format)

@app.route('/html')
def html():
    program_name = {
        'program': 'html'
    }

    programs = Article.get_all_articles(program_name)

    return render_template('articles.html', programs=programs, name=program_name['program'], date_format=date_format)

# ****************Directories******************************


#****************Articles**********************************


@app.route('/photoshop/<article>')
def photoshop_article(article):
    article_title = {
        'title': article
    }

    one_article = Article.get_one_article(article_title)

    return render_template('one_article.html', article=one_article, date_format=date_format)

@app.route('/illustrator/<article>')
def illustrator_article(article):
    article_title = {
        'title': article
    }

    one_article = Article.get_one_article(article_title)

    return render_template('one_article.html', article=one_article, date_format=date_format)

@app.route('/blender/<article>')
def blender_article(article):
    article_title = {
        'title': article
    }

    one_article = Article.get_one_article(article_title)

    return render_template('one_article.html', article=one_article, date_format=date_format)

@app.route('/substancepainter/<article>')
def substancepainter_article(article):
    article_title = {
        'title': article
    }

    one_article = Article.get_one_article(article_title)

    return render_template('one_article.html', article=one_article, date_format=date_format)

@app.route('/solidworks/<article>')
def solidworks_article(article):
    article_title = {
        'title': article
    }

    one_article = Article.get_one_article(article_title)

    return render_template('one_article.html', article=one_article, date_format=date_format)

@app.route('/unity/<article>')
def unity_article(article):
    article_title = {
        'title': article
    }

    one_article = Article.get_one_article(article_title)

    return render_template('one_article.html', article=one_article, date_format=date_format)

@app.route('/premierpro/<article>')
def premierpro_article(article):
    article_title = {
        'title': article
    }

    one_article = Article.get_one_article(article_title)

    return render_template('one_article.html', article=one_article, date_format=date_format)

@app.route('/python/<article>')
def python_article(article):
    article_title = {
        'title': article
    }

    one_article = Article.get_one_article(article_title)

    return render_template('one_article.html', article=one_article, date_format=date_format)

@app.route('/html/<article>')
def html_article(article):
    article_title = {
        'title': article
    }

    one_article = Article.get_one_article(article_title)

    return render_template('one_article.html', article=one_article, date_format=date_format)

#****************Articles**********************************

# @app.route('/<user>/articles')
# def user_articles(user):
#     username = {
#         'username': user
#     }

#     user_articles = Article.get_all_articles_by_user(username)

#     return render_template('articles.html', programs=user_articles, name=username, date_format=date_format)