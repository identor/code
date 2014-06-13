<?php
require_once(__ROOT__ . 'components/BaseController.php');
require_once(__ROOT__ . 'views/BlogView.php');

class BlogController extends BaseController
{
    public function defaultAction()
    {
        $defaultView = new BlogView();
        $defaultView->render();
    }

}
