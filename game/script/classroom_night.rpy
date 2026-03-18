label classroom:
    call iscene("classroom_Intro") from _calling_scene9
    call iscene("classroom_A_1") from _calling_scene10
    call choice_classroomA_1 from _calling_choice4
    call iscene(_return) from _calling_scene11
    call iscene("classroom_A") from _calling_scene12
    
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
            
            case _:
                renpy.call("iscene", "classroom_Intro_B")

    return

label classroom_Intro_A:
    "Está linda."

    "Ela sempre foi bonita, mas agora…"

    "Eu mal consigo desviar o olhar dela. Eu fico parado na porta, a admirando em silêncio."
    
    "A forma com que seus olhos brilham sob a luz da lua, o seu rosto suave, que parece tão delicado…"

    "Eu fico hipnotizado. Ainda mais quando seus cachos são levantados por uma pequena brisa que vem lá de fora."

    "Dou meio passo à frente, quase que inconscientemente, mas paro. A única coisa que me impede de continuar é a minha mão, que segura com uma força surpreendente a maçaneta."

    "Eu a rapidamente solto, mas o tempo que levo pra isso é o tempo que me faz imóvel de novo."

    "Seria mesmo idiota admitir que eu só comecei a ver ela desse jeito agora?"

    "Tantos momentos que passamos juntos, que ela estava tão bonita quanto nunca, e eu não sentia nada."

    "Estar ao lado dela não era nada mais do que apenas uma segunda-feira pra mim."

    "Se não fosse pela distância, eu não estaria vendo aquilo que tava bem óbvio na minha frente."

    "É por isso que nada impede que eu volte a vê-la como antes de novo."

    "Apesar que eu gostaria que isso se tornasse permanente, ainda tem uma chance que…"

    "Eu indiretamente desço minha cabeça pro chão, fico sentindo vergonha de mim mesmo mas não consigo interromper meus pensamentos."

    "Não é como se eu tivesse a segurança do meu futuro inteiro pra poder dizer isso."

    "É só que…"

    "…"

    "Não, eu não quero perder essa chance."

    "Não quero ser o cara que deixou a Miya de lado de novo."

    "Se ela me deu ao menos uma razão pra que eu possa perceber algo, que eu faça valer de alguma coisa."

    "Balanço minha cabeça rapidamente como se eu varresse esses pensamentos pro fundo da minha mente."

    "Lá, pelo menos por um tempinho, eles não vão mais me incomodar."

    "E é quando levanto o olhar preparado pra dar um passo, que uma voz fina, porém tão doce, chama meu nome."

    return

label classroom_Intro_B:
    "Parece tão bonita."

    "Na verdade, eu sempre achei ela bonita, mas agora… é um pouco diferente."

    "Difícil pôr em palavras. Seus cabelos levantados suavemente pelo vento, seu rosto iluminado pela lua, tudo é tão… surreal."

    "Eu dou meio passo pra dentro, é um passo tão silencioso, que quase pareceu insignificante."

    "Ela ficou esperando esse tempo todo por mim. Parte de mim havia se convencido de que ela nem estaria mais aqui."

    "Há quanto tempo será que ela tá assim?"

    "Sentada, com uma expressão cansada, de alguém que já entrou tão profundamente em seus pensamentos que nem se recorda mais da realidade."

    "E o que será que ela pensou quando eu não apareci?"

    "Talvez até tivesse alguma coisa pronta pra quando eu chegasse, que eu sem querer arruinei por demorar tanto."

    "Ver ela desse jeito, de uma forma tão vulnerável, me fez perceber outra coisa."

    "Dessa vez eu dou um passo inteiro na direção dela, com minha cabeça zoneando cada e única possibilidade de encontro pra assim que ela virasse a cabeça."

    "Eu quero conversar com ela, quero continuar olhando pra ela, dizer que estou aqui, ou pelo menos, que agora estou."

    "Só que, no meio do meu segundo passo, eu volto dois, como se meu corpo tremesse naturalmente por fazer isso."

    "Não quero dizer que esse não é o momento certo, mas como eu poderia agir tão direto pra algo que me sinto tão incerto?"

    "Por acaso eu devo falar algo? Devo esperar ela me olhar primeiro? O que eu faço?"

    "Mesmo depois de dizer o seu nome assim quando entrei… não fiz nada a não ser observar."

    "Passo a língua entre meus lábios, minha boca se mexe, ela se abre, pronta pra anunciar que estou aqui."

    "Mas, ao invés de palavras só sai um monte de grunhidos silenciosos como se perdessem a força no último momento."

    "Ainda sem desistir eu gesticulo algo, levanto minha mão, mas nada disso funciona, eu não falo uma única palavra."

    "Declarando derrota, eu abaixo minha mão e encaro meus pés, tentando pensar no que fazer a seguir."

    "É quando…"

    return

