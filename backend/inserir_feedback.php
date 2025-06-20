<?php
require 'conexao.php';

$cliente_id = $_POST['cliente_id'] ?? null;
$nota_nps   = $_POST['nota_nps'] ?? null;
$comentario = $_POST['comentario'] ?? null;

if($cliente_id === null || $nota_nps === null)
{
    die("Erro: Cliente e nota NPS são obrigatórios.");
}

try
{
    $sql = "INSERT INTO feedbacks(cliente_id, nota_nps, comentario)
            VALUES (:cliente_id, :nota_nps, :comentario)";

    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':cliente_id', $cliente_id, PDO::PARAM_INT);
    $stmt->bindParam(':nota_nps', $nota_nps, PDO::PARAM_INT);
    $stmt->bindParam(':comentario', $comentario, PDO::PARAM_INT);
    
    $stmt-> execute();

    echo "✅Feedback registrado com sucesso!";
} 
catch(PDOException $e)
{
    echo "❌ Erro ao salvar feedback:" . $e->getMessage();
}

?>