import matplotlib.pyplot as plt

hours_studies=[1,2,3,4,5,6,7,8]
scores=[50,55,60,65,70,75,80,85]

plt.scatter(hours_studies,scores,color='blue',marker='o',label='student data')
plt.xlabel('hours studied')
plt.ylabel('Exam scores')
plt.title('relationship between study time and exam scores')
plt.legend()
plt.grid(True)
plt.show()