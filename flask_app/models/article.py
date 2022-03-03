from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import MyCustomDB
import re

from flask_app.models.user import User

VIDEO_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')




class Article:                         # singular instance of...
    def __init__(self,data):
        self.id = data['id']
        self.program = data['program']
        self.title = data['title']
        self.video = data['video']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']






    @staticmethod
    def validate_article(data):

        is_valid = True

        if data['program'] == '':
            flash("Select a program from the list", "create")
            is_valid = False

        if len(data['title']) < 5:
            flash("Title too short", "create")
            is_valid = False

        # if not VIDEO_REGEX.match(data['video']):
        #     flash("Video link not valid", "create")
        #     is_valid = False

        if len(data['comment']) < 20:
            flash("Comments must be longer than 20 characters", "create")
            is_valid = False

        print("runing")
        return is_valid



    @classmethod
    def create_article(cls, data):
        query = "INSERT INTO articles ( program , title , video , comment , created_at , updated_at , user_id ) VALUES ( %(program)s , %(title)s , %(video)s , %(comment)s , NOW() , NOW() , %(user_id)s );"
        return connectToMySQL(MyCustomDB).query_db( query, data )

    @classmethod
    def get_one_article(cls, data):
        query = "SELECT * FROM articles JOIN users ON user_id = users.id WHERE title = %(title)s ;"
        results = connectToMySQL(MyCustomDB).query_db( query, data )

        one_article = cls(results[0])
        one_article.creator = results[0]['username']

        return one_article

    @classmethod
    def get_one_article_id(cls, data):
        query = "SELECT * FROM articles JOIN users ON user_id = users.id WHERE articles.id = %(id)s ;"
        results = connectToMySQL(MyCustomDB).query_db( query, data )

        if results:
            one_article = cls(results[0])
            one_article.creator = results[0]['username']
        else: one_article = False

        

        return one_article



    @classmethod
    def get_all_articles(cls, data):
        query = "SELECT * FROM articles JOIN users ON user_id = users.id WHERE program = %(program)s ;"
        results = connectToMySQL(MyCustomDB).query_db( query, data )

        articles = []

        for row in results:
            this_article = cls(row)

            this_user = row['username']

            this_article.creator = this_user

            articles.append(this_article)

        return articles


    @classmethod
    def update(cls, data):
        query = "UPDATE articles SET program = %(program)s, title = %(title)s, video = %(video)s, comment = %(comment)s, updated_at = NOW() WHERE id = %(id)s "
        print("updating")
        return connectToMySQL(MyCustomDB).query_db( query, data )

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM articles WHERE id = %(id)s"
        return connectToMySQL(MyCustomDB).query_db( query, data )