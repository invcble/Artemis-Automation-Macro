use Spreadsheet::WriteExcel;
use POSIX;

open (F1,'<Test.txt') or die $!;
my $workbook  = Spreadsheet::WriteExcel->new('Timestamp.xls');
my $worksheet_1 = $workbook->add_worksheet('Stage 1');

#Populate 
$worksheet_1->write(0, 0,  "From");
$worksheet_1->write(0, 1,  "To");
$worksheet_1->write(0, 2,  "Time_from");
$worksheet_1->write(0, 3,  "Time_to");
$worksheet_1->write(0, 4,  "Delay");
$worksheet_1->write(0, 5,  "Transcript");

my $count = 1;

sub return_time {
 
  $seconds = $_[0];
  $sec = (($seconds/60) - floor($seconds/60))*60;
  $min = floor ($seconds/60);
  if ($min < 10) { $MIN = "0$min"; }
  else { $MIN = $min; }
  if ($sec < 10) { $SEC = "0$sec"; }
  else { $SEC = $sec; }
  
  return ("$MIN:$SEC");

}

while (<F1>) {
	@splitter = split (' ');
	if ($splitter[0] =~ /Press/) { 
	$worksheet_1->write($count, 0,  $ENV{'PLAYERNAME'});
	$worksheet_1->write ($count,1,$splitter[7]); 
	#$worksheet_1->write ($count,2,$splitter[3]);
	$worksheet_1->write ($count,2,return_time ($splitter[3]));
	$worksheet_1->write ($count,3,return_time ($splitter[8]));
	
	#Write the delay if mission control / shout
	if ($splitter[7] =~ /MissionControl/) { $worksheet_1->write ($count, 4, return_time ($splitter[9])); }
	if ($ENV{'PLAYERNAME'} =~ /MissionControl/) { $worksheet_1->write ($count, 4, return_time ($splitter[9])); }
	
	}
	elsif ($splitter[0] =~ /Shout/) { 
	$worksheet_1->write($count, 0,  $ENV{'PLAYERNAME'}); #FIX an environment variable
	$worksheet_1->write ($count,1,"Shout"); 
	$worksheet_1->write ($count,2,return_time ($splitter[3]));
	$worksheet_1->write ($count,3,return_time ($splitter[5]));
	
	if ($ENV{'PLAYERNAME'} =~ /MissionControl/) { $worksheet_1->write ($count, 4, return_time ($splitter[6])); }
	}
	$count++;
}

close (F1);
