money  = 19863
print("money deposited is", money)

#computatiom
dot = money // 1000
dofh = money % 1000 // 500
doth = money % 1000 % 500 // 200
donh = money % 1000 % 500 % 200 // 100
doft = money % 1000 % 500 % 200 % 100 // 50
dotw = money % 1000 % 500 % 200 // 100 // 20
dotn = money // 1000 % 500 % 200 % 100 % 20 // 10
dofv = money % 1000 % 500 % 200 % 100 % 20 % 10 // 5
done = money % 1000 % 500 % 200 % 100 % 20 % 10 % 5 // 1
print("the money deposit of \"Thousands\" is:", dot)
print("the money deposit of \"Five Hundred\" is:", dofh)
print("the money deposit of \"Two Hundred\" is:", doth)
print("the money deposit of \"One Hundred\" is:", donh)
print("the momey deposit of \"Fifty\" is:", doft)
print("the money deposit of \"Twenty\" is:", dotw)
print("the money deposit of \"Ten\" is;", dotn)
print("the money deposit of \"Five\" is:", dofv)
print("the momey deposit of \"one\" is:", done)