label classroom_Intro_C:
    "Ela parece tão diferente…"

    "É como se eu não estivesse olhando pra Miya."

    "Eu não quero dizer algo como 'Ela sempre foi tão bonita assim?', porque ela foi mesmo."

    "Só que, olhando agora, é como se eu estivesse vendo uma pessoa completamente nova."

    "Eu naturalmente agarro parte da minha camisa que fica no meu peito esquerdo."

    "Meu coração bate rápido, eu sinto cada pulsar dele, mas, por quê?"

    "Não sei nem se bonita é a melhor palavra pra descrever essa cena."

    "Pensar assim parece errado, mas ao mesmo tempo tão certo."

    "Eu queria poder descrever de uma maneira mais clara o que eu sinto."

    "Não é só uma questão de aparência, é tudo. O jeito que ela está sentada, o olhar distante, a luz da lua…"

    "Pensando bem, quando pude notar o meu corpo já começou a dar passos na direção dela, quase como se algo me puxasse."

    "Eu paro no último instante, penso em tentar resistir e voltar pra trás, mas…"

    "Isso tudo cria uma atmosfera tão estranha."

    "Eu quero me aproximar mais, só que, não é o momento pra isso."

    "Posso até estar sendo muito cauteloso, é que… eu não sei."

    "Talvez eu não devesse nenhuma explicação sobre o que eu sinto."

    "Por acaso eu devo voltar e ficar próximo da porta? Como se eu nunca tivesse andado até aqui? Não, meu corpo já tá se movendo pra isso, a questão é outra."

    "Por que ela não me notou ainda?"

    "Eu a chamei assim que entrei, eu andei na direção dela, tenho certeza que ela ouviu meus passos, mas, ela continua olhando pra fora."

    "Seus olhos parecem hipnotizados por algo, é como se o mundo não existisse mais."

    "Será que ela nem percebeu que eu estou aqui?"

    "Ou, será que ela não esperava que eu fosse aparecer?"

    "…"

    "Parece até que tô olhando pra uma Miya que eu nunca tinha visto antes."

    "Uma que está conversando consigo mesma em seus pensamentos, assim como eu tô fazendo agora."

    "É estranho ver a Miya tão calada, normalmente as vezes eu me perguntava quando ela iria ficar quieta por estar exausto de ouví-la."

    "Ela não está me provocando, não está fazendo nada pra me ver estressado. E muito menos não está me questionando e me enchendo de perguntas por ter atrasado."

    "Ela me questionaria o porquê de eu ter deixado uma dama esperando, e eu responderia com 'Eu não te chamaria exatamente de uma dama.'"

    "Então por que…"

    "Tudo está tão silencioso?"

    "O que será que eu faço? Continuo parado aqui, esperando ela me notar? Ou eu viro as costas e vou embora?"

    "Se eu for embora, no final vai fazer alguma diferença? Ela parece estar tão distante mesmo tão perto de mim."

    "Então, por que eu não me aproximo e acabo logo com isso? Por que eu fico aqui mantendo as coisas como estão?"

    "Pensei que dar esse passo fosse me ajudar a resolver as coisas, mas…"

    "…"

    "Eu desvio meu rosto dela, é como se eu ficasse com vergonha de olhá-la de novo."

    "O silêncio pesa bem mais do que eu esperava."

    "Consigo até ouvir minha própria respiração. Isso me deixa inquieto."

    "Isso é ridículo, eu justamente vim até aqui pra falar com ela."

    "Só que, quando eu chego, eu nem consigo sustentar o meu olhar."

    "Mesmo assim, tudo nessa sala parece querer chamar atenção pra ela. Eu escuto uma brisa atravessando a janela enquanto move as cortinas."

    "O som ecoa pela sala e some tão rápido quanto veio."

    "E é antes que eu percebesse, assim que a olho novamente… que nossos olhos se encontram."

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

    mi "Você…"

    "Eu consigo sentir uma hesitação nos seus olhos."

    mi "Chegou tarde né…"

    scene cg miya_classroom_moonlight
    with scenechange

    "Ela volta o olhar pra janela, sei que ela está claramente decepcionada comigo, mas…"

    "Eu não sei nem o que dizer na verdade. Isso não é o que a Miya que eu conheço falaria."

    "Ela não aceitaria tão fácil assim o meu atraso numa hora tão importante, eu já até estava preparado pro pior."

    mc "…"

    "Eu penso bem no que posso falar em seguida."

    mc "É, eu cheguei…"

    "É melhor do que ficar com cara de paisagem."

    "Eu até consigo notar um sorriso aparecendo no rosto dela com meu comentário sarcástico."

    "A primeira coisa que penso em fazer é pedir desculpas, mas, eu sei que não vai adiantar de nada."

    "Não são desculpas que a Miya quer ouvir agora. Só que, isso não resolve o problema de eu também não saber o que falar."

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
    "Eu dou mais um passo pra dentro da sala. É alto o suficiente pra que ela escutasse."

    mc "Eu sei que você deve estar com raiva de mim…"

    mc "Até agora me impressiona você não ter jogado uma dessas cadeiras no meu peito."

    "Eu falo enquanto me aproximo lentamente. Eu queria estar brincando, mas a Miya com raiva é mesmo algo sério."

    mc "Quero dizer, valeu…"

    mc "Ao menos eu aprecio que você me esperou esse tempo todo."

    "Ela levanta parcialmente o rosto como se eu tivesse chamado sua atenção, isso me deixa de certa forma mais aliviado."

    "Com mais um passo, eu olho pras cadeiras que estão espalhadas pela sala inteira."

    "O lugar tá mesmo uma bagunça, mas eu já esperava isso, hoje aconteceu um dos últimos eventos de fim de ano da escola."

    "Eu pego a cadeira mais próxima e a posiciono de uma forma que eu sento apoiando meu braço no encosto, de frente pra Miya."

    if mc_routes[0] == "Close":
        mc "Eu não sou muito bom com palavras."

        mc "Não sei como dizer isso de outra maneira, mas…"

        mc "Dentro de mim, eu queria aproveitar um último momento contigo."

        mc "A gente vai se formar e…"

        "Eu tento buscar algum pensamento que me ajude a expressar o que sinto, mas a questão é que não tenho nenhuma direção do que vai acontecer quando eu me formar."

        "A maioria das pessoas já teriam alguma faculdade ou um objetivo claro em mente, mas eu não tenho nada, e mesmo tentando imaginar algo, minha cabeça continua vazia."

        "Eu sei muito bem o que a Miya pretende fazer quando nosso ensino médio acabar, mas…"

        "E aí? Como eu posso explicar pra ela que não vou mais poder vê-la porque vou gastar meu tempo sendo um vagabundo enquanto ela estuda?"

        mc "…"
    
    else:
        mc "Esse ano vai ser o nosso último, e depois disso a gente provavelmente não vai mais se ver…"

        "Dizer isso deveria pesar um pouco mas… é estranho que eu consiga falar com tanta naturalidade."

        mc "Eu ainda lembro dos planos que você tem, pra onde você vai se mudar, os cursos que quer fazer."

        mc "Mas, eu nunca me senti assim tão empolgado como você em relação a formatura."

        mc "E muito menos tenho alguma ideia de…"

        mc "Como eu…"

        "\"Vou ser depois de me formar.\" É o que eu queria dizer, mas não tenho a coragem."

        "Não quero admitir isso em voz alta pra ela."

        "…"
    
    mi "As vezes você é muito idiota."

    "Hã? De onde veio isso de repente?"

    "Não, na verdade que se dane, pelo menos ela falou algo."

    mi "Não consegue pensar em nada, não é?"

    mc "É porque eu não tenho ideia do que fazer depois de me formar."

    if mc_routes[0] != "Close":
        "Consegui admitir bem mais rápido do que pensei, na verdade."

    mc "E não vejo como eu seria útil pros negócios da família…"

    "Só de dizer isso em voz alta me faz sentir dor física."

    "Não por eu me achar inútil, mas sim de pensar em ter que ajudá-los com isso."

    mc "Até então não tenho tantas outras opções…"

    mc "E não é como se eu estivesse com mais vontade de estudar depois."

    "Não desgosto exatamente da escola, mas nenhum outro tópico me interessa pra que eu queira estudá-lo numa faculdade ou sei lá."

    "Também não sei se vou conseguir algum trabalho decente sem currículo, me tornar um caixa de uma loja de conveniências não parece tão ruim pra um começo."

    mc "Meu plano é lidar com as coisas da forma que elas são e… seguir com a vida."

    "Ouvir tudo o que eu disse faz ela sair da sua posição habitual e se ajeitar na cadeira."

    "Ela rapidamente limpa sua manga que ficou suja da poeira da janela e se vira pra mim, apoiada da mesma forma que eu."

    return

