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

y1=df_y.iloc[0:10,:]
y2=df_y.iloc[10:20,:]

df_x = np.array(df_x)
df_y = np.array(df_y)
# df_x = df_x.flatten()
# df_y = df_y.flatten()

print("df ",df)
print("df_x ",df_x)
print("df_y ",df_y)

x_train,x_test,y_train,y_test = train_test_split(df_x,df_y,test_size=0.5)

# print("x_train ",x_train)
# print("x_test ",x_test)
# print("y_train ",y_train)
# print("y_test ",y_test)
print("x1 ",y1)
print("x2 ",y2)

print("mean_squared_error ",mean_squared_error(y1,y2))