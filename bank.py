
def complain():
    a = input("Введите свою жалобу на банк:\n")
    with open("complains.txt", "a", encoding="utf-8") as complains:
        complains.write(a + "\n")

def suggestions():
    with open("suggestions.txt", "r", encoding="utf-8") as b:
        suggestion = b.read()
        print(suggestion)