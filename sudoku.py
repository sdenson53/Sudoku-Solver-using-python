a = [int(x) for x in input("Enter the digits for row 1 : ").split()]
while len(a) != 9:
    a = [int(x) for x in input("Error: digits not equal to 9 \n Enter the digits for row 1 : ").split()]

b = [int(x) for x in input("Enter the digits for row 2 : ").split()]
while len(b) != 9:
    b = [int(x) for x in input("Error: digits not equal to 9 \n Enter the digits for row 2 : ").split()]

c = [int(x) for x in input("Enter the digits for row 3 : ").split()]
while len(c) != 9:
    c = [int(x) for x in input("Error: digits not equal to 9 \n Enter the digits for row 3 : ").split()]

d = [int(x) for x in input("Enter the digits for row 4 : ").split()]
while len(d) != 9:
    d = [int(x) for x in input("Error: digits not equal to 9 \n Enter the digits for row 4 : ").split()]

e = [int(x) for x in input("Enter the digits for row 5 : ").split()]
while len(e) != 9:
    e = [int(x) for x in input("Error: digits not equal to 9 \n Enter the digits for row 5 : ").split()]

f = [int(x) for x in input("Enter the digits for row 6 : ").split()]
while len(f) != 9:
    f = [int(x) for x in input("Error: digits not equal to 9 \n Enter the digits for row 6 : ").split()]

g = [int(x) for x in input("Enter the digits for row 7 : ").split()]
while len(g) != 9:
    g = [int(x) for x in input("Error: digits not equal to 9 \n Enter the digits for row 7 : ").split()]

h = [int(x) for x in input("Enter the digits for row 8 : ").split()]
while len(h) != 9:
    h = [int(x) for x in input("Error: digits not equal to 9 \n Enter the digits for row 8 : ").split()]

z = [int(x) for x in input("Enter the digits for row 9 : ").split()]
while len(z) != 9:
    z = [int(x) for x in input("Error: digits not equal to 9 \n Enter the digits for row 9 : ").split()]


chart = [
    a,
    b,
    c,
    d,
    e,
    f,
    g,
    h,
    z
]


def find_solution(ch):
    find = find_empty(ch)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(ch, i, (row, col)):
            ch[row][col] = i

            if find_solution(ch):
                return True

            ch[row][col] = 0

    return False


def valid(ch, num, pos):  # checking validity of hit and trial
    for i in range(len(ch[0])):     # checking in row
        if ch[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(ch)):    # checking in column
        if ch[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3     # checking in their respective boxes
    box_y = pos[0] // 3     # checking in their respective boxes

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if ch[i][j] == num and (i,j) != pos:
                return False

    return True


def print_chart(ch):
    for i in range(len(ch)):
        if i % 3 == 0 and i != 0:
            print("------------------------")

        for j in range(len(ch[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(ch[i][j])
            else:
                print(str(ch[i][j]) + " ", end="")


def find_empty(ch):
    for i in range(len(ch)):
        for j in range(len(ch[0])):
            if ch[i][j] == 0:
                return (i, j)

    return None


if __name__ == '__main__':
    find_solution(chart)
    print_chart(chart)
