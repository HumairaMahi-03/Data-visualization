import matplotlib.pyplot as plt


plt.scatter([1,2,3],[56,67,78],color='blue',marker='o',label='class A')
plt.scatter([1,2,3],[45,56,65],color='red',marker='o',label='class b')
plt.xlabel('hours studied')
plt.ylabel('Exam scores')
plt.title('comparison of two classes')
plt.legend()
plt.grid(True)
plt.show()