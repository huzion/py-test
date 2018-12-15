from pprint import pprint

class dog:
    def __init__(self, **kwargs):
        print(kwargs)



        if "name" in kwargs.keys():
            self.name = kwargs["name"]
        else:
            self.name = "小狗"

        print("生成一只小狗，名叫%s" % self.name )

    def __del__(self):

        print("%s 再见！" % self.name)

    def __str__(self):

        return '我擦'

    def eat(self):
        print("%s eat meat!" % self.name)

    def drink(self):
        print("%s drink milk!" % self.name)

lazy_dog = dog()

happy_dog = dog(name="大大米")



print("---------------")
print(happy_dog)
