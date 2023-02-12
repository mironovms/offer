import time
from datetime import datetime
current_datetime = datetime.now()
vremya = datetime.now()
def offert():
        print("Welcome!")
        zarplata = int(input("Введите свою предполагаемую оплату труда: "))
        poidet = [0, 48]
        if zarplata < 50:
                dobavka = 0
                dobavka = int(input("Прибавьте еще немного и вы сможете нанять меня на работу: "))
                zarplata = zarplata + dobavka

        print("Congratulations! Вы можете нанять меня на работу\nУ вас есть 120 часов на обдумывание этого предложения и принятия положительного решения)\nВремя пошло) ")

        print(f"Сейчас {vremya}")
        return vremya

offert()
time.sleep(432000)
print(f"К сожалению Время вышло, это последняя микросекунла - {vremya}, очень жаль что мы не подходим друг другу)")
