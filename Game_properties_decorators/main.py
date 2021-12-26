from player_properties import Player as Player_p
from player_decorators import Player as Player_d


"""Player Tim with properties inside"""
tim = Player_p("Tim")

# print(tim.name)
# print(tim.lives)
# tim.lives -= 1
# print(tim.lives)
#
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
# tim._lives = 9
# print(tim)

tim.level += 1
print(tim)


""" Player Tom with decorators inside"""
tom = Player_d("Tom")

tom.score = 500
print(tom)