class Printer:
    '''
    columnar printing with optional colors
    '''
    def __init__(self, use_color=False):
        self.current_intensity = 1
        self.current_color = 37
        self.alt_color = 33
        self.colorstr = self.format_color()
        self.pos = 0
        self.line = ''
        self.use_color = use_color

    def pr(self, data, numspaces=0):
        try:
            assert isinstance(numspaces, int), 'numspaces must be an integer'
            assert numspaces >= 0, 'numspaces must be positive'
        except AssertionError as error:
            print(f'error during virtual print, {error}')
            return
        if self.use_color:
            self.line += f"{self.colorstr}"
        self.line += f"{data}{' ' * numspaces}"
        self.clrswap()
        self.pos += len(data) + numspaces

    def set_pos(self, pos=0):
        self.pos = pos

    def set_line(self, line=''):
        self.line = line

    def get_pos(self):
        return self.pos

    def get_line(self):
        return self.line

    def prline(self, str=''):
        print(str or self.line, end='\n')
        self.line = ''
        self.pos = 0
        self.current_color = 37
        self.set_color(self.current_intensity, 37)

    def set_color(self, intensity, color):
        self.current_intensity = intensity
        self.current_color = color
        self.colorstr = self.format_color()

    def format_color(self):
        return (f'\033[{self.current_intensity};{self.current_color}m')

    def clrswap(self):
        if self.current_color == 37:
            self.current_color = 33
        else:
            self.current_color = 37
        self.colorstr = self.format_color()
