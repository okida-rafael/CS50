people = [
    {"name":"Harry", "house": "Grifinoria"},
    {"name":"Cho", "house": "Corvinal"},
    {"name":"Draco", "house": "Sonserina"}
]

#essa função foi substituida pela lambda
# def f(person) :
#     return person["house"]

people.sort(key=lambda person: person["name"])

print(people)