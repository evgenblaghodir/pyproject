enemy = {
    'loc_x': 12,
    'loc_y': 55,
    'color': 'green',
    'health': 100,
    'name': 'vasya',
    'images': ['image1.jpg', 'image2.jpg', 'image3.jpg']
}

all_enemies = []
for x in range(0, 10):
    all_enemies.append(enemy.copy())


print(all_enemies)

all_enemies[5]['health'] = 30
all_enemies[5]['name'] = 'gosha'
all_enemies[9]['name'] = 'petya'
all_enemies[5]['loc_y'] +=10
for x in all_enemies:
    print(x)
print("****")
print(all_enemies[5])

