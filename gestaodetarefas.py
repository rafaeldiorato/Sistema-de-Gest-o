import json
from datetime import datetime

# Classe tarefas
class Tarefas:
    def __init__(self, titulo, descricao, data_de_vencimento):
        self.titulo = titulo
        self.descricao = descricao
        self.data_de_nascimento = data_de_vencimento
        self.completado = False

def marcar_completada(self):
    self.completado = True

def editar_tarefa(self, novo_titulo, nova_descricao, nova_data):
    self.titulo = novo_titulo
    self.descricao = nova_descricao
    self.data_de_vencimento = nova_data 

# Classe Usuário
class Usuario:
    def __init__(self, nome_usuario, contrasena):
        self.nome_usuario = nome_usuario
        self.contasena = contrasena
        self.tarefas = []
    
    def agregar_tarefas(self, tarefa):
        self.tarefas.append(tarefa)
    
    def eliminar_tarefas(self, titulo_tarefa):
        self.tarefas = [tarefa for tarefa in self.tarefas if tarefa.titulo != titulo_tarefa]

    def obtener_tarefas(self):
        return self.tarefas