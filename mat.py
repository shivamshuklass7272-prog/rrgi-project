# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np

# # # # x = np.array([0, 1, 2, 3, 4])
# # # # y = np.array([0, 1, 0, 1, 0])

# # # # x1 = np.array([2, 3])
# # # # y1 = np.array([1, 3])

# # # # # First graph
# # # # plt.subplot(1, 2, 1)

# # # # plt.plot(x, y, color="red",
# # # #          linestyle="dashed",
# # # #          linewidth=2.5,
# # # #          marker="*",
# # # #          markersize=10,
# # # #          markerfacecolor="blue",
# # # #          markeredgecolor="green")

# # # # plt.xlabel("x-axis")
# # # # plt.ylabel("y-axis")
# # # # plt.title("my-graph 1")
# # # # plt.grid()

# # # # # Second graph
# # # # plt.subplot(1, 2, 2)

# # # # plt.plot(x1, y1)

# # # # plt.xlabel("x-axis")
# # # # plt.ylabel("y-axis")
# # # # plt.title("my-graph 2")
# # # # plt.grid()

# # # # plt.show()
# # # import matplotlib
# # # import matplotlib.pyplot as plt
# # # import numpy as np
# # # import matplotlib
# # # import matplotlib.pyplot as plt
# # # import numpy as np

# # # x = np.array([0, 1, 2, 3, 4])
# # # y = np.array([0, 1, 0, 1, 0])

# # # x1 = np.array([2, 3])
# # # y1 = np.array([1, 3])

# # # plt.plot(x, y, color="red",
# # #          linestyle="dashed",
# # #          linewidth=2.5,
# # #          marker="*",
# # #          markersize=10,
# # #          markerfacecolor="blue",
# # #          markeredgecolor="green")

# # # plt.plot(x1, y1, color="black",
# # #          linewidth=2,
# # #          marker="o")

# # # plt.xlabel("x-axis")
# # # plt.ylabel("y-axis")
# # # plt.title("my-graph")
# # # plt.grid()

# # # plt.show()

# # import matplotlib
# # import matplotlib.pyplot as plt
# # import numpy as np

# # x = np.array([0, 1, 2, 3, 4])
# # y = np.array([0, 1, 0, 1, 0])

# # x1 = np.array([2, 3])
# # y1 = np.array([1, 3])

# # # Graph 1
# # plt.subplot(2, 2, 1)
# # plt.plot(x, y)
# # plt.title("Graph 1")
# # plt.grid()

# # # Graph 2
# # plt.subplot(2, 2, 2)
# # plt.plot(x1, y1)
# # plt.title("Graph 2")
# # plt.grid()

# # # Graph 3
# # plt.subplot(2, 2, 3)
# # plrsize=10, markerfacecolor="blue",
# #          markeredgecolor="green")
# # plt.title("Graph 3")t.plot(x, y, color="red", linestyle="dashed",
# #          linewidth=2.5, marker="*",
# #          marke
# # plt.grid()

# # # Graph 4
# # plt.subplot(2, 2, 4)
# # plt.plot(x1, y1, color="green", marker="o")
# # plt.title("Graph 4")
# # plt.grid()

# # plt.show()
# # #data.gov.in# 

# # import matplotlib.pyplot as plt
# # import numpy as np
# # x = np.array([1,3,5,7])
# # y = np.array([2,4,6,8])
# # plt.subplot(1,3,2)
# # plt.plot(x,y)
# # x1 = np.array([1,2,3,4,5])
# # y1= np.array([0,1,0,1,0])
# # plt.subplot(1,2,2)
# # plt.plot(x1,y1)
# # #plt.plot(x,y,x1,y1)
# #plt.show()
# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([0, 1, 2, 3, 4])
# y = np.array([0, 1, 0, 1, 0])

# x1 = np.array([2, 3])
# y1 = np.array([1, 3])

# # Graph 1
# plt.subplot(2, 2, 1)
# plt.plot(x, y)
# plt.title("Graph 1")
# plt.grid()

# # Graph 2
# plt.subplot(2, 2, 2)
# plt.plot(x1, y1)
# plt.title("Graph 2")
# plt.grid()

# # Graph 3
# plt.subplot(2, 2, 3)
# plt.plot(x, y, color="red", linestyle="dashed",
#          linewidth=2.5, marker="*",
#          markersize=10, markerfacecolor="blue",
#          markeredgecolor="green")
# plt.title("Graph 3")
# plt.grid()

# # Graph 4
# plt.subplot(2, 2, 4)
# plt.plot(x1, y1, color="green", marker="o")
# plt.title("Graph 4")
# plt.grid()

# plt.show()
from pathlib import Path

import pandas as pd

import os
os.environ.pop("MPLBACKEND", None)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

data_path = Path(__file__).with_name("data.csv")
if data_path.exists():
	df = pd.read_csv(data_path)
else:
	print("data.csv not found; using a small built-in example dataset.")
	df = pd.DataFrame({
		"Name": ["Amit", "Ananya", "Rahul"],
		"Marks": [78, 84, 91],
	})

print(df.info())
print(df.head())