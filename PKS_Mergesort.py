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
# MergeSort Algorithm is a divide and conquer algorithm.  
def Kiwi_mergeSort(lis):
	if len(lis) > 1:
   
		# getting the mid of the list
		mid = len(lis)//2
		# Dividing the list elements
		L = lis[:mid]
		# into 2 sections
		R = lis[mid:]
		# Sorting the first section
		Kiwi_mergeSort(L)
		# Sorting the second section
		Kiwi_mergeSort(R)
		i = j = k = 0
		# Copy data to temp lists L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				lis[k] = L[i]
				i += 1
			else:
				lis[k] = R[j]
				j += 1
			k += 1      
		# Checking for leftover elements
		while i < len(L):
			lis[k] = L[i]
			i += 1
			k += 1
		while j < len(R):
			lis[k] = R[j]
			j += 1
			k += 1
	return lis		

   
          

    
# Execute sorted list

def kiwi_sorting():
    kiwi = Kiwi_weight_list()
    Kiwi_mergeSort(kiwi)
    for i in range(len(kiwi)):
	    print(kiwi[i], end=" ")
    
kiwi_sorting()



