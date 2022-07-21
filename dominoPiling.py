def dominoPiling(row, column):
    
    total = ((row * column) // 2)
    print(total)

def main():
    m, n = map(int, input().split())
    if (1 <= m <= n) and n <= 16:
        dominoPiling(m, n)
if __name__ == '__main__':
    main()