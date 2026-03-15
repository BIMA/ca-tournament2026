def main():
    n, k = map(int, input().split())
    n_list = list(map(int, input().split()))
    next_round = 0
    threshold = n_list[k-1]
    for n in n_list:
        if n > 0  and n >= threshold:
            next_round += 1
    print(next_round)


if __name__ == "__main__":
    main()
