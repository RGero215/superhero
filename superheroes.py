import random

class Hero:
    def __init__(self, name, health=100):
        self.abilities = list()
        self.name = name
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        return self.abilities.append(ability)

    def attack(self):
        total = 0
        for ability in self.abilities:
            total += ability.attack()
        return total

    def add_armor(self, name):
        return self.armors.append(name)

    def defend(self):
        """
        This method should run the defend method on each piece of armor and calculate the total defense. 

        If the hero's health is 0, the hero is out of play and should return 0 defense points.
        """
        total = 0
        if self.armors == []:
            return 0
        for armor in self.armors:
            
            if self.health == 0:
                return 0
            else:
                total += armor.defend()
        return total

    def take_damage(self, damage_amt):
        """
        This method should subtract the damage amount from the 
        hero's health. 

        If the hero dies update number of deaths.
        """
        is_dead = False
        damage = damage_amt - self.defend()
        self.health -= damage
        self.health = max(0, self.health)
        if self.health == 0:
            self.deaths += 1
            is_dead = True
        # else:
        #     return self.health - damage_amt
        if is_dead:
            return 1
        else:
            return 0

    def add_kill(self, num_kills):
        """
        This method should add the number of kills to self.kills
        """
        self.kills += 1 



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

class Weapon(Ability):
    def attack(self):
        return random.randint(0, self.attack_strength)


class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        return self.heroes.append(Hero)

    def remove_hero(self, name):
        if self.heroes == []:
            return 0
        for hero in self.heroes:
            if name != hero.name:
                return 0
            else:
                return self.heroes.remove(hero)

    def find_hero(self, name):
        if self.heroes == []:
            return 0
        for hero in self.heroes:
            if name != hero.name:
                return 0
            else:
                return hero

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        """
        This method should total our teams attack strength and call the defend() method on the rival team that is passed in.

        It should call add_kill() on each hero with the number of kills made.
        """
        offense = 0
        for hero in self.heroes:
            offense += hero.attack()
            
        killstreak = other_team.defend(offense)

        for hero in self.heroes:
            hero.add_kill(killstreak)
        # hero.add_kill(killstreak)
        # counter = killstreak
        # while counter > 0:
        #     counter -= 1
        # return killstreak
                
            

    def defend(self, damage_amt):
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.

        Return number of heroes killed in attack.
        """
        # total = 0
        # for hero in self.heroes:
        #     if hero.health > 0:
        #         total += hero.defend()
        #         print("Defend total: ", total)
        #         return self.deal_damage(damage_amt)
        #     else:
        #         hero.kills += 1
        #         return hero.kills
        defense = 0 
        for hero in self.heroes:
            defense += hero.defend()
        if damage_amt > defense:
            damage = damage_amt - defense
            return self.deal_damage(damage)
        damage = max(0, damage) #this return a minimun of 0 
        killstreak = self.deal_damage(damage)
        return killstreak





    def deal_damage(self, damage):
        """
        Divide the total damage amongst all heroes.
        Return the number of heros that died in attack.
        """
        num_of_kills = 0
        if len(self.heroes) != 0:
            equal_damage = damage // len(self.heroes)
        if len(self.heroes) == 0:
            equal_damage = 1
        for hero in self.heroes:
            # print("Num: ", hero.take_damage(damage))
            num_of_kills += hero.take_damage(equal_damage)
        return num_of_kills


    def revive_heroes(self, health=100):
        """
        This method should reset all heroes health to their
        original starting value.
        """
        for hero in self.heroes:
            hero.health = hero.start_health

    def stats(self):
        """
        This method should print the ratio of kills/deaths for each member of the team to the screen. 

        This data must be output to the terminal.
        """
        for hero in self.heroes:
            print("{} has {} kills and {} deaths".format(hero.name, hero.kills, hero.deaths))

    def update_kills(self):
        """
        This method should update each hero when there is a team kill.
        """
        for hero in self.heroes:
            self.revive_heroes()

class Armor:
    def __init__(self, name, defense):
        """Instantiate name and defense strength."""
        self.name = name
        self.defense = defense

    def defend(self):
        """
        Return a random value between 0 and the 
        initialized defend strength.
        """
        return random.randint(0, self.defense)

class Arena:
    def __init__(self):
        """
        self.team_one = None
        self.team_two = None
        """
        self.team_one = None
        self.team_two = None

    def build_team_one(self):
        """
        This method should allow a user to build team one.
        """
        self.team_one = Team(input("Enter the name of your Team: "))
        add_hero = self.done("Would you like to add a superhero to Team {} Y/N: ".format(self.team_one.name))
        while  add_hero != "done":
            hero = Hero(input("Enter the name of your hero: "))
            name = input("Enter name of the ability: ")
            strength = input("Enter the strenght of the ability: ")
            ability = Ability(name, int(strength))
            hero.add_ability(ability)
            self.team_one.add_hero(hero)
            add_hero = self.done("Would you like to add another hero Y/N: ")
        else:
            if self.team_one.heroes != []:
                print("Team {} is ready to fight and this are the members: ".format(self.team_one.name))
                for hero in self.team_one.heroes:
                    print(hero.name)
            else:
                print("Your team is empty. please add at least a superhero to Team {}".format(self.team_one.name))
                add_hero = "Y"

    def build_team_two(self):
        """
        This method should allow user to build team two.
        """

    def team_battle(self):
        """
        This method should continue to battle teams until 
        one or both teams are dead.
        """

    def show_stats(self):
        """
        This method should print out the battle statistics 
        including each heroes kill/death ratio.
        """
    def done(self, prompt):
        done = input(prompt)
        if done == "N":
            return "done"
        else:
            return done

if __name__ == "__main__":
    # hero = Hero("Wonder Woman")
    # print(hero.attack())
    # ability = Ability("Divine Speed", 300)
    # hero.add_ability(ability)
    # print(hero.attack())
    # new_ability = Ability("Super Human Strength", 800)
    # hero.add_ability(new_ability)
    # print(hero.attack())
    # hero_weapon = Weapon("Bracellette", 500)
    # team = Team("One")
    # print(team.find_hero("Alexa"))
    # print(team.find_hero("Alexa") == 0)
    # jodie = Hero("Jodie Foster")
    # team.add_hero(jodie)
    # print(team.heroes[0].name)
    # print(team.remove_hero("Athena") == 0)
    # print(team.find_hero("Alexa") == 0)
    # print(team.heroes[0].name == "Jodie Foster")
    # print(team.find_hero("Jodie Foster"))
    # print(len(team.heroes) == 0)
    # team.view_all_heroes()
    # print(team.heroes[0].name)
    Arena().build_team_one()
    
