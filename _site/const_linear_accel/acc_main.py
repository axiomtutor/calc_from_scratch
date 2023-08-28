import matplotlib.pyplot as plt
import numpy as np
import js

fig = plt.figure()
ax = fig.add_subplot()

x_data = np.random.randint(0,100,(500,))
y_data = np.random.randint(0,100,(500,))
z_data = np.random.randint(0,100,(500,))

ax.scatter(x_data, y_data, z_data)

def show_plt():
    inp = js.document.getElementById("3dinput")
    display(fig, target="3dplot", append=False)
    print("TEST")
    inp.write("TEST")

