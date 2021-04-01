def modCountingSort(arr, order):
    n = len(arr)

    # Create an list of output array, initilize to all 0
    output = [0] * (n)

    # Temp list
    count = [0] * (10)

    # put the frequency of each digit
    for i in range(0, n):
        index = (arr[i] / order)
        count[int(index % 10)] += 1

    # add the sum from previous
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] / order)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radixsort(arr):
    temp=len(str(max(arr)))
    order=1
    for i in range(temp):
        modCountingSort(arr,order)
       # print(list(arr))
        order*=10

arr=[170, 45, 75, 90, 802, 24, 2, 66]
radixsort(arr)
print(list(arr))