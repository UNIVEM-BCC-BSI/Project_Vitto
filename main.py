from random import randint
pergunta = 0

objetos = [
      
    #   Pergunta 1

    ['Escolha a opção que melhor traduz, respectivamente, os seguintes objetos:\nlivro, relógio, porta e sapato.',
    # resposta
    'A',
    'a) book, clock, door, shoe',
    'b) book, time, door, shirt',
    'c) shoe, door, clock, book',
    'd) shoe, shirt, clock, door'
    ]
]

frutas = [
      
    #   Pergunta 1

    ['Quais os nomes dessas frutas?\nApple, Lemon, Orange, Watermelon and Pear',
     #  resposta certa
     'C',
     #  opções
     'a) Limão, Melancia, Pera, Laranja e Maçã',
     'b) Melancia, Pera, Limão, Maçã e Laranja',
     'c) Maçã, Limão, Laranja, Melancia e Pera',
     'd) Maçã, Limão, Melancia, Laranja e Pera',
     ],
]

animais = [
      
    #   Pergunta 1

    ['Quais os nomes desses animais?\nWolf, Eagle, Snake, Bear, Whale',
    # resposta
     'B',
     'a) Lobo, Cobra, Urso, Baleia, Águia',
     'b) Lobo, Águia, Cobra, Urso, Baleia',
     'c) Águia, Cobra, Lobo, Baleia, Urso',
     'd) Baleia, Águia, Cobra, Lobo, Urso'
     ],

    #   Pergunta 2

     ['Para essa situação Vitto foi obrigado a desvendar qual seria o nome desse animal em inglês, diante disso o animal escolhido foi o cavalo: ',
      'A',
      'a) Horse',
      'b) Mustang',
      'c) Cavallo',
      'd) Yegua'
      ],

    #   Pergunta 3

      ['Dessa vez Vitto foi desafiado a desvendar qual o nome, desse animal temido por ele, em inglês:',
       'C',
       'a) Stone',
       'b) Hermes',
       'c) Snake',
       'd) Medusa'
       ]
]

gramatica = [
      
    #   Pergunta 1

    ['Preencha a lacuna:\n.... children went to Disneyland',
     #  resposta certa
     'C',
    #  opções
     'a) Them',
     'b) Ours',
     'c) Their',
     'd) Us'
     ],

    #   Pergunta 2

    ['Preencha a lacuna:\nDo you see .... boys over there?',
     #  resposta certa
     'C',
     #  opções
     'a) this',
     'b) these',
     'c) those',
     'd) that'
     ],

    #   Pergunta 3

     ['Para que possamos testar o conhecimento de um desafio de gramática foi proposto. Qual a forma correta de se utilizar o Verbo “to be”:',
      'A',
      'a) She is beautiful.',
      'b) He are handsome.',
      'c) She to are amazing.',
      'd) We to be crazy.'
      ]
]

numeros = [
      
    #    Pergunta 1

    ['Vitto precisa ajustar o horário de um relógio para 8 horas. Ajude-o a encontrar a opção que melhor se encaixa nessa tarefa:',
    # resposta
    'D',
    "a) three o'clock",
    "b) one o'clock",
    "c) six o'clock",
    "d) eight o'clock"
    ],

    #   Pergunta 2

    ['Ajude Vitto a contar quantas letras existem em seu nome, escolha uma das alternativas:',
    # resposta
    'C',
    'a) two',
    'b) seven',
    'c) five',
    'd) nine'
    ],

    #   Pergunta 3

    ['Ajude Vitto a escolher a alternativa que melhor traduz o número 13 para o inglês:',
    # resposta
        'A',
        'a) thirteen',
        'b) thirty',
        'c) ten three',
        'd) three ten'
        ]
]

cores = [
      
    #   Pergunta 1

    ['Vitto chegou em um sala com duas portas, uma vermelha e uma azul. Porém a chave que Vitto recebeu está escrito vermelho. Qual porta ele deverá abrir?',
    # resposta
      'D',
      'a) Yellow', 
      'b) Blue', 
      'c) Purple', 
      'd) Red' 
      ],

    #   Pergunta 2

    ['Vitto pega sua camiseta favorita Branca, e quer usar um sapato da mesma cor que sua camisa, ele pega o sapato da cor:',
    # resposta
      'A',
      'a) White',
      'b) Black',
      'c) Brown',
      'd) Purple'
     ],

    #   Pergunta 3

    ['Ele é indicado a seguir as placas green para encontrar o caminho da saida, porém aparece outras três placas, qual ele deve seguir:',
    # resposta
      'C',
      'a) Amarelo',
      'b) Vermelho',
      'c) Verde',
      'd) Azul'
     ],

    #   Pergunta 4

    ['O cientista que colocou o chip da cabeça do Vitto recomenda que todas as segundas ele tome a pílula amarelas e nas quintas a pílulas roxas. Quais cores de pílulas, respectivamente, Vitto deve tomar?',
    # resposta
      'C',
      'a) Purple - Yellow',
      'b) Blue - Green',
      'c) Yellow - Purple',
      'd) Balck - Orange'
     ],

]

frases = [
      
    #   Pergunta 1

    ['Vitto então se depara com uma porta da qual é necessário traduzir uma frase aleatória para que seja aberta:\n“Os pássaros voam para o Oeste e os cavalos correm para o leste”.',
     #  resposta certa
     'A',
     #  opções
     'a) Birds fly west and horses run east',
     'b) The birds fly for west and horses run for the east',
     'c) Birds fly oest and horses run lest',
     'd) Birds fly to west so the horses run to east',
     ],
]

def inicia():
    quiz = input('Qual problema deseja resolver primeiro?\nA) Objetos B) Frutas C) Animais D) Gramática E) Números F) Cores G) Frases\nSua escolha: ').upper()
    if quiz == 'A':
          return objetos
    elif quiz == 'B':
          return frutas
    elif quiz == 'C':
          return animais
    elif quiz == 'D':
          return gramatica
    elif quiz == 'E':
          return numeros
    elif quiz == 'F':
          return cores
    elif quiz == 'G':
          return frases

def faz_Pergunta(lista):
        global pergunta
        pergunta = randint(0, (len(escolha)-1))
        print(lista[pergunta][0])

        for i in range(2,6):
              print(lista[pergunta][i])

        return input(f'\nSua resposta: ').upper()

def verifica_Resposta(escolha, resposta):

    if resposta == escolha[pergunta][1]:
          print('Resposta correta.')
    else:
          print('Resposta errada!')
    
escolha = inicia()
resposta = faz_Pergunta(escolha)
resultado = verifica_Resposta(escolha, resposta)