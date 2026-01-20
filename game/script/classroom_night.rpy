label classroom:
    call iscene("classroom_Intro") from _calling_scene9
    call iscene("classroom_A_1") from _calling_scene10
    call choice_classroomA_1 from _calling_choice4
    call iscene(_return) from _calling_scene11
    call iscene("classroom_A_2") from _calling_scene12
    
    jump end_of_build
    return

label classroom_Intro:
    $ qc_menu('hide')

    $ routes_number = []

    pause(2.5)

    $ qc_menu('show')

    mc "…"
    mc "Miya?"

    $ qc_menu('hide')

    play sound sfx_cg_woosh
    scene cg miya_classroom_moonlight:
        truecenter
        zoom 1.2 rotate -5 subpixel True
        easein 7.0 zoom 1.0 rotate 0
    with flash
        
    play music music_happy_girl fadein 0.1

    with Pause(7.0)

    $ qc_menu('show')

    "…"

    "Eu…"

    "Por que eu congelei agora?"

    "Essa é mesmo a Miya na minha frente?"

    "Ela…"

    python:
        match store.mc_routes[0]:
            case "Close":
                renpy.call("iscene", "classroom_Intro_A")
            
            case "Neutral":
                renpy.call("iscene", "classroom_Intro_B")

            case "Distant":
                renpy.call("iscene", "classroom_Intro_C")

    return

label classroom_Intro_A:
    "Está linda."

    "Ela sempre foi bonita, mas agora…"

    "Eu mal consigo desviar o olhar dela. Eu fico hipnotizado, parado na porta a admirando em silêncio."
    
    "Enquanto eu estou aqui, ela está lá, sentada próxima da janela, olhando pra fora ou quem sabe pra lua, como se estivesse esperando por algo."

    "Há algo diferente nela, algo que me atrai."

    "Os seus olhos brilham sob a luz da lua que entra pela janela. O seu rosto parece tão suave, tão delicado…"

    "Os cachos levantados pelo vento a fazem parecer ainda mais viva."

    "Eu sinto uma vontade enorme de me aproximar dela, como se pedisse para que eu me sentasse ao seu lado."

    "Eu quero fazer isso, mas… será que é válido depois de tudo o que aconteceu?"

    "Seria idiota admitir que eu só comecei a ver ela desse jeito agora?"

    "Tantos momentos que passamos por situações como essa, e eu nunca senti nada demais."

    "Seria porquê estivemos tão distantes um do outro ultimamente, que eu não consegui ver o que estava bem na minha frente?"

    "Eu não quero perder essa chance."

    "Não quero ser o cara que deixou a Miya de lado de novo."

    "No momento em que eu decido isso, uma voz fina chama meu nome."

    return

label classroom_Intro_B:
    "Parece tão bonita."

    "Na verdade, eu sempre achei ela bonita, mas agora… é um pouco diferente."

    "Difícil pôr em palavras. Seus cabelos levantados suavemente pelo vento, seu rosto iluminado pela lua… é tudo tão, surreal."

    "Eu fico parado na porta, observando enquanto ela olha pra fora da janela. Eu sei que esse tempo todo ela estava esperando por mim."

    "Talvez ela até tinha preparado alguma coisa para quando eu aparecesse na hora, seja uma pose ou até apresentação."

    "Mas ela devia ter ficado tão cansada de me esperar, que acabou desistindo e sentando ali."

    "Há quanto tempo será que ela tá assim?"

    "O que será que ela pensou quando eu não apareci?"

    "Talvez ver ela desse jeito, de uma forma tão vulnerável, me fez perceber outra coisa."

    "Eu quero me aproximar dela, quero sentar ao lado dela."

    "Eu quero conversar com ela, dizer que eu estou aqui, pelo menos agora."

    "Mas eu não sei se é o momento certo."

    "Por acaso eu devo falar algo? Devo esperar ela falar primeiro? O que eu faço?"

    "Ela ainda não me notou, mesmo após eu ter chamado seu nome, mas… porque eu não consigo fazer nada além de ficar olhando?"

    "Minha boca se abre, ela se move, mas nenhuma palavra sai."

    "Eu tento gesticular algo, levantar minha mão, mas paro no meio do caminho."

    "Será que eu viro as costas e vou embora? Será que eu continuo parado sem dizer nada?"

    "Eu olho pro chão, encaro meus pés, e tento pensar no que fazer."

    "Mas, é nesse momento que…"

    return

