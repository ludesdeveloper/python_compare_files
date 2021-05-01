import os
#getting path
current_path = os.getcwd()
before_path = os.path.join(current_path,"before")
after_path = os.path.join(current_path,"after")
#list for append file
before_files = []
after_files = []
#getting files inside before directory
os.chdir(before_path)
files = os.listdir()

for file in files:
    before_files.append(file)
#getting files inside after directory
os.chdir(after_path)
files = os.listdir()

for file in files:
    after_files.append(file)
#change root directory
os.chdir(current_path)
#sorting list
before_files.sort(reverse=False)
after_files.sort(reverse=False)
#checking files
if len(before_files) == len(after_files):
    pass
else:
    raise Exception("File Length is Not The Same!!!")
#comparing files
results = []
for index, before_file in enumerate(before_files):
    #escape init file
    if "__init__" in before_file:
        continue 
    #before file read
    os.chdir(before_path)
    file1 = open(before_file, 'r')
    #after file read
    os.chdir(after_path)
    file2 = open(after_files[index], 'r')
    #checking difference
    my_diff = set(file2).difference(file1)
    my_diff.discard('\n')
    if len(my_diff) == 0:
        results.append(f'\n\n{before_file} compare result is the same\n\n')
    else:
        results.append(f'\n\n{before_file} compare result is not the same\n\n')
    for line in my_diff:
        results.append(line)
#writing results
os.chdir(current_path)
write_result = open("result.txt","w")
for result in results:
    write_result.write(result)