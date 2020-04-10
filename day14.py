def anagram_finder(strs):
  """
  function that groups all the anagrams in a list
  :input type, strs: List[str]
  :rtype: List[List[str]]
  """
  #dictionary to hold sorted strings as key and a list of corresponding anagrams as values
  anagrams = {}

  #for each string in the list, sort the string, if the sorted string is in the dictionary,
  #append the string to the corresponding list 
  for i in range(len(strs)):
      sortedStr = tuple(sorted(strs[i]))
      if sortedStr in anagrams:
          anagrams[sortedStr].append(strs[i])
      else:
          anagrams[sortedStr] = [strs[i]]

  return list(anagrams.values())


print(anagram_finder(["eat", "tea", "tan", "ate", "nat", "bat"]))