label classroom_A_1b:
    "Sinto meu coração batendo forte, não sei se consigo me aproximar ainda mais desse jeito."

    mc "Eu… não vim até aqui pra falar do meu atraso. Muito menos vim por questão de vir."

    mc "Sei que você deve tá com raiva mas…"

    mi "Não."

    mi "Não precisa dizer mais nada."

    "Ela me interrompe antes que eu possa continuar. Sua voz é firme, mas ao mesmo tempo delicada."

    mi "Eu continuei aqui porque senti que você viria, cedo ou tarde."

    mi "Se fosse necessário eu esperaria até meia noite também."

    mi "Não importa o quão pior você seja, eu sei quais são os seus limites."

    mi "E me deixar no meio da escola sozinha, à noite, passa bem longe deles."

    "No começo, quando eu recebi aquela mensagem pela primeira vez, eu pensei que ela só estava sendo a Miya."

    "Querendo me enganar pra se divertir com a ideia de eu ter realmente ido por um convite surreal e besta."

    "Mas estranhamente tive a certeza que era algo sério, e depois de racionalizar bastante, minhas escolhas eram ser enganado ou possivelmente nunca mais vê-la."

    "Era óbvio o que eu ia escolher, mas durante esse tempo inteiro eu tentava me convencer de alguma forma contrária a não ir."

    if mc_routes[0] == "Close":
        "Não importa o quanto minha mente tentasse, ela não superou a parte de mim que se preocupa com a Miya."

        "Mesmo eu tão distante de mim quanto dela, ainda lembro de tudo o que passamos e de qualquer coisa insignificante que faz parte de nós dois."

        "E é claro que nada disso se compara com o que tô sentindo nesse exato momento e com o que tá prestes a acontecer."

        "De longe sou capaz de consertar os erros que já cometi, e eu não sinto que tenha algo quebrado entre nós dois que precisa de conserto."

        "O que eu preciso fazer é ouví-la, ouvir suas palavras, ouvir seus pensamentos e sentimentos."

        "Quero ouvir o verdadeiro motivo pra ela ter me pedido pra vir aqui."

        "Diretamente da boca dela."
    elif mc_routes[0] == "Distant":
        "E eu quase consegui, por pouco eu não dei meia volta e voltei pra casa."

        "O clima tá bem frio, eu tô cansado e muito menos tava com saco pra tudo isso."

        "Mas agora eu preciso escutar o que ela tem a dizer."

        "Eu quero saber a verdade por trás das palavras dela."

        "Se isso puder me ajudar a realizar de alguma forma alguma coisa entre nós, ou, até mesmo dentro de mim, já valeria o esforço."

        "Então pra que eu acabe essa confusão na minha mente de uma vez por todas, eu vou passar essa noite com ela."
    else:
        "E eu sinto que ainda não estou completamente decidido, falta alguma coisa que eu não sei exatamente o que é."

        "Nos últimos 5 meses que eu ignorei a Miya, eu me queixava qual era o real motivo disso."

        "Não era como se eu não fosse autoconsciente, mas eu não ligava pra causa e muito menos pro efeito, as consequências na época pouco me importavam."

        "Mas, o peso de perder a minha melhor amiga definitivamente, não é algo tão simples como ignorar uma mensagem ou evitar contato."

        "Se eu continuar com esse raciocínio vou acabar me perdendo de novo, então se for pra chegar a uma conclusão…"

        "Que seja através das próprias palavras dela."
    
    "Eu me esfrego levemente em um dos encostos da porta pra me apoiar, ela entende isso como desconforto, e eu admito, ela não tá completamente errada."

    mi "O ano já tá acabando…"

    mi "A escola ficará aberta por mais uma semana antes das preparações pro evento de formatura…"

    mi "E eu sei que você não viria em mais nenhum dia além de hoje."
    
    mi "Por isso tô mais feliz por estar certa que você viria do que com raiva de você."

    "Um pequeno sorriso aparece no seu rosto enquanto ela fecha seus olhos por conta de uma brisa que vem de fora da janela."

    "Ela move as pernas um pouco desconcertada, sua voz parece calma, mas o seu corpo…"

    "…"

    "Eu não aguento ver isso."

    "Esse sorriso é falso."

    "Essas palavras são falsas."

    "Não preciso ser nenhum vidente ou médium pra saber que ela tá se segurando."

    "E que botou uma máscara pra tentar fingir que tá tudo bem."

    "Eu sei que ela tá com raiva de mim, pra caralho."

    "E que ela quer descontar tudo o que aconteceu nos últimos seis meses agora."

    if mc_routes[0] == "Close":
        "Mas apontar isso não serviria de nada."

        "Pelo contrário, pioraria ainda mais nossa situação."

        "Se você optou por agir assim, que seja…"

        "A questão é que eu não gosto disso. Não gosto de ver você fazendo isso, porque é quase como se fosse um espelho de mim."

        "Eu não fui o Ren que você conhecia nos últimos meses, e agora você tá sendo uma Miya que eu não faço ideia de quem é."

        "A Miya ainda precisa continuar sendo a Miya, não tem porquê se entregar a isso."

        "Que se foda se eu tô trocando o mundo à fora por uma vida mais monótona e previsível…"

        "Não quero que você faça o mesmo por minha culpa e perca uma das qualidades que eu mais admiro em você."

        "Esse devia ser o certo, então mesmo que leve a noite inteira…"

        "Eu vou te ajudar a se livrar dessa máscara. Nem que seja aos poucos, até que você decida uma hora tirar por conta própria."
    else:
        "Independente de tudo, não posso julgá-la."

        "No fim, isso se trata de um jogo pra ver quem deixa sua máscara cair primeiro."
        
        "E o que vai acontecer depois disso?"

        if mc_routes[0] == "Distant":
            "No mínimo engraçado."

            "E também decepcionante."

            "Você decidiu usar a sua só por essa noite, mas, e eu?"

            "Existe um ditado que, dizem que quando se usa uma máscara por muito tempo, acaba que você nunca usou uma de verdade."

            "E ele está até hoje preso na minha cabeça, com meu consciente as vezes me recordando disso de propósito."

            "Eu continuei seguindo minha vida, dia após dia, como se o mundo não estivesse mais andando."

            "Como se ele estivesse parando o tempo, com todos ao meu redor ainda seguindo seus caminhos normais."

            "Eu desacelerava, e desacelerava, ainda estou desacelerando, e não sei quando isso vai parar."

            "E internamente dói um pouco de ver, por isso não quero que você siga esse caminho."

            "Porque nele não há nada além de uma completa perda de tempo e uma sensação de futilidade."
        else:
            "Dor? Ou felicidade?"

            "Pode tanto ser bom como ruim, se esconder atrás de uma faceta que não é sua significa que existe algum sentimento que você não quer mostrar."

            "Como a forma que uma adolescente comum age quando está próxima do seu crush."

            "Ou do jeito que um adolescente fala quando está próximo dos seus melhores amigos em privado."

            "Tudo se trata dependendo do ponto de vista, e nós dois, não fazemos ideia como é o do outro."

            "Seja lá o motivo pelo qual você quer esconder alguma coisa de mim, eu quero…"

            "Eu quero mesmo descobrir. Pode ser a verdade por trás desse {i}encontro{/i}, ou simplesmente algo que você guarda há tanto tempo."

            "Nunca senti tanto essa vontade de saber mais sobre você, de descobrir o que você sentia quando eu ficava ao seu lado."

            "Eu sei claramente como eu me sinto, e é por isso que eu me recordo de uma forma tão sem graça dessas coisas."

            "Só conheço o meu ponto de vista, e nunca parei pra me perguntar e conhecer o seu."
    
    # TODO: Continuar a história daqui, abaixo será descartado/reutilizado depois

    "Eu não sei o que ela estava pensando antes de eu entrar na sala, ou o que ela decidiu enquanto eu tava lá fora."

    "Vendo que a chance de eu não aparecer hoje era uma possibilidade, talvez ela tenha passado por um turbilhão de coisas em sua mente assim como eu."

    "Acabar pensando demais, enquanto tenta procurar mil e uma justificativas, tudo isso pra no final não chegar à lugar nenhum."

    "Isso não combina com a Miya, é por isso que vê-la assim só me deixa mais vazio."

    # Provavelmente vou reutilizar isso, gostei mt dessa parte, é uma rara brecha em que ela quer ele por perto mesmo sentindo 1001 coisas
    # dá a entender que só quer conversar mais perto, ou, "tu teve o trabalho de vir aqui e vai ficar na porta? porra, não fode", sendo que
    # o significado é outro e mais fofo de "por favor, fica perto de mim, eu te quero" enquanto ainda sente "mlk vai toma no cu desgraçado"
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

        "Talvez eu esteja vendo o que quero ver."

        "É como se a Miya estivesse cruzando por essa linha ocupando ambos os lados."

        "Ao mesmo tempo que não é justo pra mim… eu não fui justo com ela no passado."

        "De tanto pensar, já tem um tempo que minha perna tá balançando sozinha."

        "A Miya nota esse meu nervosismo e sorri pra mim, quase como um sorriso de alívio por não ser a única."
    
    "…"

    return

label classroom_A:
    stop music fadeout 2.0

    scene bg school_classroom
    with contextchange

    # não exatamente a arte que é pra aparecer, mas só pra ficar o placeholder na frente do que apenas o background
    show miya basic_annoyed at truecenter
    with charchange

    # Aqui vejo ela falando numa pose que cerra os olhos, tipo de desaprovação, enfim, usar a pose que mais encaixa com base nas artes finais
    mi "Você é mesmo um completo idiota." 
    return