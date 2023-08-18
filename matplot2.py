from matplotlib import pyplot as plt
import numpy as np

plt.style.use("fivethirtyeight")

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
x_indices = np.arange(len(ages_x))
width=0.25

dev_y = [38496, 42000, 46752, 49320, 53200,56000, 62316, 64928, 67317, 68748, 73752]
#plt.bar(ages_x, dev_y, color="#444444", label="All Devs")
plt.bar(x_indices - width, dev_y ,width=width,
          color="#444444", label="Python")


py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
#plt.plot(ages_x, py_dev_y, color="#008fd5", label="Python")
plt.bar(x_indices, py_dev_y ,width=width, 
        color="#008fd5", label="Python")


js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
#plt.plot(ages_x, js_dev_y, color="#e5ae38", label="JavaScript")
plt.bar(x_indices+width, js_dev_y,width=width, 
        color="#e5ae38", label="Python")


plt.legend()

plt.xticks(ticks=x_indices,labels=ages_x)

plt.title("Median Salary  by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary ")

plt.tight_layout()

plt.show()