<?php
$filename = "counter.txt";
$count = system("python get_count.py.cgi $filename");
system("python add_count.py.cgi $filename $count");
?>
