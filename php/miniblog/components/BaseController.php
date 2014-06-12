<?php
require_once(__ROOT__ . 'components/Component.php');

class BaseController extends Component
{
    /* Array list of arguments. */
    private $arguments;

    public function __construct($arguments=null)
    {
        $this->setArguments($arguments);
    }

    public function getArguments()
    {
        return $this->arguments;
    }

    public function setArguments($arguments)
    {
        $this->arguments = $arguments;
    }
}
