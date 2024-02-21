from csv import writer, DictReader, reader

import User


def save_user(user_tuple):
    with open('users.csv', 'a') as file:
        csv_writer = writer(file)
        user_dict = {
            'first_name': user_tuple[0],
            'last_name': user_tuple[1],
            'email': user_tuple[2],
            'telephone_number': user_tuple[3],
            'password': user_tuple[4],
            'role': user_tuple[5],
            'id_user': user_tuple[6],
        }
        csv_writer.writerow(user_dict)


def save_news(news_tuple):
    with open('news.csv', 'a') as file:
        csv_writer = writer(file)
        news_dict = {
            'id_news': news_tuple[0],
            'headline': news_tuple[1],
            'body': news_tuple[2],
            'id_author': news_tuple[3],
        }
        csv_writer.writerow(news_dict)


def save_commit(commit_tuple):
    with open('commit.csv', 'a') as file:
        csv_writer = writer(file)
        commit_dict = {
            'id_commit': commit_tuple[0],
            'text_commit': commit_tuple[1],
            'id_author': commit_tuple[2],
            'id_news': commit_tuple[3],
        }
        csv_writer.writerow(commit_dict)


def authentication(email, password) -> object:
    with open('users.csv', 'r') as file:
        csv_reader: dict = DictReader(file)
        for row in csv_reader:
            if row['email'] == email and row['password'] == hash(password):
                return User(*row)


def view_news(id_news):
    with open('news.csv', 'r') as file:
        csv_reader = DictReader(file)
        for row in csv_reader:

            return row[0], 1





