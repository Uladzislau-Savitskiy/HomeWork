"Проблема в  def all_value_card класса User "

import random
import time


class User:

    def __init__(self, name: str):
        self.__name: str = name
        self.__cards_user: list[Card] = []

    def get_name(self):
        return self.__name

    def del_cards_user(self):
        self.__cards_user = []

    def total(self) -> int:
        return sum(card.get_value() for card in self.__cards_user)

    def handle_ace_value(self, new_card):
        if new_card.get_rank() == 'A':
            if len(self.__cards_user) == 1 and self.__cards_user[0].get_rank() == 'A':
                return True
            elif len(self.__cards_user) > 2 and any(card.get_rank() == 'A' for card in self.__cards_user):
                new_card.set_value(1)

    def draw_card(self, deck) -> None:
        card = deck.draw_card()
        self.__cards_user.append(card)
        print(card)


class Card:

    def __init__(self, rank: str, suit: str):
        self.__rank: str = rank
        self.__suit: str = suit
        self._value: int = self.value_card(rank)

    def __repr__(self) -> str:
        if self.__rank != '10':
            new_style: str = f'''
            ┌─────────────┐
            │ {self.__rank}           │
            │             │
            │             │
            │      {self.__suit}      │
            │             │
            │             │
            │           {self.__rank} │
            └─────────────┘
            '''
            return new_style
        else:
            return f'''
            ┌─────────────┐
            │ {self.__rank}          │
            │             │
            │             │
            │      {self.__suit}      │
            │             │
            │             │
            │          {self.__rank} │
            └─────────────┘
            '''

    """Статистический метод присвоения карте ее значения, если карта буква"""

    @staticmethod
    def value_card(rank: str) -> int:
        rank_set: set = {'J', 'Q', 'K'}
        if rank in rank_set:
            return 10
        elif rank == 'A':
            return 11
        else:
            return int(rank)

    def get_value(self) -> int:
        return self._value

    def get_rank(self) -> str:
        return self.__rank

    def set_value(self, value: int) -> None:
        self._value = value


class Deck:

    def __init__(self):
        ranks: list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits: list = ['♠', '♣', '♥', '♦']
        self.__cards: list = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.__cards)

    def draw_card(self):
        if len(self.__cards) != 0:
            return self.__cards.pop()


def bot_draw_card() -> None:
    time.sleep(1)
    print("\'Blackjack God's\' takes a card.")


def bot(deck: [Deck]) -> int:
    bot = User("bot")
    bot_draw_card()
    bot.draw_card(deck)
    bot_draw_card()
    bot.draw_card(deck)
    while True:
        if 21 >= bot.total() >= 18:
            return bot.total()
        elif bot.total() < 21:
            bot_draw_card()
            bot.draw_card(deck)
        elif bot.total() > 21:
            return bot.total()


user_name = User(input("Welcome. What's your name?\nMy name: "))
first_question = input("You ready to lose your kidney?: YES or NO \n")
if first_question.lower() == "yes":
    while True:
        deck = Deck()
        user_name.draw_card(deck)
        user_name.draw_card(deck)
        print(f"Your total: {user_name.total()}")
        while True:
            if user_name.total() > 21:
                print("You looser")
                break
            last_question = input("Remember, card debt is sacred. Another card?: YES or NO \n")
            if last_question.lower() == "no":
                print("You're a coward")
                user_bot = bot(deck)
                name = user_name.get_name()
                total = user_name.total()
                if total < user_bot <= 21:
                    print(f"\'Blackjack God's\' win!"
                          f"\nTotal {name}: {total} \nTotal \'Blackjack God's\': {user_bot}")
                    break
                elif user_bot == total:
                    print(f"Draw. \nTotal {name}: {total} \nTotal \'Blackjack God's\': {user_bot}")
                    break
                else:
                    print(f"You win. \nTotal {name}: {total} \nTotal \'Blackjack God's\': {user_bot}")
                    break
            else:
                user_name.draw_card(deck)
                print(user_name.total())
        time.sleep(2)
        next_question = input("Shall we play again?: YES or NO \n")
        if next_question.lower() == "no":
            break
        elif next_question.lower() == "yes":
            user_name.del_cards_user()
        else:
            print("You're drunk. Bye")
            break

'''

не работает если есть туз в колоде чтобы он был 1
'''
