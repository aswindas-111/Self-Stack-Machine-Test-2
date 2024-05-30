def square_numbers(nums):
    for i in nums:
        if i % 2 == 0:
            yield i
            
my_nums = square_numbers([1,2,3,4,5,6,8])

square_nums = (x * x for x in my_nums if x % 2 == 0)

for sq in square_nums:
    print(sq)