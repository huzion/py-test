# codeing=utf8
# 输入测试

gl_address = []

def inputAddress():
    name = input("请输入姓名：")
    both = input("请输入出生日期：")
    gender = input("请输入性别：")

    dict = {
        "姓名": name,
        "生日": both,
        "性别": gender
    }
    
    gl_address.append(dict)
    
    print(gl_address)
    isContinue = input("是否继续，请输入yes/no：")

    while (isContinue != "no"):
        if isContinue == 'yes':
            inputAddress()
            return
        else:
            isContinue = input("输入错误，请输入yes/no：")

    print("输入中止！")
    return gl_address

inputAddress()