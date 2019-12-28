def create_record(name, phone, address):
    """Create record"""
    record={
        'name': name,
        'phone': phone,
        'address': address
    }
    return record
user1 = create_record("Vasya", "434-34-54", "Polevaya" )

print(user1)

def give_award(medal, *persons):
    """give medals to person"""
    for person in persons:
        print("Mister " + person.title() + " win medal " + medal)

give_award("champion", "vasya", "petua")