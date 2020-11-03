#
with open(source_file_name, "r") as source_file:
    data = source_file.read()
key = 'b'
#
context = {'b': 2}
value = context[key]
#
print(value)
