import matplotlib.pyplot as plt

regions=['Ctg','Dhaka','Sylhet','Rajshahi']
revenue=[3000,4000,1500,1000]
plt.pie(revenue,labels=regions,autopct='%1.1f%%',colors=['gold','purple','lightblue','pink'])
plt.title('revenue contribution by rigions')
plt.show()