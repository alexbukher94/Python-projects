def ground_shipping(weight):
  if weight <= 2:
    cost = 1.50
  elif weight > 2 and weight <= 6:
    cost = 3.00
  elif weight > 6 and weight <= 10:
    cost = 4.00
  else:
    cost = 10.00
  return weight * cost + 20.00

def drone_shipping(weight):
  if weight <= 2:
    cost = 4.50
  elif weight > 2 and weight <= 6:
    cost = 9.00
  elif weight > 6 and weight <= 10:
    cost = 12.00
  else:
    cost = 14.25
  return weight *cost + 0.00

  

def cheapest_method(weight):
  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  premium_shipping = 125.00
  
  if ground < drone and ground < premium_shipping:
    return ground
  elif drone < ground and drone < premium_shipping:
    return drone
  else:
    return premium_shipping

print(cheapest_method(4.8))
