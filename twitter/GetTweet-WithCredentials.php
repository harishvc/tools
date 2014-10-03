<?php

require("jsonformat.class.php");

//Join Twitter Developer
$oauth_access_token = "190820631-KHelnAT3VBSM8dxoehT8Blq4Bdu8celj32HPR8rM";
$consumer_key = "oKakhwi76AmRRqe7QCdg";
$consumer_secret = "6woLv3TqUO6MGmdlCJv7qnHtI2YxocBpsoGUVfpw";
$oauth_access_token_secret = "r9zRfHmqEmHBxdVffr2GsB8HyUa9X5wdZGv0VIrJV0";

if($argc != 2)  {
  echo "Usage: php GetTweetAsJson.php #tweetID# \n";
  die();
}
//Generate Tweet URL
$url = "https://api.twitter.com/1.1/statuses/show/" . $argv[1]. ".json";

//Source: http://erisds.co.uk/code/twitter-oauth-simple-curl-requests-for-your-own-data
function buildBaseString($baseURI, $method, $params)
{
    $r = array(); 
    ksort($params); 
    foreach($params as $key=>$value){
        $r[] = "$key=" . rawurlencode($value); 
    }            
    return $method."&" . rawurlencode($baseURI) . '&' . rawurlencode(implode('&', $r)); //return complete base string
}

function buildAuthorizationHeader($oauth)
{
    $r = 'Authorization: OAuth ';
    $values = array();
    foreach($oauth as $key=>$value)
        $values[] = "$key=\"" . rawurlencode($value) . "\""; 
    $r .= implode(', ', $values); 
    return $r; 
}

$oauth = array( 'oauth_consumer_key' => $consumer_key,
                'oauth_nonce' => time(),
                'oauth_signature_method' => 'HMAC-SHA1',
                'oauth_token' => $oauth_access_token,
                'oauth_timestamp' => time(),
                'oauth_version' => '1.0');

$base_info = buildBaseString($url, 'GET', $oauth);
$composite_key = rawurlencode($consumer_secret) . '&' . rawurlencode($oauth_access_token_secret);
$oauth_signature = base64_encode(hash_hmac('sha1', $base_info, $composite_key, true));
$oauth['oauth_signature'] = $oauth_signature;
$header = array(buildAuthorizationHeader($oauth), 'Expect:');
$options = array( CURLOPT_HTTPHEADER => $header,
                  CURLOPT_HEADER => false,
                  CURLOPT_URL => $url,
                  CURLOPT_BINARYTRANSFER => true,
                  CURLOPT_RETURNTRANSFER => true,
                  CURLOPT_SSL_VERIFYPEER => false);

$feed = curl_init();
curl_setopt_array($feed, $options);
$json = curl_exec($feed);
curl_close($feed);
$twitter_data = json_decode($json,PRETTY_PRINT);
$t1 = new JSONFormat('  ', "\n");
echo $t1->format($twitter_data,true);
?>
