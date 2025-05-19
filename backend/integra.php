<?php  
$conn = pg_connect("host=localhost dbname=postgres user=postgres password=admin123");

if(!$conn) {
    echo "Erro na Conexão com o banco de dados.";
} else {
    echo "Conexão realizada com sucesso.";
}
