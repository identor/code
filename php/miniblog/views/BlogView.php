<?php
require_once(__ROOT__ . 'components/BaseView.php');

class BlogView extends BaseView
{
    public function __construct()
    {
        $this->setRenderData(file_get_contents(__ROOT__ . 'assets/blogviewtest.html')); 
    }
}
