import re
def range_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$",name)
    # perbaikan pertama
    # if result is None:
    #     return ""
    
    #perbaikan kedua
    if result is None:
        return name
    
    return "{} {}".format(result[2], result[1])



my_txt = ""

def LetterCompiler(txt):
    result = re.findall(r'([a-c]).', txt)
    return result

print(LetterCompiler(my_txt))

