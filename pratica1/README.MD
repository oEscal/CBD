#  Exercício 1.2
```bash
$ cat initials4redis.txt | redis-cli --pipe        # comando shell para fazer a inserção massiva
```


# Exercício 1.3 a
- Comando:
```bash
$ python forum.py
```


# Exercício 1.3 b
- Comando:
```bash
$ python simple_post.py [-h] [-a] [-u] [-k]
```


# Exercício 1.4
- Comando:
```bash
$ python autocomplete.py [-h] (-n | -o) [-i] [-f]
```


# Exercício 1.5
- Neste exercício, usei um esquima publish/subscribe para construir o sistema de mansagens pedido, sendo que não usei o pub/sub default do redis. Sendo assim, a arquitetura que usei foi:
  - user:names → todos os nomes de utilizador na plataforma
  - user:\<name>:subscriptions → set onde são armazenados todos os nomes dos utilizadores aos quais o utilizador definido por \<name> é subscrito
  - user:\<name>:messages → set onde são guardadas todas as mensagens que o utilizador definido pelo nome \<name> enviou
- Para correr o programa em python que faz a gestão deste *chat* basta correr o comando:
```bash
$ python message_system [-h] [-n] [-a] [-s] [-m] [-w] [-g] [-l]
```