 <?php 
 
$a = 10;
$b = 5;
$c = 2;

$result = $a + $b * $c; // Primero se multiplica, luego se suma
echo "Resultado 1: " . $result . "<br>";

$result = ($a + $b) * $c; // Primero se suman $a y $b, luego se multiplica por $c
echo "Resultado 2: " . $result . "<br>";

$result = $a * $b / $c; // Primero se multiplican $a y $b, luego se divide por $c
echo "Resultado 3: " . $result . "<br>";

$result = $a % $b + $c; // Primero se calcula el módulo, luego se suma $c
echo "Resultado 4: " . $result . "<br>";

?>