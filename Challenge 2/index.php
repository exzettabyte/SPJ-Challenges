<?php
	include "flag.php";
	error_reporting(0);
	if(isset($_GET['debug'])){
		highlight_file(__FILE__);
		die();
	}
?>
<!DOCTYPE html>
<html>
<head>
	<link href="https://fonts.googleapis.com/css?family=IBM+Plex+Sans" rel="stylesheet"> 
	<link rel="stylesheet" href="style.css">
</head>
<body>
	<center>
		<div class="wrapper">
			<h1>Login</h1>
			<form method="POST" action="">
				<label for="user">Username</label>
				<input type="text" name="username" id="username"><br>
				<label for="pass">Password </label>
				<input type="password" name="password" id="password"><br>
				<button type="submit" name="login">Submit</button><br>
			</form>
		
		<?php 
			if(isset($_POST['username']) && isset($_POST['password'])){
				extract($_POST);
				if($_POST['username'] === $user1337 && $_POST['password'] === $pass1337){
					die("<p>ini flag buat kamu :)</p>  $flag");
				}else{
					echo "<p style='color:red'>Username atau password salah!</p>";
				}
			}
		?>
		<!-- /?debug for source code -->
		</div>
	</center>
</body>
</html>

