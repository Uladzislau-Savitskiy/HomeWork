import time
import DB
import re
import phonenumbers


class User:
    counter: int = 0

    @classmethod
    def generate_user_id(cls):
        cls.counter += 1
        return cls.counter

    def __init__(self, first_name: str, last_name: str, email: str,
                 phone_number: str, password: str, role: str,
                 id_user: int):
        self._first_name: str = first_name
        self._last_name: str = last_name
        self._email: str = email
        self._phone_number: str = phone_number
        self._id_user: int = id_user
        self._password = hash(password)
        self._created_at = time.strftime("%d.%m.%Y")
        self._updated_at = time.strftime("%d.%m.%Y")
        self._role: str = role
        self._deleted_at = None
        self._rating = 0

    @staticmethod
    def register_user() -> object:
        user_info: tuple = User.enter_parameters()
        DB.save_user(user_info)
        return User(*user_info)

    @staticmethod
    def enter_parameters() -> tuple:
        id_user: int = User.generate_user_id()
        first_name: str = input("Enter your first name: ")
        last_name: str = input("Enter your last name: ")
        email: str = User.validate_email()
        phone_number: str = User.validate_phone_number()
        while True:
            password: str = User.validate_password()
            if not password:
                continue
            password_again: str = input("Enter your password again: ")
            if password != password_again:
                print("Passwords do not match")
                continue
            else:
                break
        role: str = 'admin' if id_user == 1 else 'author'
        return first_name, last_name, email, phone_number, password, role, id_user

    @staticmethod
    def validate_email() -> str:
        while True:
            email: str = input("Enter your email address: ")
            pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if not re.match(pattern, email):
                print('Invalid email format')
            else:
                return email

    @staticmethod
    def validate_phone_number() -> str:
        while True:
            try:
                phone_number: str = input("Enter your telephone number: ")
                parsed_number = phonenumbers.parse(phone_number, None)
                if phonenumbers.is_valid_number(parsed_number):
                    return phone_number
            except phonenumbers.phonenumberutil.NumberParseException:
                print('Invalid phone number')
                continue

    @staticmethod
    def validate_password() -> str or bool:
        password: str = input("Enter your password: ")
        # Проверка длины пароля (минимум 8 символов)
        if len(password) < 8:
            print('Invalid password format')
            return False
        # Проверка наличия хотя бы одной цифры
        if not any(char.isdigit() for char in password):
            print('Invalid password format')
            return False
        # Проверка наличия хотя бы одной буквы в верхнем регистре
        if not any(char.isupper() for char in password):
            print('Invalid password format')
            return False
        # Проверка наличия хотя бы одной буквы в нижнем регистре
        if not any(char.islower() for char in password):
            print('Invalid password format')
            return False

        return password

