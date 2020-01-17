
# Exercício 4.1
## Instalação
 - Fazer download do ficheiro da [página](https://neo4j.com/download/)
 - Executar o ficheiro da seguinte forma:
 ```bash
 $ chmod +x neo4j-desktop-offline-1.2.3-x86_64.AppImage
 $ ./neo4j-desktop-offline-1.2.3-x86_64.AppImage    
 ```

## Criação dum novo projeto e nova base de dados
 - Bastante *straight forward* usando a interface gráfica aberta usando os comandos descritos anteriormente

# Exercício 4.2
## Primeiros passos
```cypher
$ // correr o tutorial
$ :play movie-graph
$ match (n) return n            // retorna todos os nós do grafo
$ match (n)
 > with count(n) as num_vertices
 > match (a)-[e]->(b)                   // ver todos os nós (a) que se ligam a outros nós (b) através de ligações (e)
 > return num_vertices, count(e) as num_edges
$ match (n)
 > return labels(n) as labels, keys(n) as keys, count(*) as total
 > order by total desc;
```

## Queries pedidas
 - no ficheiro `ex2.cyp`


# Exercício 4.3
 - Script em python para criar os ficheiros `csv` que modelam devidamente a bd: `model_3.py`
 - Ficheiro com as queries necessárias para criar a bd e com as queries pedidas: `ex3.cpy`

# Exercício 4.4
 - Script em python com a ligação à bd, a criação da bd e a execução das queries: `ex4.py`
   - Este script também armazena automáticamente os resultados das queries no ficheiro `CBD_L44c_output.txt`
   - Como executar o script:
   ```bash
   $ virtualenv venv                            # criação dum ambiente virtual para o efeito
   $ source vent/bin/activate                   # execução do ambiente virtual
   $ pip install -r requirements.txt            # instalação das bibliotecas necessárias à execução do script
   $ python ex4.py -i                           # inserção dos dados na bd
   $ python ex4.py -q                           # execução das queries e consequente armazenamento dos resultados no ficheiro pedido 
   ```
 - No diretório `ex4_data` encontram-se os ficheiros `csv` com os dados necessários para a criação da base de dados, o ficheiro `import.cyp`, com as instruções de como criar a base de dados a partir dos referidos ficheiros (posteriormente, este ficheiro é carregado pelo script em python acima referido para a criação da base de dados) e o ficheiro `datamodel.png` com o esquema da modelação da base de dados
