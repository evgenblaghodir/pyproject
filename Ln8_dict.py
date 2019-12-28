enemy = {
    'loc_x': 12,
    'loc_y': 55,
    'color': 'green',
    'health': 100,
    'name': 'vasya',
}
print(enemy)
enemy['rank'] ='Admiral'
print(enemy)

del enemy['rank']
print(enemy)

enemy['loc_x'] = enemy['loc_x']+40
enemy['health'] =enemy['health']-30
if (enemy['health']<80):
    enemy['color'] = 'yellow'

print(enemy)
print(enemy.keys())
print(enemy.values())

for item in enemy.keys():
    print(item)
for item in enemy.values():
    print(item)