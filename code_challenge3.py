sender_name = input("Sender Name: ")
item_type = input("Type of Item: ")
is_fragile = input("Fragile? yes/no --->")
weight = float(input("Weight (kg): "))
distance = float(input("Distance (km): "))
is_express = input("Express? yes/no --->")
is_international = input("International? yes/no --->")


base_cost = (weight * 2.50) + (distance * 0.15)


if weight <= 2.0 and distance <= 100 and not is_express and not is_international:
    total = 0.00

elif is_international and is_express:
    total = (base_cost * 1.40) + 50

elif is_express or (is_international and weight > 20):
    total = (base_cost * 1.20) + 25

elif weight > 30 or distance > 1000:
    total = base_cost + 30

else:
    total = base_cost


print("Sender Name:", sender_name)
print("Type of item:", item_type)
print("Fragile:", is_fragile)
print("Weight:", weight)
print("Distance:", distance)
print("Express:", is_express)
print("International:", is_international)
print("Total price: Php", total)