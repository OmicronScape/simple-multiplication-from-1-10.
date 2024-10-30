#Multiplication table

print("MULTIPLICATION TABLE")   

number = int(input(" Enter a number from 1 to 10, or 0 to exit:   "))   #(the number provided by the user )

while True:                                      # (As long as the condition is true, execute the following commands)
    if number < 0 or number >10:      # Here is the case where we do not input acceptable values)
        number = int(input(" Enter a number from 1 to 10, or 0 to exit:   "))   
        continue                                  # ( with continue, we ignore the unacceptable values to proceed with a new input)
    
    if  number > 0 and number <=10:     # (we check if the number is within the acceptable values)
        print("1 x ",number, "=" , (number * 1 ))
        print("2 x ",number, "=" , (number * 2 ))
        print("3 x ",number, "=" , (number * 3 ))
        print("4 x ",number, "=" , (number * 4 ))
        print("5 x ",number, "=" , (number * 5 ))
        print("6 x ",number, "=" , (number * 6 ))
        print("7 x ",number, "=" , (number * 7 ))
        print("8 x ",number, "=" , (number * 8 ))
        print("9 x ",number, "=" , (number * 9 ))
        print("10 x ",number, "=" , (number * 10 ))
        number = int(input(" Enter a number from 1 to 10, or 0 to exit:   "))
    
    elif number == 0:                       #(In case we input zero, the program terminates with the break command)
        break
    
print("End of the program!")
        
        
