label corridors:
    call iscene("corridors_A") from _calling_scene2
    call choice_corridorsA from _calling_choice1
    $ dest = routes_corridorA.get(_return, "corridors_Ab")
    call iscene(dest) from _calling_scene3

    call iscene("corridors_B") from _calling_scene4
    call choice_corridorsB from _calling_choice2
    $ dest = routes_corridorB.get(_return, "corridors_Bb")
    call iscene(dest) from _calling_scene5

    call iscene("corridors_C") from _calling_scene6
    call choice_corridorsC from _calling_choice3
    $ dest = routes_corridorC.get(_return, "corridors_Cb")
    call iscene(dest) from _calling_scene7

    call iscene("corridors_D") from _calling_scene8
    jump end_of_build

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

    "Você sabe como, são no máximo vinte minutos de casa até aqui, porém, o tempo inteiro que eu passei pensando sobre isso…"

    "Quando coloquei meu casaco já eram às dez, e quando pisei fora de casa já tinham se passado mais vinte."

    "Eu suspiro, sentindo novamente o peso daquela mensagem. Eu não sei o que me espera, mas não é como se eu fosse voltar atrás agora."

    "E logo, respiro fundo, eu ainda preciso ficar calmo. O que será que a Miya quer falar comigo? Na verdade, existe mesmo alguma coisa pra falar?"

    "Não estamos trocando tantas mensagens quanto costumávamos, parece que a partir de um momento eu não senti mais a necessidade de falar com ela."

    "Mas, eu não posso negar que sinto falta disso. Eu sinto falta dela."

    "A nossa amizade vem de muito tempo atrás, éramos amigos de infância, e eu sempre acreditei que isso nunca mudaria."

    "Nossas famílias eram próximas, sempre nos viamos em festas, passeios, encontros, e até mesmo nas férias de verão."

    "Eu vivia na casa dela quando criança, e ela na minha, brincávamos juntos o tempo inteiro, e ela sempre foi como uma irmã mais nova pra mim."

    "O seu sorriso, seu jeito de ser, a sua personalidade extrovertida…"

    "Eu observava tudo isso nela, e sentia uma certa satisfação por ter alguém assim ao meu lado."

    "Porém, isso não era correto."

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

    "Nos últimos 15 anos, passamos por tanta coisas juntos, desde quando nos conhecemos ao lado de nossas mães… até essa noite."

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
    $ mc_personality.append("He carries some nostalgia for the carefree days of his childhood with Miya.")

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
    $ mc_personality.append("He feels guilty for not reciprocating Miya's efforts in their friendship.")

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
    $ mc_personality.append("He struggles to admit his true feelings for Miya, masking them with irritation.")

    "Ela era irritante."

    "Pelo menos… foi o rótulo que eu dei pra ela."

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

    "E eu lembro de cada oportunidade que tive pra evitar isso."

    "Eu mesmo me afastei dela, e mesmo percebendo isso, não fiz nada."

    "Às vezes eu pensava, 'eu devia mandar uma mensagem pra ela' ou, 'é melhor eu respondê-la rápido', mas nunca o fazia."

    "Até cheguei a pensar se ela se incomodava com isso, mas esse pensamento sumia tão rápido quanto aparecia."

    "Eu deixei que as coisas chegassem a esse ponto, e quando eu me perguntava o porquê, eu não conseguia encontrar uma resposta."

    "Apenas me sentia… vazio. Indiferente. E dava uma desculpa qualquer pra justificar isso."

    "Era algo como, 'não é normal as pessoas se afastarem com o tempo?', o que não deixa de ser verdade."

    if seen_label("corridors_Aa"):
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

    "Talvez eu nem mesmo me conheça, se eu não consigo me entender, como diabos entenderei outra pessoa?"

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
    $ mc_personality.append("He rejects the idea of giving up on their friendship and wants to fight to keep Miya in his life.")

    "Não. O que eu tava pensando com isso?"    

    "Eu não posso simplesmente desistir assim do nada."

    "Afinal, a Miya ainda é minha amiga de infância, isso é algo que nunca vai mudar."

    "Eu não posso deixar que essa simples distância acabe com tudo o que a gente já viveu."

    "As memórias que temos juntos são muito importantes pra mim. E eu sei que elas são pra você também."

    "Se eu não tentar, eu nunca vou saber o que poderia ter acontecido. E eu não quero viver com esse arrependimento."

    "Muito menos quero que você viva com esse arrependimento."

    "Eu respiro fundo, tentando afastar esses pensamentos negativos."

    "Eu não posso deixar que isso me consuma."

    "Se eu quiser que as coisas voltem a ser como antes, vou ter que me esforçar pra isso."

    "Eu vim até aqui porque preciso falar com ela, e é isso que eu vou fazer."

    return

