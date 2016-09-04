#
# $Id: flatex.awk 406 2006-03-18 16:37:18Z nicb $
#
BEGIN{
	FS="|";

	print "\\documentclass{scrartcl}\n\\usepackage{longtable}\n\\begin{document}";
	print "\\begin{longtable}{|c|r|}";

}
END{
	print "\\hline\n\\end{longtable}\n\\end{document}";
}
{
	oct  = $1;
	note = $2;
	frq  = $3;

	printf("\\hline\n$F_{%d,%d}$ & %08.3f\\\\\n", oct, note, frq);
}
