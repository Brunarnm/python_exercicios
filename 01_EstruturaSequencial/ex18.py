#18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanhoArquivo = int(input("Informe o tamanho do arquivo (em MB): \n"))
velocidadeInternet = int(input("Informe a velocidade da internet (em Mbps): \n"))

tempoDownload = tamanhoArquivo / velocidadeInternet / 60

print("O download do arquivo levará %.2f minutos." %(tempoDownload))