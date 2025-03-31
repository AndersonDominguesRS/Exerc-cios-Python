import heapq

class EscalonadorDeProcessos: 
    def __init__(self):
        self.heap = []
        self.id_para_processo = {} 

    def adicionar_processo(self, processo_id, tempo_execucao, prioridade):

        heapq.heappush(self.heap, (prioridade, processo_id, tempo_execucao))
        self.id_para_processo[processo_id] = (prioridade, tempo_execucao)
		

    def executar_proximo_processo(self):
	
        if not self.heap:
            print("Nenhum processo para executar.")
            return None
        prioridade, processo_id, tempo_execucao = heapq.heappop(self.heap)
        self.id_para_processo.pop(processo_id, None)
        print(f"Executando processo {processo_id} com prioridade {prioridade} e tempo de execução {tempo_execucao}.")
        return processo_id

    def modificar_prioridade(self, processo_id, nova_prioridade):
        if processo_id not in self.id_para_processo:
            print(f"Processo {processo_id} não encontrado.")
            return
        tempo_execucao = self.id_para_processo[processo_id][1]
        self.remover_processo(processo_id)
        self.adicionar_processo(processo_id, tempo_execucao, nova_prioridade)
        print(f"Prioridade do processo {processo_id} atualizada para {nova_prioridade}.")

    def remover_processo(self, processo_id) : #removendo o processo somente uma vez
        self.heap = [(p, pid, t) for p, pid, t in self.heap if pid != processo_id]
        heapq.heapify(self.heap)
        self.id_para_processo.pop(processo_id, None)

    def listar_processos( self ):
        print("Processos na fila de prioridade:")
        for prioridade, processo_id, tempo_execucao in self.heap:
            print(f"ID: {processo_id}, Prioridade: {prioridade}, Tempo de Execução: {tempo_execucao}")