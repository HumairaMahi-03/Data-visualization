import matplotlib.pyplot as plt
months=[1,2,3,4]
sales=[1000,1500,1200,1800]
plt.plot(months,sales,color='red',linestyle='--',linewidth=2,marker='o',label='2025 sales data')
plt.xlabel('Months')
plt.ylabel('sales of per months')
plt.title('bakery sales for first four month')
plt.legend(loc='upper left')
plt.grid(color='pink' ,linestyle=':',linewidth=1)
plt.xticks([1,2,3,4],['M1','M2','M3','M4'])
plt.show()