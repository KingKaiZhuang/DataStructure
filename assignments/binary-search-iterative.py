nums = [1, 3, 5, 6]
left,right=0,len(nums)-1
search=5

while left<=right:
    middle=(left+right)//2
    if nums[middle]<search:
        left=middle+1
    elif nums[middle]>search:
        right=middle-1
    else:
        print(middle)
        break