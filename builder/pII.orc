;
; $Id: pII.orc 68 2014-02-18 23:49:56Z nicb $
;
sr = 44100
kr = 4410
ksmps = 10
nchnls = 1

giamp	init	8	; moltiplicatore globale d'ampiezza
zakinit 16,1

	instr 1
	iamp = ampdb(p4)
	if0 = p5
	if1 = p6
	if2 = p7
	idur = p3
	iidx = p8
	irise = p9
	ilev1 = p10
	irel = p11
	isust = idur-irise-irel

kenv linseg	0,irise,ilev1,isust,1,irel,0
a0	oscil	iamp,if0,1
a1	oscil	iamp,if1,1
a2	oscil	iamp,if2,1
as  =       (a0+a1+a2)/3

	zawm	as*kenv,iidx

	endin

	instr 2
	iamp = ampdb(p4)
	if0 = p5
	if1 = p6
	if2 = p7
	idur = p3
	iidx = p8
	irise = p9
	ilev1 = p10
	idec  = p11
	ilev2 = p12
	irel  = p13
	isust = idur-irise-idec-irel

kenv linseg	0,irise,ilev1,idec,ilev2,isust,1,irel,0
a0	oscil	iamp,if0,1
a1	oscil	iamp,if1,1
a2	oscil	iamp,if2,1
as  =       (a0+a1+a2)/3

	zawm	as*kenv,iidx

	endin

	instr 10
	idur = p3
	itab = p4
	iidx = p5 

asig zar	iidx
kenv oscil1i 0,1,idur,itab

aout =		asig*kenv*giamp	

ktim timek	
krms rms	aout			; this is just for plotting
	 printks "modulo %02d: %f %f\\n",0.125,iidx,ktim/kr,krms

	out		aout
	zacl	iidx,iidx
	endin
