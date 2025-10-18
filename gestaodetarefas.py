import json
from datetime import datetime

# ===============================
# CLASSE TAREFA
# ===============================
class Tarefa:
    def __init__(self, titulo, descricao, data_de_vencimento):
        self.titulo = titulo
        self.descricao = descricao
        self.data_de_vencimento = data_de_vencimento
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def editar_tarefa(self, novo_titulo, nova_descricao, nova_data):
        self.titulo = novo_titulo
        self.descricao = nova_descricao
        self.data_de_vencimento = nova_data

# ===============================
# CLASSE USUÁRIO
# ===============================
class Usuario:
    def __init__(self, nome_usuario, senha):
        self.nome_usuario = nome_usuario
        self.senha = senha
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def eliminar_tarefa(self, titulo_tarefa):
        self.tarefas = [t for t in self.tarefas if t.titulo != titulo_tarefa]

    def obter_tarefas(self):
        return self.tarefas

# ===============================
# CLASSE SISTEMA DE GESTÃO
# ===============================
class SistemaGestaoDeTarefas:
    def __init__(self, arquivo_dados='dados_usuarios.json'):
        self.usuarios = {}
        self.arquivo_dados = arquivo_dados
        self.carregar_dados()

    # ---------------------------
    # Carregar dados do JSON
    # ---------------------------
    def carregar_dados(self):
        try:
            with open(self.arquivo_dados, 'r') as arquivo:
                dados = json.load(arquivo)
                for nome_usuario, info in dados.items():
                    usuario = Usuario(nome_usuario, info['senha'])
                    for tarefa_info in info['tarefas']:
                        tarefa = Tarefa(
                            tarefa_info['titulo'],
                            tarefa_info['descricao'],
                            tarefa_info['data_de_vencimento']
                        )
                        tarefa.completada = tarefa_info['completada']
                        usuario.adicionar_tarefa(tarefa)
                    self.usuarios[nome_usuario] = usuario
        except FileNotFoundError:
            print("Nenhum dado encontrado. Um novo arquivo será criado.")

    # ---------------------------
    # Salvar dados no JSON
    # ---------------------------
    def salvar_dados(self):
        dados = {}
        for nome_usuario, usuario in self.usuarios.items():
            dados[nome_usuario] = {
                'senha': usuario.senha,
                'tarefas': [
                    {
                        'titulo': t.titulo,
                        'descricao': t.descricao,
                        'data_de_vencimento': t.data_de_vencimento,
                        'completada': t.completada
                    }
                    for t in usuario.tarefas
                ]
            }
        with open(self.arquivo_dados, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)

    # ---------------------------
    # Registrar novo usuário
    # ---------------------------
    def registrar_usuario(self, nome_usuario, senha):
        if nome_usuario in self.usuarios:
            print("Usuário já existe.")
            return False
        self.usuarios[nome_usuario] = Usuario(nome_usuario, senha)
        self.salvar_dados()
        print("Usuário registrado com sucesso!")
        return True

    # ---------------------------
    # Iniciar sessão
    # ---------------------------
    def iniciar_sessao(self, nome_usuario, senha):
        usuario = self.usuarios.get(nome_usuario)
        if usuario and usuario.senha == senha:
            print(f"Bem-vindo(a), {nome_usuario}!")
            return usuario
        print("Usuário ou senha incorretos.")
        return None

    # ---------------------------
    # Menu principal do usuário
    # ---------------------------
    def menu_usuario(self, usuario):
        while True:
            print("\n--- MENU DE USUÁRIO ---")
            print("1. Criar tarefa")
            print("2. Mostrar tarefas")
            print("3. Editar tarefa")
            print("4. Marcar tarefa como concluída")
            print("5. Excluir tarefa")
            print("6. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                titulo = input("Título da tarefa: ")
                descricao = input("Descrição: ")
                data = input("Data de vencimento (YYYY-MM-DD): ")
                tarefa = Tarefa(titulo, descricao, data)
                usuario.adicionar_tarefa(tarefa)
                self.salvar_dados()
                print("✅ Tarefa criada com sucesso!")

            elif opcao == '2':
                tarefas = usuario.obter_tarefas()
                if not tarefas:
                    print("Nenhuma tarefa encontrada.")
                else:
                    for i, t in enumerate(tarefas, start=1):
                        status = "✔️ Concluída" if t.completada else "⏳ Pendente"
                        print(f"{i}. {t.titulo} - {status} (vence {t.data_de_vencimento})")

            elif opcao == '3':
                titulo = input("Digite o título da tarefa para editar: ")
                tarefa = next((t for t in usuario.tarefas if t.titulo == titulo), None)
                if tarefa:
                    novo_titulo = input("Novo título: ")
                    nova_desc = input("Nova descrição: ")
                    nova_data = input("Nova data (YYYY-MM-DD): ")
                    tarefa.editar_tarefa(novo_titulo, nova_desc, nova_data)
                    self.salvar_dados()
                    print("✏️ Tarefa atualizada!")
                else:
                    print("Tarefa não encontrada.")

            elif opcao == '4':
                titulo = input("Digite o título da tarefa a marcar como concluída: ")
                tarefa = next((t for t in usuario.tarefas if t.titulo == titulo), None)
                if tarefa:
                    tarefa.marcar_completada()
                    self.salvar_dados()
                    print("✅ Tarefa marcada como concluída!")
                else:
                    print("Tarefa não encontrada.")

            elif opcao == '5':
                titulo = input("Digite o título da tarefa para excluir: ")
                usuario.eliminar_tarefa(titulo)
                self.salvar_dados()
                print("🗑️ Tarefa excluída com sucesso!")

            elif opcao == '6':
                print("Saindo do menu de usuário...")
                break

            else:
                print("❌ Opção inválida, tente novamente.")

# ===============================
# EXECUÇÃO DO SISTEMA
# ===============================
if __name__ == '__main__':
    sistema = SistemaGestaoDeTarefas()
    while True:
        print("\n===== SISTEMA DE GESTÃO DE TAREFAS =====")
        print("1. Registrar novo usuário")
        print("2. Iniciar sessão")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome de usuário: ")
            senha = input("Senha: ")
            sistema.registrar_usuario(nome, senha)

        elif escolha == '2':
            nome = input("Nome de usuário: ")
            senha = input("Senha: ")
            usuario = sistema.iniciar_sessao(nome, senha)
            if usuario:
                sistema.menu_usuario(usuario)

        elif escolha == '3':
            print("👋 Saindo do sistema. Até logo!")
            break

        else:
            print("❌ Opção inválida, tente novamente.")
