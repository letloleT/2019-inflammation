import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(
	fname = 'data/inflammation-01.csv',
	delimiter = ',')

ave_imflammation = np.mean(
	data,
	axis = 0
)

plt.plot(ave_inflammation)
