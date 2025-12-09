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

    "Who am I trying to fool?"

    "Ever since I left home, I haven't stopped wondering if this was actually the right choice."

    "The breeze brushing against my back gives me a slight chill, but it's more than that."

    "It's enough to remind me where I am, and why I came here. Even though summer's almost here, the night has no intention of feeling any less cold."

    "The rustling of the leaves, the trees creaking as they sway from side to side… all of it has been sending shivers down my spine."

    "Damn it. So much effort, yet for what? I didn't want to be here, but it's not like I had any other choice, not after what I received earlier."

    "'Ren, I know this sounds sudden, but could you meet me at school tonight? I really need to talk to you.'"

    "I pull my phone from my pocket and stare at Miya's message. It's become a habit ever since I started walking here."

    mc "School… at night."

    "'Around 10 is fine, right? In our classroom. I'll be there.' I check the time once again, it's already 10:50 p.m."

    with Pause(1.0)

    mc "Aaah…"

    mc "Shit."

    mc "How did I manage to get this late?"

    "You know how. It's at most a twenty-minute walk from house to school, but I spent the entire time lost in my own head about this…"

    "When I put my jacket on, it was already ten. And by the time I stepped outside, twenty minutes had passed."

    "I let out a sigh, feeling the weight of that message all over again. I don't know what's waiting for me, but it's not like I'm turning back now."

    "So I take a deep breath, I still need to calm down. What does Miya even want to talk about? Actually… is there really anything left to talk?"

    "We haven't been messaging each other as much as we used to. At some point, it felt like I didn't see much reason to talk to her anymore."

    "But I can't deny that I miss it. I miss her."

    "Our friendship goes way back, we were childhood friends, and I always believed that would never change."

    "Our families were close. We always saw each other at parties, trips, gatherings, even during summer vacations."

    "I practically lived at her house when we were kids, and she at mine. We spent all our time together, and she was always like a younger sister to me."

    "Her smile, her way of acting, her cheerful personality…"

    "I'd watch all of that in her, and feel a certain comfort in having someone like that by my side."

    "But that wasn't exactly right."

    "It wasn't like it all happened by chance, our parents were very close because of the family business. That goes back generations."

    "That's why I never felt like our friendship was something natural."

    "Our mothers are childhood friends just like we are, and our fathers have known each other since they were born."

    "The older generation always made sure to keep the families close, and that became very clear to me as I grew up."

    "The time I spent with Miya, all of the trips, our chit-chats, it kinda felt like an obligation more than anything real."

    "As if we were destined to be friends just because our families wanted it. More like a business arrangement than anything else."

    "But not for Miya. She always looked genuinely happy to be around me, even if everything was pushed by our parents. She wanted to be by my side."

    "And I always felt guilty for not being able to reciprocate that feeling."

    "I was never great at making friends, not because I wasn't sociable, but because I didn't really care. But with Miya… she was the only person I ever got close to."

    "And that's why it bothers me to think this way."

    "That our friendship is nothing more than… a social contract."

    "…"

    mc "Goddammit."

    mc "Why am I even thinking like this?"

    "I don't want to think this way."

    "I don't want to believe that everything I feel about Miya is fake."

    "But at the same time… it's not like we have anything truly genuine."

    "And if our families weren't close… would we still be friends?"

    "Would we have even met?"

    "Would I still care about her the same way?"

    "Would I still want to be by her side, no matter what?"

    "I don't think it's fair for me to think like that."

    "It's not fair to her."

    "For the past fifteen years, we've been through so much together, from when we first met beside our mothers… up until tonight."

    "Everything we lived through, everything we talked about…"

    "What do I really think about my past with Miya?"

    return

label choice_corridorsA:   
    menu:
        with menueffect
        "I had fun.":

            return "opt1"
        "I can't blame her.":

            return "opt2"
        "She was annoying.":

            return "opt3"

