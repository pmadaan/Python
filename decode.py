def decode(message_file):
    map = {}
    with open(message_file, "r") as f:
        line = f.readline()
        while line:
            parts = line.split()
            map[parts[0]] = parts[1]
            line = f.readline()
    
    res = []
    level = index = 1
    
    while index <= len(map):
        print(f"{level} {index}")
        res.append(map[str(index)])
        
        level += 1
        index = index + level
    
    return " ".join(res)
         
print(decode("/Users/priyankamadaan/Downloads/a.txt"))