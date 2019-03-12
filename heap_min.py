def swap(array,a,b):
    key=array[a]
    array[a]=array[b]
    array[b]=key
def heap_min(array,index):    #index is just as index in python
    left=2*index+1
    right=2*index+2
    if left<=(len(array)-1) and array[left]<array[index]:
        small=left
    else:
        small=index
    if right<=(len(array)-1) and array[right]<array[small]:
        small=right
    if small!=index:
        swap(array,small,index)
        heap_min(array,small)
def buld_min_heap(array):
    last=(len(array)//2-1)
    for i in range(last,-1,-1):
        heap_min(array,i)
    return array
array=[5,2,3,8,4,9]
print(buld_min_heap(array))

#for extrating the min value in heap algo.

def min_heap_extract(array):                                          #heappop in python 
    heap_leang=len(array)
    if heap_leang<=1:
        print("error that the size of array smaller than 1")
    while heap_leang>1:
        if heap_leang>1:
            maxi=array[0]
            swap(array,0,-1)
            heap_leang=heap_leang-1
            array=array[:heap_leang]                                   #for partical use we use delarray[-1] insist of "array=array[:heap_leang]"
            heap_min(array,0)
            return maxi                                         #for printing all min in coloum just put "print" insist of "return"
#for calling the the min_heap_extract function 
print(min_heap_extract(array))
