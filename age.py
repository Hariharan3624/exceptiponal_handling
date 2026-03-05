valid = False
while not valid:
    try:
        n=int(input("enter a age: "))
        if n%2==0:
           print("this is an even numbered age")
        else:
           print("this is an odd numbered age")
            
        valid = True
    except ValueError:
      print("error occured")