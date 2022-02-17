<?php
	error_reporting(0);
	if(isset($_GET['debug'])){
		highlight_file(__FILE__);
		die();
	}
	$z = "Hello World!";
	if(isset($_GET['x']) && isset($_GET['cmd'])){
		echo preg_replace($_GET['x'], $_GET['cmd'], $z);
	}else{
		echo $z;
		echo '<!-- /?debug for source -->';

	}
?>
