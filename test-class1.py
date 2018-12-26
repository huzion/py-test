# codeing=utf8
class Prosen:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def __str__(self):
        return "我叫%s，体重%.2f公斤" % (self.name, self.weight)
    def run(self):
        print("跑一跑减肥")
        self.weight -= 0.5
        print(self)
    def eat(self):
        print("吃一吃长胖")
        self.weight += 0.5
        print(self)

xiaomin = Prosen("小明", 72)

print(xiaomin)
xiaomin.eat()
xiaomin.run()