--DESCRIPTION--

Test simplest operations

--GIVEN--

($x) ==> {$x + 1}

--EXPECT--

(function($context·cfcd208495d565ef66e7dff9f98764da) {
    return function($x) use ($context·cfcd208495d565ef66e7dff9f98764da) {
        extract($context·cfcd208495d565ef66e7dff9f98764da);
        return $x + 1 ;
    };
})(get_defined_vars())