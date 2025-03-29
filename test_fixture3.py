import pytest
import sqlite3
# Fixture para criar e fechar conexão com o banco de dados
@pytest.fixture
def db_connection():
    connection = sqlite3.connect(":memory:")  # Banco de dados em memória para testes
    yield connection  # Fornece a conexão para o teste
    connection.close()  # Fecha a conexão após o teste
# Teste que utiliza a fixture
def test_db_connection(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO test (name) VALUES ('Teste')")
    db_connection.commit()
    cursor.execute("SELECT * FROM test")
    result = cursor.fetchall()
    assert len(result) == 2
    assert result[0][1] == "Teste"