import random


class Mystery:

    def __init__(self, question: str = None, answer: list = None, choices: list = None):
        self.question: str = question
        self.answer: list = answer
        self.choices: list = choices
        self.answer_option: list = []
        self.correct_answer: list = []

    def one_answer(self):
        for i, option in enumerate(self.answer_option, start=1):
            print(f"\t\t{i}. {option}")
            if option in self.answer:
                self.correct_answer.append(i)
        user_response = int(input("Select option: "))
        if user_response in self.correct_answer:
            print("Correct!")
        else:
            print(f"Incorrect! Correct answer: {self.answer}")

    def more_one_answer(self):
        for i, option in enumerate(self.answer_option, start=1):
            print(f"\t\t{i}. {option}")
            if option in self.answer:
                self.correct_answer.append(i)
        user_response = list(map(int, input("Select option: ").split()))
        if user_response.sort() == self.correct_answer.sort():
            print("Correct!")
        else:
            print(f"Incorrect! Correct answer: {self.answer}")

    def quiz(self):
        print(f"Question: {self.question}")
        self.answer_option.extend(self.answer)
        self.answer_option.extend(self.choices)
        random.shuffle(self.answer_option)
        if len(self.answer) == 1:
            self.one_answer()
        else:
            self.more_one_answer()


q1 = Mystery(question="Какое прозвище придумали для Лукашенко, когда он стал заниматься садоводством?",
             answer=["Батька-огородник"],
             choices=["Царь картошки", "Дачный диктатор", "Президент-петух", "Фермер-автократ"])
q2 = Mystery(question="Кто является основателем компании Tesla?",
             answer=["Илон Маск"], choices=["Билл Гейтс", "Марк Цукерберг", "Ларри Пейдж", "Стив Джобс"])
q3 = Mystery(question="В каком году состоялась первая поездка человека в космос?",
             answer=["1961"], choices=["1957", "1969", "1975", "1983"])
q4 = Mystery(question="Какой самый популярный язык программирования?",
             answer=["Python"], choices=["Java", "C++", "JavaScript", "Ruby"])
q5 = Mystery(question="Какое животное является символом OpenAI?",
             answer=["Дракон"], choices=["Лев", "Орел", "Кит", "Тигр"])
q6 = Mystery(question="Какие из следующих языков являются объектно-ориентированными?",
             answer=["Java", "C++"], choices=["Python", "JavaScript", "Ruby"])
q7 = Mystery(question="Какие из перечисленных стран являются членами Европейского союза?",
             answer=["Германия", "Франция"], choices=["Швейцария", "Норвегия", "Швеция"])
q8 = Mystery(question="Какие из перечисленных фильмов были режиссированы Кристофером Ноланом?",
             answer=["Inception", "The Dark Knight"], choices=["Avengers: Endgame", "Pulp Fiction", "La La Land"])
q9 = Mystery(question="Какие озера расположены на территории Беларуси?",
             answer=["Нарочь", "Свитязь", "Дрисвяты"], choices=[])
q10 = Mystery(question="Какой город является столицей Беларуси?",
              answer=["Минск"], choices=["Могилев", "Гродно", "Витебск", "Москва"])
q11 = Mystery(question="Кто является выдающимся белорусским поэтом?",
              answer=["Янка Купала", "Максим Богданович", "Уладзімір Караткевіч"],
              choices=["Рыгор Барадулін"])
q12 = Mystery(question="Какой фестиваль в Беларуси считается самым крупным музыкальным событием?",
              answer=["Славянский базар"], choices=["Витебскі вечар", "Рок за Бобров", "Фестиваль Босая", "Минская весна"])
q1.quiz()
q2.quiz()
q3.quiz()
q4.quiz()
q7.quiz()
q9.quiz()
q10.quiz()
q12.quiz()