label corridors_Bb:
    $ mc_personality.append("He feels torn about his feelings towards Miya and is unsure of what to do.")

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
    $ mc_personality.append("He tries to rationalize his feelings and the situation, but remains uncertain and conflicted.")

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

    "Tudo o que eu venho pensando, tudo o que eu venho sentindo… parece tão pequeno comparado a esse momento."

    "E é por isso que tudo tá tão estranho. Eu estou preso entre o passado e o futuro, e agora… tudo se resume a um passo."

    "Mas eu não sei se consigo dar esse passo, ou se eu quero dar."

    "Por que tudo tem que ser resumido à isso?"
    
    "Na verdade, por que eu tenho que definir tudo agora?"

    "Por que {i}tudo{/i} não sai da minha cabeça?"

    "Um único passo, e tudo muda."

    "Um único passo, e me aproximo mais de você."

    if seen_label("corridors_Bc"):
        "Ou talvez me afaste de vez."

        "E eu continue sozinho, sem saber o que fazer."

    else:
        "E também do que vou sentir depois disso."

    "Eu não sei como vai ser quando eu abrir essa porta. Ainda não entendi porque eu não giro essa maçaneta."

    "Mas, tudo quando envolve o seu nome nunca sai como o planejado. Sempre foi assim com você."

    "Eu só sei que, seja o que for, eu talvez finalmente consiga entender alguma coisa."

    "Talvez eu consiga entender o que eu realmente sinto por você."

    "Talvez eu consiga entender o que eu realmente sinto por mim mesmo."

    "Mas dizem que algumas coisas não precisam ser entendidas."

    "Que é necessário apenas senti-las. E eu acho que chegou a hora de eu fazer isso, se não, pelo menos tentar."

    "Relacionamentos nunca foram meu forte, e eu sempre evitei me envolver demais."

    "Querendo ou não, acabei me envolvendo em um de qualquer forma. Vai ver é por isso que eu nunca fui tão popular com as pessoas."

    "Eu nunca vi isso como um problema pra ser sincero, mas parando pra pensar agora…"

    "O fato de eu não saber lidar com isso é um dos principais motivos pra eu estar aqui agora."

    "Na verdade, seria tão engraçado eu abrir essa porta e descobrir que você não tá nem aqui."

    "Tantas coisas poderiam ter acontecido diferente pra que isso fosse possível, e mesmo assim, eu tô aqui no meio da escola às 11 da noite, só pra te ver."

    "Eu não sei o que te levou a querer me chamar aqui, mas o que me deixa mais incomodado é eu entender o porquê de você ter escolhido assim."

    "Acho que agora é tarde demais pra sentir vergonha."

    "Sua estratégia funcionou, mas não quer dizer que eu tô feliz por isso, só não tenho escolha a não ser isso agora."

    "Não importa o que eu pense, eu não consigo encontrar uma razão pra dar meia volta e voltar pra casa."

    "E eu queria poder encontrar uma razão, qualquer desculpa, só pra poder não encarar isso."

    "Mas fugir de você é bem difícil, é algo que sempre deixou claro comigo, seja em brincadeiras no passado, ou quando você me empurrava pra encontros."

    "Mesmo assim, eu não consigo evitar de pensar no que poderia ter sido diferente."

    "Não que isso vá mudar alguma coisa, não é como se eu pudesse voltar no tempo."

    "E mesmo que eu pudesse, não sei se teria coragem de fazer isso."

    "Porque no fim das contas, tudo o que aconteceu…"

    "Me trouxe até aqui."

    "Seja isso bom ou ruim, eu não sei."

    "Mas pelo menos, seja lá o que for acontecer depois disso…"

    "Nós não seremos mais os mesmos."

    "Talvez esse seja o grande elefante no meio da sala que me recuso enxergar. Eu queria que tudo se mantivesse igual, mas tenho quase certeza que não vai."

    "Eu não sou alguém de tomar riscos, já você decidiu apostar tudo nessa noite. E o pior de tudo é que se eu não quiser perder, também preciso dar {i}all-in{/i} como você."

    "Por quanto tempo será que você planejou isso? Na verdade, houve sequer algum planejamento?"

    "E se eu não fosse aparecer hoje, o que você faria? Se você estivesse ai atrás dessa porta, esperando por mim, por quanto tempo você aguentaria?"

    "Você faz as coisas de maneira impulsiva, sem pensar nas consequências na maioria das vezes, porém faz, enquanto eu atraso tudo do meu lado."

    "Talvez eu precise mesmo aprender algo contigo, Miya, de parar de pensar tanto nas coisas."

    "Mas ao mesmo tempo… é isso que me define de alguma forma. Mudar isso seria perder parte de mim, além de que seria muito difícil."

    "É como se fosse um hábito lapidado por anos e anos, não necessariamente um hábito bom, mas que agora faz parte de mim."

    "Porém, é curioso ver como você sempre esteve nas minhas experiências mais extremas."

    "Minha vida podia ser monótona, previsível, mas era satisfatória, até você aparecer. Tanto na nossa infância, adolescência, quanto agora."

    "Tipo, porra, eu pulei um muro de dois metros só pra poder te ver."

    "Eu invandi a escola à noite, por sorte ninguém mais tá aqui, nem segurança, nem zelador, nada."

    "Não me impressionaria se eu encontrar algum casal escondido por aí, transando atrás de uma árvore ou sei lá."

    "Talvez até eu encontre algum fantasma, já que agora descobri que a escola me dá arrepios à noite."

    "Eu nunca teria feito nada dessas coisas se não fosse por você."

    if not seen_label("corridors_Bc"):
        "E mesmo sendo difícil admitir, eu me senti mais vivo hoje do que em muitos outros dias previsíveis que venho tendo."

        "Não é algo que eu queira sentir sempre, mas… é bom saber que eu ainda sou capaz disso."

    "Talvez o problema é que eu seja muito incerto sobre tudo."

    "Eu não sei o que eu quero, eu não sei o que eu sinto, assim como não sei o que eu espero."

    "No final das contas, eu não sei nem o que eu sou."

    "Por isso, se for pra ser sincero comigo mesmo…"

    return

