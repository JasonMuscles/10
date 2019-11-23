# 提示用户输入一个整数
try:
    num = int(input("请输入一个整数："))

    # 使用 8 除以用户输入的整数并且输出
    result = 8 / num
    print(result)

except ValueError:
    print("请正确输入一个整数！")

# 捕获所有未知错误并输出错误原因。
except Exception as result:
    print("出现未知错误，错误原因为：%s" % result)
