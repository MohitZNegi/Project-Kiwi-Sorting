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
#Bubble sort algorithm swaps the adjacent elements in a list if they are out of order.
def Kiwi_bubbleSort(L):
    	
	tn = len(L) #tn is total number of elements in the kiwi list
    

# loop through each element of list
	for i in range(tn):
    	 # keep track of swapping
		switched = False
		

 # loop to compare list elements
		for j in range(0, tn-i-1):

      # compare two adjacent elements
			if L[j] > L[j+1] :
    	 # switching occurs if elements
        # are not in the intended order
				L[j], L[j+1] = L[j+1], L[j]
				switched = True
			# no switching means the list is already sorted
    # so no need for further comparison	
		if not switched:
			break
	
	return L

		

		
#Execute the list
def kiwi_sorting():
    
    kiwi = Kiwi_weight_list()
    Kiwi_bubbleSort(kiwi)
    print ("Sorted Kiwi Weights List :")
    for i in range(len(kiwi)):
        print(kiwi[i],end=" ")
	
		

kiwi_sorting()




    




	


    	

		
	    




