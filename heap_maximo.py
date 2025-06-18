import heapq

def criar_heap_maximo():
    return []

def inserir_heap_maximo(heap, valor):
    heapq.heappush(heap, -valor)

def remover_heap_maximo(heap):
    return -heapq.heappop(heap) if heap else None

def consultar_topo(heap):
    return -heap[0] if heap else None

def transformar_em_heap_maximo(lista):
    lista = [-num for num in lista]
    heapq.heapify(lista)
    return lista

def obter_n_maiores(heap, n):
    return [-val for val in heapq.nsmallest(n, heap)]

def main():
    heap = criar_heap_maximo()
    
    while True:
        print("\nMenu:")
        print("1. Inserir valor")
        print("2. Remover valor")
        print("3. Consultar topo")
        print("4. Transformar lista em heap")
        print("5. Obter N maiores valores")
        print("6. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            valor = int(input("Valor a inserir: "))
            inserir_heap_maximo(heap, valor)
            print("Heap:", heap)
        elif escolha == "2":
            valor = remover_heap_maximo(heap)
            print("Removido:", valor)
            print("Heap:", heap)
        elif escolha == "3":
            print("Topo:", consultar_topo(heap))
        elif escolha == "4":
            nums = list(map(int, input("Digite os números separados por espaço: ").split()))
            heap = transformar_em_heap_maximo(nums)
            print("Heap:", heap)
        elif escolha == "5":
            n = int(input("Quantos valores? "))
            print("N maiores:", obter_n_maiores(heap, n))
        elif escolha == "6":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
