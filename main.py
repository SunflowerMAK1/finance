import client
import bank
from utils import clear, enter_to_continue
def main():
    client.load()
    while True:
        enter_to_continue()
        clear()
        print("Доступные действия:\n1 - Посмотреть предложения банка\n2 - Отправить жалобу\n3 - Информация о счетах")
        print("4 - Прогноз доходов и расходов на следующий месяц")
        print("5 - Совершить транзакцию\n10 - Выйти")
        a = int(input("Введите номер действия, которое вы хотите сделать>> "))

        if a == 1:
            print("Посмотреть предложения банка")
            bank.suggestions()
        elif a == 2:
            print("Отправить жалобу")
            bank.complain()
        elif a == 3:
            print("Информация о счетах:\n")
            client.show_info()
        elif a == 4:
            print("Прогноз доходов и расходов на следующий месяц")
            client.predict()
        elif a == 5:
            print("Совершить транзакцию")
            client.make_transaction()
        elif a == 10:
            print("Выйти")
            client.save()
            break
        else:
            print("Нет такого действия")


if __name__ == "__main__":
    main()

enter_to_continue()
