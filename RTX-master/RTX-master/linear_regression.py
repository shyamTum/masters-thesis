import pandas as pd 
import numpy as np 
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

 
df = pd.read_csv("examples/crowdnav-sequential/results.csv",header=None)
df = pd.DataFrame(df)

df_x = df.iloc[:,0:1]
df_y = df.iloc[:,1:2]

# df_x = np.array(df_x)
# df_y = np.array(df_y)

print("df ",df)
print("df_x ",df_x)
print("df_y ",df_y)

reg = linear_model.LinearRegression()
x_train,x_test,y_train,y_test = train_test_split(df_x,df_y,test_size=0.3,random_state=4)
reg.fit(x_train,y_train)
a=reg.predict(x_test)
print("a ",a)
print("y_test ",y_test)
print("x_test ",x_test)

print("y_train ",y_train)
print("x_train ",x_train)

print("coeficients ",reg.coef_)
print("intercept ",reg.intercept_)
print("Mean squared error ",mean_squared_error(y_test,a))

for x, y in zip(x_test,y_test):
   plt.scatter(x_test,y_test, color='black')
for x, y in zip(x_train,y_train):
   plt.scatter(x_train,y_train, color='blue')

plt.plot(x_test,a)
# plt.plot(x_train,a)
# plt.plot(x_test,y_test)

plt.xlabel("route_random_sigma")
plt.ylabel("Avg_overhead")

plt.show()






