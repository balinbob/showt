import os
import sys
# import subprocess


class Eachkey():
    def __init__(self):
        self.cursor_line = 0    # top of display
        # self.last_line = int(subprocess.check_output(['tput', 'lines']))
        self.last_line = os.get_terminal_size()[1]

    def linesdown(self, y):
        return (f'\033[{y}B')

    def linesup(self, y):
        return (f'\033[{y}A')

    def back(self, x):
        return (f'\033[{x}D')

    def forward(self, x):
        return (f'\033[{x}C')

    def eachkey(self, shower, parser, mf, fn):
        '''
        for each key in column keywords, break up the value list
        and display the values
        '''
        pr = shower.pr
        pr('%s ' % shower.filename_column(fn, parser.fname_cols()), 1)
        keywords = parser.colkeywords()
        bottom_line = 0
        for keynum, key in enumerate(keywords):
            y_offset = 0
            for lineno, column in enumerate(mf.get(key, [''])):
                column = column[:23]
                if lineno == 0:
                    self.first_value(key, column, pr)
                else:
                    pr(f'{self.linesdown(1)}')
                    self.cursor_line += 1
                    sys.stdout.flush()
                    y_offset += 1
                    self.more_values(key, column, pr)
                    if lineno + 1 == len(mf.get(key, [])):  # last value?
                        pr(f'{self.linesup(y_offset)}')
                        sys.stdout.flush()
                        if y_offset > bottom_line:
                            bottom_line = y_offset
        if bottom_line:
            pr(f'{self.linesdown(bottom_line)}')
        sys.stdout.flush()
        self.cursor_line += 1

    def first_value(self, key, column, pr):
        if key in ('tracknumber', 'discnumber', 'setnumber'):
            rpadding = 1
            column = str(column).rjust(3, ' ')
        elif key in ('date', 'genre'):
            rpadding = 12 - len(column)
        else:
            rpadding = 24 - len(column)
        pr(f'{column}', rpadding)
        sys.stdout.flush()

    def more_values(self, key, column, pr):
        if key in ('tracknumber', 'discnumber', 'setnumber'):
            pr(f'{self.back(4)}')
            rpadding = 1
        elif key in ('date', 'genre'):
            pr(f'{self.back(12)}')
            rpadding = 12 - len(column)
        else:
            pr(f'{self.back(24)}')
            rpadding = 24 - len(column)
        sys.stdout.flush()
        pr(f'{column}', rpadding)
        sys.stdout.flush()
