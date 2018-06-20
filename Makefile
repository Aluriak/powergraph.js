BBLFILE=test
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

# Specific examples
automade:
	make all INDIR=automade
basics:
	make all INDIR=basics
handmade:
	make all INDIR=handmade
p-graph:
	make all INDIR=p-graph


make-bbl:
	python make_from_bubble.py data/$(BBLFILE).bbl examples/automade/code.js
make-bbl-and-run: make-bbl automade

# Instances of previous recipe
yeast:
	$(MAKE) make-bbl-and-run BBLFILE=test-yeast
cliques:
	$(MAKE) make-bbl-and-run BBLFILE=test-cliques
falsedges:
	$(MAKE) make-bbl-and-run BBLFILE=test-falsedge


.PHONY: *
