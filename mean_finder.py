def mean(D,M):
    sums = 3*M
    new_mean = (sums+D)/4
    return new_mean

def main():
    D = int(input())
    M = int(input())
    print(mean(D,M))


if __name__ == '__main__':
    main()