<?php
require_once(__ROOT__ . 'components/Component.php');

class BaseView extends Component
{
    private $renderData;

    public function render()
    {
        echo $this->renderData;
    }

    public function appendRenderData($data)
    {
        if ($this->renderData === null) {
            $this->renderData = $data;
        } else {
            $this->renderData .= $data;
        }
    }

    public function prependRenderData($data)
    {
        if ($this->renderData === null) {
            $his->renderData = $data;
        } else {
            $this->renderData = $data . $this->renderData;
        }
    }
    public function getRenderData()
    {
        return $this->renderData;
    }

    public function setRenderData($renderData)
    {
        $this->renderData = $renderData;
    }
}
