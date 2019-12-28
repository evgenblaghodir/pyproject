

cities = ["NY", "Kyiv", "Berlin", "Dnepr", "London"]
for i in cities:
    print(i)

print(len(cities))
print("aaa\t"+cities[4])
print("aaa\t"+cities[-4].upper())
cities[0] = "Boston"
print(cities)
cities.append("Paris")
print(cities)
cities.insert(0, "Praga")
print(cities)

del cities[2]
print(cities)
count=0
for i in cities:
    if (i == "Paris"):
        del cities[count]
    count+=1

print("last "+str(cities))

cities.remove("London")
print(cities)

deleted_city = cities.pop()
print(deleted_city)
print(cities)
cities.sort()
print(cities)