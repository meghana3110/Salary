import numpy as np
import matplotlib.pyplot as plt

fig, ax= plt.subplots()
width=.35

marks1=(20,30,40)
marks2=(25,30,39)
error=(1,1,1)

names=('raj','sita','mina')
ypos=np.arange(len(names))

a=ax.bar(ypos,marks1,width,yerr=error, label='Internal_1')
b=ax.bar(ypos,marks2,width,bottom=marks1, yerr=error, label='Internal_2')



ax.set_xticks(ypos,names)
ax.set_ylabel('Marks')
ax.set_xlabel('Names')
ax.set_title("marks of students")
ax.bar_label(a,label_type='center')
ax.bar_label(b,label_type='center')
ax.bar_label(b)

plt.show()