with open("C:\\Users\\yuliy\\Documents\\HTML\\hiking_website\\index_copy.html") as f:
    read_data = f.read()
read_data_upper = read_data.upper()

with open("C:\\Users\\yuliy\\Documents\\HTML\\hiking_website\\index_copy_upper.html", "w") as f_new:
    f_new.write(read_data_upper)