label corridors_Aa:
    $ mc_personality.append("He carries some nostalgia for the carefree days of his childhood with Miya.")

    "Of course I had fun."

    "No matter how much I try to complicate things now, there's no way to erase what I felt back then."

    "I remember all the times we laughed so hard it felt like we were going to die. All the stupid things we did, the random conversations, the afternoons that ended way too fast."

    "They were simple moments… but they were ours."

    "We played hide-and-seek in her backyard, grabbed brooms and pretended they were swords, she'd come up with crazy stories and dragged me into them."

    "And when it rained, we'd hide on the porch and just watch the water fall, talking about nothing and everything at the same time."

    "There were no expectations. No pressure. Just the moment."

    "You don't need obligation to laugh like that."

    "Even when our families pushed us together, there were moments when I completely forgot about it. Moments when having her around felt… natural."

    "And I never admitted that out loud."

    "Not even when we became teenagers, and things started to change."

    "Maybe I just took everything for granted. Maybe I thought it would last forever."

    "But now, standing here in this dark hallway, thinking about the past…"

    "I realize those were some of the best moments of my life."

    "We really cared about each other, for real."

    "And even if I still have doubts about what all of this means… I know I had a great time."

    "Still…"

    return

label corridors_Ab:
    $ mc_personality.append("He feels guilty for not reciprocating Miya's efforts in their friendship.")

    "It's not like I can blame her or her family for any of this. And honestly, I can't even blame myself."

    "For years, I tried to believe our friendship only existed because our families wanted it that way. It was easier to think like that."

    "If everything was just the result of an obligation, then I didn't have to admit that I never knew how to deal with what I felt."

    "It was more comfortable to blame the circumstances than face the truth."

    "Miya was always the one who started conversations. The one who asked if I wanted to hang out. The one who took the initiative."

    "I was just… there."

    "I was always the one keeping my distance."

    "She tried to bring our worlds closer, while I insisted on keeping mine small, controlled, comfortable."

    "Maybe I was afraid of depending on her too much."

    "Or afraid of realizing that without her friendship… I wouldn't have anyone else."

    "And even then, she never pressured me. Never threw her effort in my face. Never made me feel like I owed her anything."

    "She just… kept being herself."

    "And now that we're distant, I can see how much I hid behind excuses."

    "I kept saying our friendship was forced because it made it easier to justify why I couldn't reciprocate."

    "But the truth is, she was always honest with me."

    "I was the one who never had the courage to be honest with her."

    "I can only take responsibility for my part."

    "At least now I can see that clearly."

    "After all…"

    return

label corridors_Ac:
    $ mc_personality.append("He struggles to admit his true feelings for Miya, masking them with irritation.")

    "She was annoying."

    "At least… that's the label I gave to her."

    "She talked too much, laughed too loud, tried to make friends with everyone. She walked into my life way too easily, like she didn't need permission."

    "She pushed me out of my comfort zone. Dragged me to places I didn't want to go, made me join things I swore were stupid."

    "And I hated that."

    "It was annoying."

    "Or… maybe I only said that because it was easier than admitting I liked it."

    "Because in the end, she was the one who made me feel alive."

    "Every time she grabbed my arm and said, 'Come on, Ren, trust me,' it felt like the world got a little lighter."

    "And that scared me."

    "I don't know how to deal with people who walk into my life without knocking."

    "Let alone someone who can actually see me."

    "So I said she was annoying. Because admitting the opposite would mean admitting she mattered."

    "But now, after all this time, after all my attempts to push her away…"

    "If I really didn't like her, why do I remember everything so clearly?"

    "No one is annoying enough to leave that kind of mark."

    "Maybe I was just protecting myself. Maybe I still am."

    "Because feeling something has always been way scarier than feeling nothing."

    "And today is one of the worst days to feel that."

    "In the end…"

    return

