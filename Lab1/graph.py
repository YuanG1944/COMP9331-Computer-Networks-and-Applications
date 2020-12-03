import matplotlib.pyplot as plt
import numpy as np


plt.axis([0, 18000, 0, 8])
plt.grid()
plt.scatter(738.81, 6.86, alpha=0.6)
plt.scatter(6606.01, 4.48, alpha=0.6)
plt.scatter(16099.98, 5.12, alpha=0.6)
plt.xlabel("Distance(km)")
plt.ylabel("Ratio")
plt.annotate('Brisbane', xy=(838.81, 6.86))
plt.annotate('Serdang', xy=(6706.01, 4.48))
plt.annotate('Berlin', xy=(16199.98, 5.12))
plt.show()