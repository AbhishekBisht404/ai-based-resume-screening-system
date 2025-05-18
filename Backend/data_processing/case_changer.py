file_path = 'train_data.txt'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

lowercased_content = content.lower()

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(lowercased_content)

print("File content converted to lowercase.")
