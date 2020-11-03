##### event_A_B 
#---#
from helpers import read, write
#&&&#
source_file_name = 'data/A/event.txt'
sink_file_name = 'data/B/event.txt'
#+++# src helpers read type_1
data = read.type_1(
    source_file_name = source_file_name)
#+++# end
#&&&#
print(data)
#+++# src helpers write type_1
write.type_1(
    data = data,
    sink_file_name = sink_file_name)
#+++# end
##### end 