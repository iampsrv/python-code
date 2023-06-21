class FamilyMember:
    def talk(self):
        print("I can talk")
    def walk(self):
        print("I can walk")
    def lough(self):
        print("I can lough")


class Dad(FamilyMember):
    def fix_things(self):
        print("I can fix thing")
    
class Mom(FamilyMember):
    def cook(self):
        print("I can cook delicious food")
    def talk(self):
        print("I can talk so much")

class Me(Dad,Mom,FamilyMember):
    def code(self):
        print("I can code")

dad=Dad()
mom=Mom()
me=Me()

dad.walk()
mom.talk()
me.lough()
me.cook()
me.fix_things()

dad.fix_things()