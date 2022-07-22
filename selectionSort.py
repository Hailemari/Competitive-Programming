
def selectionSort(arr):

    for i in range(len(arr)):
        
        init_index= i
        for j in range(i+1, len(arr)):
            if arr[init_index] > arr[j]:
                init_index = j
            
        if init_index != i:    
            arr[i], arr[init_index] = arr[init_index], arr[i]
    print(arr)
def main():
    arr = [4, 7, 2, 6, 0, 5, 6]
    selectionSort(arr)
if __name__ == '__main__':
    main()