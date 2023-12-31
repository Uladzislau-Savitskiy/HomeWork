"Проблема в  def all_value_card класса User "

import random


class User:
    """"""

    """Создание объекта класса"""

    def __init__(self, name: str):
        self.__name: str = name
        self.__cards_user: list = []

    """Результат сумму карт на руках у объекта, до получения новой карты"""

    def all_value_card(self) -> int:
        total: int = sum(card.get_value() for card in self.__cards_user)
        return total

    """
    Получение карты.
    Если сумма карт на руках меньше 21 и есть карты в колоде:
        Если сумма карт на руках больше или равна 18, спрашиваем действительно ли он хочет взять карту?
        Если вводит ДА, то получает карту, если НЕТ, то желаем удачи.
    Если все сумма на руках больше 21 или нет карт, то сообщаем об это.
    """

    def draw_card(self, deck):
        card = deck.draw_card()
        total: int = self.all_value_card()
        if total < 21 and card:
            if total >= 18:
                print(f"{self.__name}, really want to get a card? You have {total}")
                if input("YES or NO?").lower() == "yes":
                    self.__cards_user.append(card)
                    print(card)
                else:
                    print("Good luck")
            else:
                self.__cards_user.append(card)
                print(card)
        else:
            print("Sorry, you have 21 more") if total > 21 else print("Not cards")


class Card:
    """"""

    """Создание объекта карты"""

    def __init__(self, rank: str, suit: str):
        self.__rank: str = rank
        self.__suit: str = suit
        self._value: int = self.value_card(rank)

    def __repr__(self) -> str:
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

    """Статистический метод присвоения карте ее значения, если карта буква"""

    @staticmethod
    def value_card(rank: str):
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

class Deck:
    """"""

    """
    Создание объекта колоды.
    Создается объект в виде листа, в котором есть объекты класса Card.
    Рандомно перемешивается колода(лист объекта)
    """

    def __init__(self):
        ranks: list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits: list = ['♠', '♣', '♥', '♦']
        self.__cards: list = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.__cards)

    """
    Метод выдачи карты из колоды.
    Если лист не пустой то даст последнюю карту
    """

    def draw_card(self):
        if len(self.__cards) != 0:
            return self.__cards.pop()


deck = Deck()
user = User('Vlad')
user.draw_card(deck)
user.draw_card(deck)
