# Задача 2. Семья

class Family:
    name = 'name'
    money = 0
    house = False

    def print_info(self):
        print(f'Name: {self.name}\nMoney: {self.money} рублей\nHouse: {"Есть дом" if self.house else "Дома нет"}')

    def earn_money(self, earn_money):
        if earn_money.isdigit():
            self.money += int(earn_money)
            print(f'Денег стало:{self.money}')
        else:
            print('Вы ввели не число.')

    def by_house(self, cost, discount=0):

        calculate = cost - cost * discount / 100
        if calculate <= self.money:
            self.money -= calculate
            self.house = True
            print('Поздравляем! Вы купили дом!')
        else:
            print('Вы ввели не число')


big_family = Family()
big_family.name = input('Введите фамилию семейства: ')
big_family.print_info()
big_family.earn_money(input('Введите сумму заработка: '))
big_family.print_info()
big_family.by_house(100000)
big_family.print_info()

