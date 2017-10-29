CHAPTERS=$(wildcard chapitre-*/)
TARGETS=$(CHAPTERS:/=.tar.gz)

%.tar.gz: %
	tar cfz $@ $<

all: $(TARGETS)

clean:
	rm -f *.tar.gz
