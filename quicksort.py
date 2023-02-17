def quicksort(array):
    low = 0
    high = len(array) - 1

    quicksort_helper(array, low, high)

def quicksort_helper(array, low, high):
    if(low < high):
        pivot = partition(array, low, high)
        quicksort_helper(array, low, pivot)
        quicksort_helper(array, pivot+1, high)

def partition(array, low, high):
    # getting the pivot to be almost the central element

    pivot = array[(high+low)//2]
    i = low
    j = high

    while True:
        while array[i] < pivot:
            i+=1

        while array[j] > pivot:
            j-=1

        if(i >= j):
            return j

        #swapping
        array[i], array[j] = array[j], array[i]


if __name__ == "__main__":
    array = [5, 7, 8, 2, 3, 6, 1, 9]
    print(array)
    quicksort(array)

    print(array)
