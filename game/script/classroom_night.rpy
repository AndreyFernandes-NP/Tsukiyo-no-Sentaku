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

    "Esse vento é o suficiente pra me lembrar aonde eu estou, do que vim fazer aqui. Apesar de ser quase verão, a noite não tem nenhuma intenção de estar menos fria."

    "O som do farfalhar das folhas, as árvores rangendo quando vão de um lado pra o outro… tudo isso vem me dando arrepios."

    "Droga, tanto trabalho, mas pra quê? Eu não queria estar aqui, mas não é como se eu tivesse outra opção, não depois do que recebi mais cedo."

    "'Ren, sei que parece meio aleatório, mas você poderia me encontrar na escola hoje à noite? Preciso muito falar com você.'"

    "Eu pego meu celular mais uma vez, olhando pra mensagem que a Miya me enviou. Isso se tornou um hábito desde que comecei a caminhar até aqui."

    mc "Escola hoje à noite…"

    "'Pode ser por volta das 10? Na nossa sala mesmo. Eu estarei lá'. Eu checo as horas mais uma vez, 10:50 da noite."

    with Pause(1.0)

    mc "Aaah…"

    mc "Droga."

    mc "Por que a lua tinha que estar tão cheia hoje?"

    "Eu suspiro, sentindo novamente o peso daquela mensagem. Eu não sei o que me espera, mas não é como se eu fosse voltar atrás agora."

    "E logo, respiro fundo, eu preciso ficar calmo. O que será que a Miya quer falar comigo? Na verdade, existe mesmo alguma coisa pra falar?"

    "Não estamos trocando tantas mensagens quanto costumávamos, parece que a partir de um momento eu não senti mais a necessidade de falar com ela."

    "Mas eu não posso negar que sinto falta disso. Eu sinto falta dela."

    # Mudança de planos, cortar aqui e lançar tudo abaixo pra cena B, começar a aprofundar o passado do mc e a relação com a miya aqui.
    # mudar a primeira escolha pra ele ponderar mais sobre o passado e a amizade deles, como uma introdução a novel.

    "É o que eu quero acreditar, pelo menos. Nós éramos tão próximos, e agora parece que estamos nos afastando."

    "Eu sei que isso é culpa minha, mas não é normal as pessoas se afastarem?"

    "Pouco a pouco você nem percebe quando enviou a última mensagem pra alguém importante."

    "Não percebe quando já é tarde demais para querer tentar de novo."

    "Mas o que isso tudo significa pra mim? Pra eu simplesmente ser melhor daqui em diante? Como?"

    "Eu queria mesmo ter uma resposta pra essa pergunta, mas quanto mais eu penso, mais embaralhado as coisas ficam."

    "Eu e Miya somos amigos de infância, porém, parece até que mesmo uma amizade assim não é imune a esses problemas."

    "Nosso círculo social é completamente diferente, ela tem várias amigas e está sempre saindo, já eu, conheço apenas uns dois ou três caras da minha turma. Muito menos decido sair com eles pra algum lugar."

    "Nós não temos mais tanta coisa em comum, e eu sempre acreditei que isso não seria um problema."

    "E no fim disso tudo, a maioria tomarão caminhos diferentes, ao ponto de se eu me encontrar com qualquer um deles na rua, seria apenas uma coincidência rara."

    "Dizem que é cada vez mais difícil manter uma amizade hoje em dia, ainda mais depois do ensino médio."

    "Tudo vem acontecendo tão rápido, e eu não sei se estou preparado pra isso."

    "Às vezes eu só queria que as coisas fossem mais simples, sabe?"

    "Porém, acredito que isso seja mais um sentimento de nostalgia do que qualquer outra coisa."

    "Ao menos com a Miya, tudo de fato parecia mais simples."

    mc "…"

    "Será que tem mais alguém no mundo passando por algo parecido comigo?"

    "Ou será que sou o único nessa noite que tá se sentindo assim?"

    "Eu não sei."

    "Não sei de mais nada. Eu pensava que conhecia a Miya, mas agora eu não sei mais."

    "Talvez ela tenha mudado também, que nem eu, e eu não percebi. Mas a mudança dela foi pra melhor, eu acho."

    "Como ela sempre foi tão extrovertida, eu comecei a pensar que talvez ela tenha conhecido alguém novo, ou até mesmo um grupo de amigos que a faça se sentir mais feliz."

    "Parte disso possa ser mesmo verdade, mas talvez eu esteja apenas tentando me convencer disso."

    "Como se fosse apenas uma justificativa para eu mal estar falando com ela ultimamente."

    "Eu não sei."

    "Talvez eu esteja com medo de me sentir sozinho."

    "Ou talvez eu só esteja com medo de não sentir nada."

    "Por que eu cismei tanto com isso?"

    "Eu não sei. Não sei, e não sei."

    "Eu nunca sei de nada quando se trata desses assuntos."

    "Acho que, no fundo…"

    "Eu talvez nem precise mais dela, certo?"

    return

label choice_corridorsA:   
    menu:
        with menueffect
        "Não, não é assim que funciona.":

            return "opt1"
        "Eu não consigo me decidir.":

            return "opt2"
        "As coisas são naturalmente assim.":

            return "opt3"

