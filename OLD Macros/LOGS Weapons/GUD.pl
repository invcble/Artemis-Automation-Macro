#Version 1.4
use strict;
use Spreadsheet::WriteExcel;

#script run to copy the required files
system ('copy "C:\Program Files (x86)\Artemis\dat\Missions\MISS_Stage1\*.txt" .');
system ('copy "C:\Program Files (x86)\Artemis\dat\Missions\MISS_Stage2\*.txt" .');
system ('copy "C:\Program Files (x86)\Artemis\dat\Missions\MISS_Stage3\*.txt" .');

my $workbook  = Spreadsheet::WriteExcel->new('Artemis.xls');
open (F1,'<MISS_Stage1_LOG.txt') or die $!;
open (F2,'<MISS_Stage2_LOG.txt') or die $!;
open (F3,'<MISS_Stage3_LOG.txt') or die $!;


##########Stage 2#############################################
my $worksheet_2 = $workbook->add_worksheet('Stage 2');

#populate excel headers
$worksheet_2->write(0, 0,  "CLOSE");
$worksheet_2->write(0, 1,  "FAR");
$worksheet_2->write(0, 2,  "Energy reduced");
$worksheet_2->write(0, 3,  "T1");
$worksheet_2->write(0, 4,  "T2");
$worksheet_2->write(0, 5,  "T3");
$worksheet_2->write(0, 6,  "Total");
$worksheet_2->write(0, 7,  "Game fail?");

my $count_sec = 0;
my $count_close = 0;
my $count_far = 0;
my $count_energy = 0;
my $move_1; 
my $move_2; 
my $move_4;

while (<F2>) {
	if ($_ =~ /SEC/) {
		$count_sec++;
		}
	else  {
		if ($_ =~ /CLOSE/) { $count_close++; }
		elsif ($_ =~ /FAR/) { $count_far++; }
		elsif ($_ =~ /Energy of ESCORT reduced/) { $count_energy++; }
		elsif ($_ =~ /Object energy triggered/) { $move_1 = $count_sec; }
		elsif ($_ =~ /Move 2/) { $worksheet_2->write(1, 3,  ($count_sec - $move_1)); $move_2 = $count_sec; }
		elsif ($_ =~ /Move 4/) { $worksheet_2->write(1, 4,  ($count_sec - $move_2)); $move_4 = $count_sec; }
		elsif ($_ =~ /Move 5/) { $worksheet_2->write(1, 5,  ($count_sec - $move_4)); }
		elsif ($_ =~ /Game time over/) { $worksheet_2->write(1, 7,  1);}
		}
}

print $count_sec;

#populate
$worksheet_2->write(1, 0,  ($count_close*5)); 
$worksheet_2->write(1, 1,  ($count_far*5)); 
$worksheet_2->write(1, 2,  ($count_energy*10)); 
$worksheet_2->write(1, 6,  $count_sec); 

close (F2);
#########################################################################################

################Stage 1##################################
my $worksheet_1 = $workbook->add_worksheet('Stage 1');

#populate excel headers
$worksheet_1->write(0, 0,  "Ship destroyed");
$worksheet_1->write(0, 1,  "Base destroyed?");
$worksheet_1->write(0, 2,  "Objects hit");
$worksheet_1->write(0, 3,  "T1");
$worksheet_1->write(0, 4,  "T2");
$worksheet_1->write(0, 5,  "Total");
$worksheet_1->write(0, 6,  "Game fail?");

#Fill in end game details - open slots
$worksheet_1->write(0, 7,  "Beams fired");
$worksheet_1->write(0, 8,  "Torpedos fired");
$worksheet_1->write(0, 9,  "Shots hit by enemy");
$worksheet_1->write(0, 10,  "Mines detonation");



my $count_sec = 0;
my $count_dead = 0;
my $dock1;

while (<F1>) {
	if ($_ =~ /SEC/) {
		$count_sec++;
		}
	else  {
		if ($_ =~ /Player Dead/) { $count_dead++; }
		elsif ($_ =~ /Station destroyed/) { $worksheet_1->write(1, 1,  1); }
		elsif ($_ =~ /Game time over/) { $worksheet_1->write(1, 6,  1);}
		elsif ($_ =~ /Dock in/) { $worksheet_1->write(1, 3,  $count_sec); $dock1 = $count_sec; }
		}
}

$worksheet_1->write(1, 0,  $count_dead); 
$worksheet_1->write(1, 4,  ($count_sec - $dock1)); 
$worksheet_1->write(1, 5,  $count_sec); 
print $count_sec;

close (F1);
############################################################################

##########################stage 3#######################################
my $worksheet_3 = $workbook->add_worksheet('Stage 3');

#populate excel headers
$worksheet_3->write(0, 0,  "Ship destroyed");
$worksheet_3->write(0, 1,  "Base destroyed?");
$worksheet_3->write(0, 2,  "Objects hit");
$worksheet_3->write(0, 3,  "T1"); #Start to inter dock 1
$worksheet_3->write(0, 4,  "T2"); #inter dock 1 to outer neb ring
$worksheet_3->write(0, 5,  "T3"); #Inside nebula
$worksheet_3->write(0, 6,  "T4"); #Second jolt to end
$worksheet_3->write(0, 7,  "Total");
$worksheet_3->write(0, 8,  "Game fail?");

#Fill in end game details - open slots
$worksheet_3->write(0, 9,  "Beams fired");
$worksheet_3->write(0, 10,  "Torpedos fired");
$worksheet_3->write(0, 11,  "Shots hit by enemy");
$worksheet_3->write(0, 12,  "Mines detonation");

my $count_sec = 0;
my $count_dead = 0;
my $dock1;
my $dock2;
my $dock3;

while (<F3>) {
	if ($_ =~ /SEC/) {
		$count_sec++;
		}
	else  {
		if ($_ =~ /Player Dead/) { $count_dead++; }
		elsif ($_ =~ /Station destroyed/) { $worksheet_3->write(1, 1,  1); }
		elsif ($_ =~ /Game time over/) { $worksheet_3->write(1, 8,  1);}
		elsif ($_ =~ /Dock in/) { $worksheet_3->write(1, 3,  $count_sec); $dock1 = $count_sec; }
		elsif ($_ =~ /T1/) { $worksheet_3->write(1, 4,  ($count_sec - $dock1)); $dock2 = $count_sec; }
		elsif ($_ =~ /T2/) { $worksheet_3->write(1, 5,  ($count_sec - $dock2)); $dock3 = $count_sec; }
		}
}

print $count_sec;
$worksheet_3->write(1, 0,  $count_dead); 
$worksheet_3->write(1, 6,  ($count_sec - $dock3)); 
$worksheet_3->write(1, 7,  $count_sec);
close (F3);
###############################################################################

system ('del -f *.txt');