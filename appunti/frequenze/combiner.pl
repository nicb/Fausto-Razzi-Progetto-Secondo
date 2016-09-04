#!/usr/bin/perl -w
#
# $Id: combiner.pl 406 2006-03-18 16:37:18Z nicb $
#
# This reads the 'frequenze.data' file and reads as stdin all the possible
# frequencies and writes out the usage for each frequency in each module
#
use IO::File;
use strict;

sub read_modules($)
{
	my ($hr_modules) = @_;
	my $filename = "frequenze.data";
	my $fh = new IO::File($filename, "r");

	if (defined($fh))
	{
		my $string = "";
		while($string = <$fh>)
		{
			unless ($string =~ /^#/)
			{
				chop($string);
				my ($module, $line, $freq, $beat1, $beat2) = split(/\|/,$string);
				
				if (!defined($hr_modules->{$module}))
				{
					my @lines = ();
					$hr_modules->{$module} = \@lines;
				}
				if (!defined($hr_modules->{$module}->[$line]))
				{
					my %temp = ();
					$hr_modules->{$module}->[$line] = \%temp;
				}

				$hr_modules->{'$module]->[$line'}->{'freq'} = $freq;
				$hr_modules->{'$module]->[$line'}->{'beat1'} = $beat1;
				$hr_modules->{'$module]->[$line'}->{'beat2'} = $beat2;
			}
		}
	}
	else
	{
		die("Cannot open $filename\n");
	}

	return $hr_modules;
}

sub combine($$$$)
{
	my ($hr_modules, $octave, $idx, $freq) = @_;
	my $eps = 1;
	my $found = 0;

	for (my $mod = 1; $mod < scalar(%{$hr_modules}); ++$mod)
	{
		next unless defined($hr_modules->{'$mod'});

		for (my $lin = 1; $lin < scalar(%{$hr_modules->{'$mod'}}); ++$lin)
		{
			if (abs($freq-$hr_modules->{'$mod]->[$lin'}->{'freq'}) < $eps)
			{
				my %temp = ();
				$found += 1;
				%temp =
				(
					'octave' => $octave,
					'idx'    => $idx,
				);
				$hr_modules->{'$mod]->[$lin'}->{'pcl'} = \%temp;
			}
		}
	}

	return $found;
}

sub output($)
{
	my ($hr_modules) = @_;

	for (my $i = 1; $i < scalar(%{$hr_modules}); ++$i)
	{
		next unless defined($hr_modules->{'$i'});

		for (my $j = 1; $i < scalar(%{$hr_modules->{'$i'}}); ++$j)
		{
			printf("%d|%d|%8.3f|F%d,%d\n", 	$i, $j,
								$hr_modules->{'$i'}->[$j]->{'freq'},
								$hr_modules->{'$i'}->[$j]->{'pcl'}->{'octave'},
								$hr_modules->{'$i'}->[$j]->{'pcl'}->{'idx'});
		}
	}
}
#
# main
#
	my %modules = ();


	read_modules(\%modules);

	while (my $line = <>)
	{
		chop($line);
		my ($octave, $idx, $freq) = split(/\|/,$line);

		my $result = combine(\%modules, $octave, $idx, $freq);

		warn("Frequency $freq not allocated\n") unless($result);
	}

	output(\%modules);

	exit(0);
