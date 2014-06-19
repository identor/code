<?php
require_once(__ROOT__ . 'components/Component.php');
require_once(__ROOT__ . 'components/Main.php');

class Blog
{
    private $id;
    private $title;
    private $content;

    public function __construct($id='', $title='', $content='')
    {
        $this->id = $id;
        $this->title = $title;
        $this->content = $content;
    }

    public static function getBlogById()
    {
        $sql = 'select title, content from blog where id=?';
        // TODO add dbms related calls
        return new Blog();
    }

    public static function getAllBlog()
    {
        $blogList = array();
        $sql = 'select title, contents from blog';
        // TODO add dbms related calls
        return $blogList;
    }

    public function setTitle($title)
    {
        $sql = 'update blog set title=? where id=' . $this->id;
        // execute update query or throw error here
        $this->title = $title;
    }

    public function setContent($content)
    {
        $sql = 'update blog set content=? where id=' . $this->id;
        // execute update query or throw error here
        $this->content = $content;
    }

    public function getTitle()
    {
        // decide whether to check data from the database is consistent with the current state of the object
        return $this->title;
    }

    public function getContent()
    {
        // decide whether to check data from the database is consistent with the current state of the object
        return $this->content;
    }
}
