from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        output = []
        for word in strs:
            sort_word = tuple(sorted(word))
            # group.key = sort_word
            group[sort_word].append(word)
        for val in group.values():
            output.append(val)
        return output

        