label corridors_B:
    "The one to blame for all of this is still me."

    "If it weren't for me, I wouldn't be here right now."

    "Or better… I wouldn't be in this situation."

    "Whatever happened between me and Miya didn't come out of nowhere. It happened little by little."

    "And I remember every chance I had to stop it from getting here."

    "I'm the one who pulled away, and even noticing it, I did nothing."

    "Sometimes I thought, 'I should message her,' or, 'I should reply quickly this time,' but I never did."

    "I even wondered if it bothered her, but that thought disappeared as fast as it appeared."

    "I let everything reach this point, and whenever I asked myself why… I could never find an answer."

    "I just felt… empty. Indifferent. And I threw any excuse on top of it to justify that."

    "Something like, 'Isn't it normal for people to drift apart over time?' And yeah, that's true."

    if seen_label("corridors_Aa"):
        "Even though I had so much fun with her back then… it felt like all of that had lost its value."

        "Like it was wrong to miss it."

        "Like it was wrong to want to relive something that's already gone."

        "But realistically, what matters is the present, and right now, I don't see the world the same way."

    "You barely notice when you send your last message to someone important."

    "You don't notice when it's already too late to try again."

    "But it's these doubts, these uncertainties, that bother me so much."

    "What does all this mean to me? What am I supposed to do with it?"

    "Should I try to become a better person? How?"

    "I really wish I had an answer, but the more I think, the messier everything gets."

    "Even as childhood friends… I guess not even a friendship like that is immune to problems like these."

    "We're two completely different people now."

    "Our social circles aren't the same, she's always surrounded by people, always going out whenever she gets the chance. And me? I barely talk to one or two people in my class."

    "We don't have anything in common anymore, and I always tried to believe that wasn't a problem."

    "Everything's changing so fast that I don't even know if I can keep up."

    "Maybe in the future I'll just end up frozen in time somehow."

    "Sometimes I just wish everything could be simpler."

    "But I guess that's more nostalgia talking than anything else."

    "At least with Miya, things really did feel simpler."

    mc "…"

    "Is there anyone else in the world going through something like this right now?"

    "Or am I the only one tonight feeling this way?"

    "I don't know."

    "I don't know anything anymore."

    "I thought I knew Miya, but now… I'm not even sure."

    "Maybe I don't even know myself. If I can't understand me, how the hell am I supposed to understand someone else?"

    "Maybe she changed too, and I just didn't notice. But it feels like her change was for the better… I think."

    "Since she's always been so outgoing, I started thinking maybe she found someone new. Or a new group of friends that makes her feel happier."

    "Part of that might be true. But maybe I'm just trying to convince myself of that."

    "Like it's just another excuse for why I drifted away."

    "I don't know."

    "Maybe I'm scared of ending up alone."

    "Or maybe I'm just scared of continuing to feel nothing."

    "Why am I so hung up on this?"

    "I don't know. I don't know, and I don't know."

    "I never know anything when it comes to this stuff."

    "Deep down…"

    "Maybe I don't even need her anymore, right?"

    return

label choice_corridorsB:   
    menu:
        with menueffect
        "No, that's not how it works.":

            return "opt1"
        "I can't make up my mind.":

            return "opt2"
        "Things are just the way they are.":

            return "opt3"

label corridors_Ba:
    $ mc_personality.append("He rejects the idea of giving up on their friendship and wants to fight to keep Miya in his life.")

    "No. What was I even thinking?"

    "I can't just give up out of nowhere."

    "Miya is still my childhood friend, that's something that's never going to change."

    "I can't let this distance erase everything we've been through."

    "The memories we have together mean a lot to me. And I know they mean a lot to you too."

    "If I don't try, I'll never know what could've happened. And I don't want to live with that regret."

    "Even less do I want you to live with it."

    "I take a deep breath, trying to push these negative thoughts away."

    "I can't let this consume me."

    "If I want things to go back to how they were, then I'm the one who has to put in the effort."

    "I came all the way here because I need to talk to her, and that's exactly what I'm going to do."

    return

label corridors_Bb:
    $ mc_personality.append("He feels torn about his feelings towards Miya and is unsure of what to do.")

    "It's not easy to think of an answer."

    "I don't even know what I really want."

    "I just know I don't want to feel like this."

    "I don't want to feel this lost."

    "Being childhood friends isn't something that disappears overnight, but I don't know if that's enough."

    "No matter what I do, I don't know if things will ever go back to how they were."

    "I don't even know if I want them to."

    "One thing I hate are empty promises, and I don't want to make one of those to Miya."

    "I don't want to disappoint her, but I also don't want to disappoint myself."

    "I'd love to still be her friend, but… would she even want that?"

    "Am I still important to her?"

    "No, I know I am. That's why I'm here. But at the same time, I don't know if I can live up to what she expects from me."

    "Damn it… it may not look like it, Miya, but I still care a lot about our friendship."

    "I just don't know how to act, or how to put any of this into words."

    "I don't know what I want, and I don't know what you want."

    "I just don't know, and because of that, I end up going with the flow. Whatever happens, happens."

    "But why does that bother me so much? It feels like I'm not the one in control."

    "Actually… what does it even mean to have control?"

    "Wanting to walk in one direction but always ending up somewhere else."

    "In that case, does the destination always matter?"

    "Does it matter, or am I just fooling myself?"

    "Maybe I just need to stop overthinking everything."

    "If I'm here, it's because I want to be."

    "And if I want to be here, it's because I want to talk to Miya."

    "And if I want to talk to you, Miya, it's because I still care about you."

    "So just for today… just for tonight… I want to be the one in control."
    
    return

