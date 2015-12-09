from pygments import highlight
from pygments.lexers import get_lexer_for_filename,get_lexer_by_name
from pygments.formatters import TerminalFormatter
from sys import exit


class Formatter(object):
    """

    handles the formatting of the code displayed


    """
    def __init__(self,file,language=None,direct=False):
        self.language=language        
        if direct:
            self.content = file
        else:
            self.file = file
        # for the time being reading the whole file in buffer
            self.read(file)

    def read(self,file):
        try:
            with open(file,'r') as open_file:
                self.content = open_file.read()

        except FileNotFoundError as e:
            print(e)
            exit(0)
    
    def format(self):

        try:
            self.lexer = get_lexer_for_filename(self.file)
        except Exception as e:
            if self.language !=None:
                self.lexer = get_lexer_by_name(self.language)
            else:
                raise Exception("no suitable lexer found")
        
        formatter = TerminalFormatter()

        return highlight(self.content,self.lexer,formatter)

    
