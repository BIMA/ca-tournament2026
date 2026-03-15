def main():
    x = 0
    n = int(input())
    for i in range(n):
        m = input()
        if "++" in m:
            x+=1
        elif "--" in m:
            x-=1
    print(x)


if __name__ == "__main__":
    main()
