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
        self.status=[0,0,0,0,0,0] #1,3,4,9,fg,bg
        if string: self.parser(string)

    def bgpaint(self, tag):
        if self.status[4]==1:
            print("}", end="")
        print("\\colorbox{%s}{"%pallet8[tag-40], end="");
        self.box=True

    def tag_me(self, code):
        tag=int(code)
        if code in [ "", "0" ]:   # no code condition ^[[m
            count=0
            for i in self.status: count+=i;
            self.status=[0,0,0,0,0,0]
            print("}"*count, end="");
            self.count=0;
            self.box=False
            return
        #if   self.extend==53: print("\\textcolor[rgb]{1,0,1]{", end=""); self.extend=0;
        #elif self.extend==43: print("\\textcolor[rgb]{1,1,0}{", end=""); self.extend=0;
        elif self.extend: self.extend+=tag; return; #2nd skip
        elif tag in [ 38, 48 ]: self.extend=tag; return;
        elif tag > 39: return; self.bgpaint(tag); self.status[4]+=1
        elif tag > 29: print("\\textcolor{%s}{"%pallet8[tag-30], end=""); self.status[5]+=1
        elif tag == 1: print("\\textbf{", end=""); self.status[0]+=1
        elif tag == 3: print("\\textit{", end=""); self.status[1]+=1
        elif tag == 4: print("\\uline{", end=""); self.status[2]+=1
        elif tag == 9: print("\\sout{", end=""); self.status[3]+=1

        else: return;

    def de_code(self, fp):
        self.flag=self.extend=0
        self.box=False
        fbreak=fp
        while True:
            if self.string[fp]=="m": self.tag_me(self.string[fbreak:fp]); break;
            if self.string[fp]==";": self.tag_me(self.string[fbreak:fp]); fbreak=fp+1;
            fp+=1

        return fp+1

    def parser(self, string):
        cur=pre=pcode=code=""
        spaceflag=None
        fp=cflag=0
        length=len(string)
        self.string=string
        while fp<length:

            if string[fp]=='\x1b':
                pcode=code;
                fp=self.de_code(fp+2); # +2 shift escape sequence
                continue
            elif string[fp] == '\n': print("\\\\", end="")
            #elif string[fp] == ' ': print("\\space ", end="")
            # elif string[fp] == ' ':
            #     if spaceflag == fp-1:
            #         print("\\space", end="")
            #         fp+=1; continue
            #     spaceflag=fp
            elif string[fp] == '[': print("\\lbrack ",end=""); fp+=1; continue
            elif string[fp] == ']': print("\\rbrack ",end=""); fp+=1; continue
            elif string[fp] in '$\{#_^}%&': print("\\",end="")
            print(string[fp], end="")
            fp+=1

if __name__ == "__main__" :
    if len(sys.argv)<2:
        print("Argument(s) Missing", file=sys.stderr); exit(1);

    vtk=vt100LaTeX(open(sys.argv[1]).read())
