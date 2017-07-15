--DESCRIPTION--

Test simplest operations

--GIVEN--

($x) ==> {
    $y = $x + 1;
    return $y;
}

--EXPECT--

(function($context·cfcd208495d565ef66e7dff9f98764da) {
    return function($x ) use ($context·cfcd208495d565ef66e7dff9f98764da) {
        extract($context·cfcd208495d565ef66e7dff9f98764da);
        $y = $x + 1;
    return $y;

    };
})(get_defined_vars())