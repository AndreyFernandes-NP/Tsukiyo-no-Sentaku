label corridors:
    call corridors_A from _calling_scene2
    call choice_corridorsA from _calling_choice1
    $ dest = routes_corridorA.get(_return, "corridors_Ab")
    call expression dest from _calling_scene3

    call corridors_B from _calling_scene4

    return

label corridors_A:
    window hide None

    scene bg school_corridor
    with scenechange

    $ amb_volume(0.3, 0.05)
    $ amb_play(ambience_corridor_wind, fadein=1.0)

    $ ambience_sfx_cycle.start(start_after_random=True)

    window show

    "…"

    "Quem eu estou querendo enganar."

    "Desde que sai de casa, não paro de pensar se essa foi mesmo a melhor escolha."

    "A brisa que bate nas minhas costas me dá uma leve sensação de frio, mas não é só isso."

    "Esse vento é o suficiente para me lembrar aonde eu estou, do que vim fazer aqui. Apesar de ser quase verão, a noite não tem nenhuma intenção de estar menos fria."

    "O som do farfalhar das folhas, as árvores rangendo quando vão de um lado para o outro… tudo isso vem me dando arrepios."

    "Droga, tanto trabalho, mas pra quê? Eu não queria estar aqui, mas não é como se eu tivesse outra opção, não depois do que recebi mais cedo."

    "'Ren, sei que parece meio aleatório, mas você pode me encontrar na escola hoje à noite? Preciso muito falar com você.'"

    "Eu pego meu celular mais uma vez, olhando pra mensagem que a Miya me enviou. Isso se tornou um hábito desde que comecei a caminhar até aqui."

    mc "Escola hoje à noite..."

    "'Pode ser por volta das 10? Na nossa sala mesmo. Eu estarei lá'. Eu checo as horas mais uma vez, 10:50 PM."

    with Pause(1.0)

    mc "Aaah…"

    mc "Droga."

    mc "Por que a lua tinha que estar tão cheia hoje?"

    "Eu suspiro, sentindo novamente o peso daquela mensagem. Eu não sei o que me espera, mas não é como se eu fosse voltar atrás agora."

    "E logo, respiro fundo, eu preciso ficar calmo. O que será que a Miya quer falar comigo? Na verdade, existe mesmo alguma coisa pra falar?"

    "Não estamos trocando tantas mensagens quanto costumávamos, parece que a partir de um momento eu não senti mais a necessidade de falar com ela."

    "Mas eu não posso negar que sinto falta disso. Eu sinto falta dela."

    "É o que eu quero acreditar, pelo menos. Nós éramos tão próximos, e agora parece que estamos nos afastando."

    "Eu sei que isso é culpa minha, mas não é normal as pessoas se afastarem?"

    "Pouco a pouco você nem percebe quando enviou a última mensagem para alguém importante."

    "Não percebe quando já é tarde demais para querer tentar de novo."

    "Mas o que isso tudo significa pra mim? Pra eu tentar melhor outra vez?"

    "Eu queria mesmo ter uma resposta pra essa pergunta, mas quanto mais eu penso, mais embaralhado as coisas ficam."

    "Eu e Miya somos amigos de infância, porém, parece até que mesmo uma amizade assim não é imune a esses problemas."

    "Nosso círculo social é completamente diferente, ela tem várias amigas, está sempre saindo, já eu, conheço apenas uns dois ou três caras da minha turma. Muito menos decido sair com eles pra algum lugar."

    "Nós não temos mais tanta coisa em comum, e eu sempre acreditei que isso não seria um problema."

    "E no fim disso tudo, a maioria tomarão caminhos diferentes, ao ponto de se eu me encontrar com qualquer um deles na rua, seria apenas uma coincidência rara."

    "Hoje em dia é tão difícil manter uma amizade além do ensino médio."

    "Quando eu chegar na faculdade, vou conhecer novas pessoas, fazer novos amigos, e talvez até lá…"

label choice_corridorsA:
    menu:
        "Eu acabe nem precisando mais dela, não é?"
        "Não, isso não está certo.":

            return "opt1"
        "Queria que a resposta fosse simples assim.":

            return "opt2"
        "As coisas são naturalmente desse jeito.":

            return "opt3"

label corridors_Aa:

label corridors_Ab:

label corridors_Ac:

label corridors_B:
    return