label classroom_Intro_C:
    "Ela parece tão diferente…"

    "É como se eu não estivesse olhando pra Miya."

    "Eu não quero dizer algo como 'Ela sempre foi tão bonita assim?', porque ela foi mesmo."

    "Só que, olhando agora, é como se eu estivesse vendo uma pessoa completamente nova."

    "Não sei nem se bonita é a melhor palavra pra descrever essa cena."

    "Pensar assim parece errado, mas ao mesmo tempo tão certo."

    "Eu queria poder descrever de uma maneira mais clara o que eu sinto."

    "Não é só uma questão de aparência, é tudo. O jeito que ela está sentada, o olhar distante, a luz da lua…"

    "Isso tudo cria uma atmosfera tão estranha."

    "Eu quero me aproximar, mas eu sei que não é o momento pra isso."

    "Posso até estar sendo cauteloso demais, é que… eu não sei."

    "Talvez eu não devesse nenhuma explicação sobre o que eu sinto."

    "Mesmo assim, por que eu ainda tô parado na porta?"

    "Por que eu não me movo nem um centímetro sequer?"

    "E por que ela não me notou também?"

    "Eu a chamei assim que entrei, mas ela continua olhando pra fora, como se o mundo externo não existisse."

    "Será que ela nem percebeu que eu estou aqui?"

    "Ou, será que… ela não esperava que eu fosse aparecer?"

    "Parece até que tô olhando pra uma Miya que eu nunca tinha visto antes."

    "Uma que está conversando consigo mesma em seus pensamentos, assim como eu costumo fazer."

    "Cadê aquela Miya que não calava a boca? Que sempre tinha algo pra dizer toda hora? Que me provocava?"

    "Que estaria nesse exato momento me enchendo de perguntas, questionando porquê eu me atrasei, que não se deve deixar uma dama esperando."

    "E eu responderia com 'Eu não te chamaria exatamente de uma dama.'"

    "Por que…"

    "Tudo tá tão silencioso?"

    "O que será que eu faço? Continuo parado aqui, esperando ela me notar? Ou eu viro as costas e vou embora?"

    "Se eu for embora, no final vai fazer alguma diferença? Ela parece estar tão distante mesmo tão perto de mim."

    "Então, por que eu não me aproximo e acabo logo com isso? Por que eu fico aqui mantendo as coisas como estão?"

    "Por que eu continuo fazendo exatamente o que fiz nesses últimos meses?"

    "Pensei que dar esse passo fosse me ajudar a resolver as coisas, mas…"

    "…"

    "E é antes que eu percebesse, assim que a olho de novo… nossos olhos se encontram."

    return

label classroom_A_1:
    scene cg miya_classroom_confused
    with scenechange

    mi "Ren?"

    "Ela me nota enquanto eu estava perdido nos meus pensamentos."

    "Desde que eu entrei na sala e a chamei, parecia que ambos estávamos presos em mundos completamente diferentes."

    "Mas agora, é de verdade."

    "Essa é a Miya com quem eu vim falar hoje à noite."

    mc "Miya…"

    mi "Você… chegou tarde né."

    scene cg miya_classroom_moonlight
    with scenechange

    "Ela faz uma expressão mais triste, voltando a olhar pra janela."

    "Eu não sei nem o que dizer na verdade. Pelo menos, falar alguma coisa deve ser melhor do que fazer cara de paisagem."

    mc "…"

    mc "É, eu cheguei…"

    "Eu consigo notar um sorriso sem graça surgindo no rosto dela."

    "A primeira coisa que penso é em pedir desculpas, mas, eu sei que não vai adiantar de nada."

    "Não são desculpas que a Miya quer ouvir agora."

    "Posso não saber exatamente o que ela queira ouvir, mas pelo menos eu sei o que não devo falar."

    mc "Sabe…"

    "…"

    return

label choice_classroomA_1:
    menu(duck=False, shuffle=True):
        with menueffect
        "Dar mais um passo.":
            return "classroom_A_1a"

        "Continuar parado.":
            return "classroom_A_1b"

