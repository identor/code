<?php
class Component
{
    public final function __get($property)
    {
        $getter = 'get' . $property;
        if (method_exists($this, $getter)) {
            return $this->$getter();
        } else {
            throw new ComponentException('Non existant getter for: ' . $property . '.');
        }
    }

    public final function __set($property, $value)
    {
        $setter = 'set' . $property;
        if (method_exists($this, $setter)) {
            $this->$setter($value);
        } else {
            throw new ComponentException('Non existant setter for: ' . $property . '.');
        }
    }
}

class ComponentException extends Exception
{
}
