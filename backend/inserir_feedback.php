<?php
require 'conexao.php'; // conexão PDO com PostgreSQL

// 1. Captura os dados enviados pelo formulário
$cliente_id = $_POST['cliente_id'] ?? null;
$nota_nps   = $_POST['nota_nps'] ?? null;
$comentario = $_POST['comentario'] ?? null;

?>