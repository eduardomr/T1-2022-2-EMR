# Trabalho 1 - 2022-2

## Como utilizar

Para se utilizar o sistema deve-se configrar os arquivos "configuracao_sala_01.json" e "configuracao_sala_02.json" com as informações das salas que se deseja utilizar. Após isso, deve-se executar os servidores distribuidos em suas respectivas placas raspberry pi. Para isso, deve-se executar o comando:

```bash 
python3 servidor_distribuido.py
```
Em seguida deve-se escolher a sala a configuração que deseja utilizar em cada servidor distribuido, 1 ou 2

Após isso, deve-se executar o servidor central, que é responsável por gerenciar as salas e os servidores distribuidos. Para isso, deve-se executar o comando:

```bash
python3 servidor_central.py
```
