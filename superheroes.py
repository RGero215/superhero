import random

class Hero:
    def __init__(self, name):
        self.abilities = list()
        self.name = name

    def add_ability(self, ability):
        return self.abilities.append(ability)

    def attack(self):
        total = 0
        for ability in self.abilities:
            total += ability.attack()
        return total



class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        # Calculate lowest attack value as an integer.
        # Use random.randint(a, b) to select a random attack value.
        # Return attack value between 0 and the full attack.
        lower_attack = self.attack_strength // 2
        return random.randint(lower_attack, self.attack_strength)

    def update_attack(self, attack_strength):
        #Update attack value
        self.attack_strength = attack_strength
        return self.attack_strength
        

    def add_ability(self, ability):
        #Add ability to abilities list
        pass


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
