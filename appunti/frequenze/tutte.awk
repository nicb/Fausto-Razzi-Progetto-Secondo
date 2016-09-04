#
# $Id: tutte.awk 406 2006-03-18 16:37:18Z nicb $
#
BEGIN{
	octave_start = 60;
	octave_leap = 3.4;
	num_octaves = 4;
	intervals = 25;

	frq_base = octave_start;
	for (oindex = 1; oindex <= num_octaves; ++oindex)
	{
		for (intv = 1; intv <= intervals; ++intv)
		{
			step = 2**((intv-1)/(intervals-1));
			printf("%d|%02d|%08.3f\n", oindex, intv, frq_base*step);
		}
		frq_base *= octave_leap;
	}
}
