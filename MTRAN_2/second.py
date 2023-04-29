from data import data as data2
import re


def second():
    i = 0
    j = 1

    n = len(data2.split("\n"))
    for token in data2.split("\n"):
        i+=1
        for el in token.split():

            if (len(el) >= 2 and el[0] == "i" and el[1] == "f") or (len(el) >= 3 and "if" in el):
                if len(el) != 2:
                    print(f"\n\n---------ERROR:UNEXPECTED TOKEN invalid lexic if-statement {el} on line {i} of {n}  pos {1}")
                    print(token)
                    el = "if"
                    j += 1
                    break

            elif el[0] == "v" and el[1] == "o":
                if len(el) != 4 or el[2] != "i" or el[3] != "d":
                    print(f"\n\n---------ERROR:UNEXPECTED TOKEN invalid lexic void-statement: {el} on line {i} of {n}  pos {1}")
                    print(token)
                    el = "void"
                    j += 1
                    break
            elif el[0] == "=":
                if len(el) > 2 or el[-1] != "=":
                    print(f"\n\n---------ERROR:UNEXPECTED TOKEN invalid lexic ===-statement: {el} on line {i} of {n}  pos {13}")
                    print("merged[i+j] === L[i];")
                    el = "=="
                    j += 1
            elif len(el)> 10 and el[9] == "@":
                if len(el) > 2 or el[-1] != "=":
                    print(
                        f"\n\n---------ERROR:UNEXPECTED TOKEN invalid lexic non-existing statement: {el} on line {i} of {n}  pos {10}")
                    print(el)
                    el = el.strip("@")
                    j += 1

            elif len(el) > 2 and el[0] == "i" and el[1] == "n":
                if len(el) != 3 or el[-1] != "t":
                    print(f"\n\n---------ERROR:UNEXPECTED TOKEN invalid lexic int-statement :{el} on line {i} of {n}  pos {0}")
                    j += 1
                    print(el)
                    print(token)
                    el = "int"
            elif el == '=!=':
                print(f"\n\n---------ERROR:UNEXPECTED TOKEN invalid lexic non-existing statement :{el} on line {i} of {n}  pos {13}")
                j += 1
                print(token)
                el = "!="


second()

pre_tokens=[
"return",
"new",
"endl",
"cout",
"cin",
"int",
"float",
"double",
"char",
"long",
"str",
"const",
"void",
"if",
"switch",
"for",
"case",
"else",
"while",
"do",
"break",
"continue",
]
sign_tokens = [
    "+",
    "-",
    "*",
    "/",
    "<",
    ">",
    "=",
    "<=",
    ">=",
    "=<",
    "=>",
    "==",
    "!=",
    "||",
    "<<",
    ">>",
    '""',
    '"',
    "'",
    "++",
    "{",
    "}"
]
system_tokens = [
    "main",
    "#include",
    "<iostream>",
    "namespace",
    "using",
    "std",
    "SortAlgo::mergeSort",
    "SortAlgo::merge",
    "strcat",
    "fact",
    "setlocale"
]

new_tokens = []
    
def nametable_create():
    i=0
    for token in data2.split("\n"):
        i+=1
        elements = token.split()
        for index, el in enumerate(elements) :
            el = el.strip("){").strip(")").strip("(").strip(";").strip("]\n").strip(',')
            if (el not in pre_tokens and el not in sign_tokens 
                and el not in system_tokens and [el,"arr"] not in new_tokens and 
                [el,"int"] not in new_tokens and [el,"float"] not in new_tokens and
                [el,"str"] not in new_tokens and [el,"const int"] not in new_tokens) :
                    if ('[' in el and ']' in el) : new_tokens.append([el.strip(","),"arr"])
                    elif ('[' in el) : continue 
                    elif ('*' not in el and elements[index-1] == "int") :  new_tokens.append([el,"int"])
                    elif ('*' not in el and elements[index-1] == "float") :  new_tokens.append([el,"float"])
                    elif (el.isdigit() and int(el) not in new_tokens) : new_tokens.append([(el), "const int"])

    print()

nametable_create()

new_tokens = sorted(new_tokens, key=lambda x:x[1])

    
