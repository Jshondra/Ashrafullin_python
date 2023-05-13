def devide_3(nums) -> None:
    for num in nums:
        if num == 0:
            continue
        if num % 3 == 0:
            print(num, end=' ')

try:
    nums = [int(i) for i in input().split()]
    devide_3(nums)
except ValueError:
    print('Нужно вводить только числа, через пробел!')