label corridors_Bc:
    $ mc_personality.append("He tries to rationalize his feelings and the situation, but remains uncertain and conflicted.")

    "I don't know if this is something I can control."

    "And I don't know if it's something I even want to control."

    "I don't know if I want things to be different."

    "We're childhood friends, but we're not kids anymore."

    "I don't know if I want us to go back to being as close as we used to be."

    "It's not like we're bound together by some unbreakable tie or anything."

    "I don't know if I want that…"

    "But I also don't know if I want the opposite."

    "Being away from you, Miya, does bother me."

    "But wouldn't it be weird if, after all this time, we suddenly went back to being that close?"

    "Maybe you see it differently, I don't know. Maybe this discomfort is just mine."

    "Maybe you actually want distance."

    "Or maybe you want to be just as close as before."

    "Damn it, I don't know, and I'm tired of not knowing."

    "Why does everything have to be so complicated?"

    "Why can't I just accept things the way they are?"

    "Everything was fine, I was living my life normally, and now… this?"

    "It's just a message, but damn, why is it messing with me this much?"

    "Or am I just fooling myself?"

    "Maybe I wanted to talk about this as much as you did, and just the idea of seeing you again is making me feel like this."

    "It feels wrong not to try. Wrong to just leave things as they are."

    "And that's why everything feels so confusing. I don't even know what I truly want anymore."

    "But I do know I want to see you. And that's why I'm going to try, even if I have no idea what comes next."

    "At least for one last time, Miya."

    return

label corridors_C:
    "Because everything I've done up until now led me here."

    "Everything I've been thinking, everything I've been feeling… it all seems so small compared to this moment."

    "And that's why everything feels so strange. I'm stuck between my past and my future, and now… everything comes down to a single step."

    "But I don't know if I can take that step. Or if I even want to."

    "Why does everything have to be summed up to this?"

    "Actually, why do I have to define everything right now?"

    "Why can't I get {i}everything{/i} out of my head?"

    "One step, and everything changes."

    "One step, and I'm closer to you."

    if seen_label("corridors_Bc"):
        "Or maybe further away for good."

        "And I'd still be alone, not knowing what to do."
    else:
        "And closer to whatever I'm going to feel after this."

    "I don't know what it's going to be like when I open this door. I still don't understand why I can't bring myself to turn the handle."

    "But anything that involves your name never goes the way I expect. It's always been like that with you."

    "All I know is that whatever happens, maybe I'll finally understand something."

    "Maybe I'll finally understand what I really feel about you."

    "Maybe I'll understand what I really feel about myself."

    "But people say some things aren't meant to be understood."

    "That you're supposed to just feel them. And I think it's time to do that, or at least just try."

    "Relationships were never my forte, and I've always avoided getting too involved."

    "One way or another, I ended up involved anyway. Maybe that's why I was never exactly popular with people."

    "I never saw that as a problem, to be honest, but thinking about it now…"

    "Not knowing how to deal with any of this is one of the main reasons I'm here."

    "Honestly, it'd be kind of funny if I opened this door and you weren't even here."

    "So many things could have happened differently to make that possible, and even then, here I am, in the middle of the school at 11 PM, just to see you."

    "I don't know what made you want to call me here, but what bothers me the most is understanding why you chose to do it this way."

    "I guess it's too late to feel embarrassed."

    "Your strategy worked, but that doesn't mean I'm happy about it. It's just that I don't have any other choice now."

    "No matter what I think, I can't find a single reason to go back home."

    "And I wish I could find one, any excuse at all, just so I wouldn't have to face this."

    "But running away from you is hard. You always made that clear, whether it was in our childhood games or when you pushed me into things I didn't want to."

    "Even so, I can't help thinking about how things could have been different."

    "Not that it matters now, it's not like I can go back in time."

    "And even if I could, I don't know if I'd have the courage to change anything."

    "Because in the end, everything that happened…"

    "Led me right here."

    "Whether that's good or bad, I have no idea."

    "But at the very least, whatever happens after this…"

    "We won't be the same."

    "Maybe that's the elephant in the room I'm refusing to look at. I wanted everything to stay the same, but I'm almost sure it won't."

    "I'm not someone who takes risks, but you're the one who bet everything on tonight. And the worst part is, if I don't want to lose, I have to go {i}all-in{/i} too."

    "How long did you even plan this? Actually, was there even a plan?"

    "And if I hadn't shown up, what would you have done? If you're behind this door waiting for me, how long would you have waited?"

    "You do things impulsively without thinking about the consequences most of the time, but you do them. Meanwhile, I slow everything down on my side."

    "Maybe I really do need to learn something from you, to stop overthinking everything so much."

    "But at the same time… that's part of who I am. Changing that would mean losing a piece of myself, and it'd be really hard."

    "It's like a habit shaped over years and years, not necessarily a good habit, but one that's part of me now."

    "But it's funny how you've always been there in my most extreme moments."

    "My life could be monotonous, predictable, but still satisfying… until you showed up. In our childhood, in our teens, and even now."

    "Like, seriously, I climbed a two-meter wall just to see you."

    "I broke into the school at night. Luckily there's no one here, no security, janitors, nothing."

    "I wouldn't even be surprised if I ran into some couple hiding somewhere, making out behind a tree or something."

    "Maybe I'll even run into a ghost, seeing as the school gives me chills at night."

    "I would've never done any of this if it weren't for you."

    if not seen_label("corridors_Bc"):
        "And as hard as it is to admit, I felt more alive tonight than during a lot of the predictable days I've been having."

        "It's not something I want to feel all the time, but… it's good to know I'm still capable of it."

    "Maybe the real problem is that I'm uncertain about everything."

    "I don't know what I want, I don't know what I feel, and I don't know what I expect."

    "In the end, I don't even know what I am."

    "So if I'm going to be honest with myself…"


    return

