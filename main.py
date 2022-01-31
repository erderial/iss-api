import requests

from datetime import datetime
import smtplib
import time

mylat = 44.426765
mylong = 26.102537

MY_EMAIL = input("what is your g-mail address :")
MY_PASSWORD = input("what is your mail password?: ")
RECIPIENT = input("recipient email: ")

def iss_pos():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data=response.json()
    print(data)

    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]

    iss_position = (longitude, latitude)

    return (iss_position)

def get_time():
    
    global mytime 
    param = {
        "lat": mylat,
        "lng": mylong,
        "formatted": 0 
    }

    response2 = requests.get("https://api.sunrise-sunset.org/json", params = param)
    response2.raise_for_status()
    data2 = response2.json()
    sunrise = data2["results"]["sunrise"]
    sunset = data2["results"]["sunset"]

    timenow = datetime.now()

    hour_sunrise = int(sunrise.split("T")[1].split(":")[0])
    hour_sunset = int(sunset.split("T")[1].split(":")[0])
    mytime =  int((str(timenow).split(" ")[1]).split(":")[0])
    
    return (hour_sunset,hour_sunrise)
    
sunset,sunrise = get_time()
iss_lat,iss_long = iss_pos()



def check_if_can(sunset, sunrise,iss_lat,iss_long):
    if mytime in range(sunset,25) or mytime in range(0,sunrise+1):
        print("you can start looking for the ISS, let's see where the ISS is")
        if iss_lat in range(int(mylat)-5,int(mylat)+5) and iss_long in range(mylong-5,mylong+5):
            print("THE ISS IS IN RANGE BOSS")
            return True
        else:
            print("ISS it not in range sorry")

#we can set a flag to check a number of times:
flag = 60 #minutes

x = 0
while x < flag:
    x+=1
    if check_if_can(sunset,sunrise,iss_lat,iss_long):
        connection = smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECIPIENT,
            msg="Subject:Look for the ISS chief \n\n It should be above and plain to seee if there's a clear sky"
        )
    time.sleep(60)
=======


