
def start():
    print()
    txt = input("Digite a chave: ")
    pointer = -1
    begin(txt, pointer)

def begin(txt, pointer):
    pointer += 1
    if (pointer < len(txt)):
        state00(txt, pointer)
    else:
        start()

def state00(txt, pointer):
    if (txt[pointer] == "<"):
        state01(txt, pointer)
    elif (txt[pointer] == "="):
        state05(txt, pointer)
    elif (txt[pointer] == ">"):
        state06(txt, pointer)
    else:
        print("Error key ... Try again ...")
        start()

def state01(txt, pointer):
    print(f"estado 01 {txt[pointer]}")
    pointer += 1
    if (pointer >= len(txt)):
        start()
    else:
        if (txt[pointer] == "="):
            state02(txt, pointer)
        elif (txt[pointer] == ">"):
            state03(txt, pointer)
        else:
            state04(txt, pointer)

def state06(txt, pointer):
    print(f"estado 06 {txt[pointer]}")
    pointer += 1
    if (pointer >= len(txt)):
        start()
    else:
        if(txt[pointer] == "="):
            state07(txt, pointer)
        else:
            state08(txt, pointer)

def state02(txt, pointer):
    print(f"estado 02 {txt[pointer]}    LE")
    # print("estado 02: os simbolos '<=' -> LE")
    begin(txt, pointer)

def state03(txt, pointer):
    print(f"estado 03 {txt[pointer]}    NE")
    # print("estado 3: os simbolos '<>' -> NE")
    begin(txt, pointer)

def state04(txt, pointer):
    # print("estado 04: os simbolos '<' -> EQ")
    print(f"estado 04 {txt[pointer]}    LT")
    begin(txt, pointer)

def state05(txt, pointer):
    # print("estado 05: os simbolos '=' -> EQ")
    print(f"estado 05 {txt[pointer]}    EQ")
    begin(txt, pointer)

def state07(txt, pointer):
    # print("estado 07: os simbolos '<=' -> GE")
    print(f"estado 07 {txt[pointer]}    GE")
    begin(txt, pointer)

def state08(txt, pointer):
    # print("estado 08: os simbolos '>' -> GT")
    #print(f"estado 08 >{txt[pointer]}    GT")
    print(f"estado 08 {txt[pointer]}    GT")
    begin(txt, pointer)

start()