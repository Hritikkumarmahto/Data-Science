string1 = input("Enter the string: ")

i = 0
vowel_count = 0
consonant_count = 0
index_sum = 0

while i < len(string1):
    ch = string1[i]

    if ch.isalpha():  
        if ch in "aeiouAEIOU":
            vowel_count += 1
        else:
            consonant_count += 1

    index_sum += i
    i += 1

print("Vowels =", vowel_count)
print("Consonants =", consonant_count)
print("Sum of indices =", index_sum)