# exercise_3: Times Table.Looping concept with for loop applied.
count = int(input("Which Times Table do you want to see: "))
for i in range (1,13,1) :
    result = count * i
    print(f"{count} x {i} = {result}")                    
