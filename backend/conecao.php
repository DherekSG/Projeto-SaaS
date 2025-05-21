<?php

use Dom\Mysql;

$servidor = "Localhost";
$usuario = "root";
$senha = "";
$banco = "Union.db";

//Agora vou conectar

$conn = new Mysql($servidor, $usuario, $senha, $banco);

//Teste conexão

if ($conn->connect_error){
    die("Conexão Falha".
$conn->connect_error);
}

//Seloco fi
?>