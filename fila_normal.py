from fila_base import FilaBase
from constantes import CODIGO_NORMAL

class filanormal(FilaBase):

    
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_NORMAL}{self.codigo}'
        

            
  
        
    def chama_cliente(self,caixa:str) -> str:
        cliente_atual:str = self.fila.pop(0)    
        self.clientes_atendidos.append(cliente_atual)
        return (f'Cliente atual :{cliente_atual}, dirija-se ao caixa {caixa}')
        
        
        
            