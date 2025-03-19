import pytest
import math

#obs: o assert é verifica os teste que perterce a linguage python não é do pytest
# o pytest verificar os teste em produção que começam com prefixo test_nome_arquivo.py
# para testar no pyteste : python -m pytest ou pytest test_nome_do_arquivo.py no mesmo diretório
# Por prof. Me . Wanderlan Carvalho de ALbuquerque
    
def test_soma():
    assert sum([1,2,3])==6

def test_potencia():
    assert pow(2,3)==8
    
def test_produto():
    assert math.prod([5,3,20])==300

def test_raiz_quadrada():
    assert math.sqrt(4)==2
   
def test_modulo():
    assert math.fmod(5,4)==1
def test_fatorial():
    assert math.factorial(5 )==120
def teste_log():
    assert math.log(1550)==7.346010209913293
def teste_cosseno():
    assert math.cos(0)==1
def teste_seno():
    assert math.sin(0)==0
def teste_tangente ():
    assert math.tan(0)==0            
def add(a,b):
    return a+b;
def subtrai(a,b):
    return a-b;
def multiplica(a,b):
    return a*b;
def divide (a,b):
    if b==0:
        raise ValueError("não pode ocorrer divisao por zero !")
    return a/b
def test_add():
    assert add(3,4)==7
    assert add(-1,1)==0
    assert add(0,0)==0
 
def test_divide():
    assert divide(10,2)==5
    assert divide(-4,2)==-2
    #assert divide(10,0)
def test_combina():
    assert add(multiplica(2,3),divide(10,2))==11
 

lista_1=[1,5,7]
lista_2=[3,6,7]

soma=sum(lista_1)
def test_soma_lita():
    assert soma==13
    

def soma_list(lista_1,lista_2):
    if len(lista_1) !=len(lista_2):
        raise ValueError ("As listas devem ter o mesmo cumprimento !") 
    return [x+y for x, y in zip(lista_1, lista_2)]
def test_soma_list():
    assert soma_list(lista_1, lista_2)==[4,11,14]

      
if __name__ =="__main__" :
    pytest.main()
       