#Receive the amount
amount = eval(input("enter an amount, for example , 11.56: "))

#Convert the amount to cents

remainingAmount = int(amount * 100)

# end 不会换行了

print("your amount", amount, end = '')
print("your remaningAmount is ", remainingAmount)

