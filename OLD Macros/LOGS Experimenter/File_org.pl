$input_num = $ARGV[0];
$input_phase = $ARGV[1];

$path  = $ENV{'AUDIOPATH'};
$newdir = "NASA-goE_Session_${input_num}_Phase_${input_phase}";
system ("mkdir ${newdir}");

#copy audio files
system ("move ${path}\\*.wav ${newdir}");

#copy transcript timestamp
system ("perl Transcript.pl");
system ("perl GUD.pl");

#renaming and moving the excel files to the folder
rename "Artemis.xls","${newdir}_Performance_results.xls";
rename "Timestamp.xls","${newdir}_Timestamps.xls";

system ("move *.xls ${newdir}");

#file renaming 	
chdir ${newdir};
@files = <*.wav>;
foreach $file (@files) {
	print $file . "\n";
	if ($file =~ /Helm/) { rename $file, "${newdir}_Helm.wav"; }
	if ($file =~ /MissionControl/) { rename $file, "${newdir}_MissionControl.wav"; }
	if ($file =~ /Weapons/) { rename $file, "${newdir}_Weapons.wav"; }
	if ($file =~ /Engineer/) { rename $file, "${newdir}_Engineering.wav"; }
	if ($file =~ /Recorder/) { rename $file, "${newdir}_Outgoing_$ENV{'PLAYERNAME'}.wav"; }
	print "Done\n";
}
	
	
	
	
 