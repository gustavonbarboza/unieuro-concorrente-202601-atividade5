import matplotlib.pyplot as plt

threads = [1, 2, 4, 8, 12]
tempo = [31.47, 23.88, 16.17, 11.61, 10.27]

plt.figure(figsize=(8,5))

plt.plot(threads, tempo, marker='o', color='blue')

plt.xlabel('Nº de Threads/Processos')
plt.ylabel('Tempo de Execução (s)')
plt.title('Tempo de Execução vs Número de Threads')
plt.grid(True)

plt.savefig('grafico_tempo_execucao.png')
plt.show()