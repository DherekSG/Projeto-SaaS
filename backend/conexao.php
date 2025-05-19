<?php
// conexão do banco de dados
$host = "localhost";
$dbname = "projeto_SaaS";
$port = "5432";
$user = "root";
$pass = "admin123"; // COLOCA A SENHA AQUI CABAÇO

$coon = new PDO("mysql:host=$host;dbname=$dbname", $user, $pass);
$coon->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
echo "Conexão realizada com sucesso!";
?>