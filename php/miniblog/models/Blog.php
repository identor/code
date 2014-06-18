<?php
require_once(__ROOT__ . 'components/Component.php');
require_once(__ROOT__ . 'components/Main.php');

class Blog
{
    private $title;
    private $contents;

    public function __construct($title='', $contents='')
    {
        $this->title = $title;
        $this->contents = $contents;
    }

    public static function getBlogById()
    {
        return new Blog();
    }
}
