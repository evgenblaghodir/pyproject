


my_string = "adasdasd"
name = "vAsYa pupKin"
print(name.title())

print(name.capitalize())
print(name.upper())


print("Stroka1\nStroka2\n\n\tStorka3")

a = " . , dadya vanya "
print(a)
print(a.rstrip())
print(a.lstrip())
new_str = ""
for i in a:
    if ( i == "." or i== ","):
        new_str=new_str
    else:
        new_str=new_str+i.lstrip()


print(new_str)