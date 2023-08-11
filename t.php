<?php

class Telegram {

    const CHAT_ID =  -1001966416783;
    
    const TOKEN = '6292566248:AAEqDZCW3DBgxugrnKvIzbDGzyK-TewclQ0';

    public static function sendMessage($message)
    {
        $url = "https://api.telegram.org/bot" . self::TOKEN . "/sendMessage?chat_id=" . self::CHAT_ID;
        $url = $url . "&text=" . urlencode($message);
        $ch = curl_init();
        $optArray = array(
            CURLOPT_URL => $url,
            CURLOPT_RETURNTRANSFER => true
        );
        curl_setopt_array($ch, $optArray);
        $result = curl_exec($ch);
        curl_close($ch);
    }

}