label classroom_A_1a:
    "Eu dou mais um passo pra dentro da sala."

    "Logo em seguida, eu dou outro. E mais outro. Até que fico perto o suficiente."

    if mc_routes[0] == "Close":
        mc "Eu não sou muito bom com palavras. Pra falar a verdade, eu tô até feliz que você me chamou."

        mc "Nosso ano já tá acabando, e eu não faço ideia de quando poderia te ver novamente."

        mc "As nossas vidas vão mudar, nós dois nos tornaremos adultos e…"

        mc "…"

        mc "No fim das contas, eu só queria tentar aproveitar um último momento contigo."
    
    else:
        mc "Eu não vim aqui pra falar sobre o meu atraso. Nem pra pedir desculpas."

        mc "Esse ano vamos nos formar, e a nossa vida vai mudar por completo."

        mc "Você já sabe pra qual faculdade vai, e eu… ainda não tenho nem certeza do que quero fazer."

        mc "Eu não faço ideia de quando poderia te ver de novo, é por isso… que hoje eu precisava ver você."

    scene cg miya_classroom_confused
    with scenechange

    "Ela me olha por alguns segundos, e esboça um sorriso tímido. Eu viro meu rosto pro lado, não por vergonha, mas é estranho encará-la depois de dizer algo assim."

    mi "{size=*0.8}Por que as vezes você é tão idiota…?{/size}"

    "Ela sussurra isso, quase inaudível, mas de uma forma que eu ainda consigo escutar."

    return

label classroom_A_1b:
    "Sinto meu coração batendo forte, é como se pedisse pra eu sentar ao lado dela."

    "Mas, ao mesmo tempo, eu fico com medo de acabar estragando alguma coisa."

    mc "Eu… não vim até aqui pra falar do meu atraso. Também não vim apenas por questão de vir."

    mc "Eu só…"

    mi "Não."

    mi "Não precisa dizer mais nada."

    scene cg miya_classroom_confused
    with scenechange

    "Ela me interrompe antes que eu possa continuar. Sua voz é firme, mas ao mesmo tempo delicada."

    mi "Só o fato de você ter vindo hoje já significa muito mim."

    "É como se sua voz estivesse um pouco trêmula, porém, ainda decisiva."

    "Eu não sei o que ela estava pensando antes de eu entrar na sala, ou o que ela decidiu enquanto eu tava lá fora."

    "Vendo que a chance de eu não aparecer hoje era uma possibilidade, talvez ela tenha passado por um turbilhão de coisas em sua mente assim como eu."

    "Acabar pensando demais, enquanto tenta procurar mil e uma justificativas, tudo isso pra no final não chegar à lugar nenhum."

    "Isso não combina com a Miya, é por isso que vê-la assim só me deixa mais vazio."

    mi "Não fica parado aí na porta."

    mi "Vem cá."

    "Ela faz um gesto com a mão, me chamando pra perto dela."

    "Eu me aproximo devagar, como se cada passo meu fosse um esforço enorme."

    "O silêncio deixado entre nós enquanto eu caminho parece durar uma eternidade, o suficiente pra eu voltar a sentir meu próprio coração batendo rápido."

    "Quando eu finalmente chego perto dela, eu sento em uma cadeira próxima."

    return

