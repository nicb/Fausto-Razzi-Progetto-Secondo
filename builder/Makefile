#
# $Id: Makefile 68 2014-02-18 23:49:56Z nicb $
#
DRAFT=pII-DRAFT.wav
DRAFTORC=$(DRAFT:.wav=.orc)
DRAFTSCO=$(DRAFT:.wav=.sco)
DRAFTLOG=$(DRAFT:.wav=.log)
DRAFTHEADER=header-draft.orc
FINAL=pII-FINAL.wav
FINALORC=$(FINAL:.wav=.orc)
FINALSCO=$(FINAL:.wav=.sco)
FINALLOG=$(FINAL:.wav=.log)
FINALHEADER=header-final.orc
DRIVER=pII.orc.in
MODULES=1 2 3 4 5 6 7 8 9 10 11 12 13 14a 14b
MODULESSCO= modulo-1.sco modulo-2.sco modulo-3.sco modulo-4.sco\
		modulo-5.sco modulo-6.sco modulo-7.sco modulo-8.sco \
		modulo-9.sco modulo-10.sco modulo-11.sco modulo-12.sco \
		modulo-13.sco modulo-14a.sco modulo-14b.sco
MODULESWAV=$(MODULESSCO:.sco=.wav)
RENDERER=./pIICsound
CSOUND=csound
LN=ln -sf
HDRFILE=header.orc
SPATFILE=posizioni.sco
NORMALIZE=normalize-audio --peak
SED=sed


all:
	@echo "make draft to compile the draft version of piece"
	@echo "make singlesco to produce the sco's for single modules"
	@echo "make singles to produce the single modules"
	@echo "make final to create the production version of the piece"

draft:	$(DRAFT)

$(DRAFT):	$(DRAFTORC) $(DRAFTSCO) $(SPATFILE) 
	$(CSOUND) -dWo ./$@ $(DRAFTORC) $(DRAFTSCO) > $(DRAFTLOG) 2>&1

$(DRAFTSCO) $(FINALSCO):
	$(RENDERER) > $@

$(DRAFTORC):	$(DRIVER)
	$(SED) -e 's/@@HEADER@@/#include "$(DRAFTHEADER)"/' $(DRIVER) > $@

final:	$(FINAL)

$(FINAL):	$(FINALORC) $(FINALSCO) $(SPATFILE)
	$(CSOUND) -dWo ./$@ \
		$(FINALORC) $(FINALSCO) > $(FINALLOG) 2>&1
	$(NORMALIZE) $@

$(FINALORC):	$(DRIVER)
	$(SED) -e 's/@@HEADER@@/#include "$(FINALHEADER)"/' $(DRIVER) > $@

singles:	$(MODULESWAV)

singlesco:	$(MODULESSCO)

$(MODULESSCO):
	for i in $(MODULES);\
	do\
		$(RENDERER) $$i > modulo-$$i.sco;\
	done

clean:
	$(RM) $(DRAFTSCO) $(FINALSCO) $(DRAFTORC) $(FINALORC) \
	      $(MODULESSCO) $(DRAFT) $(MODULESWAV) $(FINAL) *.log

.SUFFIXES:	.wav .sco

%.wav:	%.sco
	$(CSOUND) -dWo ./$@ $(DRIVER) $< > $*.log 2>&1 
