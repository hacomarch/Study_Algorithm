def palindrom(word):
  word = list(word)
  for i in range(0, len(word)//2):
    if word[i] == word[len(word)-1-i]:
      continue
    else:
      return False
  return True

print(palindrom('stars'))
print(palindrom('racecar'))
print(palindrom('토마토'))
print(palindrom('hello'))