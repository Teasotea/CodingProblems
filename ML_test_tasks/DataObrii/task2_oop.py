"""
Написати клас друзі з методами:

    init(friendship), - ініціалізувати початковий список друзів

    add_friends(friendship) - додати друзів,

    remove_friends(friendship), видалити друзів

    return_friends(a), повернути список друзів певної людини.

Використати знання ООП та Паттернів програмування (вказати в коментарях до рішення що саме й чому використано).

friendship - змінна яка має показувати чи дружать між собою дві людини - тип tuple.

"""

# I have implemented more than one class to demonstrate, how SOLID OOP Patterns work


from abc import ABC, abstractmethod

class Relations(ABC):
    @abstractmethod
    def add_friends(self, friends):
        pass

    def remove_friends(self, friends):
        pass

    def return_friends(self, id) -> tuple:
        pass

class Friends(Relations):
  '''Each person has unique ID
     friendship - tuple that contains all friends pairs'''

  def __init__(self, friendship: tuple):
    self.friendship = friendship

  def add_friends(self,friends):
    self.friendship = self.friendship + (friends,)

  def __remove_friends(self, friends):
    self.friendship =  tuple(item for item in self.friendship if item != friends)

  def return_friendship(self):
    return self.friendship

  def return_friends(self, id):
    friends = tuple()
    for tup in self.friendship:
        if id == tup[0]:
          friends = friends + (tup[1],)
        elif id == tup[1]:
          friends = friends + (tup[0],)
    return friends

class MultipleFriends(Relations):
  '''Each person has unique ID
     friendship - tuple that contains all friends in a company'''

  def __init__(self, friendship: tuple):
    self.friendship = friendship

  def add_friends(self,friends):
    self.friendship = tuple(set(self.friendship + friends))

  def __remove_friends(self, friends):
    self.friendship = tuple(set(self.friendship) - set(friends))

  def return_friendship(self):
    return self.friendship

  def return_friends(self, id) -> tuple:
    return tuple(item for item in self.friendship if item != id)

if __name__ == '__main__':
  a = Friends(friendship = ((0, 1), (0, 6), (1,2), (0,2)))
  print(a.return_friendship())
  a.add_friends((5, 2))
  print(a.return_friendship())
  a._Friends__remove_friends((0, 1))
  print(a.return_friendship())
  print(a.return_friends(2))

  b = MultipleFriends(friendship = (0,1,6,2))
  print(b.return_friendship())
  b.add_friends((5, 2, 8))
  print(b.return_friendship())
  b._MultipleFriends__remove_friends((0, 1))
  print(b.return_friendship())
  print(b.return_friends(2))



"""
SOLID Patterns: 
- The Single-responsibility principle: 
 - Every class should have only one responsibility. 
 - For our classes Friends and MultipleFriends it is used: class has resposibility - save friendship information

- The Open–closed principle: 
 - Software entities ... should be open for extension, but closed for modification. 
 - Our classes are open for extention. And I have decided to make method remove_friends private to follow this pattern

- The Liskov substitution principle: 
 - This principle states that a child class must be substitutable for its parent class.
 - To demonstrate this principle, I have created Relations base class. As you can see: child classes Friends and MultipleFriends can assume the place of its parent class without causing any errors.

- The Interface segregation principle: 
 - This principle states that an interface should be as small a possible in terms of cohesion. In other words, it should do ONE thing.
 - In our case, Friends class just add or remove friends, so this principle is followed

- The Dependency inversion principle:
 - Abstractions should not depend on details. Details should depend on abstractions. To follow this principle, I have added type specifications to the methods in both classes
"""
