import abc
from constantes import TAMANHO_MAXIMO_PADRAO
from constantes import TAMANHO_PADRAO_MINIMO


class FilaBase(metaclass=abc.ABCMeta):
    codigo:int = 0
    fila = []
    clientes_atendidos = []
    senha_atual:str = ""
    
    
    
    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_MAXIMO_PADRAO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo +=1
            
            
    def insere_cliente(self):
        self.fila.append(self.senha_atual)
    
    
    @abc.abstractmethod
    def gera_senha_atual(self):
       ...
       
       
   
    def atualiza_fila(self):
        self.reseta_fila()
        self.gera_senha_atual()
        self.insere_cliente()
        
        
        
    @abc.abstractmethod
    def chama_cliente(self):
         ...