from random import shuffle

"""
Класс Card:
:переменная класса suits: значения мастей карт
:переменная класса values: значения карт
Самая слабая масть имеет индекс 0 в списке suits, самая сильная - 3

None в values добавлены для того, чтобы значения элементов, начиная со 2-го,
совпадали с индексами списка

Переменные экземпляра (объекта) класса:
value - значение карты
suit - масть карты
"""
class Card():
    suits=["пик", "червей", "бубей", "треф"]
    values=[None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "валета", "даму", "короля", "туза"]

    def __init__(self, v, s):
        #suit и value - целые числа
        self.value=v
        self.suit=s
        
    def __lt__(self, c2):
        if self.value<c2.value:
            return True
        if self.value==c2.value:
            if self.suit<c2.suit:
                return True
            else:
                return False
        return False
    
    def __gt__(self, c2):
        if self.value>c2.value:
            return True
        if self.value==c2.value:
            if self.suit>c2.suit:
                return True
            else:
                return False
        return False
    
    def __repr__(self):
        v=self.values[self.value]+" "+self.suits[self.suit]
        return v

card1=Card(10, 2)
print(card1)
card2=Card(5, 1)
print(card2)
print(card1>card2)

"""
Класс Deck - колода карт
:переменная объекта cards: список, представляющий собой колоду из 52 карт
"""
class Deck:
    def __init__(self):
        self.cards=[]   #создание списка колоды
        for i in range(2,15):                   #номинал карты
            for j in range (4):                 #масть карты
                self.cards.append(Card(i,j,))   #наполнение колоды картами разных номиналов и мастей
        shuffle(self.cards)                     #перемешать колоду, рандомно расположив элементы списка cards[]

    def rm_card(self):
        if len(self.cards)==0:
            return
        return self.cards.pop()                 #метод pop удаляет последний элемент списка cards
    
deck1=Deck()
for i in deck1.cards:
    print(i)

"""
Класс Player - игрок
:переменная экземпляра класса wins: количество раундов
:переменная экземпляра класса card: карта, которую держит игрок в данный момент
:переменная экземпляра класса name: имя игрока
"""
class Player:
    def __init__(self, name):
        self.wins=0
        self.card=None
        self.name=name

class Game:
    
    def __init__(self):
        name1=input("Имя игрока 1: ")
        name2=input("Имя игрока 2: ")
        self.deck=Deck()
        self.p1=Player(name1)
        self.p2=Player(name2)
        
    def wins(self, winner):
        w="{} забирает карты"
        w=w.format(winner)
        print(w)
        
    def draw(self, p1n, p1c, p2n, p2c):
        d="{} кладёт {}, а {} кладёт {}"
        d=d.format(p1n, p1c, p2n, p2c)
        print(d)
        
    def play_game(self):
        cards=self.deck.cards
        print("Поехали!")
        while len(cards)>=2:
            response=input("Нажмите Х для выхода. Нажмите любую другую клавишу для начала игры.")
            if response=="X":
                break
            p1c=self.deck.rm_card()
            p2c=self.deck.rm_card()
            p1n=self.p1.name
            p2n=self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c>p2c:
                self.p1.wins+=1
                self.wins(self.p1.name)
            else:
                self.p2.wins+=1
                self.wins(self.p2.name)
        win=self.winner(self.p1, self.p2)
        print("Игра окончена. {} выиграл".format(win))
        
    def winner(self, p1, p2):
        if p1.wins>p2.wins:
            return p1.name
        if p1.wins<p2.wins:
            return p2.name
        return "Ничья!"
            
game=Game()
game.play_game()
