from player_decorators import Player
from enemy import Enemy, Troll

""" Player Tom with decorators inside"""
tom = Player("Tom")

# en1 = Enemy("Basic Enemy", 12, 1)
# print(en1)
#
# en1.take_damage(4)
# print(en1)
#
# en1.take_damage(8)
# print(en1)
#
# en1.take_damage(8)
# print(en1)

""" Troll inherited from Enemy """
t1 = Troll()
print(t1)

t2 = Troll("t2", 18, 1)
print(t2)

t3 = Troll("t3", 23)
print(t3)
