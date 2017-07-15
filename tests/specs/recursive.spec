--DESCRIPTION--

Test recursive and precedence

--GIVEN--

$x ==> { $y ==> {$x + $y} }

--EXPECT--

(function($context·cfcd208495d565ef66e7dff9f98764da) {
    return function($x) use ($context·cfcd208495d565ef66e7dff9f98764da) {
        extract($context·cfcd208495d565ef66e7dff9f98764da);
        return (function($context·c4ca4238a0b923820dcc509a6f75849b) {
    return function($y) use ($context·c4ca4238a0b923820dcc509a6f75849b) {
        extract($context·c4ca4238a0b923820dcc509a6f75849b);
        return $x + $y ;
    };
})(get_defined_vars())  ;
    };
})(get_defined_vars())