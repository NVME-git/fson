import os

def path_gen(folders):
    folder_path = ''
    for folder in folders:
        folder_path += f'/{folder}'
    return folder_path[1:]

def three_fs(prop):
    prop = prop.strip()
    items = prop.split(' ')
    # function is the last
    function = items[-1]
    # file is the second last
    file = items[-2]
    # folders are the items 
    # after the initial comment 
    # until and excluding the last 2
    folders = items[1:-2]
    # Join paths together with slash
    folder_path = path_gen(folders)
    # print(f"folder_path: {folder_path}")
    return folder_path, file, function


def fson(folder, file, function, fsrc='fson_files', ext='py', tab_length=4):
    if not os.path.exists(f"{fsrc}"):
        os.makedirs(f"{fsrc}")

    with open(f"{folder}/{file}.{ext}","r") as f:
        lines = f.readlines()
    funcode = []

    simple_states = ['#---#', '#&&&#'] 
    states = ['#####','#---#', '#&&&#','#+++#']

    state = states[0]
    in_function = False
    for i in range(len(lines)):

        line = lines[i].rstrip()
        line = line.replace('\t', tab_length*' ')

        if (len(line) >= 5) and (line[:5] in states):
            # Check if in the correct function
            # If given function 
            line_function = line.split(' ')[-1]
            line_state = line.split(' ')[0]
            if (line_state == states[0]) and (line_function == function):
                in_function = True
            if (line_state == states[0]) and (line_function != function):
                continue

            # Handle states with attributes here
            # eg. #+++# helpers read type_1
            state = line[:5]

            if (state == '#+++#') and (line[-3:] != 'end'):
                # Add expansion code here
                # print(i, line)
                funcfolder, funcfile, funcfunction = three_fs(line)
                funcpath = f"{fsrc}/{funcfolder}/{funcfile}_{funcfunction}.{ext}"
                # print(f"<--- {funcpath}")
                print(f"<--- {funcfile}_{funcfunction}.{ext}")
                with open(funcpath,"r") as f:
                    funclines = f.readlines()
                for funcline in funclines:
                    funcode.append(funcline)

        if (state == states[0]) and (line[-3:] == 'end'):
            break

        if in_function and (state == '#&&&#'):
            if file != function: line = line[tab_length:]
            funcode.append(line+'\n')

            # if state in simple_states:
            #     print(i, state)

    # Remove duplicate file name content for main function files.
    if file == function:
        func_file = f"{fsrc}/{folder}/{file}.{ext}"
    else:    
        func_file = f"{fsrc}/{folder}/{file}_{function}.{ext}"

    # Create folder if it does note exist.
    if not os.path.exists(f"{fsrc}/{folder}"):
        os.makedirs(f"{fsrc}/{folder}")
    with open(func_file, "w") as f:
            f.writelines(funcode)

def main():
    with open(f"fson.properties","r") as f:
        props_list = f.readlines()

    for prop in props_list:
        folder, file, function = three_fs(prop)

        print(f"\n{folder}/{file}.py ---> {function}")
        fson(folder, file, function)

if __name__ == '__main__':
    main()