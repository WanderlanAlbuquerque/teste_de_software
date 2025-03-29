def test_listas_iguais():
    lista_esperada= [1,2,3,4,5]
    lista_resultado=[1,2,3,4,5]
    assert lista_resultado== lista_esperada, "lista não são iguais"
def test_chave_no_dicionario():
    dicionario = {"nome": "Ana", "idade": 25, "cidade": "Manaus"}
    assert "nome" in dicionario
    assert dicionario["cidade"]=="Manaus"
    assert dicionario["idade"] == 25  
    
      