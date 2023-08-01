#purpose first project (وظيفة عمل)
name=input("please what is your name ? ")
print("welcome ",name)
i=0
print("please aswear these questions")
yearsin=int(input("How many years are you in this field "))
if yearsin >= 3:
    print ("so good")
else:
    print("we need more years in this field but we may try to accept you if you answer three of the questions that will be presented to you")
q1=input ("what is data type of 9.5 ")
if q1 == "float" or q1 == "flt":
    print("so good")
    i = i + 1
else:
    print("no, its flt or float")
q2=input ("what is data type of \"1000\" ")
if q2 == "str" or q2 == "string":
   print("so good")
   i = i + 1
else:
        print("no, its str or string ")
q3=input("If we want to write equal, we write it like this = or like this == ")
if q3 == "==":
      print ("so good")
      i = i + 1
else:
      print("no, we write it like this ==.")
q4=input("ok you are so good so i will tell you a hard question, How many data types does Python have apart from array ")
if q4 =="5":
      print("perfect")
      i = i+1
else:
      print("no, its 5")
q5 = input ("In Python we use & or and")
if q5== "and":
     print ("so good")
     i = i+1
else:
     print ("no we use and in python")
if i >= 3:
     print("you are accepted")
else:
     print("sorry but you are rejected")
