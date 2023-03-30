# Jogo da Velha Python  

## Objetivo  

O objetivo deste projeto é fazer um jogo da velha tradicional na linguagem **Python**.

## Funcionalidades  

O jogo inicia solicitando ao usuário para escolher 'X' ou 'O'. Após a entrada do usuário o jogo inicia.  
Para inserir o 'X' ou o 'O', o usuário deve colocar a coluna e a linha correspondente.  

![Inicio do jogo da velha](https://github.com/pauloszuparits/Imagens/blob/485c07736b6d8a570fb0165b2c25b14832416b6b/imgJogoDaVelhaPython/InicioDoGameJogoDaVelha.png)

Após o terminar o jogo, o usuário pode jogar novamente ou escolher sair do jogo

![Término do jogo da velha](https://github.com/pauloszuparits/Imagens/blob/86970c69da322a79cf819e4c399ceca5aa890c98/imgJogoDaVelhaPython/FinalDoGameJogoDaVelha.png)  

## Documentação técnica  

O programa é dividido em 6 funcoes.

#### Funcao imprimir_jogo  

A funcao imprimir_jogo recebe uma uma lista matriz, e ela é responsavel por imprimir essa matriz de forma que o será impressa em forma de grade como o jogo da velha.  

![Funcao imprimir_jogo]()  

#### Funcao jogada  

A funcao jogada recebe 2 matrizes, e uma escolha, caso a escolha seja 1, o simbolo usado será o X, se não, o simbolo será 0. O programa inicia um laço que só sairia no momento que o usuário digitar uma coluna e linha válida e que nao esteja ocupada. Saindo do laço, é inserido nas matrizes o simbolo e é retornado as matrizes.  

![Funcao jogada]()  

#### Funcao check

A funcao check recebe uma lista. 9 flags são iniciadas com 0 e começa uma sequencia de estruturas condicionais para verificar se algum dos jogadores ganhou e retorna uma lista com essas flags.

![Funcao check]()  

#### Funcao comecar_jogo
A funcao comecar_jogo recebe um contador, 3 flags, 2 matrizes e uma lista de flags. Essa funcao é resposável por comecar o jogo. A funcao inicia perguntando ao usuário se o primeiro player ficará com X ou 0. Após isso, comeca um laço que irá chamar a função imprimir_jogo para imprimir em forma de grade ao usuário. Após isso, é chamada a função jogada e após isso a função check. Caso a função check retorne um ganhador, ou um empate, o laço termina e chama a função jogar_novamente. 

![Funcao comecar_jogo1]()
![Funcao comecar_jogo2]()  

#### Funcao jogar_novamente  
A funcao jogar novamente tem o objetivo de reiniciar o jogo com todas as variaveis zeradas. Caso o usuário escolha nao continuar o jogo, o programa para.  

![Funcao jogar_novamente]()
