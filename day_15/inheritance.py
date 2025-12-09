class Human:
    def eat(self):
        print("I can eat")
    def sleep(self):
        print("I can sleep")

class Man(Human):
    def play(self):
        print("I can play")
    def sleep(self):
        super().sleep()
        print("I can sleep for 8 hours")

rahul = Man()
rahul.eat()
rahul.play()
rahul.sleep()