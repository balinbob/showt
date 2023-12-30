#! /usr/bin/env python3
# vim: set ft=python ts=4 sw=4 et ai:

import sys
import mutagen


def print_extra_items(fname, ext):

    mf = mutagen.File(fname)
    if ext.lower() == '.mp3':
        my_keys = ['TALB', 'TIT2', 'TRCK', 'TPE1',
                   'TPE2', 'TPOS', 'TDRC', 'TCON']
        for key in mf:
            if key in my_keys:
                continue
            elif key.startswith('APIC'):
                print('APIC')
                continue
            elif not mf[key][0]:
                continue
            frame_desc = mf[key].__class__.__doc__.partition('\n')[0]
            tab = (16 - len(frame_desc)) * ' '
            print(frame_desc, tab, mf[key][0])
        print
    else:
        my_keys = ['album',
                   'artist',
                   'date',
                   'venue',
                   'genre',
                   'title',
                   'discnumber',
                   'tracknumber',
                   'length']
        for key in mf:
            if key in my_keys:
                continue
            tab = (16 - len(key)) * ' '
            if len(mf[key]) > 1:
                print(key, tab, mf[key])
            elif len(mf[key]) == 1:
                print(key, tab, mf[key][0])


def eachkey(shower, parser, fn, mf, color, opts, files):
    s = '%s  ' % shower.filename_column(fn, parser.fname_cols())
    for key in parser.colkeywords():
        multival = ''
        if key in mf:
            if color:
                s += shower.insert_colors(opts)
            if key == 'tracknumber':
                tn = str(mf.get(key, [0])[0])
                col = tn.rjust(3, ' ')
                s += col
            elif key == 'discnumber':
                dn = str(mf[key][0])
                col = dn.rjust(2, ' ')
                s += col
            else:
                n = 0
                while True:
                    try:
                        val = '%s' % mf[key][n]
                    except IndexError:
                        break
                    if n > 0:
                        multival += '\n' + val
                    else:
                        multival = val
                    n += 1
                    if 'm' not in opts:
                        break
            s += '%s ' % multival
    return s


if __name__ == '__main__':
    print_extra_items(sys.argv[1], sys.argv[2])
