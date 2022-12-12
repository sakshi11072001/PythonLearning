import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats


two_d = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [ 3, 7], [3, 4]]
np_array = np.array(two_d)
print(np_array)
np_bool = np.array([0, 1, -1, 1], dtype= bool)
print(np_bool)
np_list = np_array.tolist()
print(np_list)
np_tuple = (12, 34, 78, 89)
np_array1 = np.array(np_tuple)
print(type(np_array1))
print(np_array.shape)
print(np_array.size)
print(np_array[0])
print(np_array[0:3])
first_shape  = np.array([(1,2,3), (4,5,6)])
print(first_shape)
reshaped = first_shape.reshape(3,2)
print(reshaped)
print(reshaped.flatten())
random_floats = np.random.random(5)
print(random_floats)
random_int = np.random.randint(2,10, size=(3,3))
print(random_int)

temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()
