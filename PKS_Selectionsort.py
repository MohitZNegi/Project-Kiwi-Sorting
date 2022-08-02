#import txt file, read data from it, convert string data into float
def Kiwi_weight_list():	

    
	kiwi_data = open("data.txt", "r")
	kiwi_dataread = kiwi_data.read()
	kiwi_dataread_list = kiwi_dataread.split("\n")
	kiwi_data.close()


	for kiwi_weight in range(0, len(kiwi_dataread_list), 1):
		kiwi_dataread_list[kiwi_weight] = kiwi_dataread_list[kiwi_weight].replace('"', "");
		kiwi_dataread_list[kiwi_weight] = float(kiwi_dataread_list[kiwi_weight]);
	
	return kiwi_dataread_list
# selection sort finds the minimum element in a list puts it in the first position.
def kiwi_selectionsort(L):
# loop through each element of list
    for i in range(len(L)):
        
        # Find the minimum element in remaining
        # unsorted list
        min_idx = i

         # loop to compare list elements
        for j in range(i+1, len(L)):
            if L[min_idx] > L[j]:
                min_idx = j
                
        # switch the found minimum element with
        # the first element		
        L[i], L[min_idx] = L[min_idx], L[i]
        if L == sorted(L):
            break

    return L

def kiwi_sorting():

    kiwi = Kiwi_weight_list()
    kiwi_selectionsort(kiwi)
    print ("Sorted Kiwi Weights List :")
    for i in range(len(kiwi)):
        print(kiwi[i],end=" ")

kiwi_sorting()