import matplotlib.pyplot as plt
from PKS_Bubblesort import Kiwi_bubbleSort, Kiwi_weight_list 
e= Kiwi_weight_list()
f= Kiwi_bubbleSort(Kiwi_weight_list())

plt.plot(e)
plt.plot(f)
plt.ylabel("Kiwi Weights(kg)")
plt.xlabel("Total Number of Kiwi")

plt.show()