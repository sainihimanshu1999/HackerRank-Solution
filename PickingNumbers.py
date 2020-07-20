import sys
if __name__ == '__main__':
    n = int(input().strip())
    array = list(map(int, input().strip().split(' ')))
    frequency = [0] * 100
    max_value = 0
    for number in array:
        frequency[number] += 1
    for i in range(1, 100):
        max_value = max(max_value, frequency[i] + frequency[i - 1])
    print(max_value)
