#선형탐색알고리즘
#element가 someList안에 있으면, 그 위치를 리턴
def linearSearch(element, someList):
  for i in range(len(someList)):
    if someList[i] == element:
      return i
  return None

print(linearSearch(2, [2, 3, 5, 7, 11]))
print(linearSearch(0, [2, 3, 5, 7, 11]))
print(linearSearch(5, [2, 3, 5, 7, 11]))
print(linearSearch(3, [2, 3, 5, 7, 11]))
print(linearSearch(11, [2, 3, 5, 7, 11]))