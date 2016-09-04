#
# $Id: pause.awk 406 2006-03-18 16:37:18Z nicb $
#
BEGIN{
	r = 1.149;	
	p = 9.609;

	accu = 0;
	for (i = 0; i < 13; ++i)
	{
		print p - accu;
		accu += (r/((i+1)*2));
	}
}
