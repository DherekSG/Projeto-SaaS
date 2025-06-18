<?php
$host = "localhost";
$port = "5432";
$dbname = "projeto_saas"; 
$user = "postgres";       
$pass = "0232610082";      
try {
    $conn = new PDO("pgsql:host=$host;dbname=$dbname", $user, $pass);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Erro na conexão com o banco de dados PostgreSQL: " . $e->getMessage());
}
?>
