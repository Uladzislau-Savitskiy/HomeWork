import csv
from datetime import datetime
from passlib.hash import sha256_crypt


class User:
    def __init__(self, user_id, first_name, last_name, phone, email, password, role='author', created_at=None,
                 updated_at=None, deleted_at=None, rating=0):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.password = password
        self.role = role
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
        self.deleted_at = deleted_at
        self.rating = rating

    @staticmethod
    def hash_password(password):
        return sha256_crypt.hash(password)

    def verify_password(self, password):
        return sha256_crypt.verify(password, self.password)

    def save(self):
        with open('users.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.user_id, self.first_name, self.last_name, self.phone, self.email,
                             self.password, self.role, self.created_at, self.updated_at, self.deleted_at,
                             self.rating])

    @staticmethod
    def get_all():
        with open('users.csv', 'r') as file:
            reader = csv.reader(file)
            users = []
            for row in reader:
                user = User(*row)
                users.append(user)
            return users

    def update(self):
        users = User.get_all()
        for i, user in enumerate(users):
            if user.user_id == self.user_id:
                users[i] = self
                break
        User.save_all(users)

    @staticmethod
    def save_all(users):
        with open('users.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for user in users:
                writer.writerow([user.user_id, user.first_name, user.last_name, user.phone, user.email,
                                 user.password, user.role, user.created_at, user.updated_at, user.deleted_at,
                                 user.rating])

    def delete(self):
        users = User.get_all()
        for i, user in enumerate(users):
            if user.user_id == self.user_id:
                del users[i]
                break
        User.save_all(users)


class News:
    def __init__(self, news_id, title, body, author_id, created_at=None, updated_at=None, deleted_at=None):
        self.news_id = news_id
        self.title = title
        self.body = body
        self.author_id = author_id
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
        self.deleted_at = deleted_at

    def save(self):
        with open('news.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.news_id, self.title, self.body, self.author_id, self.created_at,
                             self.updated_at, self.deleted_at])

    @staticmethod
    def get_all():
        with open('news.csv', 'r') as file:
            reader = csv.reader(file)
            news_list = []
            for row in reader:
                news = News(*row)
                news_list.append(news)
            return news_list

    def update(self):
        news_list = News.get_all()
        for i, news in enumerate(news_list):
            if news.news_id == self.news_id:
                news_list[i] = self
                break
        News.save_all(news_list)

    @staticmethod
    def save_all(news_list):
        with open('news.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for news in news_list:
                writer.writerow([news.news_id, news.title, news.body, news.author_id, news.created_at,
                                 news.updated_at, news.deleted_at])

    def delete(self):
        news_list = News.get_all()
        for i, news in enumerate(news_list):
            if news.news_id == self.news_id:
                del news_list[i]
                break
        News.save_all(news_list)


class Comment:
    def __init__(self, comment_id, text, author_id, news_id, created_at=None, updated_at=None, deleted_at=None):
        self.comment_id = comment_id
        self.text = text
        self.author_id = author_id
        self.news_id = news_id
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
        self.deleted_at = deleted_at

    def save(self):
        with open('comments.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.comment_id, self.text, self.author_id, self.news_id, self.created_at,
                             self.updated_at, self.deleted_at])

    @staticmethod
    def get_all():
        with open('comments.csv', 'r') as file:
            reader = csv.reader(file)
            comments = []
            for row in reader:
                comment = Comment(*row)
                comments.append(comment)
            return comments

    def update(self):
        comments = Comment.get_all()
        for i, comment in enumerate(comments):
            if comment.comment_id == self.comment_id:
                comments[i] = self
                break
        Comment.save_all(comments)

    @staticmethod
    def save_all(comments):
        with open('comments.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for comment in comments:
                writer.writerow([comment.comment_id, comment.text, comment.author_id, comment.news_id,
                                 comment.created_at, comment.updated_at, comment.deleted_at])

    def delete(self):
        comments = Comment.get_all()
        for i, comment in enumerate(comments):
            if comment.comment_id == self.comment_id:
                del comments[i]
                break
        Comment.save_all(comments)


class Menu:
    def __init__(self, user):
        self.user = user

    def register_user(self):
        user_id = input("Enter user ID: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        password = User.hash_password(input("Enter password: "))
        role = 'user'
        new_user = User(user_id, first_name, last_name, phone, email, password, role)
        new_user.save()
        print("Registration successful. You can now log in.")

    def display_menu(self):
        print("-------- News Management System --------")
        print("1. View News")
        print("2. Delete News")
        print("3. View Comments")
        print("4. Delete Comment")
        if self.user.role == 'admin':
            print("5. Create Moderator")
            print("6. Delete Moderator")
            print("7. View Users")
            print("8. Delete User")
        print("0. Exit")

        choice = input("Enter your choice: ")
        if self.user.role == 'admin':
            if choice == '1':
                self.view_news()
            elif choice == '2':
                self.delete_news()
            elif choice == '3':
                self.view_comments()
            elif choice == '4':
                self.delete_comment()
            elif choice == '5':
                self.create_moderator()
            elif choice == '6':
                self.delete_moderator()
            elif choice == '7':
                self.view_users()
            elif choice == '8':
                self.delete_user()
            elif choice == '0':
                exit()
            else:
                print("Invalid choice. Please try again.")
        else:
            if choice == '1':
                self.view_news()
            elif choice == '2':
                self.delete_news()
            elif choice == '3':
                self.view_comments()
            elif choice == '4':
                self.delete_comment()
            elif choice == '0':
                exit()
            else:
                print("Invalid choice. Please try again.")

    def view_news(self):
        news_list = News.get_all()
        for news in news_list:
            print(f"News ID: {news.news_id}")
            print(f"Title: {news.title}")
            print(f"Body: {news.body}")
            print("-----")

    def delete_news(self):
        news_id = input("Enter news ID to delete: ")
        news_list = News.get_all()
        for news in news_list:
            if news.news_id == news_id:
                news.delete()
                print("News deleted successfully.")
                break
        else:
            print("News not found.")

    def view_comments(self):
        comments = Comment.get_all()
        for comment in comments:
            print(f"Comment ID: {comment.comment_id}")
            print(f"Text: {comment.text}")
            print(f"Author ID: {comment.author_id}")
            print(f"News ID: {comment.news_id}")
            print("-----")

    def delete_comment(self):
        comment_id = input("Enter comment ID to delete: ")
        comments = Comment.get_all()
        for comment in comments:
            if comment.comment_id == comment_id:
                comment.delete()
                print("Comment deleted successfully.")
                break
        else:
            print("Comment not found.")

    def create_moderator(self):
        user_id = input("Enter user ID: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        password = User.hash_password(input("Enter password: "))
        role = 'moderator'
        moderator = User(user_id, first_name, last_name, phone, email, password, role)
        moderator.save()
        print("Moderator created successfully.")

    def delete_moderator(self):
        user_id = input("Enter moderator ID to delete: ")
        users = User.get_all()
        for user in users:
            if user.user_id == user_id and user.role == 'moderator':
                user.delete()
                print("Moderator deleted successfully.")
                break
        else:
            print("Moderator not found.")

    def view_users(self):
        users = User.get_all()
        for user in users:
            print(f"User ID: {user.user_id}")
            print(f"First Name: {user.first_name}")
            print(f"Last Name: {user.last_name}")
            print(f"Phone: {user.phone}")
            print(f"Email: {user.email}")
            print(f"Role: {user.role}")
            print("-----")

    def delete_user(self):
        user_id = input("Enter user ID to delete: ")
        users = User.get_all()
        for user in users:
            if user.user_id == user_id:
                user.delete()
                print("User deleted successfully.")
                break
        else:
            print("User not found.")


class Menu:
    # ... предыдущий код ...

    def view_news(self):
        news_list = News.get_all()
        for news in news_list:
            print(f"News ID: {news.news_id}")
            print(f"Title: {news.title}")
            print(f"Body: {news.body}")
            print("-----")

    def delete_news(self):
        news_id = input("Enter news ID to delete: ")
        news_list = News.get_all()
        for news in news_list:
            if news.news_id == news_id:
                news.delete()
                print("News deleted successfully.")
                break
        else:
            print("News not found.")

    def view_comments(self):
        comments = Comment.get_all()
        for comment in comments:
            print(f"Comment ID: {comment.comment_id}")
            print(f"Text: {comment.text}")
            print(f"Author ID: {comment.author_id}")
            print(f"News ID: {comment.news_id}")
            print("-----")

    def delete_comment(self):
        comment_id = input("Enter comment ID to delete: ")
        comments = Comment.get_all()
        for comment in comments:
            if comment.comment_id == comment_id:
                comment.delete()
                print("Comment deleted successfully.")
                break
        else:
            print("Comment not found.")

    def create_moderator(self):
        user_id = input("Enter user ID: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        password = User.hash_password(input("Enter password: "))
        role = 'moderator'
        moderator = User(user_id, first_name, last_name, phone, email, password, role)
        moderator.save()
        print("Moderator created successfully.")

    def delete_moderator(self):
        user_id = input("Enter moderator ID to delete: ")
        users = User.get_all()
        for user in users:
            if user.user_id == user_id and user.role == 'moderator':
                user.delete()
                print("Moderator deleted successfully.")
                break
        else:
            print("Moderator not found.")

    def view_users(self):
        users = User.get_all()
        for user in users:
            print(f"User ID: {user.user_id}")
            print(f"First Name: {user.first_name}")
            print(f"Last Name: {user.last_name}")
            print(f"Phone: {user.phone}")
            print(f"Email: {user.email}")
            print(f"Role: {user.role}")
            print("-----")

    def delete_user(self):
        user_id = input("Enter user ID to delete: ")
        users = User.get_all()
        for user in users:
            if user.user_id == user_id:
                user.delete()
                print("User deleted successfully.")
                break
        else:
            print("User not found.")


def main():
    user_id = input("Enter your user ID: ")
    password = input("Enter your password: ")

    users = User.get_all()
    for user in users:
        if user.user_id == user_id and user.verify_password(password):
            menu = Menu(user)
            while True:
                menu.display_menu()
        else:
            print("Invalid credentials. Please try again.")


if __name__ == "__main__":
    main()
