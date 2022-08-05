import requests
import ctypes
import datetime
import time
from datetime import date
SPI_SETDESKWALLPAPER = 20
path_to_folder = r"C:\Users\Muhammet\Desktop\Twittervehavauyg\image"  #Buraya arka plan resimlerimizin bulunduğu klasörümüzün tam yolunu ekliyoruz.
api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
city = "istanbul"
url = api_address + city 

def main():
    timestamp = datetime.datetime.now().time() #şimdi ki zaman
    start_night = datetime.time(18, 1)  #akşam 6 dan 1 dakika sonrası
    end_night = datetime.time(6, 0)     #sabah 6 ve gece bitişi
    start_day = datetime.time(6, 1)     #sabah 6 1 dakka sonrası sabah başlangıcı
    end_day = datetime.time(18, 0)      #akşam 6 gündüz vakti bitişi
    json_data = requests.get(url).json()
    format_data = json_data["weather"][0]["main"]  
    print(timestamp)
    print(start_night)
    print(end_night)
    print(start_day)
    print(end_day)
    print("Looped")
    print(format_data)
    if date.today().weekday() == 6:
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_folder + "\Sunday.jpg", 3)
        time.sleep(100)
        print("Sunday")
        main()
    if format_data == "Rain":
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_folder + "\rain.jpg", 3)
        time.sleep(100)
        print("Rain")
        main()
    elif format_data == "Thunderstorm":
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_folder + "\storm.jpg", 3)
        time.sleep(100)
        print("Storm")
        main()
    elif format_data == "Drizzle":
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_folder + "\Drizzle.jpg", 3)
        time.sleep(100)
        print("Drizzle")
        main()
    elif format_data == "Clouds":
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_folder + "\clouds.jpg", 3)
        time.sleep(100)
        print("Clouds")
        main()
# Night & Day
    elif format_data == "Clear" and start_night <= timestamp or timestamp <= end_night:
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_folder + "\night.jpg", 3)
        time.sleep(100)
        print("Night")
        main()
    elif format_data == "Clear" and start_day <= timestamp <= end_day:
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_folder + "\day.jpg", 3)
        time.sleep(100)
        print("Day")
        main()
    else:
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_folder + "\River.jpg", 3)
        time.sleep(100)
        print("Other")
        main()
main()