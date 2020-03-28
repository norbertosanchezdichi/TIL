#Part I
nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]

print(list(zip(nums1, nums2)))
print(dict(zip(nums1, nums2)))

words = ['hi', 'ho', 'lol']

print(list(zip(words, nums1, nums2)))

five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*five_by_two)))

#Part II
midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

#Using list
final_grades = [pair[0]:max(pair[1], pair[2]) for pair in zip(students, midterms, finals)]
print(final_grades)

#Using zip(..) and map(..)
final_grades = dict(
    zip(
        students,  
        map(
            lambda pair: max(pair),
            zip(midterms, finals)
            )
        )
)
print(final_grades)