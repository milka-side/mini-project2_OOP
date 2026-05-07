def change(money):
    num_10 = money // 10
    money %= 10
    num_5 = money // 5
    money %= 5
    return num_10 + num_5 + money

if __name__ == '__main__':
    m = int(input())
    print(change(m))
