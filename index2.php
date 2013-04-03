<?php
$filename = "counter.txt";
$count = system("python get_count.py.cgi $filename");
system("python add_count.py.cgi $filename $count");
echo "<br/>";
$timerange = system("python get_time.py.cgi");
$timecount = system("python get_time_count.py.cgi $timerange");
system("python add_time_count.py.cgi $timerange $timecount");
system("python show_time_counts.py.cgi")
?>
