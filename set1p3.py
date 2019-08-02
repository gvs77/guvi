c=input()
if(c.isAlpha()==True):
  if(c=='a' or c=='e' or c=='i' or c=='o' or c=='u'):
    print("Vowles")
  elif(c!='a' or c!='e' or c!='i' or c!='o' or c!='u'):
    print("Consonant")
else:
  print("Invalid")
