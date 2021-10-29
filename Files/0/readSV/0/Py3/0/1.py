def readSV ( filepath , sep = ( ',' , '\n' ) ) :
    with open ( filepath ) as f:
        TEXT = f.read()
    if not TEXT:
        return ()
    LINES = TEXT.split ( sep [ 1 ] )
    LINES = LINES if LINES[-1] != '' else LINES[:-1]
    record = lambda string: tuple ( string.split ( sep [ 0 ] ) )
    return tuple ( map ( record , LINES ) )
