import json

client_info = {}


def load():
    global client_info
    with open("client_info.json", "r", encoding="utf-8") as a:
        client_info = json.load(a)


def save():
    with open("client_info.json", "w", encoding="utf-8") as a:
        json.dump(client_info, a, ensure_ascii=False)


def show_info():
    for i in client_info["accounts"]:
        print(f"Имя: {i["name"]}")
        print(f"Платежная система: {i["system"]}")
        print(f"Номер: {i["number"]}")
        print(f"Тип: {i["type"]}")
        print(f"Баланс: {i["balance"]}")
        print(f"Срок действия: {i["validity period"]}")
        print("----------------------------------")


def predict():
    expenses = 0
    income = 0
    ex = []
    inc = []
    for i in client_info["transactions"]:
        month = i["date"]
        if i["type"] == "списание":
            expenses += i["amount"]
            if month not in ex:
                ex.append(month)
        elif i["type"] == "зачисление":
            income += i["amount"]
            if month not in inc:
                inc.append(month)
    print(f"Предполагаемые расходы в следующем месяце: {expenses / len(ex)}")
    print(f"Предполагаемые доходы в следующем месяце: {income / len(inc)}")


def make_transaction():
    print("Доступные счета:")
    for a, i in enumerate(client_info["accounts"]):
        print(f"{a + 1} - {i["name"]} - {i["number"]}")
    while True:
        try:
            b = int(input("Введите номер счета из списка>> "))
            break
        except:
            print("Ошибка ввода!")
    while True:
        if b > len(client_info["accounts"]) or b < 1:
            print("Ошибка ввода!")
            b = int(input("Введите номер счета из списка>> "))
        else:
            break

    n = client_info["accounts"][b - 1]["number"]

    print("Типы транзакций:")
    for a, i in enumerate(client_info["transactions"]):
        print(f"{a + 1} - {i["type"]}")
        if a == 1:
            break
    while True:
        try:
            c = int(input("Введите номер транзакции из списка>> "))
            break
        except:
            print("Ошибка ввода!")
    while True:
        if c > 2 or c < 1:
            print("Ошибка ввода!")
            c = int(input("Введите номер транзакции из списка>> "))
        else:
            break

    if c == 1:
        t = "списание"
    else:
        t = "зачисление"

    while True:
        try:
            summ = int(input(f"Введите сумму для {t}>> "))
            break
        except:
            print("Ошибка ввода!")
    while True:
        if summ < 1:
            print("Ошибка ввода!")
            summ = int(input(f"Введите сумму для {t}>> "))
        else:
            break

    while True:
        try:
            year = int(input("Введите год>> "))
            month = int(input("Введите месяц> "))
            break
        except:
            print("Ошибка ввода!")
    while True:
        if month < 1 or month > 12:
            print("Ошибка ввода!")
            month = int(input("Введите месяц> "))
        if year < 1:
            print("Ошибка ввода!")
            year = int(input("Введите год>> "))
        else:
            break

    tr = {"account": n, "type": t, "date": {"year": year,"month": month}, "amount": summ}
    print(tr)


    if t == "списание":
        client_info["accounts"][b - 1]["balance"] -= summ
    else:
        client_info["accounts"][b - 1]["balance"] += summ

    client_info["transactions"].append(tr)
    print(f"Транзакция записана, текущий баланс на счете: {client_info["accounts"][b - 1]["balance"]}")

