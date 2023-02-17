def partition(array, low, high):
	
	pivot = array[high]  # considers the right-most element as pivot
	i = low
	for j in range(low, high):
		
		if array[j] <= pivot:
            # swap the lower in the right with the higher in the left
			array[i], array[j] = array[j], array[i]
			i += 1
			
	array[i], array[high] = array[high], array[i]
	return i


def kthSmallest(array, k, low, high):


	if (k > 0 and k <= high - low + 1):

		pindex = partition(array, low, high)

		# if position is same as k
        # return array of the pivot index
		if (pindex - low == k - 1):
			return array[pindex]

		# If position is greater use the left sub array
		if (pindex - low > k - 1):
			return kthSmallest(array, k, low, pindex - 1)

		# Else use the right sub array
		return kthSmallest(array, k - pindex + low - 1, pindex + 1, high)


def quickselect(array, k):
    low = 0
    high = len(array) - 1 
    return kthSmallest(array, k, low, high)



if __name__ == "__main__":
    array = [ 2, 6, 4, 9, 10, 100, 8 ]
    print("K-th smallest element is :", end = "")
    print(quickselect(array, 4))




