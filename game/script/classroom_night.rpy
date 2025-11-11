label corridors:
    call corridors_A from _calling_scene2
    call choice_corridorsA from _calling_choice1
    $ dest = routes_corridorA.get(_return, "corridors_Ab")
    call expression dest from _calling_scene3

    call corridors_B from _calling_scene4
    call choice_corridorsB from _calling_choice2
    $ dest = routes_corridorB.get(_return, "corridors_Bb")
    call expression dest from _calling_scene5

    call corridors_C from _calling_scene6

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

    "Ela é o suficiente pra me lembrar aonde eu estou, e o que vim fazer aqui. Apesar de ser quase verão, a noite não tem nenhuma intenção de estar menos fria."

    "O som do farfalhar das folhas, as árvores rangendo quando vão de um lado pro outro… tudo isso vem me dando arrepios."

    "Droga, tanto trabalho, mas pra quê? Eu não queria estar aqui, mas não é como se eu tivesse outra opção, não depois do que recebi mais cedo."

    "'Ren, sei que parece meio aleatório, mas você poderia me encontrar na escola hoje à noite? Preciso muito falar com você.'"

    "Eu puxo meu celular do bolso, e encaro essa mensagem da Miya. Isso se tornou um hábito desde que comecei a caminhar até aqui."

    mc "Escola hoje à noite…"

    "'Pode ser por volta das 10? Na nossa sala mesmo. Eu estarei lá'. Eu checo as horas mais uma vez, já são 10:50 da noite."

    with Pause(1.0)

    mc "Aaah…"

    mc "Droga."

    mc "Como eu consegui me atrasar tanto?"

    "Você sabe como, são no máximo vinte minutos daqui até em casa, porém, o tempo inteiro que eu passei pensando sobre isso…"

    "Quando coloquei meu casaco já eram às dez, e quando pisei fora de casa, já tinham se passado mais vinte minutos."

    "Eu suspiro, sentindo novamente o peso daquela mensagem. Eu não sei o que me espera, mas não é como se eu fosse voltar atrás agora."

    "E logo, respiro fundo, eu ainda preciso ficar calmo. O que será que a Miya quer falar comigo? Na verdade, existe mesmo alguma coisa pra falar?"

    "Não estamos trocando tantas mensagens quanto costumávamos, parece que a partir de um momento eu não senti mais a necessidade de falar com ela."

    "Mas, eu não posso negar que sinto falta disso. Eu sinto falta dela."

    "A nossa amizade vem de muito tempo atrás, éramos amigos de infância, e eu sempre acreditei que isso nunca mudaria."

    "Nossas famílias eram próximas, sempre nos viamos em festas, passeios, encontros, e até mesmo nas férias de verão."

    "Eu vivia na casa dela quando criança, e ela na minha, brincávamos juntos o tempo inteiro, e ela sempre foi como uma irmã mais nova pra mim."

    "O seu sorriso, seu jeito de ser, a sua personalidade extrovertida…"

    "Eu observava tudo isso nela, e sentia uma certa satisfação por ter alguém assim ao meu lado."

    "Porém, isso não parece correto."

    "Não é como se tivesse sido tudo por acaso, nossos pais realmente eram muito próximos por conta do negócio da família. Isso já vem de gerações atrás."

    "É por isso que eu nunca senti que a nossa amizade fosse algo natural."

    "Nossas mães são amigas de infância como nós, e nossos pais também se conhecem desde que nasceram."

    "A geração antiga sempre fez questão de manter essa proximidade entre as famílias, e tudo isso ficou muito claro pra mim quando eu crescia."

    "Os momentos que eu passava com a Miya, os passeios, as conversas, tudo isso parecia ser mais uma obrigação do que algo espontâneo."

    "Como se estívessemos fadados a ser amigos, só porque nossas famílias queriam isso. Era mais como um negócio do que qualquer outra coisa."

    "Mas não pra Miya. Ela sempre pareceu genuinamente feliz por estar comigo, mesmo que tudo fosse meio forçado pelos nossos pais, ela queria estar ao meu lado."

    "E eu sempre me senti mal por não conseguir retribuir isso da mesma forma."

    "Eu nunca fui muito bom em fazer amigos, não que eu não fosse sociável, mas sim por um certo desinteresse. Porém, com a Miya, ela foi a única pessoa com quem eu pude me aproximar mais."

    "E é por isso que me incomoda pelo fato de eu pensar assim."

    "Que nossa amizade não é nada além de… um contrato social."

    "…"

    mc "Cacete."

    mc "Por que é que eu tô pensando dessa forma?"

    "Eu não quero ter que pensar assim."

    "Não quero achar que tudo o que eu sinto pela Miya é falso."

    "Mas ao mesmo tempo, não é como se tivéssemos algo verdadeiro."

    "E se nossas famílias não fossem próximas… será que ainda seríamos amigos?"

    "Será que sequer nos conheceríamos?"

    "Será que eu ainda me importaria com ela da mesma forma?"

    "Que independente de tudo, eu ainda iria querer estar ao lado dela?"

    "Não acho que seja justo eu pensar assim."

    "Não é justo pra ela."

    "Nos últimos 14 anos, passamos por tanta coisas juntos, desde quando nos conhecemos ao lado de nossas mães… até essa noite."

    "Sobre tudo o que já vivemos, tudo o que conversamos…"

    "O que eu realmente acho do meu passado com a Miya?"

    return

