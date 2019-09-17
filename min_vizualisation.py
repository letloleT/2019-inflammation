import numpy as np
import matplotlib.pyplot as plt

data = np.loadetxt(
	fname = 'data/inflammation-01.csv',
	delimiter = ','
)

min_inflammation = np.min(
	data,
	axis = 0
)
plt.plot(min_inflammation)
