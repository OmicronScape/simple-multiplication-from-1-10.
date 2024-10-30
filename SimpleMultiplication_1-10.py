#Πρόγραμμα προπαίδειας 

print("ΠΙΝΑΚΑΣ ΠΡΟΠΑΙΔΕΙΑΣ")   

number = int(input(" Δώστε έναν αριθμό από το 1 έως 10, ή 0 για έξοδο:   "))   #(o αριθμός που δίνει ο χρήστης )

while True:                                      # (Οσο η συνθήκη ειναι αληθής εκτέλεσε τις παρακάτω εντολές)
    if number < 0 or number >10:      # Εδώ ειναι η περίπτωση που δεν εισάγουμε  αποδεκτές τιμές)
        number = int(input(" Δώστε έναν αριθμό από το 1 έως 10, ή 0 για έξοδο:   "))   
        continue                                  # ( με το continue αγνοουμε τις μη αποδεκτές τιμές για να συνεχίσουμε με νεα εισαγωγή)
    
    if  number > 0 and number <=10:     # (ελέγχουμε εαν ο αριθμός ειναι μεσα στις αποδεκτές τιμές)
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
        number = int(input(" Δώστε έναν αριθμό από το 1 έως 10, ή 0 για έξοδο:   "))
    
    elif number == 0:                       #(Σε περίπτωση που εισάγουμε μηδέν το πρόγραμμα τερματίζεται με την εντολή break)
        break
    
print("Τέλος προγράμματος")
        
        
