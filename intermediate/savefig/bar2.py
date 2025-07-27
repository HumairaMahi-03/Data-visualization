import matplotlib.pyplot as plt

product=['A','B','C','D']
sales=[1000,1500,800,1200]
plt.bar(product,sales,color='purple',label='sales 2025')
plt.xlabel('Product')#identify x-axis
plt.ylabel('Sales')#identify y-axis
plt.title('product sales comparison')#identify the chart
plt.legend()#to show the label
plt.xticks(['A','B','C','D'],['M1','M2','M3','M4'])#to rename the x-axis list
plt.savefig('bar_chart.png',dpi=300,bbox_inches='tight')
plt.show()