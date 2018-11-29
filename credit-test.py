# -*- coding: UTF-8 -*-
# credit test

import random

# 基础积分
baseCredit = 100

# 积分发放年限
releaseYears = 3

# 积分最大增长系数
maxIncreaseCoefficient = 1.1

# 积分最小增长系数
mixIncreaseCoefficient = 0.99

# 积分发放周数
releaseWeeks = releaseYears * 52

# 最后一周发放积分的最大值
lastMaxCredit = 0

# 最后一周发放积分的最小值
lastMixCredit = 0

# 每周积分增长系数数组
arrCreditPerWeeks = []


# 计算最大积分
'''
def countMaxCredit(baseCredit, releaseYears, maxIncreaseCoefficient, mixIncreaseCoefficient, releaseWeeks):
    _baseCredit = baseCredit
    _maxIncreaseCoefficient = maxIncreaseCoefficient
    _releaseWeeks = releaseWeeks
    lastMaxCredit = _baseCredit * (_maxIncreaseCoefficient ** _releaseWeeks)

    print("基础积分：")
    print(_baseCredit)
    print("最大增长系数：")
    print(_maxIncreaseCoefficient)
    print("最后一周最大发放积分数：")
    print(lastMaxCredit)
'''

# 当前周积分
currentWeekCredit = baseCredit

# 每周发放积分数组
arrEveryWeekCredit = []

# 当前发放总积分
currentTotcalCredit = 0

# 发放积分总数
allCredit = 0

# 随机生成每周增长系数
for i in range(releaseWeeks):
    randomCoefficient = random.uniform(mixIncreaseCoefficient, maxIncreaseCoefficient)
    arrCreditPerWeeks.append(randomCoefficient)

    currentWeekCredit = currentWeekCredit * randomCoefficient
    arrEveryWeekCredit.append(currentWeekCredit)

    allCredit = allCredit + currentWeekCredit

    #print("\n\n当前周发放积分：")
    #print(currentWeekCredit)

# countMaxCredit(baseCredit, releaseYears, maxIncreaseCoefficient, mixIncreaseCoefficient, releaseWeeks)

# 每周积分
print(arrEveryWeekCredit)

# 总发放积分
print(allCredit)