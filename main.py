file_path = r"C:\Users\heet5\Downloads\THE VERDICT.txt"
with open(file_path,'r',encoding="utf-8") as r:
    text = r.read()

# use regular expression for tokenize
import re
# re.split(pattern , text)
split_text = re.split(r'(\s)',text)  # just split on whitespace 

split_text = re.split(r'([,.:;?_!"()\']|--|\s)',text) # remove [,.:;?_!"()\'] and split at -- and at space do not remove -- and spce
split_text[20:40]

final_text = [text for text in split_text if text.strip() ] # .strip() remove space,new line charecter etc...

sorted_text_set= sorted(set(final_text))
len(sorted_text_set),sorted_text_set[:20]