file = open("py_scripts\store_data.txt")

loc_data = []
new_data = {}
for char in file:
    sub = char.split('|')
    for s in sub:
        if s !=  "" and s != "\n":
            s = s.strip()
            loc_data.append(s)

start = 0
end = 4
for i in range(len(loc_data)):
    new_data[loc_data[start]] = loc_data[start+1:end+1]
    start += 5
    end += 5
    if start > len(loc_data) - 1:
        break
    #print(loc_data[i])





