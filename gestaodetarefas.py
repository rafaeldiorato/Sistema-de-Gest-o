import json
from datetime import datetime

# Classe tarefas
class Tarefa:
    def __init__(self, titulo, descricao, data_de_vencimento):
        self.titulo = titulo
        self.descricao = descricao
        self.data_de_nascimento = data_de_vencimento
        self.completado = False

def marcar_completada(self):
    self.completada = True

def editar_tarefa(self, novo_titulo, nova_descricao, nova_data):
    self.titulo = novo_titulo
    self.descricao = nova_descricao
    self.data_de_vencimento = nova_data 

# Classe Usuário
class Usuario:
    def __init__(self, nome_usuario, contrasena):
        self.nome_usuario = nome_usuario
        self.contrasena = contrasena
        self.tarefas = []
    
    def agregar_tarefas(self, tarefa):
        self.tarefas.append(tarefa)
    
    def eliminar_tarefas(self, titulo_tarefa):
        self.tarefas = [tarefa for tarefa in self.tarefas if tarefa.titulo != titulo_tarefa]

    def obtener_tarefas(self):
        return self.tarefas
    
class SistemaGestaoDeTarefas:
    # inicialização de gestão de um arquivo
    def  __init__(self, arquivo_datos = 'datos_usuario.json'):
        self.usuario = {}
        self.arquivos_datos = arquivo_datos
        self.cargar_datos()

    def cargar_datos(self):
        # recargar dados do usuario em json
        try:
            with open(self.arquivos_datos, 'r') as arquivo:
                datos = json.load(arquivo)
                for nome_usuario, info in datos.items():
                    # crear objeto usuario para cada usuario dos dados
                    usuario = Usuario(nome_usuario, info['contrasenha'])
                    for tarefa_info in info['tarefas']:
                        tarefa = Tarefa(tarefa_info['titulo'], tarefa_info['descricao'], tarefa_info['data_de_vencimento'])
                        tarefa_completado = tarefa_info['completada']
                        usuario.agregar_tarefas(tarefa)
                    self.usuario[nome_usuario] = usuario
        except FileNotFoundError: # manejo de excepcão
            print('Arquivo de dados não encontrado, criaremos um novo arquivo para guardar.')
    
    def guardar_dados(self):
        # guardar dados dos usuario no arquivo
        dados = {} # este é um dicionário
        for nome_usuario, usuario in self.usuario.items():
            # organiza os dados e informação do usuario
            dados[nome_usuario] = {
                'contrasena': usuario.contrasena,
                'tarefas': [
                    {'titulo': Tarefa.titulo, 'descricao': Tarefa.descricao, 'data_de_vencimento': Tarefa.data_de_vencimento, 'completada': Tarefa.completado}
                    for tarefa in usuario.tarefas
                ]
            }
        with open(self.arquivos_datos, 'w') as arquivo:
            json.dump(dados, arquivo)
    
    def registrar_usuario(self, nome_usuario, contrasena):
        # registrar um novo usuário, se o nome do usuário não existir
        if nome_usuario in self.usuario:
            print('O usuario já existe.')
            return False
        else:
            self.usuario[nome_usuario] = Usuario(nome_usuario, contrasena)
            self.guardar_dados()
            print('Usuário guardado com sucesso!')
            return True
    
    def menu_usuario(self, usuario):
        while True:
            print('\n1.Criar tarefa')
            print('2. Mostrar tarefa')
            print('3. Editar tarefa')
            print('4. Completar tarefa')
            print('5. Excluir tarefa')
            print('6. Fechar sistema')

            opcao = input('Seleciona uma opção: ')
            if opcao == '1':
                titulo = input('Titulo da tarefa: ')
                descricao = input('Ingressa a descrição: ')
                data_de_vencimento = input('Data de vencimento (YYYY-MM-DD): ')
                tarefa = Tarefa(titulo, descricao, data_de_vencimento)
                usuario.agregar_tarefa(tarefa)
                self.menu_usuario
                print('Tarefa criada com sucesso!')

            elif opcao == '2':
                tarefas = usuario.obtener_tarefas()
                if not tarefas:
                    print('Não existe tarefa.')
                for idx, tarefa in enumerate(tarefa, start=1):
                    estado = 'Completado' if tarefa.completado else 'Pendente'
                    print(f"{idx}. {tarefa.titulo} - {estado} - Vence {tarefa.data_de_vencimento}")
            
            elif opcao =='3':
                titulo_tarefa = input('Titulo da tarefa para edição: ')
                tarefa = next((t for t in usuario.tarefas if t.titulo == titulo.tarefa), None)
                if tarefa:
                    novo_titulo = input('Novo titulo: ')
                    nova_descricao = input('Nova descrição: ')
                    nova_data = input('Nova da de vencimento(YYYY-MM-DD)')
                    tarefa.editar_tarefa(novo_titulo, nova_descricao, nova_data)
                    self.guardar_dados()
                    print('Tarefa atualizada com sucesso!')
                else:
                    print('Tarefa não encontrada.')

            elif opcao == '4':
                # marcar uma tarefa completada
                titulo_tarefa = input('Titulo da tarefa para completar: ')
                tarefa = next((t for t in usuario.tarefas if t.titulo == titulo.tarefa), None)
                if tarefa:
                    tarefa.marcar_completada()
                    nova_descricao = input('Nova descrição: ')
                    nova_data = input('Nova da de vencimento(YYYY-MM-DD)')
                    tarefa.editar_tarefa(novo_titulo, nova_descricao, nova_data)
                    self.guardar_dados()
                    print('Tarefa marcada com sucesso!')
                else:
                    print('Tarefa não encontrada.')
            
            elif opcao == '5':
                # eliminar tarefa
                titulo_tarefa = input('Titulo d a tarefa a eliminar: ')
                usuario.eliminar_tarefa(titulo_tarefa)
                self.guardar_dados()
                print('Tarefa eliminada com sucesso!')
            
            elif opcao == '6':
                # fechar sistema
                print('Fecha sessão...')
                break
            else:
                print('Opção inválido, tenta de novo!')
    
 # ejecução do sistema
 # ejecução do sistema
if __name__ == '__main__':
    sistema = SistemaGestaoDeTarefas()
    while True:
        print('\n-----Sistema de Gestão de Tarefas-----')
        print('1. Registrar Usuário')
        print('2. Iniciar Sessão')
        print('3. Salir')
        opcao = input('Selecione uma opção: ')

        if opcao == '1':
            nome_usuario = input('Ingresse o nome do usuário: ')
            contrasena = input('Ingressa a contrasenha: ')
            sistema.registrar_usuario(nome_usuario, contrasena)

        elif opcao == '2':
            nome_usuario = input('Nome do usuário: ')
            contrasena = input('Contrasenha: ')
            usuario = sistema.iniciar_sessao(nome_usuario, contrasena)
            if usuario: 
                sistema.menu_usuario(usuario)
        
        elif opcao == '3':
            print('Sair do sistema.')
            break
        else:
            print('Opção inválida, tenta de novo!')
