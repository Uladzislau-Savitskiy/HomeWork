import time


class User:
    counter: int = 0

    @classmethod
    def generate_user_id(cls):
        cls.counter += 1
        return cls.counter

    def __init__(self, first_name, last_name, email, telephone_number, password, password_reset, role, user_id):
        self._first_name: str = first_name
        self._last_name: str = last_name
        self._email: str = email
        self._telephone_number: str = telephone_number
        self._id_user = user_id
        self._password = hash(password)
        self._password_reset = hash(password_reset)
        self._created_at = time.strftime("%d.%m.%Y")
        self._updated_at = time.strftime("%d.%m.%Y")
        self._role: str = role
        self._deleted_at = None
        self._rating = 0

    def get_id_user(self):
        return self._id_user

    def __repr__(self):
        return f"""{self._id_user}:
        First Name: {self._first_name},
        Last Name: {self._last_name},
        Email: {self._email},
        Telephone Number: {self._telephone_number},
        Role: {self._role},
        Created At: {self._created_at},
        Updated At: {self._updated_at},
        Rating: {self._rating}."""

    @classmethod
    def register_user(cls):
        user_info = cls.register_enter_parameters()
        first_name, last_name, email, telephone, password, password_again, role, user_id = user_info
        new_user = User(first_name, last_name, email, telephone, password, password_again, role, user_id)
        return new_user

    @staticmethod
    def register_enter_parameters():
        user_id = User.generate_user_id()
        first_name: str = input("Enter your first name: ")
        last_name: str = input("Enter your last name: ")
        email: str = input("Enter your email address: ")
        telephone: int = int(input("Enter your telephone number: "))
        while True:
            password = input("Enter your password: ")
            password_again = input("Enter your password again: ")
            if password != password_again:
                print("Passwords do not match")
                continue
            else:
                break
        role: str = "admin" if user_id == 1 else "user"
        return first_name, last_name, email, telephone, password, password_again, role, user_id


class News:
    counter: int = 0

    @classmethod
    def generate_news_id(cls):
        cls.counter += 1
        return cls.counter

    def __init__(self, news_id: int, headline: str, body: str, id_author):
        self._id_news: int = news_id
        self._headline: str = headline
        self._body: str = body
        self._id_author: int = id_author
        self._created_at = time.strftime("%d.%m.%Y")
        self._updated_at = time.strftime("%d.%m.%Y")
        self._deleted_at = None

    def get_id_news(self):
        return self._id_news

    def __repr__(self):
        return f"""{self._id_news}:
            Headline: {self._headline},
            Body: {self._body},
            Author: {self._id_author},
            Created At: {self._created_at},
            Updated At: {self._updated_at}."""

    @classmethod  # Создание новой новости
    def add_new_news(cls, id_author):
        news_info = cls.register_enter_parameters()
        headline, body = news_info
        new_news = News(headline, body, id_author)
        return new_news

    @staticmethod  # Создание новой новости
    def register_enter_parameters():
        headline = input("Enter headline: ")
        body = input("Enter news body: ")
        return headline, body


class Commit:
    counter: int = 0

    @classmethod
    def generate_news_id(cls):
        cls.counter += 1
        return cls.counter

    def __init__(self, id_commit: int, text_commit: str, author: int, id_news: int):
        self._id_commit: int = id_commit
        self._text_commit: str = text_commit
        self._id_author: int = author
        self._id_news: int = id_news
        self._created_at = time.strftime("%d.%m.%Y")
        self._updated_at = time.strftime("%d.%m.%Y")
        self._deleted_at = None

    def __repr__(self):
        return f"""{self._id_commit}:
            Text commit: {self._text_commit},
            Author: {self._id_author},
            News: {self._id_news},
            Created At: {self._created_at},
            Updated At: {self._updated_at}."""

    @classmethod  # Создание новой новости
    def add_new_commit(cls, author_id, news_id):
        commit_info = cls.get_commit_info()
        text_commit = commit_info
        new_commit = Commit(text_commit, author_id, news_id)
        return new_commit

    @staticmethod  # Создание новой новости
    def get_commit_info():
        text = input("Enter text commit: ")
        return text


# user = User.register_user()

# Создание новости
# news = News.add_new_news(user.get_id_user())
User.register_user()
