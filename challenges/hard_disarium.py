def is_disarium(x):
    n = x
    total = 0
    count = 1
    nums = []
    while n / 10 > 1:
        nums.append(n % 10)
        n //= 10
        count += 1
    c = len(nums)
    for i in range(1, count + 1):
        total += n**i
        if c > 0:
            n = nums[c - i]
    return total == x