label corridors_Aa:
    # Depois colocar o valor da variável de personalidade/pensamentos que vai atualizar nessa escolha.

    "Não. O que eu tava pensando com isso?"    

    "Eu não posso simplesmente desistir assim do nada."

    "Afinal, a Miya ainda é minha amiga de infância, isso é algo que nunca vai mudar."

    "Eu não posso deixar que essa simples distância acabe com tudo o que a gente já viveu."

    "As memórias que a gente tem juntos são muito importantes pra mim. E eu sei que elas são pra você também."

    "Se eu não tentar, eu nunca vou saber o que poderia ter acontecido. E eu não quero viver com esse arrependimento."

    "Muito menos quero que você viva com esse arrependimento."

    "Eu respiro fundo, tentando afastar esses pensamentos negativos."

    "Eu não posso deixar que isso me consuma."

    "Se eu quiser que as coisas voltem a ser como antes, vou ter que me esforçar pra isso."

    "Eu vim até aqui porque preciso falar com ela, e é isso que eu vou fazer."

    return

label corridors_Ab:
    # Depois colocar o valor da variável de personalidade/pensamentos que vai atualizar nessa escolha.

    "Não é fácil pensar numa resposta."

    "Eu não sei o que eu realmente quero."

    "Eu só sei que eu não quero me sentir assim."

    "Eu não quero me sentir tão perdido."

    "Sermos amigos de infância não é algo que se perde da noite pro dia, mas eu não sei se isso é o suficiente."

    "Independente do que eu faça, eu não sei se as coisas vão voltar a ser como antes."

    "Eu não sei se nem quero que elas voltem a ser."

    "Uma coisa que eu detesto são promessas vazias, e eu não quero fazer uma promessa dessas pra Miya."

    "Eu não quero decepcioná-la, mas eu também não quero me decepcionar."

    "Eu adoraria continuar sendo amigo dela, mas será que ela ainda gostaria disso?"

    "Será que eu ainda sou importante pra ela?"

    "Não, eu sei que sou, é por isso que estou aqui, mas, ao mesmo tempo, não sei se conseguiria cumprir o que ela espera de mim."

    "Mas que merda… pode não parecer Miya, mas eu ainda prezo muito pela nossa amizade."

    "Só não sei como agir, como pôr isso em palavras."

    "Eu não sei o que eu quero, e eu não sei o que você quer."

    "Eu apenas não sei, e por causa disso, que eu só vou seguindo o fluxo das coisas. O que for, for. O que tiver que ser, será."

    "Mas por que isso me incomoda tanto? É como se não fosse eu que estivesse no controle."

    "Na verdade, o que é ter controle?"

    "Querer andar todo dia pra outro lado, mas acabar indo parar sempre no mesmo."

    "Nesse caso, o destino mesmo importa?"

    "Importa, ou eu só tô me iludindo?"

    "Talvez eu só precise parar de pensar tanto nessas coisas."

    "Se eu estou aqui, é porque eu quero estar."

    "E se eu quero estar aqui, é porque eu quero falar com a Miya."

    "E se eu quero falar com você, Miya, é porque eu ainda me importo contigo."

    "Então só hoje, apenas por hoje, eu quero estar no controle."
    
    return

label corridors_Ac:
    # Depois colocar o valor da variável de personalidade/pensamentos que vai atualizar nessa escolha.

    "Eu não sei se isso é algo que eu possa controlar."

    "E eu não sei se isso é algo que eu queira controlar."

    "Eu não sei se eu quero que as coisas sejam diferentes."

    "Somos amigos de infância, mas não somos mais crianças."

    "Eu não sei se eu quero que a gente volte a ser tão próximos quanto antes."

    "Não é como se estivéssemos preso por um laço inquebrável ou algo assim."

    "Eu não sei se eu quero isso…"

    "Mas eu também não sei se eu quero o contrário."

    "Estar longe de você, Miya, é algo que me incomoda."

    "Mas não seria estranho demais de repente, depois de tanto tempo, voltarmos a ser próximos assim?"

    "Talvez você pense de outra forma, mas eu não sei. Talvez esse incômodo seja só meu."

    "Talvez você queira mesmo se afastar."

    "Ou talvez queira estar tão próxima quanto antes."

    "Droga, eu não sei e não aguento mais não saber."

    "Por que tudo tem que ser tão complicado?"

    "Por que eu não posso simplesmente aceitar as coisas como elas são?"

    "Tudo estava indo bem, eu estava seguindo minha vida normalmente, e agora, isso?"

    "É só uma mensagem, mas cacete, por que isso tá mexendo tanto comigo?"

    "Ou será que eu só tô me iludindo?"

    "Talvez eu quisesse falar tanto sobre isso quanto você, que só a ideia de te ver já me deixa assim."

    "É como se fosse errado eu não tentar, errado em te deixar."

    "E por isso que tudo tá tão confuso. Eu não sei nem mais o que eu quero de verdade."

    "Mas eu sei que eu quero te ver. E é por isso que eu vou tentar, mesmo que eu não saiba o que vai acontecer depois."

    "Ao menos por uma última vez, Miya."

    return

label corridors_B:
    "acabou aqui por enquanto."

    return