#Defining the 2x4function to get input from the user
def m_size():
    
    row=int(size[0])
    column=int(size[2])
    
    for i in range(1,row+1):
        for a in range(1,column+1):
            
            
            y=input(f"Value for ({i},{a}) : ")
            matrix.append(y)
                    
        print()
    
while True:
    #Get the variables from the user
    size=str(input("Type matrix size (2x2 to 9x9) only: "))

    #Checking whether user inserts  the valid matrix size
    if len(size)==3 and int(size[0])>1 and int(size[0])<10 and int(size[2])>1 and int(size[2])<10:
        matrix=[]
        row=int(size[0])
        column=int(size[2])
        #Calling m_size function
        m_size()

        print("Matrix size : ",size)


                   
        list2=[]    
        for x in range (row):
            for y in range (column):
                value=matrix[0]
                list2.append(value)
                print(value ,end=" ")
                matrix.pop(0)

            print()

        print()

        #Taking user inputs to multiply the matrix by a number
        multiply=int(input("Type a value to multiply the matrix : "))
        print()
        m=[]
        for i in list2:
            p=int(int(i)*multiply)
            m.append(p)

        for x in range (row):
            for y in range (column):
                value=m[0]
                m.append(value)
                print(value ,end=" ")
                m.pop(0)

            print()
        break

    else:
        print()
        print("Invalid matrix size")
        print("Re-enter the correct matrix size")
        print()
        continue
