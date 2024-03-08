from fila_normal import filanormal
from fila_prioritaria import FilaPrioritaria

fila_teste = filanormal()

#fila_teste.atualiza_fila()
#fila_teste.atualiza_fila()
#fila_teste.atualiza_fila()
#fila_teste.atualiza_fila()

#print(fila_teste.chama_cliente(12))
#print(fila_teste.chama_cliente(10))


fila_teste2 = FilaPrioritaria()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
print(fila_teste2.chama_cliente(10))
print(fila_teste2.chama_cliente(12))
print(fila_teste2.estatistica("12/02/2003", 198, 'detail'))