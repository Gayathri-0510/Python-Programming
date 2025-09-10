def library():
    lib={}
    print("1. Add a Book\n2. Remove a book\n3. Search for a book\n4. Display all books\n5. Count total no. of books\n6. check if a book title exists\n7. Exit")
    ch=int(input("Enter your choice"))
    while(ch!=7):
        if ch==1:
            bid=int(input("Enter book id : "))
            bname=str(input("Enter book name : "))
            lib[bid]=bname
            print("Added successfully")
        elif ch==2:
            bid=int(input("Enter book id : "))
            if bid in lib:
                removed=lib.pop()
                print("Removed successfully")
            else:
                print("Book not found")
        elif ch==3:
            bid=int(input("Enter book id : "))
            if bid in lib:
                print("Book found")
            else:
                print("Book not found")
        elif ch==4:
            bid=int(input("Enter book id : "))
            bname=str(input("Enter book name to update"))
            if bid in lib:
                lib[bid]=bname
                print("Updated successfully")
            else:
                print("Book id not found")
        elif ch==5:
            print(lib)
        elif ch==6:
            print("Total no. of books : ",len(lib))
        elif ch==7:
            bname=str(input("Enter book name"))
            if bname in lib.values():
                print("Book found")
            else:
                print("Book not found")
        else:
            print("Invalid choice")
            
        ch=int(input("Enter your choice : "))
library()