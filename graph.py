import matplotlib.pyplot as plt
import random

data = [random.randint(0, 50) for i in range(20)]
print(data)
plt.plot(data)
data_str = list(map(str, data))

with open('data.txt', 'w') as outp:
    outp.write('\n'.join(data_str))

plt.show()