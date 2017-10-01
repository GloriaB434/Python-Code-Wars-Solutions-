def camel_case(string):
    new_string = ''.join(s[0].upper() + s[1:] for s in string.split())
    return new_string