label classroom_A_2:
    mi "Não foi só pra isso que eu te chamei hoje."

    "Ela suspira um pouco, falando com uma voz meio emburrada."

    if seen_label("classroom_A_1b"):
        mi "Eu também queria te ver."

    mi "Já faz tanto tempo que não conversamos ultimamente."

    mi "Você até deixou de me visitar durante seu tempo livre enquanto eu tinha clubes."

    mi "Se tivesse vindo anteontem, não teria perdido a festa de despedidas que a Yuki fez."

    mi "Ela trouxe vários daqueles bolinhos que você gostou muito…"

    "Eu nunca fui alguém de gostar de clubes, apesar de serem boas atividades extracurriculares e complementarem nas notas, é algo que eu não conseguia engolir direito."

    "A Miya sempre participou de três, era o máximo permitido por nossa escola. Tinha o de vôlei, o de culinária e o de leitura, que eu cheguei a entrar numa época."

    "Os momentos que eu tive com ela durante os clubes foram na maior parte bons, porém isso porquê era eu quem decidia quando ou não ir."

    mi "Ah, você sabia que eu acabei adotando dois gatinhos?"

    mc "Dois? Você não disse que não tinha coragem de cuidar de animais?"

    mi "Sim… mas, é que eu acabei achando eles três numa caixa naquela rua que a gente sempre passa indo pra casa."

    mi "Eu não aguentei vê-los jogados no meio da rua."

    mc "Se você disse que tá cuidando de dois, quer dizer que um…"

    mi "Não, um deles ficou com a Yuki, e desde então venho cuidando dos dois há alguns meses."

    mi "Eu até havia te mandado uma foto quando os encontrei…"

    "…"

    "Eu não me lembro. Se eu não me lembro, é porque eu não me importei. Saber que ela aprendeu a cuidar de gatos me deixa surpreso, mas, não sei se é de uma maneira boa."

    "Quando você é um dos últimos a receber uma notícia, é como se ela perdesse parte de seu peso total."

    "Isso era pra ser uma grande coisa pra Miya conhecendo ela, mas, será que posso dizer isso agora?"

    mi "Você também perdeu a nossa vitória no campeonato entre escolas de vôlei… sabe, eu fiquei tão feliz nesse dia com o pessoal todo gritando."

    mi "No dia seguinte, foi como se eu tivesse me tornado uma daquelas heroínas de manga, por onde eu passava, havia alguém me cumprimentando e sorrindo."

    "Miya sempre adorou Vôlei, ela não fazia questão nenhuma de perder qualquer aula extra ou treinamento desse clube."

    "Mas, o que ela quer dizer com isso é…"

    mi "Ano passado, quando perdemos na semi-final…"

    mi "Eu sei que você não é do tipo que gosta de esportes, mas, você havia dito algo pra mim que, eu duvido muito que teria ganhado se não fosse por isso."

    "'Quem se importa com perder ou vencer. Você jogou, e foi incrível, é só isso. Mas, aqueles que são incríveis, nunca desistem de verdade. É por isso que eu sei que no próximo ano você vai ganhar.'"
    
    "Por que eu lembro tão bem dessa frase?"

    "Não é como se fosse algo especial, é um monte de palavras que eu inventei na hora pra tentar animar a Miya…"

    if mc_routes[0] != "Distant":
        "Na verdade, pode até não ser especial pra mim, mas pra ela, com certeza foi."

        "E é por isso que eu me lembro tão bem dessa frase, e também do momento de quando falei."

    mi "Eu queria ter te visto na arquibancada durante o último jogo."

    "…"

    "Eu não tenho nenhuma resposta que não pareça vazia à primeira vista."

    if mc_routes[0] == "Close":
        "Eu me arrependo amargamente de não ter ido nesse jogo. Mesmo não torcendo, eu ainda queria estar lá nem que fosse só pra vê-la jogar."

        "Se fosse tão simples admitir isso pra ela, de uma forma que não pareça uma desculpa pra me fazer sentir menos pior."

        "Só que não, não é isso que ela quer que eu fale. Ela não tá me contando essas coisas pra que eu diga algo em troca, ou que eu me sinta pior."

        "Ela só quer que eu entenda as coisas, ainda mais do ponto de vista dela."

        "Porém, não dizer nada também é o mesmo que admitir que eu ainda não entendi."

        "Ou que eu esteja tão confuso que a única coisa que posso fazer agora é me remoer pelo passado."

        "Talvez, a Miya não quer nem que eu diga nada."

        "Seja isso ou não, ao invés de eu ter que pensar quando preciso ou não falar, vou confiar tudo isso apenas ao momento."

        "Se for pra eu falar, que eu fale antes de pensar duas vezes e acabe quieto de novo."

    elif mc_routes[0] == "Neutral":
        "Qualquer coisa que eu possa falar pode ser vista apenas como uma desculpa pra me fazer sentir menos pior."

        "Que no final, possa até ser, mas isso não resolveria nada entre a gente."

        "Ela não está reclamando dos erros que cometi no passado, muito menos me crucificando agora por isso."

        "Não é essa intenção que ela quer passar. Ela teve tempo o suficiente pra pensar em como abordaria seja lá o que ela queria desde o início."

        "Se ela tá fazendo assim, é porque tem um motivo, é de propósito. Agora cabe a mim tentar adivinhar ou entender o que seria esse motivo."

        "Ou talvez… como sempre, eu só esteja pensando muito, e a única coisa que a Miya está fazendo como sempre fez, é seguindo seus próprios sentimentos."

        "Se for isso a resposta, se for pra eu admitir alguma coisa, é melhor que eu seja honesto comigo mesmo e também com ela."
    
    else:
        "Mas, não é como se falar pudesse mudar muita coisa agora."

        "O maior erro dela foi acabar se prendendo à mim pra essas coisas."

        "Ela acabou se frustrando em algo que… ela mesma projetou na sua mente."

        "Só que, é claro que não posso dizer que ela tá errada."

        "Existe uma linha tênue entre o que é ilusão e o que é verdade."

        "É como se a Miya estivesse cruzando por essa linha ocupando ambos os lados."

        "Ao mesmo tempo que não é justo pra mim… eu não fui justo com ela no passado."

        "De tanto pensar, já tem um tempo que minha perna tá balançando sozinha."

        "A Miya nota esse meu nervosismo e sorri pra mim, quase como um sorriso de alívio por não ser a única."
    
    "…"

    return

label classroom_A:
    "A Miya se levanta, e eu faço o mesmo."
    return