label choice_corridorsC:   
    menu:
        with menueffect
        "Eu vou até o fim.":

            return "opt1"
        "Só vou descobrir tentando.":

            return "opt2"
        "Talvez nada mude.":

            return "opt3"

label corridors_Ca:
    $ mc_personality.append("He's determined to face his feelings and the situation head-on, regardless of the outcome.")

    "Eu já pensei demais. Já duvidei demais. Já tentei me convencer do contrário tantas vezes…"

    "Mas, se existe um momento pra parar de fugir, é esse."

    "Talvez eu esteja errado."
    
    "Talvez eu esteja me enganando."

    "Talvez eu nem consiga dizer o que realmente sinto quando olhar pra você."

    "Mas não importa."

    "Nada disso importa mais. O que importa é que eu estou aqui, e eu vou até o fim."

    "Eu não vou mais me esconder, eu cheguei até aqui porque parte de mim quer, precisa entender o que ainda restou entre nós."

    "Eu continuarei nessa corda bamba e vou atravessá-la até o outro lado."

    "O lado em que você está, e o que você me espera."

    "E se eu fraquejar num momento desses, nunca vou me perdoar. Eu não quero viver com mais um arrependimento."

    "Eu poderia até não ligar pra isso no presente, mas eu sei que no futuro vou me culpar por não ter tentando ir em frente."

    "Assim como eu me culpo por coisas que eu não fiz no passado de vez em quando."

    "De tantas oportunidades que eu deixei passar, de tantos momentos que eu não aproveitei, que eu me senti incerto sobre tudo."

    "Pelo menos, agora eu quero tentar."
    
    "Quero começar a viver minha vida de uma forma parecida com a sua."

    if seen_label("corridors_Aa"):
        "Afinal, eu sempre me diverti muito mais quando estive ao seu lado, e eu ainda continuo."

        "Quero que mesmo depois do ensino médio, eu ainda possa sair com você de vez em quando."

        "Te contar sobre as coisas novas que ando vivendo, enquanto te escuto falar sobre as suas."

        "Quero continuar rindo contigo seja de qualquer coisa, ou de nada, não precisa de motivos pra rir."

        "Isso foi uma das coisas que você me ensinou quando criança e eu nunca esqueci."

        "Eu quero continuar me divertindo contigo."

        "Assim como eu sempre me diverti."

        if seen_label("corridors_Ba"):
            "E a única coisa que desejo essa noite, é que seja o começo de algo novo entre nós."

            "Talvez eu finalmente esteja entendendo o que eu quero de verdade."

            "Na verdade é como se eu sempre soubesse, e só agora estou tendo coragem de admitir isso pra mim."

            "De pouco em pouco pelo menos, e no fim, só precisarei admitir pra você."

        else:
            "Mesmo andando tão distante de como eu era antes, ainda quero estar perto de você."

            "Na verdade, quero estar mais próximo ainda."

            "Eu não quero mais me afastar de ninguém, nem de mim mesmo."

            "E não há ninguém melhor pra me ensinar isso do que você."

            "De todas as vezes que eu me senti vivo por sua causa, mesmo naquelas em que eu não queria."
            
            "Eu ainda me lembro de quase todas elas. Em todas eu quis me sentir vivo na verdade, mesmo que inconscientemente, sempre quis."

            "E isso é algo que não mudou até hoje, só preciso ser mais sincero comigo mesmo."

            "Em principal, com você também."

    else:
        "E não importa como as coisas terminem depois disso, pelo menos vou poder olhar lá na frente e dizer que tentei."

        "Tentei com medo, porém tentei."

        "Se tudo acabar dando certo, ótimo. Se tudo acabar dando errado, tudo bem também."

        "Porque eu pelo menos terei a certeza de que fiz o que pude."

        "E terei certeza que aos poucos vou aprendendo a lidar com essas coisas."

        "De que eu não sou mais aquele garoto que foge de tudo o que sente."

        "E na minha perspectiva, mesmo que contra esse pensamento, acredito que seria o melhor pra mim."

        "Muitas coisas eu só passei a apreciar assim que eu tentei elas de alguma forma."

        "Pra mim o mais difícil sempre foi isso, tentar, dar o primeiro passo, e eu sempre acabava desistindo antes mesmo de continuar."

        "E se não fosse pela Miya me forçando a dar esse primeiro passo pra tantas coisas, eu provavelmente ainda estaria me sentindo tão preso quanto nunca."

        "Uma zona de conforto não é mais confortável quando você percebe que está sozinho nela."

        "Se ela deixa de estar confortável, se torna uma zona de dor, e sair dela é tão difícil quanto sair de uma zona de conforto."

        if seen_label("corridors_Bc"):
            "E é por isso que eu preciso sair dessa zona."

            "Preciso me arriscar, mesmo que eu não saiba o que vai acontecer depois."

            "Preciso aprender a lidar com essas coisas."

            "Preciso aprender a me abrir mais pras pessoas."

            "Preciso aprender a me importar mais."

            "Mesmo que eu me sinta vulnerável pra isso."

            "E mesmo que eu não queira, preciso aprender a dar o primeiro passo sozinho."

            "Pois no fim das contas, ninguém vai fazer isso por mim além dela."

            "Eu devia ter aprendido isso há muito tempo, mas antes tarde do que nunca."

        else:
            "E eu já passei por várias dessas zonas, mas nunca consegui sair totalmente delas."

            "É como se eu estivesse preso num ciclo vicioso de tentar e falhar."
            
            "E eu não quero mais isso pra mim."

            "Preciso aprender a dar o primeiro passo sozinho."

            "Preciso aprender a me arriscar mais."

            "Nada vai mudar se eu continuar esperando que as coisas simplesmente mudem por vontade própria."

            "Dessa forma eu apenas estaria repetindo o mesmo ciclo que venho estando em alguns meses."

            "E no fim das contas, ninguém vai fazer isso por mim além dela."

            "Só por hoje, vou deixar me levar."

    "Afinal, não há nenhum problema em não carregar nada sozinho."

    "Então, vou até o fim."

    "Mesmo que eu tenha medo de onde esse fim vai me levar."

    if not seen_label("corridors_Bc"):
        "Mas, eu me sinto estranhamente positivo sobre isso."

    return

