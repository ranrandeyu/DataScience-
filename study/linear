import pandas as pd
import numpy as np

from sklearn import cross_validation
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.neighbors import  KNeighborsRegressor
from sklearn.metrics import mean_squared_error



df = pd.read_csv('housing.csv',sep=',',header=None)
#shuffle the data
df = df.iloc[np.random.permutation(len(df))]
X= df[df.columns[:-1]].values
Y = df[df.columns[-1]].values

cv = 10
print( 'linear regression')
lin = LinearRegression()
scores = cross_validation.cross_val_score(lin, X, Y, cv=cv)
print("mean R2: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
predicted = cross_validation.cross_val_predict(lin, X,Y, cv=cv)
print ('MSE:',mean_squared_error(Y,predicted))

print( 'ridge regression')
ridge = Ridge(alpha=1.0)
scores = cross_validation.cross_val_score(ridge, X, Y, cv=cv)
print("mean R2: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
predicted = cross_validation.cross_val_predict(ridge, X,Y, cv=cv)
print('MSE:',mean_squared_error(Y,predicted))

print ('lasso regression')
lasso = Lasso(alpha=0.1)
scores = cross_validation.cross_val_score(lasso, X, Y, cv=cv)
print("mean R2: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
predicted = cross_validation.cross_val_predict(lasso, X,Y, cv=cv)
print ('MSE:',mean_squared_error(Y,predicted))
