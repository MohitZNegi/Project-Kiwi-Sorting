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
# selection sort finds the minimum element in a list puts it in the first position.

def kiwi_selectionsort(kiwi):


# loop through each element of list
    for i in range(len(kiwi)):
        
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i

         # loop to compare list elements
        for j in range(i+1, len(kiwi)):
            if kiwi[min_idx] > kiwi[j]:
                min_idx = j
                
        # Swap the found minimum element with
        # the first element		
        kiwi[i], kiwi[min_idx] = kiwi[min_idx], kiwi[i]

kiwi = Kiwi_weight_list()
kiwi_selectionsort(kiwi)
print ("Sorted array")
for i in range(len(kiwi)):
	print(kiwi[i],end=" ")