label choice_corridorsC:   
    menu:
        with menueffect
        "I'll go all the way.":

            return "opt1"
        "I'll only know if I try.":

            return "opt2"
        "Maybe nothing'll change.":

            return "opt3"

label corridors_Ca:
    $ mc_personality.append("He's determined to face his feelings and the situation head-on, regardless of the outcome.")

    "I've thought too much already, doubted too much. Tried to convince myself otherwise so many times…"

    "But if there's a moment to stop running, it's this one."

    "Maybe I'm wrong."

    "Maybe I'm fooling myself."

    "Maybe I won't even be able to say what I really feel when I look at you."

    "But it doesn't matter."

    "None of that matters anymore. What matters is that I'm here, and I'm going all the way."

    "I'm done hiding, I came this far because a part of me wants, needs to understand what's still left between us."

    "I'll stay on this tightrope and walk it to the other side."

    "The side where you are, the side where you're waiting for me."

    "And if I hesitate now, I'll never forgive myself. I don't want to live with another regret."

    "I might not care about this in the present, but I know that in the future I'd blame myself for not trying to move forward."

    "Just like I blame myself sometimes for things I never did in the past."

    "For all the opportunities I let slip away, for all the moments I never lived because I felt uncertain about everything."

    "At the very least, now I want to try."

    "I want to start living my life a little more like you do."

    if seen_label("corridors_Aa"):
        "After all, I always had way more fun when I was by your side, and I still do."

        "I want that even after high school, I'll still get to hang out with you sometimes."

        "To tell you about the new things happening in my life, while I listen to you talk about yours."

        "I want to keep laughing with you, whether it's about anything or nothing at all, there doesn't need to be a reason to laugh."

        "That's something you taught me when we were kids, and I never forgot it."

        "I want to keep having fun with you."

        "Just like I always did."

        if seen_label("corridors_Ba"):
            "And the only thing I want tonight is for this to be the start of something new between us."

            "Maybe I'm finally starting to understand what I truly want."

            "Actually, it's like I always knew, and only now I'm finding the courage to admit it to myself."

            "Little by little, at least. The only thing left is that I just need to admit it to you."

        else:
            "Even if I'm far from who I used to be, I still want to be close to you."

            "Actually, I want to be even closer."

            "I don't want to pull away from anyone anymore, not even from myself."

            "And there's no one better to teach me that than you."

            "For all the times you made me feel alive, even when I didn't want to."

            "I still remember almost all of them. And in every one, I wanted to feel alive. Even unconsciously, I always wanted that."

            "And that's something that hasn't changed to this day. I just need to be more honest with myself."

            "And most importantly, with you too."

    else:
        "And no matter how things end after this, at least I'll be able to look back and say I tried."

        "Tried even while afraid, but tried."

        "If it all goes well, great. If it all goes wrong, that's fine too."

        "Because at least I'll know I did what I could."

        "And I'll know that little by little I'm learning how to deal with things like this."

        "That I'm not the same kid who runs away from everything he feels."

        "And honestly, even if it goes against how I think, I believe that would be the best for me."

        "There are so many things I only learned to appreciate after giving them a chance somehow."

        "Trying has always been the hardest part for me, taking the first step, and I always gave up before I even continued."

        "And if it weren't for Miya forcing me to take that first step so many times, I'd probably still feel as stuck as ever."

        "A comfort zone isn't comfortable anymore once you realize you're alone in it."

        "And once it's no longer comfortable, it becomes a pain zone, and getting out is just as hard as leaving a comfort zone."

        if seen_label("corridors_Bc"):
            "And that's why I need to get out of that zone."

            "I need to take risks, even if I don't know what will happen next."

            "I need to learn how to deal with things like this."

            "I need to learn how to open up to people more."

            "I need to learn how to care more."

            "Even if being vulnerable scares me."

            "And even if I don't want to, I need to learn how to take the first step on my own."

            "Because in the end, no one is going to do that for me except her."

            "I should have learned that a long time ago, but better late than never."

        else:
            "And I've gone through so many versions of that zone, but I was never able to fully leave any of them."

            "It's like I'm stuck in a cycle of trying and failing."

            "And I don't want that for myself anymore."

            "I need to learn how to take the first step alone."

            "I need to learn how to take more risks."

            "Nothing will change if I keep waiting for things to change on their own."

            "That would just mean repeating the same cycle I've been in for months."

            "And in the end, no one is going to do this for me except her."

            "Just for today, I'll let myself go with it."

    "In the end, there's nothing wrong with not carrying everything alone."

    "So, I'm going all the way."

    "Even if I'm scared of where that ending might take me."

    if not seen_label("corridors_Bc"):
        "But still, I feel strangely positive about it."

    return

