words = input().lower()
vowel = ['a','e','i','o','u']

for word in words:
    if word == vowel:
        continue
    
print(word)
