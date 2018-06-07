INDIR=pgraph


all: copy open

copy:
	- rm -r site/graph/*
	mkdir -p site/graph/
	cd site/graph/ ; ln -s ../../examples/$(INDIR)/* .

open:
	xdg-open site/index.html


basics:
	make all INDIR=basics
handmade:
	make all INDIR=handmade
p-graph:
	make all INDIR=p-graph