label corridors_Cb:
    $ mc_personality.append("He is willing to take things as they come, without overthinking the situation.")

    "The truth is that I don't have any answers."

    "I have no idea what I want, what I feel, or what I expect."

    "I don't have a plan, much less control over what's going to happen."

    "All I have is this tightness in my chest, this anxiety, this fear… this confused urge to see Miya and, at the same time, disappear from the world."

    "I spent the whole night thinking of every possibility, trying to rationalize what I feel, but in the end none of it matters."

    "I'm still lost."

    "I know I'm complicating something that could be simple in the end, but I can't help it."

    "You're still an enigma to me. I think, again and again, but nothing makes sense."

    "I can't find an answer that satisfies me, or any logic behind all this."

    "But is there even supposed to be logic? Is it even possible to find a real answer?"

    "Is there a chance you did all of this just because, without a real reason?"

    "Actually, saying it isn't real would feel like I'm taking away your right to be here."

    "You have a purpose, that much is clear, but what is it?"

    "If I had known even a little earlier, I might already be inside that room."

    "I might've already come up with an answer or even a conclusion long before arriving here."

    "But it's exactly because of your ambiguity that I've never felt as lost as I do now."

    "And what irritates me the most is that something tells me this was intentional."

    "As if you knew exactly what you were doing."

    "As if you knew I'd be here, stuck in front of this door, not knowing what to do."

    "I want to believe that, so I can feel less stupid for being in this situation."

    "All that's left is this feeling of guilt."

    "Guilt for distancing myself from you."

    "…"

    "I miss you, Miya."

    if not seen_label("corridors_Bc"):
        "I miss when we walked home together."

        "I miss the random hangouts you'd drag me into."

        "I even miss talking to you more."

    "And that should be enough for me to take this step."

    if seen_label("corridors_Bc"):
        "But it isn't."

        "It feels like I'm stuck in a cycle of trying and failing."

        "Except this time, I can't even manage that."

        "I don't want to fail you. I don't want to fail myself."

        "But if I don't try, then what's the point?"

        "In that case I'd already be failing either way."

        "Even if I don't want this, it feels inevitable."

        "But I know I have the power to change things."

        "And I need to do that."

        "Because if I don't, I'll regret it for the rest of my life."

        "I may not know how to act right now, but I know I'll figure it out when the time comes."

        "And even if I don't, I know you'll help me with that."

    else:
        "But what if I try and nothing changes?"

        "What if I open this door and nothing gets resolved?"

        "No, that wouldn't happen."

        "I'm already walking in knowing I won't be the same after this."

        "What I don't know is how things will go back to being after all this."

        "Will things go back to how they were?"

        "Will you and I be close again?"

        "As close as before?"

        "With something changing, what will remain of us?"

        "What will remain between us?"

        "And what will remain of me?"

    "I have no idea what's going to happen when I walk in there, I've repeated that in my head so many times I've lost count."

    "I don't know if it's going to be awkward, embarrassing, or even painful."

    "I don't know if I'm going to feel relieved, happy, or maybe even sad."

    "Maybe nothing will change, or maybe everything will flip upside down."

    "But if I don't try… if I don't turn this damn handle… I'll never know whether things could've changed."

    "And maybe that 'not knowing' is worse than any answer I could get tonight."

    if seen_label("corridors_Ba"):
        "I may have the right to doubt, but I don't have the right to give up."

        "Standing here won't give me the clarity I need."

        "I need to act."

        "If not for me, then at least for her."

        "Because I know Miya deserves an answer."

        "And I owe her that."

        "Even if I don't know what that answer is."

        "Because in the end…"

    else:
        "Because I know I owe that to myself."

        "I can't keep living like this, not knowing what I really feel."

        "I can't keep feeling lost."

        "My guilt will only grow if I do nothing."

        "And the worst part is there's no one else to blame but myself."

        "So I need to act."

        "I need answers."

        "And I'll only get them if I open this door."

        "Because in the end…"

    "Like it or not, I'll only know if I try."

    return

