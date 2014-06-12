<?php
require_once(__ROOT__ . 'components/BaseController.php');

class BlogController extends BaseController
{
    public function defaultAction()
    {
        print_r($this->getArguments());
    }

}
