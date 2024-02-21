import time

# from User import User
import DB


class News:
    counter: int = 0

    @classmethod
    def id_generate(cls):
        cls.counter += 1
        return cls.counter

    def __init__(self, id_news: int, headline: str, body: str, id_author: int):
        self._id_news: int = id_news
        self._headline: str = headline
        self._body: str = body
        self._id_author: int = id_author
        self._created_at = time.strftime("%d.%m.%Y")
        self._updated_at = time.strftime("%d.%m.%Y")
        self._deleted_at = None

    @classmethod
    def creat_news(cls, id_author: int) -> object:
        info_news = cls.enter_parameters(id_author)
        DB.save_news(info_news)
        news = News(*info_news)
        # DB.save_news1(news)
        return news

    @staticmethod
    def enter_parameters(id_author: int) -> tuple:
        headline = input("Enter headline: ")
        body = input("Enter news body: ")
        id_news: int = News.id_generate()
        return id_news, headline, body, id_author


news = News.creat_news(12)