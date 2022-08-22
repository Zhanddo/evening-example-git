
password = 220822
for attempt in range(3):
    user = int(input("Введите пароль: "))
    if user == password:
        print("Пароль верный!")
        break
    else:
        print("Доступ запрещен!")