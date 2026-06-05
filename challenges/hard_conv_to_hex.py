def convert_to_hex(txt):
    nString = ""
    for char in txt:
        nString += char.encode("utf-8").hex().lower()
        nString += " "
    return nString.rstrip()