label choice_corridorsA:   
    menu:
        with menueffect
        "Eu me diverti.":

            return "opt1"
        "Não posso culpá-la.":

            return "opt2"
        "Ela era irritante.":

            return "opt3"

label corridors_Aa:
    # Depois colocar o valor da variável de personalidade/pensamentos que vai atualizar nessa escolha.

    "É claro que eu me diverti."

    "Por mais que eu tente complicar as coisas agora, não tem como apagar o que eu senti naquela época."

    "Eu lembro dos momentos que quase morremos de rir. De todas as coisas bobas que fazíamos, das conversas sem sentido, das tardes que passavam rápido demais."

    "Eram coisas simples… mas eram nossas."

    "Brincávamos de esconde-esconde no quintal, pegávamos vassouras e fingíamos que eram espadas, ela inventava histórias malucas e me fazia participar."

    "E quando chovia, a gente se escondia na varanda e ficava observando a água cair, falando sobre nada e tudo ao mesmo tempo."

    "Não tinha cobrança. Não tinha medo. Só existia o momento."

    "Ninguém precisa de obrigação pra rir daquele jeito."

    "Mesmo quando nossas famílias nos empurravam um pro outro, existiam momentos em que eu esquecia completamente disso. Momentos em que parecia que… ter ela por perto era natural."

    "E eu nunca admiti isso em voz alta."

    "Nem mesmo quando nos tornamos adolescentes, e as coisas começaram a mudar."

    "Talvez eu tenha levado tudo aquilo por garantido. Talvez eu tenha achado que aquilo duraria para sempre."

    "Mas agora, parado nesse corredor escuro, pensando no passado…"

    "Eu percebo que foram alguns dos melhores momentos da minha vida."

    "Nós dois nos importávamos um com o outro, de verdade."

    "E mesmo que eu tenha dúvidas sobre o que tudo isso significa, eu sei que eu me diverti muito."

    "Mesmo assim…"

    return

