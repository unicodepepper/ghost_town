define g = Character("", kind=nvl, what_outlines=[(1,"#d47e00",0,0)]) #girl
define m = Character("", kind=nvl, what_outlines=[(1,"#0a1932",0,0)]) #guy
define narrator = Character(kind=nvl)
image filmoverlay:
    "film 1.png"
    0.1
    "film 2.png"
    0.1
    "film 3.png"
    0.1
    "film 4.png"
    0.1
    "film 5.png"
    0.1
    "film 6.png"
    0.1
    repeat

# image filmcomposite = LiveComposite(
    # (1280,800),
    # (0,0), "filmoverlay"
    # (0,0), "main underlay.png")


image bg black = "#000"
image bg white = "#fff"
transform nvlbgshow:
    alpha 0.0
    xpos 0.0
    xanchor 0.5
    parallel:
        linear 1.0 alpha 1.0
    parallel:
        easein_quad 1.0 xpos 0.5

label hideitall: #because the scene statement sucks #actually I'm not sure if it really sucks as much as I thought but I think I'll leave this be #at least for now
    hide girl
    hide guy
    hide bg
    hide nvlbg
    hide black
    hide white
    return


# this is just a general note on the script but... throughout the whole
# story, i feel like it should be hinted that the man wants to take her
# to his home, and, you know, take care of her as a parent would.

# it only becomes clear that he's looking to take her to the other side
# (and that he's dead, lol) near the end

# he is, of course, trying to take revenge onto her father, the evil
# mine owner who care about profits more than about lives. But in the
# good ending, where she actually wanted to help the ghosts of the hurt
# townspeople, he's conflicted about it - should i hurt this kind soul
# just for my revenge?

# he decides on a middle ground, and gives her a happy and comfortable
# death

# of course, on the bad ending, he has no mercy for her and leads her on
# to believe she'll be saved, only to let her die in the cruelest way he
# can think - starved, cold, and alone


