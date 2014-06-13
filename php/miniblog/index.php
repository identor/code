<?php
define('__ROOT__', dirname(__FILE__) . '/');
require_once(__ROOT__ . 'components/Main.php');
try {
    $app = new Main();
    $app->run();
} catch (Exception $exception) {
    echo $exception->getMessage();
}
exit;