label corridors_Ab:
    # Depois colocar o valor da variável de personalidade/pensamentos que vai atualizar nessa escolha.

    "Não é como se eu pudesse culpá-la ou a sua família de qualquer coisa disso. Muito menos a mim mesmo."

    "Durante anos, eu tentei acreditar que nossa amizade só existia porque nossas famílias queriam assim. Era mais fácil pensar nisso dessa forma."

    "Se tudo fosse consequência de uma obrigação, então eu não precisaria admitir que eu nunca soube lidar com o que sentia."

    "Era mais confortável culpar as circunstâncias do que encarar a verdade."

    "A Miya sempre foi quem puxava a conversa. Quem perguntava se eu queria sair. Quem tomava iniciativa."

    "Eu só estava lá."

    "Sempre fui eu quem mantive distância."

    "Ela tentava aproximar nossos mundos, enquanto eu fazia questão de manter o meu pequeno, controlado, confortável."

    "Talvez eu tivesse medo de depender demais dela."

    "Ou medo de descobrir que, sem essa amizade… eu não teria mais ninguém."

    "E ainda assim, ela nunca me cobrou. Nunca me jogou na cara o esforço que fez. Nunca me fez sentir que eu estava em dívida."

    "Ela só… continuou sendo ela."

    "E agora que estamos distantes, eu percebo o quanto me escondi atrás de desculpas."

    "Eu dizia que nossa amizade era forçada pra justificar o fato de eu não conseguir corresponder."

    "Mas a verdade é que ela sempre foi sincera comigo."

    "Eu é quem nunca tive coragem de ser sincero com ela."

    "Eu só posso assumir a parte que foi minha."

    "Pelo menos agora eu consigo ver isso claramente."

    "Afinal…"

    return

label corridors_Ac:
    # Depois colocar o valor da variável de personalidade/pensamentos que vai atualizar nessa escolha.

    "Ela era irritante."

    "Ou pelo menos… foi o rótulo que eu dei pra ela."

    "Ela falava demais, ria alto demais, queria fazer amizade com todo mundo. Entrava na minha vida com uma facilidade absurda, como se não precisasse pedir permissão."

    "Ela me forçava a sair da minha zona de conforto. Me arrastava pra lugares que eu não queria ir, me fazia participar de coisas que eu jurava achar estúpidas."

    "E eu odiava isso."

    "Era irritante."

    "Ou… será que eu dizia isso porque era mais fácil do que admitir que eu gostava?"

    "Porque no fim das contas, ela conseguia me fazer sentir vivo."

    "Cada vez que ela puxava meu braço e dizia 'vamos, Ren, confia em mim', eu sentia como se o mundo ficasse mais leve."

    "E isso me assustava."

    "Eu não sei lidar com pessoas que entram na minha vida sem pedir licença."

    "Muito menos com alguém que consegue me enxergar."

    "Então eu dizia que ela era irritante. Porque aceitar o contrário significaria admitir que ela importava."

    "Mas agora, depois de tanto tempo, depois de tantas tentativas de me afastar…"

    "Se eu realmente não gostasse dela, por que eu ainda lembro de tudo com tanta clareza?"

    "Não existe ninguém irritante o bastante para marcar alguém dessa forma."

    "Talvez eu só estivesse me protegendo. Talvez eu ainda esteja."

    "Porque sentir algo sempre foi muito mais assustador do que não sentir nada."

    "E hoje tá sendo um dos piores dias pra sentir isso."

    "No fim…"

    return

