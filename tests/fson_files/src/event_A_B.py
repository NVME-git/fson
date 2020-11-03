#&&&#
source_file_name = 'data/A/event.txt'
sink_file_name = 'data/B/event.txt'
#
with open(source_file_name, "r") as source_file:
    data = source_file.read()
key = 'b'
#
context = {'b': 2}
value = context[key]
#
print(value)
#&&&#
print(data)
#
with open(sink_file_name, "w") as sink_file:
    sink_file.write(data)
