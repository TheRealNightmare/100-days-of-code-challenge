travel_log = [
    {
        "country" : "France",
        "visits" : 12,
        "cities" : ["Paris","Lille", "Dijon"]
    },
    {
        "country" : "Japan",
        "visits" : 30,
        "cities" : ["Tokyo","Kyoto","Osaka"]
    }
]

def add_country(country,times,cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = times
    new_country["cities"] = cities

    travel_log.append(new_country)
add_country("Korea",5,["seaol","sss"])

print(travel_log)