
import collections


from collections import Counter
#import txt file, read data from it, convert string data into float
def Kiwi_weight_list():	

    
	kiwi_data = open("data.txt", "r")
	kiwi_dataread = kiwi_data.read()
	kiwi_dataread_list = kiwi_dataread.split("\n")


	for kiwi_weight in range(0, len(kiwi_dataread_list), 1):
		kiwi_dataread_list[kiwi_weight] = kiwi_dataread_list[kiwi_weight].replace('"', "");
		kiwi_dataread_list[kiwi_weight] = float(kiwi_dataread_list[kiwi_weight]);
	
	return kiwi_dataread_list
#Bubble sort algorithm swaps the adjacent elements in a list if they are out of order.
def Kiwi_bubbleSort(kiwi):
	tn = len(kiwi) #tn is total number of elements in the kiwi list
    

# loop through each element of list
	for i in range(tn):
    	
		swapped = False
		


		for j in range(0, tn-i-1):


			if kiwi[j] > kiwi[j+1] :
				kiwi[j], kiwi[j+1] = kiwi[j+1], kiwi[j]
				swapped = True
				
		if not swapped:
			break
    
		


kiwi = Kiwi_weight_list()

Kiwi_bubbleSort(kiwi)

print ("Sorted array :")
for i in range(len(kiwi)):
	print (kiwi[i],end=" ")



	


    	

		
	    




