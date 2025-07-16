#=====INTEGER======
print("=====INTEGER=====")

data_int = 9;
print("data = ", data_int, "type = ", type(data_int))

data_float = float(data_int)
data_str =str(data_int)
data_bool = bool(data_int)

print("=====HASIL CASTING=====")
print("data = ", data_float, "type = ", type(data_float))
print("data = ", data_str, "type = ", type(data_str))
print("data = ", data_bool, "type = ", type(data_bool))

#=====FLOAT======                                                
print("=====FLOAT=====")

data_float = 9.6;
print("data = ", data_float, "type = ", type(data_float))

data_int = int(data_float)
data_str =str(data_float)
data_bool = bool(data_float)

print("=====HASIL CASTING=====")
print("data = ", data_int, "type = ", type(data_int))
print("data = ", data_str, "type = ", type(data_str))
print("data = ", data_bool, "type = ", type(data_bool))


#=====BOLEAN(BOOL)======
print("=====BOLEAN(BOOL)=====")

data_bool = True; #jika false akan menjadi nol (0)
print("data = ", data_bool, "type = ", type(data_bool))

data_int = int(data_bool)
data_str =str(data_bool)
data_float =float(data_bool)

print("=====HASIL CASTING=====")
print("data = ", data_int, "type = ", type(data_int))
print("data = ", data_float, "type = ", type(data_float))
print("data = ", data_bool, "type = ", type(data_bool))

#=====STRING======
print("=====STRING=====")

data_string = ""; #jika kosong "bool" akan menjadi false
print("data = ", data_string, "type = ", type(data_string))

data_int = int(data_string)
data_float =float(data_string)
data_bool = bool(data_string)

print("=====HASIL CASTING=====")
print("data = ", data_int, "type = ", type(data_int)) #akan error
print("data = ", data_float, "type = ", type(data_float)) #akan error
print("data = ", data_bool, "type = ", type(data_bool))















