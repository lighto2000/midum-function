# get the midum of numbers

> it's will remove all the element in list until the len of numbers be 1 or 2 and sum them togther 


```python

from time import sleep
def midum(the_list):
    counter = 0
    while len(the_list) > 2:
        the_list.remove(the_list[0])
        the_list.remove(the_list[-1])
        counter+=1
        print(the_list)
        sleep(2)
    print(the_list[0] + the_list[1])
    print((the_list[0] + the_list[1]) / 2)


midum([1,2,3,4,2,25,6,7])

```