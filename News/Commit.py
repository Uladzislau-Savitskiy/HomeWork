import time

from User import User
from News import News
import DB


class Commit:
    counter: int = 0

    @classmethod
    def generate_id(cls):
        cls.counter += 1
        return cls.counter

    def __init__(self, id_commit: int, text_commit: str, id_author: int, id_news: int):
        self._id_commit: int = id_commit
        self._text_commit: str = text_commit
        self._id_author: int = id_author
        self._id_news: int = id_news
        self._created_at = time.strftime("%d.%m.%Y")
        self._updated_at = time.strftime("%d.%m.%Y")
        self._deleted_at = None

    @classmethod
    def creat_commit(cls, id_news: int, id_author: int) -> object:
        info_commit: tuple = cls.enter_parameters(id_news, id_author)
        DB.save_commit(info_commit)
        return Commit(*info_commit)

    @staticmethod
    def enter_parameters(id_news: int, id_author: int) -> tuple:
        text_commit = input("Enter text: ")
        id_commit: int = Commit.generate_id()
        return id_commit, text_commit, id_author, id_news

