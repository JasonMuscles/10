def input_password():

    # 1.提示用户输入密码
    pwd = input("请输入密码：")

    # 2.判断密码长度 >= 8,返回用户输入的密码
    if len(pwd) >= 8:
        return pwd

    # 3.如果密码长度 < 8，主动抛出异常
    print("主动抛出异常")

    # 1>创建异常对象 - 可以使用错误信息作为字符串参数
    exc = Exception("密码长度应该>=8，请重新输入！")

    # 2>主动抛出异常
    raise exc


# 提示用户输入密码
try:
    print(input_password())
except Exception as result:
    print("未知错误 %s" % result)