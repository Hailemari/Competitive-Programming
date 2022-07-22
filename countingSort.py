def countingSort(arr):
    freqCount = [0]*100
    for i in arr:
        freqCount[i] = freqCount[i]+1

    print (' '.join(map(str, freqCount)))
def main():
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    countingSort(arr)
if __name__ == '__main__':
    main()