--DESCRIPTION--

Test default value: 42, one argument

--GIVEN--

($x = 42) ==> {$x}

--EXPECT--

(function($context·cfcd208495d565ef66e7dff9f98764da) {
    return function($x =42) use ($context·cfcd208495d565ef66e7dff9f98764da) {
        extract($context·cfcd208495d565ef66e7dff9f98764da);
        return $x ;
    };
})(get_defined_vars())