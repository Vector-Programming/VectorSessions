#Question Set Classes and Objects Q2 Solution

class Enemy:
     
    def __init__ (self):
        age = int()
        movement_speed = int()
        health = int()
        attack_power = int()

        self.age = age
        self.movement_speed = movement_speed
        self.health = health
        self.attack_power = attack_power

    def move(self):
        self.movement_speed += 5

    def stop(self):
        self.movement_speed = 0

    def take_damage(self):
        self.health -= 5

    def heal(self):
        self.health += 5

    def booster(self):
        self.attack_power += 5

    def attack(self,Player):
        Player.take_damage      

    def __str__ (self):
        print("Age:", self.age)
        print("Speed:", self.movement_speed)
        print("Health is:", self.health)
        print("Attack power is:", self.attack_power)


SmallMamaPyscho = Enemy()

SmallMamaPyscho.attack_power = 100
SmallMamaPyscho.health = 100
SmallMamaPyscho.movement_speed = 0
SmallMamaPyscho.age = 3500

# He's old too,why not?

print("----------------------")

print("Move")
SmallMamaPyscho.move()
SmallMamaPyscho.__str__()
print("\n")


print("Stop")
SmallMamaPyscho.stop()
SmallMamaPyscho.__str__()
print("\n")


print("Take Damage")
SmallMamaPyscho.take_damage()
SmallMamaPyscho.__str__()
print("\n")


print("Heal")
SmallMamaPyscho.heal()
SmallMamaPyscho.__str__()
print("\n")


print("Boost")
SmallMamaPyscho.booster()
SmallMamaPyscho.__str__()
print("\n")


print("Attack")
SmallMamaPyscho.attack(Player)
SmallMamaPyscho.__str__()
print("\n")

print("----------------------")
