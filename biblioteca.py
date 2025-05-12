class ListaDeTarefa():
    def __init__(self, lista):
        self.lista = lista

    def menu(self):
        self.opcoes = int(input("Digite a opção desejada(1-Listar; 2-Inserir; 3-Deletar; 4-Sair):  "))
        if self.opcoes == 1:
            self.listarTarefas()
        elif self.opcoes == 2:
            self.inserirTarefas()
        elif self.opcoes == 3:
            self.deletarTarefas()
        elif self.opcoes == 4:
            self.Sair()
        else:
            print("esse não é um comando válido")

    def listarTarefas(self):
            for i in self.lista:
                print(i)
            novaAtividade = input("deseja realizar mais alguma ação?(s/n): ")
            if novaAtividade == "s":
                self.menu()
    def inserirTarefas(self):
        novatarefa = input("digite a nova tarefa: ")
        self.lista.append(novatarefa)
        novaAtividade = input("deseja realizar mais alguma ação?(s/n): ")
        if novaAtividade == "s":
            self.menu()
    def deletarTarefas(self):
        deletar = int(input("Digite o número da tarefa que deseja deletar: "))
        if deletar >= 1 and deletar <= len(self.lista):
            self.lista.pop(deletar - 1)
            print("Tarefa removida com sucesso.")
            novaAtividade = input("deseja realizar mais alguma ação?(s/n):  ")
            if novaAtividade == "s":
                self.menu()

    def Sair(self):
       print("encerrando o programa")

