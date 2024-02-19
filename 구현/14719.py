h, w = map(int, input().split())
block = [map(int, input().split())]
rain = 0

for i in range(1, w-1):
    left_max = max(block[:i])
    right_max = max(block[i+1:])

    compare = min(left_max, right_max)

    if block[i] < compare:
        rain += compare - block[i]

print(rain)