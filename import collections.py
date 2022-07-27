import collections


from collections import Counter

def Kiwi_weight_list():	
    kiwi_data = open("kiwidata.txt", "r")
    kiwi_weights = []
    for kiwi_weight in kiwi_data:
    	kiwi_weights.append(int(kiwi_weight))
	    #return kiwi_weights
    
kiwi_data = open("data.txt", "r")
kiwi_dataread = kiwi_data.read()
kiwi_dataread_list = kiwi_dataread.split("\n")
print(kiwi_dataread)

for kiwi_weight in range(0, len(kiwi_dataread_list), 1):
   kiwi_dataread_list[kiwi_weight] = kiwi_dataread_list[kiwi_weight].replace('"', "");
   kiwi_dataread_list[kiwi_weight] = float(kiwi_dataread_list[kiwi_weight]);
print(kiwi_dataread_list)
print(kiwi_dataread_list[1]+kiwi_dataread_list[2])


#print(type(kiwi_dataread_list[0]))