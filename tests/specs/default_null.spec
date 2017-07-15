--DESCRIPTION--

Test default value: null, one argument

--GIVEN--

($x = null) ==> {$x}

--EXPECT--

(function($context·cfcd208495d565ef66e7dff9f98764da) {
    return function($x =null) use ($context·cfcd208495d565ef66e7dff9f98764da) {
        extract($context·cfcd208495d565ef66e7dff9f98764da);
        return $x ;
    };
})(get_defined_vars())