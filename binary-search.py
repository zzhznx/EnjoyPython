#! /usr/bin/env python
# encoding: utf-8

#求任意一个i使得array[i]等于val，不存在返回-1
def binary_search_1(nums, target):
    low, high = 0, len(nums) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] <= target:
            low = mid + 1
            if nums[mid] == target:
                ans = mid
                break
        else:
            high = mid - 1
    return ans

#求最小的i使得array[i]等于val，不存在返回-1
def binary_search_2(nums, target):
    low, high = 0, len(nums) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            if nums[mid] == target:
                ans = mid
    return ans

#求最大的i使得array[i]等于val，不存在返回-1
def binary_search_3(nums, target):
    low, high = 0, len(nums) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] <= target:
            low = mid + 1
            if nums[mid] == target:
                ans = mid
        else:
            high = mid - 1
    return ans

#求最大的i使得array[i]小于val，不存在返回-1
def binary_search_4(nums, target):
    low, high = 0, len(nums) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
            ans = mid
        else:
            high = mid - 1
    return ans

#求最小的i使得array[i]大于val，不存在返回-1
def binary_search_5(nums, target):
    low, high = 0, len(nums) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
            ans = mid
    return ans
    
def main():
    L = [1, 2, 2, 2, 3, 3, 4, 5, 6]
    L2 = [1, 2, 3, 4, 5]
    print(binary_search_1(L, 2))
    print(binary_search_2(L, 2))
    print(binary_search_3(L, 3))
    print(binary_search_4(L, 2))
    print(binary_search_5(L, 2))

    print(binary_search_2(L2, 1))

if __name__ == '__main__':
    main()