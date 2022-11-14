# Задача 1. Машина 2

class Toyota:
    color = 'red'
    cost = 1000000
    speed_max = 200
    current_speed = 0

    def print_info(self):
        print(f'Color: {self.color}\nCost: {self.cost}\n'
              f'Max speed: {self.speed_max}\nCurrent speed: {self.current_speed}')

    def input_current_speed(self, speed):
        if speed.isdigit():
            self.current_speed = int(speed)
        else:
            print('Вы ввели не числовое значение.')


car = Toyota()
car.print_info()
car.input_current_speed(input('Введите скорость: '))
car.print_info()