label corridors_Cc:
    $ mc_personality.append("He's conflicted about his feelings and fears change, preferring the comfort of the status quo.")

    "Maybe I'm just making a storm out of something small. Something that was never as deep as I made it seem."

    "Maybe you just want to talk, or vent about something, and here I am overthinking something simple."

    "I keep setting expectations, placing this huge weight on your shoulders when I haven't even seen your face today."

    "Sure, there might be something important for us to talk about, but I don't know if it'll change anything."

    "At the same time that I feel something will change, I also feel like it doesn't matter what happens."

    "I don't know if I'm willing to have this conversation."

    "And honestly… I don't know if I'm ready for any change."

    "Because if nothing changes…"

    "If everything stays exactly as it is…"

    "Maybe I'll actually feel relieved. Maybe it's easier to deal with it that way than admit something broke."

    with Pause(1.0)

    mc "Hah…"

    "I let out a soft sigh, just to see if it helps with anything."

    "Of course it's not right, but why do I feel comfort in that thought?"

    "Miya has always been someone who made me feel alive, even when I didn't want to."

    if not seen_label("corridors_Bc"):
        "And even if I have doubts about what I feel, I know being around her is good for me."

        "I want it and I don't want it at the same time."

        "Maybe it's easier if nothing changes, but… what about the times when something changes for the better?"

        "I'm thinking about every possible scenario in a situation where anything, good or bad related could happen."

        "Up until now, I have absolutely no idea what she's going to say to me."

        "I'm repeating the same thoughts I had on the way here, but why?"

        "I thought I had already decided what to do the moment I jumped that wall, but now it feels like I'm just stalling again."

        "Stalling so I don't have to face her, as if I already knew something definitive was going to happen."

        "But what if it does? In the end it doesn't matter, what matters is opening this door and dealing with whatever's waiting."

        if seen_label("corridors_Aa"):
            "I had so much fun with her in the past, and I kept having fun the whole time we were still close."

            "I feel good around her, and I only realized that once I started walking home alone."

            "It's something trivial, routine, but the moment I stopped doing it with you, I felt the absence."

            "I may have felt it, but it still wasn't anything huge, there were more important things to worry about."

            "And I stayed that way, even when you still made time to walk with me and I didn't care."

            "But even something that simple made me feel something."

            "Not much, but something."

            "And that bothers me."

            "Why are you the only one who gets to make me feel these things?"

            "Why can't I feel anything like that with anyone else?"

            "I've gone out with other friends and I liked being with them, but… it's never the same."
    else:
        "But I can't help thinking that maybe I'm just fooling myself."

        "Maybe I just want to feel something, anything, even if it's just an illusion."

        "But I can't. I can't feel anything special about this."

        if seen_label("corridors_Ac"):
            "Weren't we supposed to be childhood friends? Have some unshakable bond, so strong nothing could break it?"

            "So why can't I feel that? Why does everything feel so fragile?"

            "It's like I'm trying to find a reason to give up."

            "And maybe I'm actually close to finding it, honestly."

            "But I won't know if I stay frozen here forever."

            "What could happen if I open this damn door?"

            "If nothing changes, if all of this was for nothing, will I feel relieved? Or even more lost?"

            "I should care more about Miya, care about not hurting her, but I don't know if I can do that right now."

            "I'm more frustrated with myself for not being able to sort out my feelings than anything else."

            "So in that case… did I fail as her friend? Or did I fail myself?"

            "I don't know what I want."

            "Actually, I do… but I don't want to admit it."

            "It wasn't supposed to be this hard. It wasn't supposed to be like this."

            "But it feels like I'm starting to stop caring."

            "Not about her, but about everything in general."

            "Even about our friendship, which I know has always meant so much to me."

            "And it's not like I need time alone, lately that's all I've had, and I don't mind."

            "It's like I'm distancing myself not just from her, but from the world itself. Leaving only me as my own company."

    "It's not going to be easy, I know that."

    "But whether things change or not, standing here isn't going to get me anywhere."

    "If I want any kind of answer, even the smallest one, I need to go in."

    "I need to see you before anything else, just so I can at least make sense of what I'm feeling."

    "Maybe my mind will flip upside down, maybe all of this will completely change the way I think."

    "Or maybe in the end I'll just stay the same as always."

    "But either way…"

    "At least I'll finally know what you wanted to tell me."
    
    return

