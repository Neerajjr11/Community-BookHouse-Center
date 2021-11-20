import re
given_input=input()
regular_expression=r'[a-zA-Z]+\[[a-aA-Z0-9-]+\]'
matches_found=re.findall(regular_expression,given_input)
if not matches_found:
    print(-1)
for word in matches_found:
    word=word.replace("["," ")
    word=word.replace("]","")
    print(word)