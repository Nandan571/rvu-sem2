import numpy as np

array = np.random.randint(1, 21, size=(3, 3))
print("Original array:")
print(array)

array[array < 10] = 0
print("\nModified array:")
print(array)
