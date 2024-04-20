class Teste:
    def __enter__(self):
        print('Estou entrando')
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Estou saindo')


with Teste() as Ts:
    print('Estou no meio') 
  