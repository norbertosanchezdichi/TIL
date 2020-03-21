nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]

print(list(zip(nums1, nums2)))
print(dict(zip(nums1, nums2)))

words = ['hi', 'ho', 'lol']

print(list(zip(words, nums1, nums2)))

five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*five_by_two)))