label corridors_B:
    "O culpado disso tudo ainda sou eu."

    "Se não fosse por minha causa, eu não estaria aqui agora."

    "Ou melhor… eu não estaria nessa situação."

    "Isso entre eu e a Miya não aconteceu do nada. Foi acontecendo aos poucos."

    "E eu lembro de cada oportunidade que eu tive pra evitar isso."

    "Eu mesmo me afastei dela, eu percebia isso acontecendo."

    "Às vezes eu pensava, 'eu devia mandar uma mensagem pra ela' ou, 'é melhor eu respondê-la rápido', mas nunca o fazia."

    "Até cheguei a pensar se ela se incomodava com isso, mas esse pensamento sumia tão rápido quanto aparecia."

    "Eu deixei que as coisas chegassem a esse ponto, e quando eu me perguntava o porquê, eu não conseguia encontrar uma resposta."

    "Apenas me sentia… vazio. Indiferente. E dava uma desculpa qualquer pra justificar isso."

    "Era algo como, 'não é normal as pessoas se afastarem com o tempo?', o que não deixa de ser verdade."

    if renpy.seen_label("corridors_Aa"):
        "Mesmo tendo me divertido tanto com ela no passado… parecia que aquilo tudo tinha perdido o valor."

        "Como se fosse errado sentir saudade."

        "Como se fosse errado querer reviver algo que já passou."

        "Mas, sendo realista, o que importa mesmo é o presente, e no presente, eu não vejo mais o mundo da mesma forma."

    "Pouco a pouco, você nem percebe quando enviou a última mensagem pra alguém importante."

    "Não percebe quando já é tarde demais pra querer tentar de novo."

    "Mas são essas dúvidas e incertezas que me incomodam tanto."

    "O que isso significa pra mim? O que eu deveria fazer com isso?"

    "Devo tentar me tornar uma pessoa melhor? Como?"

    "Eu queria mesmo ter uma resposta pra essa pergunta, mas quanto mais eu penso, mais embaralhado as coisas ficam."

    "Mesmo sendo amigos de infância, até parece que uma amizade assim não é imune a esses problemas."

    "Somos duas pessoas completamente diferentes agora."

    "Nosso círculo social não é o mesmo, ela é rodeada de gente, sempre saindo na primeira oportunidade. Já eu, no máximo troco duas palavras com um ou dois da minha classe."

    "Não temos mais nada em comum, e eu sempre tentei acreditar que isso não é um problema."

    "Tudo anda mudando tão rápido, que eu não sei se consigo acompanhar mais."

    "Talvez no futuro eu acabe ficando congelado no tempo de alguma forma."

    "Às vezes eu só queria que tudo fosse mais simples."

    "Porém, acredito que isso seja mais um sentimento de nostalgia do que qualquer outra coisa."

    "Ao menos com a Miya, tudo de fato parecia mais simples."

    mc "…"

    "Será que tem mais alguém no mundo passando por algo assim?"

    "Ou será que sou o único nessa noite que tá se sentindo desse jeito?"

    "Eu não sei."

    "Eu não sei de mais nada."

    "Eu pensava que conhecia a Miya, mas agora, eu nem sei mais."

    "Talvez eu nem mesmo me conheço, se eu não consigo me entender, como vou entender outra pessoa?"

    "Pode ser que ela também tenha mudado, e eu só não percebi. Mas a mudança dela foi pra melhor, eu acho."

    "Como ela sempre foi tão extrovertida, eu comecei a pensar que talvez ela tenha conhecido alguém novo, ou até mesmo um grupo de amigos que a faça se sentir mais feliz."

    "Parte disso possa ser mesmo verdade, mas talvez eu esteja apenas tentando me convencer disso."

    "Como se fosse apenas mais uma desculpa pra justificar eu me afastar dela."

    "Eu não sei."

    "Talvez eu esteja com medo de me sentir sozinho."

    "Ou talvez eu só esteja com medo de continuar não sentindo nada."

    "Por que eu cismei tanto com isso?"

    "Eu não sei. Não sei, e não sei."

    "Eu nunca sei de nada quando se trata desses assuntos."

    "Acho que, no fundo…"

    with Pause(1.0)

    "Eu talvez nem precise mais dela, certo?"

    return

label choice_corridorsB:   
    menu:
        with menueffect
        "Não, não é assim que funciona.":

            return "opt1"
        "Eu não consigo me decidir.":

            return "opt2"
        "As coisas são naturalmente assim.":

            return "opt3"

label corridors_Ba:
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

label corridors_Bb:
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

label corridors_Bc:
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

label corridors_C:
    "Pois tudo o que eu fiz até agora, me levou até aqui."

    "acabou por enquanto"

    return