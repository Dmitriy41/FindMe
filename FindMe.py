import requests
from pyfiglet import Figlet

def getInfo(ip):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        result = {
            'IP': response.get('query'),
            'Город': response.get('city'),
            'Страна': response.get('country'),
            'Широта':response.get('lat'),
            "Долгота": response.get('lon')
        }
        for i in result:
            print(str(i)+":"+str(result[i]))
    except requests.exceptions.ConnectionError:
        print("Проверьте ваше соединение")

def main():
    a = Figlet(font="slant")

    print(a.renderText("Find me"))
    print('''Программа позволяющая с легостью вычислить положение ip(Страну, город, координаты) @DEVELOPED by kodel_lite 
             telegram:https://t.me/Kodel_lite
             Instagram: https://www.instagram.com/kodel_lite/
             gitHub:https://github.com/Dmitriy41
''')

    a== '0'
    while a!='1':
        print("Введите IP цели")
        ip = input()
        getInfo(ip=ip)
        print("Еще раз(1-выход, 0-заново)")
        a = input()

if __name__ == '__main__':
    main()