label corridors_Cb:
    $ mc_personality.append("He is willing to take things as they come, without overthinking the situation.")

    "A verdade é que eu não tenho resposta nenhuma."

    "Não tenho certeza do que eu quero, do que eu sinto, ou do que eu espero."

    "Não tenho um plano, muito menos controle sobre o que vai acontecer."

    "Eu só tenho esse aperto no peito, essa ansiedade, esse medo… essa vontade confusa de ver a Miya e, ao mesmo tempo, de desaparecer do mundo."

    "Passei a noite inteira pensando em todas as possibilidades, de racionalizar o que eu sinto, mas no fim das contas nada disso importa."

    "Eu ainda continuo me sentindo perdido."

    "Eu sei que só estou complicando algo que poderia ser simples no final, mas eu não consigo evitar."

    "Você é uma incógnita pra mim, eu penso, de novo e de novo, porém nada faz sentido."

    "Não consigo encontrar uma resposta que me satisfaça, muito menos uma lógica pra tudo isso."

    "Mas sequer existe algum tipo de lógica? Por acaso é possível eu encontrar uma resposta?"

    "Existe a chance de você ter feito tudo isso por fazer, sem um motivo real?"

    "Na verdade, se eu disser que não for real, é como se eu tirasse seu direito de estar aqui."

    "Você tem um propósito isso é claro, mas qual é?"

    "Se eu soubesse pelo menos, muito antes de chegar aqui, talvez eu já estivesse dentro dessa sala."

    "Eu já teria pensado numa resposta, ou até numa conclusão antes mesmo de chegar aqui."

    "Mas é justamente pela suas ambiguidades que eu nunca me senti tão perdido como agora."

    "E o que me deixa mais irritado, é que algo me diz que tudo isso foi proposital."

    "Como se você soubesse exatamente o que estava fazendo."

    "Como se você soubesse que eu estaria aqui, parado nessa frente dessa porta, sem saber o que fazer."

    "É o que eu quero acreditar, assim eu me sinto menos idiota por estar nessa situação."

    "Tudo o que me resta é esse sentimento de culpa."

    "Culpa por ter me afastado de você."

    "…"

    "Eu sinto sua falta, Miya."

    if not seen_label("corridors_Bc"):
        "Falta de quando andávamos juntos pra casa."

        "Falta dos nossos rolês aleatórios que você me arrastava."

        "Falta até de conversar mais contigo."

    "E isso deveria ser o suficiente pra eu dar esse passo."

    if seen_label("corridors_Bc"):
        "Mas não é."

        "É como se eu estivesse preso num ciclo vicioso de tentar e falhar."

        "Só que dessa vez nem mesmo isso eu tô conseguindo."

        "Eu não quero falhar com você. Eu não quero falhar comigo mesmo."

        "Porém se eu não tentar, do que adianta?"

        "Nesse caso eu já vou estar falhando de qualquer forma."

        "Mesmo não querendo isso, parece que é inevitável."

        "Só que eu sei que tenho o poder de mudar as coisas."

        "E eu preciso fazer isso."

        "Porque se eu não fizer, vou me arrepender pelo resto da minha vida."

        "Posso não saber como agir agora, mas sei que vou descobrir na hora certa."

        "E mesmo que eu não descubra, eu sei que você vai me ajudar com isso."

    else:
        "Mas e se eu tentar e nada mudar?"

        "Se eu abrir essa porta e simplesmente nada for resolvido?"

        "Não, isso não aconteceria."

        "Eu já estou indo com a certeza de que não vou voltar a ser o mesmo depois disso."

        "Mas o que eu não sei é como elas vão voltar depois de tudo."

        "As coisas vão voltar a ser como eram antes?"

        "Eu e você vamos voltar a ser próximos novamente?"

        "Tão próximos como nunca?"

        "Com alguma coisa mudando, o que vai restar de nós?"

        "O que vai restar entre nós?"

        "E o que vai restar de mim?"

    "Eu não faço ideia de verdade do que vai acontecer quando eu entrar ai, já repeti isso tantas vezes na minha mente que perdi a conta."
    
    "Não sei se vai ser estranho, constrangedor, ou até mesmo doloroso."

    "Não sei se vou me sentir aliviado, feliz, ou talvez até triste."

    "Pode ser que muito pouco mude, ou que tudo vire de cabeça pra baixo."

    "Mas se eu não tentar… se eu não girar essa droga de maçaneta… nunca vou saber se eu poderia ter mudado alguma coisa."

    "E talvez esse 'não saber' seja pior do que qualquer resposta que eu possa receber essa noite."

    if seen_label("corridors_Ba"):
        "Eu posso ter o direito da dúvida, mas não o direito de desistir."

        "Ficar parado aqui não vai me dar a razão que eu preciso."

        "Eu preciso agir."

        "Se pelo menos não por mim, ao menos por ela."

        "Porque eu sei que a Miya merece uma resposta."

        "E eu devo isso a ela."

        "Mesmo que eu não saiba qual é essa resposta."

        "Porque no fim das contas…"
    
    else:
        "Porque eu sei que eu devo isso a mim mesmo."

        "Eu não posso continuar vivendo assim, sem saber o que eu realmente sinto."

        "Eu não posso continuar me sentindo perdido."

        "Meu sentimento de culpa só vai aumentar se eu não fizer nada."

        "E o pior de tudo é que não há ninguém mais pra culpar além de mim."

        "Então eu preciso agir."

        "Preciso de respostas."

        "E eu só vou conseguir isso se eu abrir essa porta."

        "Porque no fim das contas…"

    "Querendo ou não, eu só vou descobrir se tentar."

    return

