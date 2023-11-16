Jimport pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def multList(a,b):
    l0=[]
    for i in range(len(a)):
        l0.append(a[i]*b[i])
    return l0

# Read database
df = pd.read_excel('database.xlsx')
df.index = df['ID']
df.drop(['ID'],axis=1,inplace=True)

# Store into arrays
X,Y = [],[]
for x,y in df.iterrows():
    X.append(y['Height']/1.0)
    Y.append(y['Weight']/1.0)
X = np.array(X)
Y = np.array(Y)

# Calculate intercept values    
sqX = [x*x for x in X]
sqY = [y*y for y in Y]
n = len(X)
a = ((np.sum(Y) * np.sum(sqX)) - (np.sum(X) * np.sum(multList(X,Y)))) / ((n * np.sum(sqX)) - np.square(np.sum(X)))
b = (((n * np.sum(multList(X,Y))) - np.sum(X) * np.sum(Y)) / ((n * np.sum(sqX)) - np.square(np.sum(X))))

# Predicted value of Y
newY = a + b*X

# Plotting the graph
plt.scatter(X,Y,color='red')
plt.plot(X,newY,color='black')
plt.ylabel('Weight')
plt.xlabel('Height')
plt.title('Linear Regression')
plt.show()

# Predict weight based on height
W = float(input("Enter height: "))
pred_height = a + b*W
print(f"Predicted weight: {round(pred_height,2)}")

# Regression Coefficient
b0 = X-np.mean(X)
sum = 0
for i in b0:
    sum+=round(i,1)
    sum=round(sum,1)
print("\nRegression Coefficient: ",sum)