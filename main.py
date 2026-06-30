print("_"*120,"\n                                                             *****Welcome to management system*****                                                    \n","_"*120)

student=['priya','preeti','geeta']
while(True):
    print()
    print("please choose any one option:")
    
    print("1.","To view student list")
    print("2.","To add new list")
    print("3.","To remove the data")
    print("4.","To search data")
    print("5.","Exit")
    print()

    choice=int(input("Enter your choice:"))
    
    if choice==1:
        print("student list:")
        for i in student:
            print(i)

        chr=input("Do u want continue this(y/n):")
        if chr=='y' or chr=='Y':
                continue
        if chr=='n' or chr=='N':
            exit
                       
    elif choice==2:
        name =input("enter student name:")
        student.append(name)
        print("name added successfully!")
        
    elif choice==3:
        name=input("enter name to remove:")
        if name in student:
            student.remove(name)
            print("name removed successfully!")
        else:
            print("not found......!")
                
    elif choice==4:
        name=input("enter name to search:")
        if name in student:
            print("name found!!!")
        else:
            print("not found!!!")

    elif choice==5:
        exit()
    else:
        not found
        
                
                
                    

                   
                
                   
               
               
               
               
               

