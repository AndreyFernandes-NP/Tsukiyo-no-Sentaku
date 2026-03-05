### Audio/Sound system definitions

define corridor_ambience_sfx = [
        {"file": sfx_tree_rustle, "tags": ["tree"], "vol": 0.2},
        {"file": sfx_tree_rustle_intense, "tags": ["tree"], "vol": 0.1},
        {"file": sfx_tree_rustle_soft, "tags": ["tree"], "vol": 0.2},
        {"file": sfx_wind_howl_1, "tags": ["wind"], "vol": 0.3},
        {"file": sfx_wind_howl_2, "tags": ["wind"], "vol": 0.3}
]

### IMPORTANT STORY DEFINITIONS/DEFAULTS
### Character Thoughts / Personality

default mc_personality = ["Ren is calm, introspective, and observes before acting. He avoids emotional confrontation and rarely reveals his feelings. He lives with an internal conflict between what he feels and what he believes he should feel. Tonight, something is changing that, for better or for worse."]

# Define the type of routes taken by the player for each main scene.
# Mostly used to have different types of dialogue and even generation based on choices.
# Starts with an empty list, and appends route types for each scene.
# In order we have: corridors scene, classroom introduction scene... etc. (Add the rest later)
# E.g. ["A", "C"] means the player took approach A from the first scene, the corridors, and C for the next scene, classroom introduction.
default mc_routes = []

default miya_personality = ["Miya is quietly cheerful and outgoing, sometimes impulsive. She values friendship and loyalty, even to the point of stubbornness. Her energetic nature can both uplift and overwhelm those around her. She speaks her mind when comfortable, but can also retreat into silence when she feels unsure. Tonight, she wants Ren alongside her, even if it hurts."]

### Scenes Context
default corridor_context = ["It's late at night, around 11 PM. The school is quiet and empty. Ren stands at his classroom door, hesitating after Miya, his childhood friend, asked him to meet her here. Their friendship has grown distant recently. Now, he's moments from stepping inside."]

### Choices dictionaries

define routes_corridorA = {
        "opt1": "corridors_Aa",
        "opt2": "corridors_Ab",
        "opt3": "corridors_Ac",
}

define routes_corridorB = {
        "opt1": "corridors_Ba",
        "opt2": "corridors_Bb",
        "opt3": "corridors_Bc",
}

define routes_corridorC = {
        "opt1": "corridors_Ca",
        "opt2": "corridors_Cb",
        "opt3": "corridors_Cc",
}

