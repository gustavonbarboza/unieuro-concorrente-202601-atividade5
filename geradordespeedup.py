import matplotlib.pyplot as plt

threads = [1, 2, 4, 8, 12]
tempo = [31.47, 23.88, 16.17, 11.61, 10.27]
speedup = [1.0, 1.32, 1.95, 2.71, 3.07]
eficiencia = [1.0, 0.66, 0.49, 0.34, 0.26]

plt.figure(figsize=(10,6))

plt.plot(threads, tempo, marker='o', label='Tempo (s)')
plt.plot(threads, speedup, marker='s', label='Speedup')
plt.plot(threads, eficiencia, marker='^', label='Eficiência')

plt.xlabel('Threads / Processos')
plt.ylabel('Valores')
plt.title('Desempenho vs Número de Threads')
plt.grid(True)
plt.legend()

plt.savefig('grafico_desempenho.png')
plt.show()