label start:
    play music "music/bruh_moment.cropped.mp3"
    scene bg black
    scene bg snow
    show girl 2
    with dissolve
    show nvlbg at nvlbgshow
    g "It's... It's been a long time."
    g "He hasn't been around since yesterday... I'm starting to feel a bit worried..."
    g "He always comes. He said he would. He would take care. Of me."
    g "I don't know his name, but how does it matter? He's the only one who... Who wouldn't turn away from me."
    show girl 1 with dissolve
    nvl clear
    g "It's really cold tonight..."
    g "I hope he'll come today too... He..."
    scene bg snow path
    show guy 4
    with dissolve
    pause 1.0
    scene bg snow closeup
    show girl 3
    with dissolve
    show guy 1:
        alpha 0.0
        truecenter
        xpos 0.6
        parallel:
            easein_quad 1.0 xpos 0.5
        parallel:
            linear 0.5 alpha 1.0
    show nvlbg at nvlbgshow
    nvl clear
    g "I knew you wouldn't leave me! I knew, I knew, I knew... I'm so glad you're here. You don't even know."
    #until you pass away... isn't this too on the nose?? ideally the
    #fact that he wants her dead should be a surprise till the end :>
    m "I told you I would be with you until you pass away. And I am not a person to break promises, I assure you, sunny."
    m "I brought you the usual necessities; food, twigs for a fire, too."
    m "And... a surprise!"
    g "You... You really didn't have to!... I'm not worth the bother, you know..."
    show guy 2 with dissolve
    m "I hope it will fit you just fine. I believe... It might be something of your liking, too."
    g "I can't believe this, t-thank you... Thank you so much!"
    show girl 4 with dissolve
    g "I love it..."
    show bg snow closeup dark
    with dissolve
    g "I know it's rude of me to ask, since you help me out so much, but... {w}Can you tell me... {w}How long, until... {w}Until the day?"
    m "My sweet child, soon enough you will know. Fret not, I have not forgotten. All my preparations are heading to the end."
    m "There is but one thing itching my mind though, sunny... You have never truly told me how it all happened."
    m "Or maybe you did - you know how an old man's memory can rot away..."
    g "It's hard for me to speak about it, but... For you, I will... I will try."
    m "Do not push yourself too far, my child. Take it slow, alright?"
    show bg black as black:
        alpha 0.0
        linear 0.5 alpha 1.0
    g "You probably don't know me, since you're a foreigner, but..."
    call hideitall from _call_hideitall
    show bg white with None
    scene bg factory view1 #todo: add animations
    show filmoverlay
    show filmunderlay
    show nvlbg
    with Dissolve(2.0)
    nvl clear
    g "I'm the daughter of the richest man on the town that's past that trail."
    g "The factories around the city are the main source of income for my father. {w} He's the most influential person around here, I believe..."
    g "He never told me much about the factories, but I think these are coal and lead mines. They need big chimneys, you know?"
    m "I may not have grown up here, but I'm quite familiar with those."
    m "That is correct, lead mines are quite harmful. They need good ventilation so as to avoid poisoning people with the fumes."
    m "I was a safety inspector for the council, so my job was to make sure these rules are followed properly, for the well-being of the population."
    g "Ah, the fumes... God..."
    m "I apologize for my interruption. Please, do continue with your story."
    #show girl 4 but more scared
    g "That must be why..."..
    g "You see, this town has been getting worse and worse after the factories had started running."
    show bg field with dissolve
    g "The people started falling sick and dying, especially the workers."
    g "These fumes... {w}They came from the chimneys, and you could tell that if someone went down the mine, they would get sicker, day by day."
    g "They told me about what was happening... They... They tried to warn me..."
    #her eyes get watery
    show bg mines2 with dissolve
    m "Who tried to warn you? The workers that came back from the mines?"
    g "No... It was the ones that didn't make it out alive."
    g "I saw them every day."
    g "At home or outdoors, they were always there."
    g "I'm sure they were looking for me, because it seems like I was the only one who could see them."
    #show capitalist dad oink oink
    show bg factory view1 with dissolve
    g "But my dad never listened."
    g "I told him about all the people who were suffering and dying because of him, but it was pointless."
    g "He didn't care at all. But I...  I couldn't take it..."
    #girl cries and falls down
    scene bg black with Dissolve(2.0)
    nvl clear
    show bg snow closeup dark
    show girl 5
    show guy 3
    with dissolve
    show nvlbg at nvlbgshow
    m "He really does seem like a wrongful person, I am sorry, sunny."
    m "Maybe you should rest a bit? You look tired.{w} I promise I will come again."
    #they get comfier
    m "The fire will soon be gone too so please, darling."
    g "...Thank you so much for taking care of me."
    g "I'll try to rest, but..."
    g "Please take me with you as soon as you can."
    g "I don't want to keep sleeping out in the cold."
    scene bg black with dissolve
    nvl clear
    # change of scenes, it's the morning now
    pause 1.0
    call hideitall from _call_hideitall_1
    show bg white with None
    scene bg snow closeup
    show girl 5
    with Dissolve(2.0)
    show nvlbg at nvlbgshow
    nvl clear
    g "He's gone again..."
    g "It's a little warmer than yesterday, at least, but it's still very cold."
    g "I really hope he'll be back sooner today..."
    scene bg black with dissolve
    pause 1.0
    scene bg snow closeup
    show girl 2
    show guy 2
    with Dissolve(1.0)
    show nvlbg at nvlbgshow
    #girl lies down on the snow
    #change of scenes maybe?
    nvl clear
    #guy wakes her up kneeling
    m "How did you sleep, my dear?"
    g "Not too well... {w}It was really cold..."
    g "And there seems to be a storm coming up."
    g "I don't wanna be here when it arrives..."
    g "It's dangerous."
    g "Please."
    g "You have to take me home with you."
    #maybe the guy changes expressions?
    m "I am almost ready, my dear."
    m "I promise the wait will be fruitful."
    m "Soon we will not have to worry about any of this."
    m "I will take good care of you once you are with me."
    m "For now, the most I can do is keep you company."
    g "Thank you so much."
    g "I think I'd be dead by now if it wasn't for you."
    m "Don't worry about it, precious."
    m "Please, try to eat at least a little. You need strength."
    m "It is not much, but it should get you through today."
    m "I promise we will leave by tomorrow's night."
    g "It feels like such a long time..."
    #she lies down again
    g "I just hope the ghosts will stop bothering me once I'm there."
    #he seems surprised
    m "... Ghosts?"
    m "What ghosts?"
    g "I thought... {w}I had told you about them yesterday..."
    g "Didn't I? I'm sure I did... I..."
    m "You should not tell me if it awakens bad feelings in your heart, young lady."
    g "No! You don't understand."
    g "I want you to know."
    g "You need to protect me. I need you to understand what's going on."
    m "..."
    m "I see."
    m "In that case, please tell me."
    m "Who are these ghosts?{w} Why are they bothering you?"
    g "They... {w}They are the victims of my father."
    g "I don't know if they are looking for revenge{w} or for justice, but..." #maybe make dramatic scene change during this sentence
    nvl clear
    scene bg black with dissolve
    g "But..."
    nvl clear
    "Hey."
    #she tries to ignore the ghost, as the world materializes around her
    "Young lady, please look at me."
    "Please look at us."
    "Look at what your father has done to us."
    # the man should faaaaaintly appear here as an inspector for the council
    # not yet revealed that it's the same person as the man though
    # but he does have some very distinctive cracked glasses because of the murder attempt
    # which are later shown on the man to tie that together

    "We need your help."
    "Please, we beg you."
    "I'm begging you." #repeat this a bunch of times from different people for psychological effect
    g "What do you want?"
    g "Why does it have to be me?"
    "You're blessed with a very unique ability, young lady."
    "You're the only one who can carry our will forward."
    "Will you help us save this town from the evil that governs it?"
    "Will you help us finally rest in peace?"
    "It won't be easy. It never is. But we know. We know what to do."
    "We just need you to help us. We will guide you."
    "It's all in your hands..."
    "Just say a word and we will be ready. We will."
    "You can make it all better again. You can fix this place."
    "You can save {i}the rest of us{/i}."
    "There isn't much time left..."
    "But we know you're the great one. You possess what we need."
    "What we don't have."
    "We are mere ghosts... That's why we're begging for your aid. Please."
    "Please."
    "Please."
    # also probably make this more... of a difficult decision
    # right now it's just "will you help lol"
    # should be more of a 
    # "you will have to do something unspeakable,
    # but it's the only way to bring justice to us"

    # another thing we discussed - instead of just "lol put this bomb on
    # his car" she's... radicalized by the ghosts, and builds a bomb
    # fully knowing what's going to happen. 

    # i think this makes the choice more difficult - will you build a
    # bomb to kill your own father to help these people he's wronged?

    # of course, later on she realizes how horrible that was, and
    # escapes out of guilt.

    # another idea for the bomb setup scene:

    # just random snippets of text talking about what she's building, like:

    # "...Trinitrotoluene, used commonly for hydraulic fracturing..."
    # "...spare key to the tool storage..."
    # "...ignition cable under the dashboard..."

    # g "This is for them... This is for the best. It'll make everything good again... No more dying people... No more suffering... The pain... It'll all be pure again."


    # and then she snaps back to reality when she hears the news of the assassination attempt 


    menu:
        "Yes.":
            $helped=1
            g "..."
            g "Okay."
            "Thank you, young lady."
            "We just need you to do a very simple thing."
            "We are aware that mechanics might not be the most fit task for a person like you, but you're the only hope we have left."
            #change of scenes, mechanical noises (maybe showing the underside of the car)
            nvl clear
            g "And that's all?"
            "Yes, that is all we need from you."
            g "Will you leave me in peace now?"
            "Oh,  soon enough. We just need the mechanism to go into effect."
            #another change of scenes
            nvl clear
            "Young lady, young lady! There's an emergency!"
            "Someone has tried to assassinate your father!"
            g "What?! {w}How?"
            "An explosion happened on his car just now."
            "It was far too powerful to be accidental."
            "Thankfully, it was parked in the new mining site, so no one was around when it happened."
            "But just a bit of bad luck, and your father wouldn't be here right now."
            g "I... I think I need a minute alone..."
            "I can understand, young lady. {w}I know how shocking hearing something like this can be."
            "But I want you to know that we have already contacted some of the best detectives in the country to find out who the culprit is."
            "I'm sure in just a few days we will know for sure who rigged your father's car, so you don't have to worry about it."
            "They won't receive any mercy from us, or from the sheriff."
            #she breaks down even more (I don't know if I should add some dialogue here)
            "We will be waiting for you at the dining room."
            "There will be increased security in the whole area, so you we want to notify you about all the new changes, young lady."
            "Please come when you feel more composed."
            #another change of scenes, now the girl is alone in the room
            g "This can't be happening..."
            g "I can't believe what I've done."
            g "It's all my fault."
            g "I'll never be able to look at my father to the face again."
            g "What will he do when he finds out it was me?"
            g "What will everyone do when they find out it was me?"
            g "I can't stay here any longer..."
            #change of scenes to the snow
        "No.":
            # I think if you pick No, the man should appear shaken after the story ends.
            # Something like "but why didn't you help them? didn't you care about their suffering?"
            # "yeah but.. they were asking too much of me"
            # 
            # "do you think I did wrong?"
            # "it doesn't matter. let's just forget about it and worry about you."
            # OH BUT IT REALLY DOES MATTER :]

            # another thing - if she chooses not to help, i think it
            # should be clear that she has to flee anyways because the
            # ghosts keep harassing her.

            # "their weeps only got louder and louder... I couldn't
            # escape them - even in my dreams"
            # or something like that 


            $helped=0
            g "I don't want to."
            g "I won't do this to my father."
            g "I know what you want from me, but I refuse."
            g "You won't get anywhere by talking to me."
            "We won't be able to rest until justice has been served, young lady."
            g "Can't you find someone else?"
            "We are tied to this place."
            "And you're the only one in here who can hear us."
            g "If you can't leave, then I'll do."
            g "I don't want to see any of you ever again in my life."
            "The winter is coming near. You will not survive."
            "You're cruel... Not any less than your father."
            "We had hope. We put our hope in you. Our faith."
            "There's no hope in this world."
            "You don't deserve hope either."
            g "Leave me alone! Leave!"
            g "God..."
            g "I hope if I run far enough, I will lose them finally..."
            g "I don't know how to cope with this anymore. I don't."
            #change of scenes to the snow
            pass
    nvl clear
    #it's already nighttime
    m "I have nothing but respect for you, young lady."
    m "It takes a great bravery to take such a decision."
    m "There is a question that troubles my mind, however; and I hope you don't feel I've disrespected you by asking this."
    m "Why do you wish to come with me, instead of going back to your home?"
    m "I'm sure your family will understand how you were forced into doing this, against your will."
    g "I don't think so..."
    g "I don't think my family will ever forgive me."
    g "My father is known for ruling with an iron fist - not only in business but in our family as well."
    g "It's the way he is."
    g "If he were to know, he would likely kick me out of the home in an even more shameful way."
    g "I think... {w}I think it's best for me to disappear. {w}So no one can find me again."
    g "Do you live far away from here?"
    m "Not really."
    m "But you could say I'm free to go where I feel like, so you don't have to worry about it."
    m "If that is your wish, I will make sure that you don't have to encounter your father again."
    #man sits down probably
    m "I know what it feels like to flee from your crimes."
    "..."
    nvl clear
    g "Will you stay with me tonight?"
    m "I'm afraid I can't today, young lady."
    m "But I promise you'll come with me tomorrow."
    m "Everything is ready."
    m "It's almost time."
    #she lies down maybe?
    g "Thank you."
    g "Thank you so much."
    g "I think I'd probably be dead already without your help."
    m "Don't you worry, my dear."
    m "You will be safe with me."
    m "We just need to wait until tomorrow, okay?"
    #she gets uhhh  a little comfier
    "..."
    g "Please come back quickly tomorrow."
    g "I can feel the storm coming closer."
    g "It's very dangerous if it hits and I'm still here."
    m "I can understand, young lady."
    m "I promise I will come for you as soon as I can."
    m "Goodnight, my dear. {w}It's quite late."
    g "Goodnight."
    nvl clear

    #change of scenes, the snow sound gets stronger, now there's more snow on the screen and stuff

    g "He said he would come today..."
    g "He will come, right?"
    g "He won't leave me here, in the storm..."

    # the storm gets even stronger
    nvl clear
    if helped==True:
        jump goodEnding
    else:
        jump badEnding
    return