### Ervilha Testing
define miya_poses = {
        "basic": {
                "neutral": ["Nome: miya_basic_neutral\ncaminho: sprites/miya/miya_basic_neutral.png", "Essa é a pose neutra da Miya, com uma expressão normal, serena, de pé e com os braços pra trás.", "Seria usado na verdade em poucas situações, já que como a quantidade de variações/emoções pra cada pose é alta, todas serão sempre trocadas entre si."],
                "impressed": ["Nome: miya_basic_impressed\ncaminho: sprites/miya/miya_basic_impressed.png", "Essa pose seria ela sutilmente impressionada ou surpresa com alguma coisa, pode ser uma fala ou até escolha do MC que a fez ficar assim."], 
                "grin": ["Nome: miya_basic_grin\ncaminho: sprites/miya/miya_basic_grin.png", "Um sorriso mais largo ou mais sutil dependendo, é quando ela fica levemente felizinha com algo, pode até fazer ela de olhos fechados, mas ai teria que deixar claro como  miya_basic_grin / closed_grin."],
                "smug": ["Nome: miya_basic_smug\ncaminho: sprites/miya/miya_basic_smug.png", "Essa aqui seria um sorrisinho mais smug, não exatamente >:3, mas, um tantinho parecido quando ela fica se achando de alguma coisa."],
                "happy": ["Nome: miya_basic_happy\ncaminho: sprites/miya/miya_basic_happy.png", "Essa é a pose de felicidade da Miya, um sorriso aberto (ou não, depende), alegre, com os olhos brilhando. Seria usada quando ela estivesse genuinamente feliz ou animada por algo."],
                "sad": ["Nome: miya_basic_sad\ncaminho: sprites/miya/miya_basic_sad.png", "Essa aqui ela teria um olhar não exatamente triste, porém mais pra baixo desviando o olhar, o cachorrinho triste é em outra pose, aqui ela está genuinamente triste ou sentida e não fazendo manha."],
                "confused": ["Nome: miya_basic_confused\ncaminho: sprites/miya/miya_basic_confused.png", "Esse aqui é uma confusão síncera, e não aquele rosto de pássaro confuso que seria mais ou menos fofo como em outra pose, aqui ela não entende o que o protagonista expressa ou diz."],
                "shy": ["Nome: miya_basic_shy\ncaminho: sprites/miya/miya_basic_shy.png", "Essa aqui ela teria uma expressão tímida, evitando olhar diretamente para o protagonista, com os olhos baixos e um sorriso leve."],
                "annoyed": ["Nome: miya_basic_annoyed\ncaminho: sprites/miya/miya_basic_annoyed.png", "Essa aqui ela teria uma expressão de irritação ou descontentamento, com o cenho franzido e os lábios apertados (ou não), seria mais um, irritadinha do que sentindo raiva de verdade."],
                "angry": ["Nome: miya_basic_angry\ncaminho: sprites/miya/miya_basic_angry.png", "Essa aqui ela teria uma expressão de raiva, com o cenho franzido, não é algo tão óbvio mas anda assim você nota quando ela tá com raiva só de ver."]
        },
        "worried": {
                "neutral": ["Nome: miya_worried_neutral\ncaminho: sprites/miya/miya_worried_neutral.png", "Essa é uma pose um tanto mais aflita da Miya, ela teria os braços cruzados na frente do peito com um deles apoiado no busto.", "Algumas expressões também podem mudar as mãos, deixando ou elas fechadas ou elas abertas como se ela sentisse o próprio batimento cardíaco."],
                "shocked": ["Nome: miya_worried_shocked\ncaminho: sprites/miya/miya_worried_shocked.png", "Seria um chocado mais forte, já que ela também está preocupada, é aquele momento em que você sente uma tensão logo dentro de si, quase um pequeno caláfrio ou as vezes até mesmo um calafrio."], 
                "unsettled": ["Nome: miya_worried_unsettled\ncaminho: sprites/miya/miya_worried_unsettled.png", "Essa expressão seria uma de desconforto, quase como se ela sentisse que algo ruim vai vir, nisso dá pra dizer que ela fecha o punho com mais força naturalmente."], 
                "sad": ["Nome: miya_worried_sad\ncaminho: sprites/miya/miya_worried_sad.png", "Essa aqui ela teria um olhar de preocupação e tristeza, com os olhos baixos e uma expressão de inquietação. Seria usada quando ela estivesse mais preocupada ou triste por algo que o protagonista expressa ou faz."],
                "happy": ["Nome: miya_worried_happy\ncaminho: sprites/miya/miya_worried_happy.png", "Essa aqui ela teria um sorriso triste, meio que um sorriso de quem tá tentando se animar ou animar o protagonista, mas ainda assim tem uma preocupação ali, é aquele sorriso que você dá quando quer tentar ser positivo mas não consegue deixar de sentir aquela pontinha de preocupação.", "Um bom indicativo seriam os olhos passando dúvida ou incerteza, ou ela desviando olhar enquanto sorri e etc."],
                "silent_happy": ["Nome: miya_worried_silent_happy\ncaminho: sprites/miya/miya_worried_silent_happy.png", "Aqui o sorriso dera seria meio silencioso, acho que nessa se encaixaria mais o fato dela desviar o olhar e brevemente levantar a boca como um sorriso (que nem naquela imagem que vimos), mas seria uma felicidade mais sincera que outra."]
        },
        "angry": {
                "neutral": ["Nome: miya_angry_neutral\ncaminho: sprites/miya/miya_angry_neutral.png", "Nessa pose em principal ela vai estar com os punhos cerrados, os braços estariam mais juntos seja na frente do peito, cintura, mas seria algo mais parecido que a posição do corpo na pose padrão.", "Nessa daqui dá até pra criar outras variações das mesmas expressões, já que pode ser bem ampla pra indicar uma raiva tsundere, ou raiva sincera."],
                "annoyed": ["Nome: miya_angry_annoyed\ncaminho: sprites/miya/miya_angry_annoyed.png", "Não exatamente ela estaria puta de verdade aqui, pode ser tanto usado num pequeno momento tsundere de raiva, como na verdade ela começando a ficar irritada mesmo, se passar essas duas impressões, perfeito."], 
                "shout": ["Nome: miya_angry_shout\ncaminho: sprites/miya/miya_angry_shout.png", "Aqui ela já começa a demonstrar raiva, a boca está bem aberta podendo ver alguns dentes (ou um dentinho) dela, onde ela levantaria a voz contra o protagonista, mas não exatamente gritar.", "Pode ter variação de pose como ela com os braços cruzados e a boca mais aberta e afins."], 
                "closed_shout": ["Nome: miya_angry_closed_shout\ncaminho: sprites/miya/miya_angry_closed_shout.png", "É ela levantando o tom mas com os olhos fechados, só uma pequena variação do shout."],
                "sad": ["Nome: miya_angry_sad\ncaminho: sprites/miya/miya_angry_sad.png", "Ela está com raiva, ela está triste, parabéns MC pelo o que você fez, não é um sad bom aqui, ela está genuinamente triste e com raiva de ti."],
                "smug": ["Nome: miya_angry_smug\ncaminho: sprites/miya/miya_angry_smug.png", "Essa aqui poderia ser tanto usada de maneira divertida/tranquila, como apenas pra botar pressão ainda mais na cena, um exemplo seria 'Ren, eu te trai.' e ai ela demonstra um sorriso mais vingativo ou smug."],
                "mildly_smug": ["Nome: miya_angry_mildly_smug\ncaminho: sprites/miya/miya_angry_mildly_smug.png", "É uma variação mais suave do smug, onde ela demonstra um sorriso levemente vingativo ou satisfeito."],
                "furious": ["Nome: miya_angry_furious\ncaminho: sprites/miya/miya_angry_furious.png", "RAIVA! ÓDIO! PARABÉNS PLAYER, O QUE VOCÊ FEZ PRA MIYA FICAR TÃO PUTA CONTIGO? NÃO FAÇO IDEIA, MAS PARABÉNS!", "Nesse nível ela estaria tão puta da vida que a expressão já se contorceria um pouco, ela até socaria o MC se pudesse ,ou simplesmente saísse fugindo. Se o player focar em só fazer merda e dizer o pior, ela vai ficar frustrada consigo mesma e muito puta, logo, ativaria esse sprite."]
        },
        "shy": {
                "neutral": ["Nome: miya_shy_neutral\ncaminho: sprites/miya/miya_shy_neutral.png", "A posição do corpo seria parecida com a da posse normal, mas os seus braços estariam pra trás, como se uma mão segurasse na outra (só visualização mental mesmo, não vai ter como ver).", "A pose de Shy seria uma que mais aconteceria em momentos positivos ou felizes, ainda mais nos intimos, então, não rolaria em situações ruins (ou raramente)."],
                "timid": ["Nome: miya_shy_timid\ncaminho: sprites/miya/miya_shy_timid.png", "Sim, um envergonhado tímido, dá pra colocar ela com um leve blush, ou talvez, nem precise, mas sim que ela se sente mais tímida, olhando pro chão/pra baixo."], 
                "blush": ["Nome: miya_shy_blush\ncaminho: sprites/miya/miya_shy_blush.png", "Ela aqui olharia pro MC de uma forma envergonhada, com um blush sincero, pode deixar as pupilas/os olhos pequenos, ou normais porém com ela transmitindo mais vergonha."], 
                "smug": ["Nome: miya_shy_smug\ncaminho: sprites/miya/miya_shy_smug.png", "É o padrão anime, o famoso smug fofinho tímido, esse aqui é bem óbvio, então confio na sua criatividade."],
                "happy": ["Nome: miya_shy_happy\ncaminho: sprites/miya/miya_shy_happy.png", "Ela está felizinha enquanto também se sente envergonhada, é o combo perfeito pra alguns momentos mais próximos que eles vão ter, ainda mais quando o protagonista falar algo desse calibre, logo, segue o que sua imaginação desejar."],
                "sad": ["Nome: miya_shy_sad\ncaminho: sprites/miya/miya_shy_sad.png", "Nesse aqui ela não vai estar necessariamente triste, pode ser usado em algumas situações positivas ou que são mais pra baixo, se o MC falar algo fofo ou fazer ela rir logo após chorar ou algo parecido, provavelmente essa expressão entraria em cena."],
                "grin": ["Nome: miya_shy_grin\ncaminho: sprites/miya/miya_shy_grin.png", "Um sorriso tímido, meio envergonhado, que a expressão dela já fala tudo o que devia falar só de você a observá-la."],
                "confused": ["Nome: miya_shy_confused\ncaminho: sprites/miya/miya_shy_confused.png", "É um tímido/envergonhado confuso, bom ou ruim, depende muito do contexto, mas que serviria ambos os lados quando precisasse."],
                "annoyed": ["Nome: miya_shy_annoyed\ncaminho: sprites/miya/miya_shy_annoyed.png", "Esse aqui tá mais pra uma emoção de tsundere, ela fica irritadinha mas é quase no bom sentido, não vejo eu usando isso pra algo ruim ou ela com raiva de verdade, seria mais de sacanagem mesmo, nível das tsundere ou parecido."],
                "shocked": ["Nome: miya_shy_shocked\ncaminho: sprites/miya/miya_shy_shocked.png", "Ela aqui estaria surpresa, com os olhos bem abertos e a boca em forma de 'O', transmitindo um choque real. Ao mesmo tempo, pode ser também um pouquinho súbito se achar que ficaria melhor."],
                "really_shy": ["Nome: miya_shy_really_shy\ncaminho: sprites/miya/miya_shy_really_shy.png", "Essa aqui é o nível máximo de timidez, ela está tão envergonhada que mal consegue olhar pro protagonista, talvez até esconda o rosto com as mãos ou algo do tipo, mas é aquele tipo de timidez que é tão intensa que chega a ser fofa."]
        }
}