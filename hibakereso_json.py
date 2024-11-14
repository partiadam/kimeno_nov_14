import json

with open('hibakereso.json', 'r') as file:
    data = json.load(file)

class Charcter:
    def __init__(self, name, level, health, attack, defense):
        self.name = name
        self.level = level
        self.heal = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.heal -= damage
        if self.heal < 0:
            self.heal = 0
        print(f"{self.name} took {damage} damage and now has {self.heal} health left.")

characters = [Charcter(**char) for char in data['characters']]

def fight(character1, character2):
    print(f"Battle between {character1.name} and {character2.name} starts!")
    while character1.heal > 0 and character2.heal > 0:
        damage = character1.attack 
        character2.take_damage(damage)

        if character2.heal <= 0:
            print(f"{character2.name} is defeated! {character1.name} wins!")
            break

       
        damage = character2.defense + character1.attack
        character1.take_damage(damage)

   
        if character1.heal <= 0:
            print(f"{character1.name} is defeated! {character2.name} wins!")
            break

fight(characters[0], characters[1])