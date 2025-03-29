#No pytest, uma fixture é uma função utilizada para configurar ou preparar o ambiente de teste antes de cada execução.
#Elas são muito úteis para fornecer dependências ou dados necessários para os testes, como inicializar bancos de dados, criar objetos, conectar-se a APIs, entre outras tarefas.
#O diferencial das fixtures no pytest é que elas são extremamente reutilizáveis e fáceis de compartilhar entre múltiplos testes, aumentando a legibilidade e a manutenção do código de teste.
import pytest
@pytest.fixture #ele define um decorador e dar para funções dele e funcionalidade extras
def sample_list():
    return [1,2,3,4,5]
def test_soma(sample_list):
    assert sum(sample_list)==15
def test_tamanho(sample_list):
    assert len(sample_list)==5    
def test_maior(sample_list):
    assert max(sample_list)==5
def test_minimo(sample_list):
    assert min(sample_list)==1
       