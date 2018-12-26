class Women:

    def __init__(self, name):
        self.name = name
        self.__age = 18

    def secret(self):
        print("%s的年龄是%d岁" % (self.name, self.__age))

amy = Women("Amy")

print(amy._Women__age)

amy.secret()