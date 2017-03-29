# Amazon

balance = [12, 32, 10, 23, 24, 43, 35,]

def apps(prices):
    print('Ingress money(45)')
    money = input()
    i = 0
    while i in range (len(prices)):
        app1 = prices[i]
        m = i + 1
        while m in range (len(prices)):
            app2 = prices[m]
            if (app1 + app2) == int(money):
                print('A posible combination is: ' + str(app1) + ' + ' + str(app2))
            m += 1
        i += 1

apps(balance)
