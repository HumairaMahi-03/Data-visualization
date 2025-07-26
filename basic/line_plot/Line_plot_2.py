import matplotlib.pyplot as plt
x=['Mon','Tues','wed','Thurs',"fri"]
y=[10,20,15,25,12]

plt.plot(x,y)
plt.title('bakery sales this week ')

plt.xlabel('day of the week')
plt.ylabel('sales per day')
plt.show()