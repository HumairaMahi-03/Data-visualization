import matplotlib.pyplot as plt

scores=[45,56,67,78,89,90,98,87,76,65,54,43,68,69,47,59,60,67,58,59]

plt.hist(scores,bins=5,color='purple',edgecolor='black')
plt.title('scores of the students')
plt.xlabel('score range')
plt.ylabel('number of students')


plt.show()
