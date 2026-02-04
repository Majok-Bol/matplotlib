import matplotlib
import numpy as np 
matplotlib.use("TkAgg")  # must be before pyplot
import matplotlib.pyplot as plt
print(matplotlib.get_backend())
import numpy as np 
x=np.array([2023,2024,2025,2026,2030,2040])
y=np.array([150,250,300,200,500,600])
y2=np.array([100,300,350,450,700,800])
y3=np.array([450,600,800,300,400,500])
plt.plot(x,y,marker="o",markersize=8,markerfacecolor="cyan",linestyle="solid")
plt.plot(x,y2,marker="o",linestyle="dashed")
plt.plot(x,y3,marker="o",linestyle="dashdot")
plt.savefig("output.png")
print("Saved plot as output.png")
plt.show()
