<?php
$name = $_REQUEST['name'];
$email = $_REQUEST['email'];
$subject = $_REQUEST['subject'];
$message = $_REQUEST['message'];

mail("attrikunal16@gmail.com", $subject, $message, "From: $name <$email>");
echo "<script type='text/javascript'>alert('Message sent successfully');
    window.history.go(-1);
    </script>";
?>