#  49. Group Anagrams

from collections import defaultdict
from typing import Dict, List, Set


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for i in range(len(strs)):
            std_word = ''.join(sorted(strs[i]))
            mp[std_word].append(strs[i])  # either way as default dict
        return list(mp.values())

        def sa(s: str):
            x = [c for c in s]
            x.sort()
            return x
        lu: List[list[str]] = []
        anagrams: List[List[str]] = []
        for i in range(len(strs)):
            if sa(strs[i]) not in lu:
                lu.append(sa(strs[i]))
                anagrams.append([strs[i]])
            else:
                ind = lu.index(sa(strs[i]))
                anagrams[ind] = [strs[i]] + anagrams[ind]
        return anagrams
