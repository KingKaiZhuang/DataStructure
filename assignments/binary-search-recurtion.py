def BinarySearch(nums,search,x,y):
    middle=(x+y)//2

    if x<=y:
        if nums[middle]>search:
            return BinarySearch(nums,search,x,middle-1)
        elif nums[middle]<search:
            return BinarySearch(nums,search,middle+1,y)
        else:
            return middle
    return -1

nums=[1, 3, 5, 6]
tar=6
left,right=0,len(nums)-1

ans=BinarySearch(nums,tar,left,right)
print(ans)