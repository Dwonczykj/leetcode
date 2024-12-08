from typing import List
from collections import deque


class Solution:
    def fullJustifyAllLines(self, words: List[str], maxWidth: int) -> List[str]:
        cur_line_length = 0
        start_word_ind = 0
        n = len(words)
        page = []
        for i, w in enumerate(words):
            if cur_line_length > 0:
                cur_line_length += 1
            cur_line_length += len(w)
            if cur_line_length > maxWidth:
                # end the line to [i-1]th
                cur_line_length -= (len(w) + 1)
                num_words_in_line = i - start_word_ind
                if num_words_in_line == 1:
                    line = words[start_word_ind] + \
                        (" "*(maxWidth - len(words[start_word_ind])))
                else:
                    num_spaces_in_line = i - 1 - start_word_ind
                    num_spaces_per_space = ((
                        maxWidth - cur_line_length) // num_spaces_in_line) + 1
                    single_extra_space_for_first_n = (
                        maxWidth - cur_line_length) % num_spaces_in_line
                    line = (" "*num_spaces_per_space+" ").join(words[start_word_ind:start_word_ind+single_extra_space_for_first_n]) + (" "*num_spaces_per_space+" " if single_extra_space_for_first_n > 0 else "") + (
                        " "*num_spaces_per_space).join(words[start_word_ind+single_extra_space_for_first_n:i])
                if len(line) != maxWidth:
                    raise Exception("BUG")
                page.append(line)
                cur_line_length = len(w)
                start_word_ind = i
            elif cur_line_length == maxWidth:
                # end the line to [i]th
                line = " ".join(words[start_word_ind:i+1])
                if len(line) != maxWidth:
                    raise Exception("BUG")
                page.append(line)
                cur_line_length = 0
                start_word_ind = i + 1

        num_words_in_line = n - start_word_ind
        if num_words_in_line == 1:
            line = words[start_word_ind] + \
                (" "*(maxWidth - len(words[start_word_ind])))
        else:
            num_spaces_in_line = n - 1 - start_word_ind
            num_spaces_per_space = ((
                maxWidth - cur_line_length) // num_spaces_in_line) + 1 if num_spaces_in_line > 0 else 1
            single_extra_space_for_first_n = (
                maxWidth - cur_line_length) % num_spaces_in_line if num_spaces_in_line > 0 else 1
            line = (" "*num_spaces_per_space+" ").join(words[start_word_ind:start_word_ind+single_extra_space_for_first_n]) + (
                " "*num_spaces_per_space).join(words[start_word_ind+single_extra_space_for_first_n:n])
        if len(line) != maxWidth:
            raise Exception("BUG")
        page.append(line)
        cur_line_length = 0
        return page

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        cur_line_length = 0
        start_word_ind = 0
        n = len(words)
        page = []
        for i, w in enumerate(words):
            if cur_line_length > 0:
                cur_line_length += 1
            cur_line_length += len(w)
            if cur_line_length > maxWidth:
                # end the line to [i-1]th
                cur_line_length -= (len(w) + 1)
                num_words_in_line = i - start_word_ind
                if num_words_in_line == 1:
                    line = words[start_word_ind] + \
                        (" "*(maxWidth - len(words[start_word_ind])))
                else:
                    num_spaces_in_line = i - 1 - start_word_ind
                    num_spaces_per_space = ((
                        maxWidth - cur_line_length) // num_spaces_in_line) + 1
                    single_extra_space_for_first_n = (
                        maxWidth - cur_line_length) % num_spaces_in_line
                    line = (" "*num_spaces_per_space+" ").join(words[start_word_ind:start_word_ind+single_extra_space_for_first_n]) + (" "*num_spaces_per_space+" " if single_extra_space_for_first_n > 0 else "") + (
                        " "*num_spaces_per_space).join(words[start_word_ind+single_extra_space_for_first_n:i])
                if len(line) != maxWidth:
                    raise Exception("BUG")
                page.append(line)
                cur_line_length = len(w)
                start_word_ind = i
            elif cur_line_length == maxWidth:
                # end the line to [i]th
                line = " ".join(words[start_word_ind:i+1])
                if len(line) != maxWidth:
                    raise Exception("BUG")
                page.append(line)
                cur_line_length = 0
                start_word_ind = i + 1
        if start_word_ind < n:
            line = " ".join(words[start_word_ind:n])
            line += " " * (maxWidth - len(line))

            if len(line) != maxWidth:
                raise Exception("BUG")
            page.append(line)
            cur_line_length = 0
        return page


runner = Solution()

words = ["ask", "not", "what", "your", "country", "can", "do", "for",
         "you", "ask", "what", "you", "can", "do", "for", "your", "country"]
maxWidth = 16
output = runner.fullJustify(words, maxWidth)
assert output == ["ask   not   what", "your country can",
                  "do  for  you ask", "what  you can do", "for your country"]

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
output = runner.fullJustify(words, maxWidth)
assert output == [
    "This    is    an",
    "example  of text",
    "justification.  "
]

words = ["What", "must", "be", "acknowledgment", "shall", "be"]
maxWidth = 16
output = runner.fullJustify(words, maxWidth)
assert output == [
    "What   must   be",
    "acknowledgment  ",
    "shall be        "
]

words = ["Science", "is", "what", "we", "understand", "well", "enough", "to",
         "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
maxWidth = 20
output = runner.fullJustify(words, maxWidth)
assert output == [
    "Science  is  what we",
    "understand      well",
    "enough to explain to",
    "a  computer.  Art is",
    "everything  else  we",
    "do                  "
]


print('Done')
