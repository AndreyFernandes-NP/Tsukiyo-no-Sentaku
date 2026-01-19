label classroom:
    call iscene("classroom_Intro") from _calling_scene9
    call iscene("classroom_A_1") from _calling_scene10

    call choice_classroomA_1 from _calling_choice4
    call iscene(_return) from _calling_scene11
    
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

    "Desde que eu entrei na sala e a chamei, parecia que ambos estávamos presos em mundos completamente diferentes ao mesmo tempo."

    "Mas agora, é de verdade."

    "Essa é a Miya com quem eu vim falar hoje à noite."

    mc "Miya…"

    mi "Você… chegou tarde né."

    scene cg miya_classroom_moonlight
    with scenechange

    "Ela faz uma expressão mais triste, deixando de olhar de canto de olho pra mim."

    "Eu não sei nem o que dizer na verdade."

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

        "Ficar quieto.":
            return "classroom_A_1b"

        "Sentar-se em uma cadeira próxima.":
            return "classroom_A_1c"

        "Ser honesto.":
            return "classroom_A_1d"

label classroom_A_1a:
    "Eu dou mais um passo pra dentro da sala."

    "Logo em seguida, eu dou outro. E mais outro. Até que fico perto o suficiente."

    scene cg miya_classroom_confused
    with scenechange

    "Ela me olha um pouco surpresa, esperando eu dizer algo."

    mc "Eu não sou tão bom com palavras… mas, quero que saiba que tô feliz de estar aqui."

    "Ela me olha por alguns segundos, e esboça um sorriso tímido. Eu viro meu rosto pro lado, não por vergonha, mas é estranho encará-la depois de dizer algo assim."

    mc "Nosso ano já tá acabando, e eu não faço ideia de quando poderia te ver novamente."

    mc "Então, eu queria tentar aproveitar esse momento contigo."

    mc "Posso acabar falando nada com nada, mas, hoje eu vim pra ficar ao seu lado."

    "Eu olho pra ela de novo, apesar de não ter total certeza do que eu realmente sinto ou do que tô fazendo, ficar ao lado dela nem que seja por hoje, é a única coisa que eu sei que quero."

    mc "Se você quiser, claro."

    mi "…"

    mi "{size=*0.8}É claro que eu quero…{/size}{nw}"

    mc "…"

    mc "O quê? Não deu pra ouvir direito…"

    mi "…"

    mi "É claro que pode ficar, ou já se esqueceu de quem foi que te chamou até aqui?"

    return