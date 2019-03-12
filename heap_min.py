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