label corridors_Cc:
    $ mc_personality.append("He's conflicted about his feelings and fears change, preferring the comfort of the status quo.")

    "Talvez eu esteja fazendo tempestade em copo d'água. Em algo que nunca foi tão profundo assim como faço parecer."

    "Talvez você só queira conversar, ou desabafar sobre algo, e eu tô aqui me preocupando demais com algo simples."

    "Fico criando expectativas, colocando um peso enorme em seus braços sendo que nem mesmo sequer vi teu rosto hoje."

    "É claro que possa existir algo importante pra conversarmos, mas eu não sei se isso vá mudar alguma coisa."

    "Ao mesmo tempo que eu sinto que vai mudar, também sinto que tanto faz o que aconteça."

    "Eu não sei se tô disposto a ter essa conversa."

    "E, sinceramente… não sei se estou pronto pra qualquer mudança."

    "Porque se nada mudar…"

    "Se tudo continuar exatamente como está…"

    "Talvez eu até me sinta aliviado. Talvez seja mais fácil lidar com isso assim do que admitir que alguma coisa quebrou."

    with Pause(1.0)

    mc "Hah…"

    "Eu dou um leve suspiro, só pra ver se isso pelo menos me ajuda com alguma coisa."

    "É claro que não tá certo, mas por que eu sinto conforto nesse pensamento?"

    "A Miya sempre foi alguém que me fez sentir vivo, mesmo quando eu não queria."

    if not seen_label("corridors_Bc"):
        "E mesmo que eu tenha dúvidas sobre o que eu sinto, eu sei que estar perto dela me faz bem."

        "Eu quero e não quero ao mesmo tempo."

        "Pode ser até mais fácil lidar com isso se nada mudar, mas, e nos casos em que algo mude pra melhor?"

        "Eu estou criando todo tipo de suposição em uma situação que algo bom ou ruim pode acontecer."

        "Até então eu não tenho absolutamente nenhuma certeza do que ela vai dizer pra mim."
        
        "Eu ando repetindo os mesmos pensamentos que eu tive no caminho pra cá, mas, por qual motivo?"

        "Achei que já tivesse decidido o que fazer quando pulei o muro, mas, parece que só tô enrolando mais ainda."

        "Enrolando pra não ter que encarar ela, como se eu já soubesse que algo definitivo fosse acontecer."

        "Mas e se acontecer? No fim nada importa, o que importa é eu abrir logo essa porta e encarar o que for pra encarar."

        if seen_label("corridors_Aa"):
            "Eu me diverti tanto com ela no passado, e eu continuei me divertindo pelo tempo que ficamos juntos no presente."

            "Eu me divirto ao lado dela, e eu só fui perceber isso quando passei a voltar sozinho pra casa."

            "É apenas algo trivial, tão rotineiro, que no instante que eu parei de fazer isso contigo que eu senti falta."

            "Eu posso ter sentido mas ainda não era nada demais, haviam coisas mais importantes com que me preocupar."

            "E eu continuei assim, até mesmo quando você arrumava tempo pra voltar comigo e eu não dava a mínima."

            "Mas, até mesmo uma simples ação como essa foi capaz de me fazer sentir algo."

            "Mesmo que pouco, porém algo."

            "E isso me incomoda."

            "Por que só você tem o direito de me fazer sentir essas coisas?"

            "Por que eu não consigo me sentir de outra forma com outras pessoas?"

            "Eu já sai com outros amigos e eu gostei de andar com eles, mas, nunca é a mesma coisa."
        
    else:
        "Mas eu não consigo evitar de pensar que talvez eu só esteja me iludindo."

        "Talvez eu só queira sentir algo, qualquer coisa, mesmo que seja só uma ilusão."

        "Mas eu não consigo de nenhuma forma. Eu não consigo sentir nada especial sobre isso."
    
        if seen_label("corridors_Ac"):
            "Não éramos pra sermos amigos de infância? Termos uma amizade inabalável, tão forte que nada poderia nos separar?"

            "Então por que eu não consigo me sentir assim? Por que tudo parece tão frágil?"

            "É como se eu estivesse tentando encontrar um motivo pra desistir."

            "E talvez eu esteja quase perto de encontrá-lo, sério."

            "Mas eu não vou saber se eu ficar parado aqui pra sempre."

            "O que pode acontecer se eu abrir essa maldita porta?"

            "Se nada mudar, se tudo isso for em vão, eu vou me sentir aliviado? Ou eu vou me sentir ainda mais perdido?"

            "Eu deveria prezar mais pela Miya, me importar em não magoá-la, mas eu não sei se eu consigo fazer isso agora."

            "Eu tô mais frustrado comigo mesmo por não consegui colocar meus sentimentos em ordem, do que com qualquer outra coisa."

            "Nesse caso, eu falhei como amigo dela? Ou eu falhei comigo mesmo?"

            "Eu não sei o que eu quero."

            "Na verdade, eu sei, mas não quero admitir."

            "Não era pra ser tão difícil assim, não era pra ser assim."

            "Mas parece que eu tô deixando de me importar."

            "Não com ela, mas com tudo de maneira geral."

            "Até mesmo com nossa amizade, que eu sei que sempre foi tão importante pra mim."

            "E não é como se eu precisasse de um tempo sozinho, ultimamente o que eu mais ando tendo é isso, e eu não me incomodo."

            "É como se eu estivesse me afastando não só dela mas do mundo em si. Só restando eu como minha própria companhia."
    
    "Não vai ser fácil, eu sei disso."

    "Mas, mesmo se algo mudar ou não, ficar parado aqui não vai me levar à lugar nenhum."

    "Se eu pelo menos quero alguma resposta, nem que seja qualquer uma, eu preciso entrar aí."

    "Eu preciso te ver antes de tudo, pra pelo menos eu conseguir racionalizar o que eu sinto."

    "Talvez minha mente fique de ponta cabeça, talvez isso tudo mude completamente o meu jeito de pensar."

    "Ou no fim, eu apenas continue o mesmo de sempre."

    "Mas de qualquer forma…"
    
    "Ao menos eu vou saber o que você queria me contar."
    
    return


