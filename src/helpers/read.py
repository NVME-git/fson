from helpers import context

##### type_1
#---#
def type_1(source_file_name):
#&&&# 
    with open(source_file_name, "r") as source_file:
        data = source_file.read()
    key = 'b'
#+++# src helpers context type_b
    value = context.type_b(key) 
#+++# end
#&&&#
    print(value)
#---#
    return data
##### end
