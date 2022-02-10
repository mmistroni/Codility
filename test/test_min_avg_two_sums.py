import unittest

from pprint import pprint
from src.min_avg_two_sums import solution
class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [4, 2, 2, 5, 1, 5, 8]
        res = solution(A)
        #pprint(res)

        '''
        
        test_min_avg_two_sums.py .INPUT ARRAY :
        
        
Original Array        [4,    2,     2,     5,      1,     5,      8]

Prefix Sum Array

idx 0..7

    range (2, 7)

    holder= []
    

    for idx in range(2, 7):
         tpl_idx = idx -1
         diff = idx -2
         
         for idx, item in enumerate(A[idx:]):
            
            holder.append(tpl_idx, item, (item-A[idx-2]) / (idx + 2) 


[0,      4,    6,     8,    13,     14,    19,     27]   we start from item at index 2, dividing by 2
                              
               3      2.6   3.25    2.8    3.1     3.8
                  
              (8-4)/2  13-4 /3  14-4 / 4    19-4 / 5   27-4 / 6       // start from item at index 3, subtracting item at index 1
                         2     3    2.5    3   3.8
                      
                                                          // start from item at index 4, subtracting item at index 2
                  13-6/2   14-6/3   19-6 /4   27-6/5                                     
                    3.5     2.66      3.25     4.2 
                 
                  14-8 /2  19-8/3  27-8 / 4                                     
                    3       3.66     4.75                                // start from item at index 5, subtracting  item at index 3
                  
                  19-13/2    27-13/2                                      
                    3          7  
                  
                  
                   27-14 /2                                      
                     6.5                                  // start from item 6, subtracting item 5 
                                                        
                                                       
                      
                      
                  
                      2                                  // start from item=13, take away 8
                      vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
Prefixed sums is:[0, 4, 6, 8, 13, 14, 19, 27]
        
        
        
        '''



if __name__ == '__main__':
    unittest.main()
