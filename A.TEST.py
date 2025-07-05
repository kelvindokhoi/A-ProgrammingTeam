# Filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(num):
    return num % 2 == 0

even_numbers_iterator = filter(is_even, numbers)
even_numbers = list(even_numbers_iterator)
print(even_numbers)
# Output: [2, 4, 6, 8, 10]

# Using a lambda function to filter vowels
letters = ['a', 'b', 'c', 'd', 'e']
vowels = ['a', 'e', 'i', 'o', 'u']

filtered_vowels_iterator = filter(lambda letter: letter in vowels, letters)
filtered_vowels = list(filtered_vowels_iterator)
print(filtered_vowels)
# Output: ['a', 'e']