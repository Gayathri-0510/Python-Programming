def e_com():
    l=[]
    print("1. Add to cart \n2. Remove from cart\n3. Search in cart\n4. Display cart\n5. Show total no. of products\n6. Sort the items alphabetically\n7. Clear the cart\n8. Exit")
    ch=int(input("Enter your choice:"))
    while ch!=8:
        if(ch == 1):
            add=str(input("Enter a product to add: "))
            l.append(add)
        elif(ch==2):
            pro=str(input("Enter a product to remove : "))
            if pro in l:
                l.remove(pro)
            else:
                print("Product not found")
        elif ch==3:
            pro=str(input("Enter a product to search : "))
            if pro in l:
                print("Product found")
            else:
                print("Product not found")
        elif ch==4:
            print("Products in cart : ")
            print(l)
        elif ch==5:
            print("Total no. of products in cart : ",len(l))
        elif ch==6:
            l.sort()
            print("Sorted cart : ",l)
        elif ch==7:
            l.clear()
            print("Your cart is empty")
        else:
            print("Default choice")
        ch=int(input("Enter your choice:"))
e_com()