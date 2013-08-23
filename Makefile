current: default

default:
	@echo "make [hello|ls]"

convert:
	cat ${FILE} > /tmp/dump.in
	./main.py /tmp/dump.in > template.tex

compile: clean convert
	pdflatex main.tex

hello:
	echo -e "\x1b[31;1;4mHello \LaTeX\x1b[0m\nThis is the output of \"\x1b[34;3mecho -e\x1b[0m\"" > /tmp/dump.in
	./main.py /tmp/dump.in > template.tex
	pdflatex main.tex

ls:
	ls --color=always > /tmp/dump.in
	./main.py /tmp/dump.in > template.tex
	pdflatex main.tex

clean:
	rm -f *aux *idx *log *out *pdf *toc *.nav *.snm *.bbl *.blg *.lof *.lot *.bcf
