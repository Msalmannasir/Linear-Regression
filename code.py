import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

 

data = pd.read_csv('dataset.csv')
#print(data.head(10))

 

realX = data.iloc[:,0:4].values
realY = data.iloc[:,4].values

 

le = LabelEncoder()
realX[:,3] = le.fit_transform(realX[:,3])
#print(realX[:,3])

 

OH = OneHotEncoder(categorical_features=[3])

 

realX = OH.fit_transform(realX).toarray()
#print(realX)

 

training_X, testing_X, training_Y, testing_Y = train_test_split(realX, realY, test_size = 0.2, random_state = 0)

 

lin = LinearRegression()
lin.fit(training_X, training_Y)
pred = lin.predict(testing_X)

 

print(pred, "     ")
print(testing_Y)