#create class

class Person:

    def __init__(self, firstname, lastname, health, status):
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        print("Hi, I'm {} {}.".format(self.firstname, self.lastname))

    def status_change(self):
        self.health = (self.health - 25)
        if self.health == 100:
            print("{} is fully healthy!".format(self.firstname))
        elif self.health >= 76:
            print("{} feels a little tired.".format(self.firstname))
        elif self.health >= 51:
            print("{} feels unwell.".format(self.firstname))
        elif self.health <= 50:
            print("{} goes to the doctor.".format(self.firstname))
        else:
            print("{} is unconscious.".format(self.firstname))
            
    def emote(self):
        emotion = random.randrange(1,3)
        if emotion == 1:
            print("{} is happy today".format(self.firstname))
        elif emotion == 2:
            print("{} is sad right now".format(self.firstname))           

Maria = Person("Maria", "Gutierrez", 95, status=True)
Rey = Person("Rey", "Jones", 88, status=False)
Lee = Person("Lee", "Williams", 72, status=True)

print("{} is my friend? {}".format(Maria.firstname, Maria.status))
print("{} is my friend? {}".format(Rey.firstname, Rey.status))

Maria.introduce()
Rey.introduce()
Lee.introduce()

Maria.status_change()
Rey.status_change()
Lee.status_change()

Maria.emote()
Rey.emote()
Lee.emote()
