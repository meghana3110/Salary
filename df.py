import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tst=pd.read_csv("Salary_Data.csv")

sal=tst.iloc[:,1].values
ye=tst.iloc[:,0].values
ts=tst.loc[tst["Salary"]>50000]
t1=ts.iloc[:,1].values
y=ts.iloc[:,0].values
print(ts)
plt.plot(ye,sal,color='m')
plt.plot(y,t1,color='m',marker='.')
plt.ylabel('Salary')
plt.xlabel('Years of Experience')
plt.title('Employee Salary-Experience Relation')
plt.show()









# val=pd.DataFrame(sal,index=ye)
# val=val.sort_values(by=0)

# df=val[val[0]>50000.0]

# c=df.index
# d=df.iloc[ : , 0].values

# #plotting graph
# fig,ax=plt.subplots()
# a=ax.plot(ye,sal,color='m')
# #b=ax.plot(c,d,color='m',marker='.')