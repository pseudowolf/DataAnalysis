"""
Проверьте, возможно ли изменить список в процессе итерирования.
Ответ: воможно
"""
numbers = list(range(10))
print(numbers)
i = 1
for num in numbers:
    numbers[len(numbers) - i] = num
    i += 1
    if i >= len(numbers) / 2:
        break

print(numbers)