def prettyPrint(string: str, size: int = 72) -> str:
    dashcount = (size - len(string))//2
    print('-' * dashcount, '[', string, ']', '-' * dashcount)
