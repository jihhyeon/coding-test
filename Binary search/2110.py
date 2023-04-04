#공유기 c개를 설치, 최대한 많은 곳에 와이파이 사용, 한집에 공유기 하나 설치
#c개의 공유기를 n개의 집에 적당히 설치, 가장 인접한 두 공유기 사이 거리 최대
n, c = list(map(int, input().split(' '))

array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

start = array[1] - array[0]
end = array[-1] - array[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    value = array[0]
    count = 1
    for i in range(1,n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1

    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)