class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        result = []

        for s in strs:
            sortedS = tuple(sorted(s)) # sort the word s as a key
            anagram_map[sortedS].append(s) # then append it to the values in the hashmap

        for value in anagram_map.values(): # go through the values in hashmap
            result.append(value) # append those values to the list of results 
        return result # return the resulting list 