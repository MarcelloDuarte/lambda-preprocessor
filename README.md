A hack-like lambda syntax for PHP
=================================

In [Hacklang](https://docs.hhvm.com/hack/lambdas/introduction), a lambda expression is denoted by using the lambda arrow `==>`. Left of the arrow are arguments to the anonymous function and on the right hand side is either an expression or a list of statements.

This pre-processor is meant to make that syntax available in native PHP applications. This does not happen at runtime, so there is no hit on perfomance. The pre-processor works on top of the [pre](https://github.com/preprocess/pre-plugin) plugin and the [yay macro library](https://github.com/marcioAlmada/yay).

Syntax wise, and due to the fact that Yay does not have an expresison parser yet, even though Hack supports a single expression to be written without the need of curly brakets, this pre-processor will always require the curly brakets to be written. Hopefully this will change once we Yay develops further.

Oneliner anonymous function
---------------------------

The simplest example is an anonymous function that returns the argument it was given in the first place. In PHP it could be written as:

```php
$id = function($x) { return $x };
```

Which can be written, using this pre-processor, much simpler:

```php
$id = $x ==> { $x };
```

Should we need to declare typehints or pass more than one argument, we will need to use parenthesis. We could also use parenthesis in the example above, but it is optional for single arguments with no type hinting.

```php
$addNumbers = ($x, $y) ==> { $x + $y };
```

Which is translated to:

```php
$addNumbers = function ($x, $y) { return $x + $y };
```

Or with type hints:

```php
$addNumbers = (int $x, int $y): int ==> { $x + $y };
```

Which is translated to:

```php
$addNumbers = function (int $x, int $y): int { return $x + $y };
```

Multiple lines anonymous functions
----------------------------------

The same rules for arguments, typehints and return types still apply for anonymous functions with multiple lines. The only difference is that you will need to write the `return` keyword in the last statement of the block, and you must now end every statement with a semicolon.

```php
$increment = $x ==> {
    $y = $x + 1;
    return $y;
};
```

This is translated into:

```php
$increment = function($x) {
    $y = $x + 1;
    return $y;
};
```

Closures
--------

PHP provides the keyword `use` to capture variables from the enclosing scope. Hack's lambdas make this even easier. You can use variables implicitly inside of a lambda. This is available when you use this pre-processor.

```php
function addLastname(array $names, string $lastname): array
{
    return array_map($name ==> { $name . " " . $lastname }, $names);
}
```

Note that to use `$lastname` with the official syntax you would have to use the `use` keyword, as shown below:

```php
function addLastname(array $names, string $lastname): array
{
    return array_map(function($name) use ($lastname) { return $name . " " . $lastname }, $names);
}
```

Recursive calls and precedence
------------------------------

The pre-processor will translate the inner block and then the outer. The precedence with this syntax is a bit more obvious than the hack one. In hack you can ommit the brakets `{`, `}`. Here, it should be straightforward that the expression:

```php
$lambda = $x ==> { $y ==> { $x + $y } };
```

will be translated into:

```php
$lambda = function($x){ return function($y){ return $x + $y; }; };
```

Final Notes
-----------
 - This pre-processor is alpha software. Do not use it in production.