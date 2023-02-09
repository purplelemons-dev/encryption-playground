
def main(text:str, key:str):
    byte_text, byte_key = text.encode(), key.encode()
    output:list[int] = []
    for idx, byte in enumerate(byte_text):
        output += [byte ^ byte_key[idx % len(byte_key)]]
    return "".join(chr(i) for i in output)

if __name__ == "__main__":
    key = input("Enter key: ")
    if not key:
        key = "reread"
    while 1:
        text = input("Enter text: ")
        if text in ("\n", "exit"):
            break
        print(main(text, key))

