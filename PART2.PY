import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

people = ['kiran', 'arun', 'vijay', 'varun']
age = [25, 30, 35, 40]
height = [145, 151, 165, 173]
weight = [45, 55, 65, 75]

data = pd.DataFrame({'People': people, 'Age': age, 'Height': height, 'Weight': weight})

plt.figure(figsize=(10, 6))
plt.scatter(data['Age'], data['Height'], color='blue')
plt.title('Scatter Plot of Age vs Height')
plt.xlabel('Age')
plt.ylabel('Height (cm)')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(data['People'], data['Weight'], color='green')
plt.title('Bar Chart of Weight of Individuals')
plt.xlabel('People')
plt.ylabel('Weight (kg)')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(data['Age'], bins=5, color='orange', alpha=0.7)
plt.title('Histogram of Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()