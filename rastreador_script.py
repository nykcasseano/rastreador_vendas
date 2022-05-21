estoque =  1000
calça_vendida = 500
meta_loja = 600

objetivo_meta = calça_vendida == meta_loja + 100
if calça_vendida < meta_loja:    
    print("Ainda falta para atingirmos a meta de vendas")

elif calça_vendida <= 100:
    print("Ainda falta para 500 calças para  atingirmos no meta de vendas")
else :
    print("Atingimos nossa meta!!! Eba, vamos comemorar!")
    print(meta_loja)

estoque_atual = estoque - calça_vendida
noEstoque = estoque_atual != 0
print("Estoque de calças:")
print(estoque_atual)