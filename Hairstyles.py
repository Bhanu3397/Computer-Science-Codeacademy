hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
# print(len(prices))
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0
new_prices = [price - 5 for price in prices] 
#List Comprhension
for price in prices:
  total_price += price
average_price = total_price / len(prices)
print("Average Haircut Price: ${}".format(average_price))
# new_prices=[]
# for price in prices:
#   new_prices.append(price-5)
# print(new_prices)
total_revenue =0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: "+str(total_revenue))
average_daily_revenue= total_revenue/7
print(average_daily_revenue)
cuts_under_30=[hairstyles[i] for i in range(len(hairstyles)) if new_prices[i]<30]
print(cuts_under_30)