#https://www.youtube.com/watch?v=46_cL0O6xyQ&feature=emb_title
ground_premium_shipping=125.00
def ground_shipping(weight):
  flat_charge=20.00
  if weight <=2.0:
    price_per_pound=1.50
  elif weight <=6.0:
    price_per_pound=3.00
  elif weight <=10.0:
    price_per_pound=4.00
  else:
    price_per_pound=4.75

  return weight*price_per_pound+flat_charge

#print(ground_shipping(8.4))

def drone_shipping(weight):
  flat_charge=0.0
  if weight <=2.0:
    price_per_pound=4.50
  elif weight <=6.0:
    price_per_pound=9.00
  elif weight <=10.0:
    price_per_pound=12.00
  else:
    price_per_pound=14.25

  return weight*price_per_pound+flat_charge
#print(drone_shipping(8.4))

def print_cheap_shipping_method(weight):
    ground=ground_shipping(weight)
    drone= drone_shipping(weight)

    if ground < drone and ground < ground_premium_shipping:
        print("Ground shipping is cheaper and it costs {}".format(ground))
    elif drone < ground and drone < ground_premium_shipping:
        print("Drone shipping is cheaper and it costs {}".format(drone))
    else:
        print("Premium ground shipping is cheaper and it costs {}".format(ground_premium_shipping))

print(print_cheap_shipping_method(41.5))