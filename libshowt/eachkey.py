def eachkey(shower, parser, mf, fn):
    '''
    for each key in column keywords, break up the value list
    and display the values
    '''
    pr = shower.pr
    pr('%s ' % shower.filename_column(fn, parser.fname_cols()), 1)
    for key in parser.colkeywords():
        use_comma = False
        for column in mf.get(key, [f'']):
            if key in [f'tracknumber', f'discnumber', f'setnumber']:
                n = str(mf.get(key, [0])[0])
                column = n.rjust(3, f' ')
                pr(f'{column}', 1)
            elif key in [f'title', f'comment']:
                if column:
                    if use_comma:
                        nn = 16 - len(column[:15])
                        pr(f',{column[:14]}', abs(nn -  len(column[:14])))
                    else:
                        nn = 24 - len(column[:23])
                        pr(f'{column[:23]}', nn)
                        use_comma = True
            else:
                pr(f'{column}', 1)
    return
