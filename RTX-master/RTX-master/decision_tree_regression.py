import pandas as pd 
import numpy as np 
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
from scipy.interpolate import *
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv("examples/crowdnav-sequential/results.csv",header=None)
df = pd.DataFrame(df)
# print("df ",df)

df_x = df.iloc[:,0:1]
df_y = df.iloc[:,1:2]

df_x = np.array(df_x)
df_y = np.array(df_y)
# df_x = df_x.flatten()
# df_y = df_y.flatten()

print("df ",df)
print("df_x ",df_x)
print("df_y ",df_y)

x_train,x_test,y_train,y_test = train_test_split(df_x,df_y,test_size=0.3,random_state=4)

regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_1.fit(x_train, y_train)
regr_2.fit(x_train, y_train)


y_1 = regr_1.predict(x_test)
y_2 = regr_2.predict(x_test)


print('y_1 predicted  ',y_1)
print('y_2 predicted  ',y_2)

print('y_test  ',y_test)
print('x_test  ',x_test)

print("y_1 mean square error !!!!!!!!! ", mean_squared_error(y_test,y_1))
print("y_2 mean square error !!!!!!!!! ", mean_squared_error(y_test,y_2))

x_test=np.linspace(0,5,100)
y_2=np.linspace(0,5,100)
y_test=np.linspace(0,5,100)
y_1=np.linspace(0,5,100)
plt.scatter(x_test, y_test, c="darkorange")
plt.plot(x_test, y_1, color="cornflowerblue")

plt.plot(x_test, y_2, color="yellowgreen")
plt.plot(df_x,df_y,'o')
plt.xlabel("input")
plt.ylabel("avg_overhead")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()