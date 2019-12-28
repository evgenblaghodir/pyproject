inputfile = ("../names.txt")
myfile = open(inputfile, mode='r', encoding='utf8')

#print(myfile.read())

for num, line in enumerate(myfile):
    if ("Lana" in line):
        print(str(num) + " Hello " +line.strip())

myfile.close()

inputfile = ("../rockyou.txt")
outputfile = ("../mypass.txt")
pass_to_find = "kolya"
myfile2 = open(inputfile, mode='r', encoding='latin_1')
myfile3 = open(outputfile, mode='a', encoding='latin_1')
for num, line in enumerate(myfile2):
    if (pass_to_find in line):
        print(str(num) + " " +line.strip())
        myfile3.write("Find pass" +line)

myfile2.close()
myfile3.close()

