while (character:=input()):
    if len(character)==1:
        print(f'{((ord(character))):04X}')
    else:
        print(f'{((int(character,16) ^ 0x30)):01X}')