
<?php

//MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oLSktKCgrbjY%3D
//"{"showpassword":"no","bgcolor":"#ffffff"}"
//0l;\$\$98-8=?#9*jvi\ 'ngl*+(!$#9lrnh-)-((+n67


$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
$crack = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_encrypt($in) {
    $key = base64_decode("MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY=");
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
$dat =  array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

$inn = "{\"showpassword\":\"no\",\"bgcolor\":\"#ffffff\"}";
$out = base64_decode("MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY=");

$hacked_cookie = json_encode($crack);
print($out);

//print(base64_encode(xor_encrypt(json_encode($crack))));
?>
