use Time::Piece;
use Archive::Zip;

$zip = Archive::Zip->new ();

$today = Time::Piece->new->strftime ('%m_%d_%Y');

$input = $ARGV[0];

$path  = $ENV{'AUDIOPATH'};
$newdir = "DHSIR_Run_${input}_${today}";
system ("mkdir ${newdir}");

#copy audio files
system ("copy ${path}\\*.wav ${newdir}");

#copy transcript timestamp
system ("perl Transcript.pl");
system ("copy Test.txt ${newdir}");
system ("perl GUD.pl");
system ("copy Artemis.xls ${newdir}");
system ("copy Timestamp.xls ${newdir}");



$zip->addTree ("${newdir}\\");
$zip->writeToFileNamed ("${newdir}.zip");

 system ("del *.xls");
 system ("del -r ${newdir}");