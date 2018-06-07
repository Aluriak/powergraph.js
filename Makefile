INDIR=pgraph


all: copy open

copy:
	- rm -r site/graph/*
	mkdir -p site/graph/
	cd site/graph/ ; ln -s ../../examples/$(INDIR)/* .

open:
	xdg-open site/index.html


get-powergrasp-output:
	cp ~/packages/powergrasp/out/out.bbl data/test.bbl


make-bbl:
	python make_from_bubble.py data/test.bbl examples/automade/code.js


automade:
	make all INDIR=automade
basics:
	make all INDIR=basics
handmade:
	make all INDIR=handmade
p-graph:
	make all INDIR=p-graph
