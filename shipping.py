weight = 8.4

#Ground Shipping
if weight <= 2:
  price_per_pound = 1.50
elif weight <= 6:
  price_per_pound = 3.00
elif weight <= 10:
  price_per_pound = 4.00
else:
  price_per_pound = 4.75

cost_ground_shipping =(20.00 + price_per_pound * weight)
print(cost_ground_shipping)

#Ground Shipping Premium

cost_of_premium_shipping = 125.00
print(cost_of_premium_shipping)

#Drone Shipping

if weight <= 2:
  price_per_pound = 4.50
elif weight <= 6:
  price_per_pound = 9.00
elif weight <= 10:
  price_per_pound = 12.00
else:
  price_per_pound = 14.25

cost_of_drone_shipping = (price_per_pound * weight)
print(cost_of_drone_shipping)

#the cheapest method of shipping a 4.8 pound package is ground shipping and it would cost $34.4 

#the cheapest method of shipping a 41.5 pound package is ground shipping premium and it would cost $125.0



