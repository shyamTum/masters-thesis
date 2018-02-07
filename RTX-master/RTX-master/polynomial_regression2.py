import pandas as pd 
import numpy as np 
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
from scipy.interpolate import *
from sklearn import preprocessing as pp
from sklearn.metrics import mean_squared_error

df = pd.read_csv("examples/crowdnav-sequential/results.csv",header=None)
df = pd.DataFrame(df)

df_x = df.iloc[:,0:1]
df_y = df.iloc[:,1:2]

df_x = np.array(df_x)
df_y = np.array(df_y)
# df_x = df_x.flatten()
# df_y = df_y.flatten()

print("df ",df)
print("df_x ",df_x)
print("df_y ",df_y)

# df_x = np.array([0,1,2,3,4,5])
# df_y = np.array([0,0.8,0.9,0.1,-0.8,-1])

x_train,x_test,y_train,y_test = train_test_split(df_x,df_y,test_size=0.3,random_state=4)

for x, y in zip(x_test,y_test):
   plt.scatter(x_test,y_test, color='black')
for x, y in zip(x_train,y_train):
   plt.scatter(x_train,y_train, color='blue')


regression2 = pp.PolynomialFeatures(degree=2)
x_train_=regression2.fit_transform(x_train)
x_test_ = regression2.fit_transform(x_test)
# a=regression.predict(x_test)

lr2 = linear_model.LinearRegression()
lr2.fit(x_train_,y_train)
a2=lr2.predict(x_test_)


regression5 = pp.PolynomialFeatures(degree=5)
x_train_=regression5.fit_transform(x_train)
x_test_ = regression5.fit_transform(x_test)
# a=regression.predict(x_test)

lr5 = linear_model.LinearRegression()
lr5.fit(x_train_,y_train)
a5=lr5.predict(x_test_)


regression6 = pp.PolynomialFeatures(degree=6)
x_train_=regression6.fit_transform(x_train)
x_test_ = regression6.fit_transform(x_test)
# a=regression.predict(x_test)

lr6 = linear_model.LinearRegression()
lr6.fit(x_train_,y_train)
a6=lr6.predict(x_test_)

print("y_test ",y_test)
print("x_test ",x_test)
print("coefficients for deg 2 ",regression2.get_feature_names())
print("coefficients for deg 5 ",regression5.get_feature_names())
print("coefficients for deg 6 ",regression6.get_feature_names())
print("degree2 prediction ",a2)
print("degree5 prediction ",a5)
print("degree6 prediction ",a6)
print("mean_squared_error for degree 2 ",mean_squared_error(y_test,a2))
print("mean_squared_error for degree 5 ",mean_squared_error(y_test,a5))
print("mean_squared_error for degree 6 ",mean_squared_error(y_test,a6))




x_test=np.linspace(0,1,3)
# a2=np.linspace(4.5,0.5,5)
# a5=np.linspace(3.5,0.5,5)
# a6=np.linspace(2.5,0.5,5)

plt.plot(x_test,a2,'b-')
plt.plot(x_test,a5,'r-')
plt.plot(x_test,a6,'black')

plt.xlabel("route_random_sigma")
plt.ylabel("Avg_overhead")

plt.show()