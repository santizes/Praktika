import re

str = input("\nВведіть рядок: ")
word = ''.join([i for i in str if not i.isdigit()])
nums = re.findall(r'\d+', str)
nums = [int(i) for i in nums]

print("\nРядок без чисел:", word)
print("Числа з рядка:", nums)

WithLarge = ' '.join(word[0].upper() + word[1:-1] + word[-1:].upper() for word in word.split())
print("\nРядок після змін:", WithLarge)

if not nums:
    print(False)
else:
    nums.remove(max(nums))
    numberIndex = [nums[i]**i for i in range(0,len(nums))]
    print("Масив чисел в степені за їхнім індексом:", numberIndex)

print("\n")