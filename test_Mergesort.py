import unittest
from random import randint, random 
from PKS_Mergesort import Kiwi_mergeSort, Kiwi_weight_list, kiwi_sorting
from time import time 
# generate list of numbers in random order
averagecase= [randint(1,10000) for _ in range(700)] 
# generate list of sorted numbers
bestcase= sorted(averagecase) 
# generate list of completely unsorted numbers
worstcase= sorted(averagecase, reverse=True) 
class test(unittest.TestCase):
        # test the kiwi weights list - average sorted list with float data 
    def test_merge_sort_Kiwi(self):
        start= time()
        self.assertEqual(Kiwi_mergeSort(Kiwi_weight_list()), Kiwi_mergeSort(Kiwi_weight_list()))
        print("Kiwi Weight Case:", time()-start)    
    # test the average sorted list
    def test_merge_sort_average(self):
        start= time()
        self.assertEqual(Kiwi_mergeSort(averagecase), bestcase)
        print("Average Case:", time()-start)
    #test the completely sorted list
    def test_merge_sort_best(self):
        start= time()
        self.assertEqual(Kiwi_mergeSort(bestcase), bestcase)
        print("Best Case:", time()-start)
    
    # test the completely unsorted list
    def test_merge_sort_worst(self):
        start= time()
        self.assertEqual(Kiwi_mergeSort(worstcase), bestcase)
        print("Worst Case:",time()-start)
#Execute the test
if __name__ == '__main__':
    unittest.main()