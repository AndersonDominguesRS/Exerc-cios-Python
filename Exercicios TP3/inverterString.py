def inverter(string):
    print(string)
    if len( string ) == 0:
        return ""
    else:
        return string[-1] + inverter( string[:-1] )