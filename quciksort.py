import random
def QuickSort(nums:list[int], l:int, r:int):
    if l>=r:
        return
    # 随机找一个划分点，使得左边的值都比该值小，右边的都比该值大
    pivot = random.randint(l,r)
    pivot_value = nums[pivot]
    nums[l],nums[pivot] = nums[pivot],nums[l]
    i,j = l+1,r
    while True:
        while i<j and nums[i] <= pivot_value:
            i += 1
        while i<j and nums[j] >= pivot_value:
            j -= 1
        if i == j:
            break
        # 将小于等于pivot_value的值和大于等于的交换位置
        nums[i],nums[j] = nums[j],nums[i]
    # 定义下一个分割点
    new_pivot = i if nums[i]<=nums[l] else i-1
    nums[l],nums[new_pivot] = nums[new_pivot],nums[l]
    QuickSort(nums,l,new_pivot-1)
    QuickSort(nums,new_pivot+1,r)

a = [8,4,5,6,45,8,1,2,23,18,4,12,7,3,9,2,6,8]

QuickSort(a,0,len(a)-1)
print(a)
