class DemoClass:
    def method1(self):
        print("This is method 1")

    def method2(self):
        print("This is method 2")



#obj = DemoClass()
#obj.method1()
#print("===")
#obj.method2()


#=========
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi!.. I am {self.name}")


dvs = Person("Divyesh")
dvs.talk()

divyesh = Person("DVS")
divyesh.talk()