label corridors_D:
    "Tonight might be the last chance I have to talk to you."

    "To finally clear up what's going on between us."

    if seen_label("corridors_Aa") and seen_label("corridors_Ba") and seen_label("corridors_Ca"):
        $ mc_personality.append("Ren is ready to confess his true feelings to Miya.")

        "To finally admit what I've always felt for you."

        "Even if it took me so long to realize it… to admit it."

        "I just hope you still feel the same way about me."

    elif seen_label("corridors_Ab") and seen_label("corridors_Bb") and seen_label("corridors_Cb"):
        $ mc_personality.append("Ren is uncertain about his feelings.")

        "To understand what I really feel for you."

        "And what I really want from our friendship."

        "Even if I still have no idea what that is."

    elif seen_label("corridors_Ac") and seen_label("corridors_Bc") and seen_label("corridors_Cc"):
        $ mc_personality.append("Ren is resigned to the possibility of losing Miya.")

        "To realize that maybe we don't have anything left to say."

        "And that maybe there's nothing left for us to be."

        "Even if I don't want to accept that at all."

        "It's still an unfortunate possibility."
    
    else:
        "Even if I don't know what to say right now…"

        "At the very least, that's what I'm going to do."

        "For both of us."

    "After losing myself in my thoughts for so long, I finally gather the courage I needed."

    "I take a deep breath, place my hand on the doorknob, and turn it slowly."

    play sound sfx_door_open
    "The sound of the door opening echoes through the silent hallway."

    "It's happening."

    "Everything I thought, everything I felt, everything I feared…"

    "All of it comes down to a single thought."

    "And that thought is…"

    python:
        user_response = renpy.input(_("And that thought is…"), length=100)
        ren_thought = user_response.strip()

        if not ren_thought or ren_thought.isspace():
            renpy.say("", "…")
            renpy.say("", _("It seems like I can't put this into words right now."))
            renpy.say("", _("It's not like I really know what I'm feeling."))
            renpy.say("", _("But I can't express it to myself."))
            renpy.say("", _("If I had to sum it all up with one word, I'd say it's confusion."))
            renpy.say("", _("But even confused, I still understand very well what I feel for you."))
            renpy.say("", _("Deep inside, I know I do."))
            renpy.say("", _("Still, there's only one thing left for me to do…"))
            pass
        else:
            # Add later the implementation of the LLM integration for the player's response.
            pass
    
    $ amb_stop()
    $ ambience_sfx_cycle.stop(stop_all=True)
    
    scene black
    with scenechange

    "I step into the classroom."

    play sound sfx_door_creak

    return