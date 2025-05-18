def find_indexes(file_path, word):
    with open(file_path, 'r') as file:
        content = file.read()
    start = content.find(word)
    if start == -1:
        return None
    end = start + len(word)
    return start,end
file_path = 'annotate.txt.txt'
word = 'SQL'
indexes = find_indexes(file_path, word)
print(indexes[0],indexes[1])



