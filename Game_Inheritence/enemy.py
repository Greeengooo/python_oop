class Enemy:

    def __init__(self, name="Enemy", hp=0, lives=1):
        self.name = name
        self.hp = hp
        self.lives = lives

    def take_damage(self, damage):
        remaining_points = self.hp - damage
        if remaining_points >= 0:
            self.hp = remaining_points
            print(f"-{damage} hp and {self.hp} left")
        else:
            self.lives -= 1

    # toString
    def __str__(self):
        return f"Name {self.name}, Lives: {self.lives}, Hp: {self.hp}"


class Troll(Enemy):
    pass
