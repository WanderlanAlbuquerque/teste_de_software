import pytest
import sqlite3
# Fixture para criar e fechar conexão com o banco de dados
@pytest.fixture
def db_connection():
    connection = sqlite3.connect(":memory:")  # Banco de dados em memória para testes
    yield connection  # Fornece a conexão para o teste
    connection.close()  # Fecha a conexão após o teste
# Teste que utiliza a fixture
def test_db_connection(db_connection: sqlite3.Connection):
    cursor = db_connection.cursor()
    cursor.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO test (name) VALUES ('Teste')")
    # cursor.execute("INSERT INTO test (name) VALUES ('Alice')")
    # cursor.execute("INSERT INTO test (name) VALUES ('Wanderlan')")
    db_connection.commit()
    cursor.execute("SELECT * FROM test")
    result = cursor.fetchall()
    assert len(result) == 2
    assert result[0][1] == "Teste"
    assert result[0][0] == True
    assert isinstance(result[0][0], int)  # Verifica se é um número inteiro
    #assert isinstance(result[0], str)
    assert result[0][0] > 0  # Garante que o ID é positivo
   
'''
1-Faça teste para executar um UPDATE para modificar o nome "Teste"
para "Atualizado"
2-Usa Select para confirmar que o nome foi alterado com sucesso
3-Assert garante que o registro atualizado está no banco e que o 
nome corresponde ao esperado.
'''    
'''
*Faça teste para verificar uma exclusão no banco 
'''
