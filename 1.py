class CoffeeMachine:

    def __init__(self, water, milk, coffeeBeans, cups, money):
        self.water = water
        self.milk = milk
        self.coffeeBeans = coffeeBeans
        self.cups = cups
        self.money = money

    def __str__(self):
        return f'The coffee machine has:\n' \
               f'{self.water} of water\n' \
               f'{self.milk} of milk\n' \
               f'{self.coffeeBeans} of coffee beans\n' \
               f'{self.cups} of disposable cups\n' \
               f'{self.money} of money\n'

    def status(self, action):
        self.action = action
        if self.action == 'remaining':
            print(self)
        elif self.action == 'take':
            print(f'I gave you ${self.money}\n')
            self.money = 0
        elif self.action == 'fill':
            addWater = int(input('Write how many ml of water do you want to add:\n'))
            self.water += addWater
            addMilk = int(input('Write how many ml of milk do you want to add:\n'))
            self.milk += addMilk
            addBeans = int(input('Write how many grams of coffee beans do you want to add:\n'))
            self.coffeeBeans += addBeans
            addCups = int(input('Write how many disposable cups of coffee do you want to add:\n'))
            self.cups += addCups
        elif self.action == 'buy':
            choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
            self.buy(choice)
        elif self.action == 'exit':
            action = 'exit'
            return action

    def buy(self, coffee):
        espresso = [250, 0, 16, 1, -4]
        latte = [350, 75, 20, 1, -7]
        cappuccino = [200, 100, 12, 1, -6]
        statusList = [self.water, self.milk, self.coffeeBeans, self.cups, self.money]
        coffeeType = []
        newStatusList = []
        errorList = []
        if coffee == '1':
            coffeeType = espresso
        elif coffee == '2':
            coffeeType = latte
        elif coffee == '3':
            coffeeType = cappuccino
        elif coffee == 'back':
            return None
        for num in range(len(statusList)):
            if statusList[num] >= coffeeType[num]:
                newStatusList.append(statusList[num] - coffeeType[num])
            else:
                errorList.append(num)
        if len(errorList) > 0:
            errorMessage = 'Sorry, not enought'
            for error in range(len(errorList)):
                if errorList[error] == 0:
                    errorMessage += ' water'
                elif errorList[error] == 1:
                    errorMessage += ' coffee beans'
                elif errorList[error] == 2:
                    errorMessage += ' milk'
                elif errorList[error] == 3:
                    errorMessage += ' cups'
                if (error + 1) != len(errorList):
                    errorMessage += ','
                else:
                    errorMessage += '!'
            print(errorMessage)
        else:
            self.water = newStatusList[0]
            self.milk = newStatusList[1]
            self.coffeeBeans = newStatusList[2]
            self.cups = newStatusList[3]
            self.money = newStatusList[4]
            print('I have enough resources, making you a coffee!')


coffeeMaker = CoffeeMachine(400, 540, 120, 9, 550)
action = ''
while action != 'exit':
    action = input('Write action (buy, fill, take, remaining, exit):\n')
    CoffeeMachine.status(coffeeMaker, action)
