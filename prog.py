import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from blh2xyz import blh2xyz
from xyz2enu import xyz2enu
from mvg_avg import mvg_avg
from kalman_filter import kalman_filter

data = pd.read_excel("coordinates.xlsx")
d = pd.DataFrame(data)

xyz = blh2xyz(data)
enu = xyz2enu(xyz)
e = [item[0] for item in enu]
n = [item[1] for item in enu]
u = [item[2] for item in enu]

#t1 = t[0:(len(t)-5)]
t = np.linspace(0, len(e), len(e))

# Signal filtration stage

e_mvg_avg = mvg_avg(e)
e_kal = kalman_filter(e)

e_kal = e_kal[0]
e = e[0:100]
e_kal = e_kal[0:100]
e_mvg_avg = e_mvg_avg[0:100]
t = t[0:100]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(t,e, 'k--', linewidth=1.0, label='Measurement')
ax.plot(t,e_kal, 'r', label='Kalman filtering')
ax.plot(t,e_mvg_avg, 'g',label='Moving average filtering')
plt.xlabel(r'Time $\Delta$T [s]')
plt.ylabel('E - coordinate values')
plt.title('Moving average and Kalman filtering comparison')
ax.legend()

plt.show()


