import re

def sumnums(sentence):
    regexp = r"[0-9]+"
    sum = 0
    for n in re.findall(regexp, sentence):
        sum += int(n)
    return sum