label goodEnding:
    #guy comes closer and holds her hand
    m "I have returned, young lady."
    m "I said I would not abandon you."
    #her eyes light up, her fingers are purple already
    g "I'm cold..."
    g "I'm so cold..."
    g "Please bring me with you..."
    m "Soon enough, my dear."
    m "This will not take too long. You have waited enough. We are close."
    #he takes her blanket out (?)
    g "I-I'm... G-going to freeze..."
    m "We shall be together soon, my dear."
    #change of music and tone of the scene (it gets dark at first then it becomes light, almost ethereal)
    nvl clear
    g "... What happened?"
    g "I'm not... I don't feel cold anymore..."
    m "I know, my dear."
    m "Let's go home."

    #here goes the Emotional Slideshow(TM)

    # description of the emotional slideshow:
    # - she is walking by his hand through a hill, towards the sun, like a happy ending
    # (moved the rest to the credits)

    # another thing i feel should happen in the good ending is some
    # mention of the workers' loved ones getting pensions... cause what
    # was the purpose of the terrorist attack if not? silver lining :)
    jump credits
    return


label badEnding:
    #she wakes up in the snow
    #the breeze is even stronger

    # In the bad ending, he is revengeful - he wants her to suffer
    # because of not helping the ghosts, and he also wants her dad to
    # suffer for... obvious reasons. So as discussed, he disappears in
    # front of her (with a "you deserve this, now you will know what
    # it's like to be helpless and alone" while she begs him to save
    # her)

    #m "When it's all over... You will see for yourself how the eternal restlessness feels like."

    # I honestly think this whole part needs to be rewritten like it says
    # above. It also should hit her that now that she realizes the food
    # and coat never existed, the cold and hunger hits her at once. 

    g "My God... It's freezing... It's a-awful..."
    g "Where is he?"
    g "He said he'd come back, right?"
    g "He said he would come for me..."
    g "Where is... {w}Where is the bonfire? {w}Where is the coat he brought for me?"
    g "I'm hungry... {w}Have I really eaten anything?"
    g "Was he real?"
    g "Was... {w}Was any of it real?"

    #Emotional Slideshow 2.0: now it's sad
    jump credits
    return

label credits:
    nvl clear
    # emotional slideshow (continued)
    # - there's a couple timelapsed shots of the town slowly crumbling - the factory chimneys crashing down, things going to dust
    # - maybe a couple newspaper shots talking about the town's demise, and the fight for the worker's rights
    # - at the end of the credits, there is a grassy spring hill - where the camera pans down and shows a half-buried skull with some flowers growing in and around it 


    scene bg white with dissolve
    "these are the credits"
    $renpy.pause(1.0,hard=True)
    return
