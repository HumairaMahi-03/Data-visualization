import matplotlib.pyplot as plt;

contribution =['NGO Contribution','Safe Water Access','Sanitation Facilities','Hygiene Awareness']
revenue=['15','35','30','20']
plt.pie(revenue,labels=contribution,autopct='%1.1f%%',colors=['skyBlue','Lightgreen','lightblue','gold'])
plt.title('SDG 6 Achievements & NGO Contribution in Bangladesh')
plt.savefig('Water&Sanitation.png',dpi=300,bbox_inches='tight')
plt.show()