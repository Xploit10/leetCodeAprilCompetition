class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for n in strs:
            string = ''.join(sorted(n))
            if string in dict:
                dict[string].append(n)
            else:
                dict[string] = [n]
        annograms = []
        for key, value in dict.items():
            annograms.append(value)
        return annograms

"""
Given an array of strings, group anagrams together.

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

"""