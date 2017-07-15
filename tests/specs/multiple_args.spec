--DESCRIPTION--

Test function with multiple arguments

--GIVEN--

($x, $y) ==> {$x + $y}

--EXPECT--

(function($context·cfcd208495d565ef66e7dff9f98764da) {
    return function($x, $y) use ($context·cfcd208495d565ef66e7dff9f98764da) {
        extract($context·cfcd208495d565ef66e7dff9f98764da);
        return $x + $y ;
    };
})(get_defined_vars())