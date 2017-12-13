file_object = open('re.py')
try:
    file_context = file_object.read()
    print type(file_context)
    #  file_context = open(file).read().splitlines() 
finally:
    file_object.close()