<?php
require_once(__ROOT__ . 'components/Component.php');
require_once(__ROOT__ . 'controllers/BlogController.php');
require_once(__ROOT__ . 'models/Blog.php');

class Main extends Component
{
    private $activeController;
    private $activeAction;
    private static $db;

    public static function getDb()
    {
        if (self::$db instanceof mysqli) {
            return self::$db;
        } else {
            self::$db = new mysqli('localhost', 'root', 'password', 'test'); // TODO add db params
            if (self::$db->mysqli_connect_error) {
                throw new ComponentException(self::$db->connect_errno . ': ' . self::$db->mysqli_connect_error);
            }
            return self::$db;
        }
    }

    public function __construct()
    {
        print_r($_GET);
        $this->activeController = new BlogController();
        if (isset($_GET['controller'])) {
            $controller = $_GET['controller'];
            $this->activeController = new $controller();
        }
        $this->activeAction = 'default';
        if (isset($_GET['action'])) {
            $this->activeAction = $_GET['action'];
        }
        if (isset($_GET['arguments'])) {
            $this->activeController->arguments = $_GET['arguments'];
        }
    }

    public function run()
    {
        $actionCall = $this->activeAction . 'Action';
        if (method_exists(new BlogController(), $actionCall)) {
            echo 'Function ' . $actionCall . ' Exists' . PHP_EOL;
            $this->activeController->$actionCall();
        } else {
            echo 'Function ' . $actionCall . ' Non-Existant' . PHP_EOL;
        }
        echo 'Success...' . PHP_EOL;
    }
}
