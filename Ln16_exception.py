import sys

file = input("enter file name")
filefull = "../"+file+".txt"
#filefull = filepath+file
print(filefull)

while True:
  try:
      print("inside try")
      myfile = open(filefull, mode='r', encoding='Latin_1')
  except Exception:
      print("inside exeption")
      print("Error found!!!!!!!!")
      print(sys.exc_info()[1])
      file = input("enter correct file name")
      filefull = "../" + file + ".txt"
  else:
      print("inside else")
      print(myfile.read())
      sys.exit()
  finally:
      print("inside FINALY")


print("end of file")
