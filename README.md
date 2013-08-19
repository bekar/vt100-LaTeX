# vt100-LaTeX

`vt100 colors` is no good when you wan't to show it to someone who doesn't use or  have terminal! here comes `vt100-LateX` convert your colorful terminal output to LaTeX, which can be converted to `pdf`, `dvi`, `html` .. etc

![screenshot][screenshot]

#### HOW-TO-RUN

```bash
$ ./vtk100.py <color terminal dump> # which will give you template.tex
```
include you template.tex into `*.tex` file and compile

If you have no idea what's suppose to be done run `make`:
##### * Note: make sure you have texlive installed

```bash
$ make
make [hello|ls]
```

to parse other files you can set env variable `FILE`

```bash
$ FILE=<file> make compile
```


#### Read more

 - [ANSI color][ansi]
 - [256 color chart][chart]
 - [Ecma-048][ecma]
 - [VT100][vt100]

[vt100]: http://en.wikipedia.org/wiki/VT100
[ecma]: http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-048.pdf
[screenshot]: https://raw.github.com/bekar/vt100-LaTeX/dump/images/screenshot.png
[extreme]: https://raw.github.com/bekar/vtk100-colors/dump/samples/colorextreme
[chart]: http://www.calmar.ws/vim/256-xterm-24bit-rgb-color-chart.html
[ansi]: https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
