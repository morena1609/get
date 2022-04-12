import matplotlib.pyplot as plt

data = [i**2 for i in range(20)]
plt.plot(data)
data_str = list(map(str, data))

with open('data.txt', 'w') as outp:
    outp.write('\n'.join(data_str))

plt.show() 