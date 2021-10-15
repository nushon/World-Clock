import datetime

while (True):

    city = input("Enter a City name: ")

    PresentTime = datetime.datetime.now()

    hour = PresentTime.hour
    minute = PresentTime.minute
    second = PresentTime.second


    if city == "Boston":
        hour = hour - 4
        print(city, str(hour) + ":" + str(minute) + ":" + str(second))


    elif city == "Tokyo":
        hour = hour + 9
        print(city, str(hour) + ":" + str(minute) + ":" + str(second))

    elif city == "Chicago":
        hour = hour - 5
        print(city, str(hour) + ":" + str(minute) + ":" + str(second))

    elif city == "America":
        hour = hour + 6
        print(city, str(hour) + ":" + str(minute) + ":" + str(second))

    elif city == "Egypt":
        hour = hour + 2
        print(city, str(hour) + ":" + str(minute) + ":" + str(second))

    elif city == "Ukraine":
        hour = hour + 3
        print(city, str(hour) + ":" + str(minute) + ":" + str(second))

    elif city == "Zambia":
        hour = hour + 2
        print(city, str(hour) + ":" + str(minute) + ":" + str(second))

    elif city == "France":
        hour = hour + 2
        print(city, str(hour) + ":" + str(minute) + ":" + str(second))

    elif city == "Germany":
        hour = hour + 2
        print(city, str(hour) + ":" + str(minute) + ":" + str(second))

    elif city == "China":
        hour = hour - 4
        print(city, str(hour) + ":" + str(minute) + ":" + str(second))

    elif city == "South Africa":
        hour = hour - 4
        print(city, str(hour) + ":" + str(minute) + ":" + str(second))

    elif city == "Nigeria":
        hour = hour + 1
        print(city, str(hour) + ":" + str(minute) + ":" + str(second))

    elif city == "Cyprus":
        hour = hour + 3
        print(city, str(hour) + ":" + str(minute) + ":" + str(second))

    elif city == "Seattle":
        print(hour)
        hour = hour - 7
        print(city, str(hour) + ":" + str(minute) + ":" + str(second))
        break

    elif city == "exit":
        break

    else:
        print(city, str(hour) + ":" + str(minute) + ":" + str(second))