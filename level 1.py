# Shopping Cart Total
# Write a program that calculates the total price of a product based on the product selected and the quantity entered by the user. The program should support the 
# four available products and display the total amount that needs to be paid


#double quotes removed
#semi colon ';' removed from every line
headPhone = 999
smartWatch = 1599
PS5 = 1299
iPad = 599

productName = input("Enter Product Name: ")
#added int for integer input
quantity = int(input("Enter the Quantity of the Product: "))

if productName == "headPhone":
    totalPrice = headPhone * quantity

#smartWatch instead of headPhone
elif productName == "smartWatch":
    totalPrice = smartWatch * quantity
#PS5 instead of headPhone
elif productName == "PS5":
    totalPrice = PS5 * quantity
#iPad instead of headPhone
elif productName == "iPad":
    totalPrice = iPad * quantity
#else statement added
else:
    print("Invalid Product Name!")
    exit()
#removed curly bracket from totalPrice and write this after double quotes comma ',' is added
print("Total Amount To Be Paid:", totalPrice)