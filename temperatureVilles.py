# coding: UTF-8
"""
Script: pythonProject6/temperatureVilles
Création: admin, le 15/01/2021
"""


# Imports
import requests
import mysql.connector
import time

# Fonctions
def get_temperature(ville):
    url="http://api.openweathermap.org/data/2.5/weather?q="+ville+",fr&units=metric&lang=fr&appid=0a73790ec47f53b9e1f2e33088a0f7d0"
    return float(requests.get(url).json()['main']['temp'])


def get_pression(ville):
    url="http://api.openweathermap.org/data/2.5/weather?q="+ville+",fr&units=metric&lang=fr&appid=0a73790ec47f53b9e1f2e33088a0f7d0"
    return float(requests.get(url).json()['main']['pressure'])


def set_temperature_bdd(ville, temperature, pression):


    #update dans la bdd
    cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='bdd_temperaturesvilles')
    cursor = cnx.cursor()
    update_temp = ("UPDATE temperaturevilles SET temperatures = (%s), pression = (%s) WHERE ville = (%s)")
    data = (temperature, pression, ville)
    cursor.execute(update_temp, data)
    cnx.commit()
    cursor.close()
    cnx.close()

    print("fin exec set_temp_bdd")


# Programme principal
def main():
    villes = ["la buisse", "plouhinec", "vic-fezensac", "rouen"]
    #set_temperature_bdd("la buisse", get_temperature("la buisse"))
    #set_temperature_bdd("plouhinec", get_temperature("plouhinec"))
    #set_temperature_bdd("vic-fezensac", get_temperature("vic-fezensac"))
    #set_temperature_bdd("rouen", get_temperature("rouen"))

    while 1:
        for ville in villes:
            set_temperature_bdd(ville, get_temperature(ville), get_pression(ville))

            print(ville, get_temperature(ville), get_pression(ville))
        print(time.asctime(time.localtime(time.time())))
        time.sleep(300)




if __name__ == '__main__':
    main()
# Fin
