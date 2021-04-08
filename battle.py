"""
Pokemon Battle Simualtor

>>> battle(Charmander(),  Squirtle())
Squirtle wins in 2 moves (8 HP remaining)

>>> battle(Bulbasaur(),  Squirtle())
Bulbasaur wins in 2 moves (15 HP remaining)

>>> battle(Bulbasaur(),  Charmander())
Charmander wins in 2 moves (10 HP remaining)

>>> battle(Charmander(),  Ratatta())
Charmander wins in 3 moves (12 HP remaining)

>>> battle(Charizard(),  Venusaur())
Charizard wins in 2 moves (55 HP remaining)
"""

class Attack:
    def __init__(self, damage):
        self.damage = damage

    def apply_damage(self, target):
        target.hp -= self.damage

class WaterAttack(Attack):
    def apply_damage(self, target):
        multiplier = 1
    
        if isinstance(target, FirePokemon):
            multiplier = 2

        target.hp -= multiplier * self.damage
    
class FireAttack(Attack):
    pass
    
class WaterGun(WaterAttack):
    def __init__(self):
        super().__init__(5)

class Ember(FireAttack):
    def __init__(self):
        super().__init__(6)

class Pokemon:
    def __init__(self, hp, attack):
        self.hp = hp
        self.attack = attack
        
    def do_attack(self, opponent):
        self.attack.apply_damage(opponent)

class FirePokemon(Pokemon):
    pass

class WaterPokemon(Pokemon):
    pass

class Charmander(FirePokemon):
    def __init__(self):
        super().__init__(hp=20, attack=Ember())

class Squirtle(WaterPokemon):
    def __init__(self):
        super().__init__(hp=20, attack=WaterGun())

def battle(a, b):
    for i in range(1, 100):
        for attacker, target in [(a,b), (b,a)]:
            attacker.do_attack(target)
            if target.hp <= 0:
                print(f"{type(attacker).__name__} wins in {i} moves ({attacker.hp} HP remaining)")
                return
    else:
        print("Exceeded move limit")

if __name__ == '__main__':
    battle(Charmander(), Squirtle())
