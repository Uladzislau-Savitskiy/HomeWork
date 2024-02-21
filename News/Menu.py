from User import User
from News import News
from Commit import Commit


class MenuMixin:

    @staticmethod
    def creat_news(author):
        News.creat_news(author)

    @staticmethod
    def edit_news():
        pass

    @staticmethod
    def delete_news():
        pass

    @staticmethod
    def rate_the_news():
        pass

    @staticmethod
    def view_news():
        pass

    @staticmethod
    def approve_news():
        pass

    @staticmethod
    def view_comments():
        pass

    @staticmethod
    def edit_comment():
        pass

    @staticmethod
    def delete_comment():
        pass

    @staticmethod
    def create_moderator():
        pass

    @staticmethod
    def delete_moderator():
        pass

    @staticmethod
    def view_users():
        pass

    @staticmethod
    def delete_user():
        pass

    @staticmethod
    def exit():
        pass

