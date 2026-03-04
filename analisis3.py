class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")


class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        # super().__init__(name, hp, attack_power)  
        self.mana = mana

    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")


# -- Main Program --
eudora = Mage("Eudora", 80, 30, 100)
eudora.info()


