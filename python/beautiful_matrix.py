def main():
    rows = []
    for n in range(5):
        rows.append(list(map(int, input().split())))

    mid_position = (2, 2)
    one_position = (2, 2)

    for r in range(5):
        for c in range(5):
            if rows[r][c] == 1:
                one_position = (r, c)
                break

    answer = abs(mid_position[0] - one_position[0]) + abs(mid_position[1] - one_position[1])

    print(answer)


if __name__ == "__main__":
    main()
