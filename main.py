#!/usr/bin/python3

import os, sys

pallet16 = [
    "000000","800000","008000","808000","000080","800080","008080","c0c0c0",
    "808080","ff0000","00ff00","ffff00","0000ff","ff00ff","00ffff","ffffff",
]
pallet8 = [
    "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",
    "magic",  # 8 enable 256 color
    "def",    # 9 default foreground color
]
xx = [ "00", "5f", "87", "af", "d7", "ff" ]

class vt100LaTeX():
    def __init__(self, string=None):
        self.count=0
        if string: self.parser(string)

    def de_code(self, fp):
        self.flag=0
        self.extend=0
        def tag_me(code):
            if code in [ "", "0" ]: print("}"*self.count, end=""); self.count=0; return  # no code condition ^[[m
            #elif self.flag==0: print("{", end=""); self.flag=1
            tag=int(code)
            if   self.extend==53: print("bg"+code, end=""); self.extend=0;
            elif self.extend==43: print("fg"+code, end=""); self.extend=0;
            elif self.extend: self.extend+=tag; return; #2nd skip
            elif tag in [ 38, 48 ]: self.extend=tag; return;
            elif tag > 39: print("\\colorbox{%s}{"%pallet8[tag-40], end=""); self.count+=1
            elif tag > 29: print("\\textcolor{%s}{"%pallet8[tag-30], end=""); self.count+=1
            elif tag == 1: print("\\textbf{", end=""); self.count+=1
            elif tag == 3: print("\\textit{", end=""); self.count+=1
            elif tag == 9: print("\\sout{", end=""); self.count+=1
            elif tag == 4: print("\\uline{", end=""); self.count+=1

        fbreak=fp

        while True:
            if self.string[fp]=="m": tag_me(self.string[fbreak:fp]); break;
            if self.string[fp]==";": tag_me(self.string[fbreak:fp]); fbreak=fp+1;
            fp+=1

        return fp+1

    def parser(self, string):
        cur=pre=pcode=code=""
        fp=cflag=0
        length=len(string)
        self.string=string
        while fp<length:
            if string[fp]=='\x1b':
                pcode=code;
                fp=self.de_code(fp+2); # +2 shift escape sequence
                continue
            elif string[fp]=='\n': print("\\\\", end="")
            elif string[fp] in '{}[]&': print("\\",end="")
            print(string[fp], end="")
            fp+=1

if __name__ == "__main__" :
    if len(sys.argv)<2:
        print("Argument(s) Missing", file=sys.stderr); exit(1);

    vtk=vt100LaTeX(open(sys.argv[1]).read())
