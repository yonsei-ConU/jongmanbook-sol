def hasWord(y, x, word):
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    if boggle[y][x] != word[0]:
        return False
    if len(word) == 1:
        return True
    flag = False
    for i in range(8):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < 5 and 0 <= nx < 5:
            flag = flag or hasWord(ny, nx, word[1:])
    return flag


for _ in range(int(input())):
    boggle = [input() for _ in range(5)]
    N = int(input())
    for __ in range(N):
        word = input()
        ans = False
        for i in range(5):
            for j in range(5):
                ans = ans or hasWord(i, j, word)
        print(word, 'YNEOS'[1-ans::2])