label corridors_D:
    "Hoje a noite, talvez seja a última chance que eu tenho de falar com você."
    
    "De uma vez por todas, esclarecer o que tá acontecendo entre nós."

    if seen_label("corridors_Aa") and seen_label("corridors_Ba") and seen_label("corridors_Ca"):
        $ mc_personality.append("Ren is ready to confess his true feelings to Miya.")

        "De finalmente, admitir o que eu sempre senti por você."

        "Mesmo que eu tenha demorado tanto pra perceber isso. Pra admitir isso."

        "Eu só espero que você ainda sinta o mesmo por mim."

    elif seen_label("corridors_Ab") and seen_label("corridors_Bb") and seen_label("corridors_Cb"):
        $ mc_personality.append("Ren is uncertain about his feelings.")

        "De entender o que eu realmente sinto por você."

        "E o que eu realmente quero da nossa amizade."

        "Mesmo que eu não tenha certeza do que isso seja ainda."

    elif seen_label("corridors_Ac") and seen_label("corridors_Bc") and seen_label("corridors_Cc"):
        $ mc_personality.append("Ren is resigned to the possibility of losing Miya.")

        "De perceber que talvez a gente não tenha mais o que falar."

        "E que talvez a gente não tenha mais o que ser."

        "Mesmo que eu não queira aceitar isso de jeito nenhum."

        "Ainda é uma possibilidade infeliz."
    
    else:
        "Por mais que eu não saiba o que dizer agora."

        "Pelo menos é isso o que eu vou fazer."

        "Por nós dois."

    "Depois de me perder tanto tempo em meus pensamentos, eu finalmente tomo a coragem que precisava."

    "Eu respiro fundo, coloco a mão na maçaneta, e a giro devagar."

    play sound sfx_door_open
    "O som da porta se abrindo ecoa pelo corredor silencioso."

    "Está acontecendo."

    "Tudo o que eu pensei, tudo o que eu senti, tudo o que eu temi…"

    "Tudo isso acaba se resumindo a um único pensamento."

    "E esse pensamento é…"

    python:
        user_response = renpy.input("E esse pensamento é…", length=100)
        ren_thought = user_response.strip()

        if not ren_thought or ren_thought.isspace():
            renpy.say("", "…")
            renpy.say("", "Parece que eu não consigo colocar isso em palavras agora.")
            renpy.say("", "Não é como se eu soubesse exatamente o que sinto.")
            renpy.say("", "Mas eu não consigo expressar isso pra mim mesmo.")
            renpy.say("", "Se for pra resumir tudo em uma palavra, eu diria que é confusão.")
            renpy.say("", "Mas até mesmo confuso, eu entendo muito bem o que eu sinto por você.")
            renpy.say("", "Por fim, só tenho uma coisa a fazer…")
            pass
        else:
            # Add later the implementation of the LLM integration for the player's response.
            pass
    
    $ amb_stop()
    $ ambience_sfx_cycle.stop(stop_all=True)
    
    scene black
    with scenechange

    "Eu entro na sala de aula."

    play sound sfx_door_creak

    return