<?php

    $link = mysqli_connect("shareddb1b.hosting.stackcp.net", "cl29-users-bzh", "YTTMcfhK.", "cl29-users-bzh");

    if (mysqli_connect_error()) {
        
        die ("There was an error connecting to the database");
        
    } 

    $query = "SELECT * FROM users";

    if ($result = mysqli_query($link, $query)) {
        
        $row = mysqli_fetch_array($result);
        
        echo "Your email is ".$row[1]." and your password is ".$row[2];
        
    }


?>