label ch5:
        
    show text "Chapter 5" with Pause(1.5)
    scene black with dissolve

    "Dogs weren't allowed in the main library which was a pity, because Jeanne reckoned that it would lift people's spirits up and thus improve their grades, increase their motivation, and overall their university's ranking." 
    "They had booked a study room a month in advance to avoid having to fight for the library seats. Exam period was that dreadful." 
    "The seats were nice and comfy. The tables were clean and well-lit. Come to think of it, there really were people whose jobs were to design chairs and tables. In order to pay them respect, she should take a picture of them, right?"

    show lise smile at left
    e "Quit procrastinating. Your reports aren't going to write themselves."
    show jeanne casual smile at right
    j "It's already been two days in a row. Let's take a break, please."

    "Elise shut her laptop."

    e "I could do with a cup of tea. I'm almost finished."
    j "Are you kidding me?"
    e "Regular and punctual studying does wonders."
    j "Gimme that superpower."

    "They took their laptops with them in precaution and closed the door tightly."
    "The cafeteria was full of students cramming for their exams so they found a random staircase next to a skatepark outside."

    scene bg another_school_building_day with fade
    show lise smile at left
    show jeanne casual smile at right

    "Grey. That was the taste of the coffee Jeanne felt on her tongue as she looked at the moody skies and the concrete walls surrounding her in silence. But, the taste changed as soon as she saw Elise texting. A newfound sweetness circled around her palette. She held back from teasing her friend, but she couldn't hold back her curiosity."

    j "How's it going?"
    e "It's going well."

    "The last word of her sentence sounded a bit hesitant."

    j "You've made more progress in two months than the whole last semester. If he answers your texts, that's already a good sign. He's been so busy lately."

    "Elise finished her last sip of tea."

    e "I've got to finish my group work too."
    j "Doing everything by yourself?"
    e "Like usual."
    j "You should learn to rely on others."
    e "Cannot do. Let's go."

    "Elise sighed."

    j "Five more minutes, please. My brain's going to dry out. I'm sure you have more stuff to share. We're also studying this afternoon. We've got plenty of time."
    e "The faster I'm done with the assignments, the faster I'll be able to finish revising the contents of the written exams and relax."
    j "“Apart from you, I don't know anybody who can relax during the exams period."

    "Jeanne paused to think a second."

    j "Ah! How about your choice for masters? Do you have an idea of what you want to apply for?"

    "Elise said yes with her head like it was obvious."

    e "Why are you asking me this question? We didn't even finish our first year of Bachelors."
    j "I'm thinking of going on a gap year."
    e "To do what?"
    j "To think about what I want to do."
    e "Well, think while studying."
    "Jeanne's shoulders dropped at the idea of spending the rest of her day at the library while Elise looked more motivated than ever."
    "Honors students were really a species on their own."

    j "You always seem to have everything figured out."
    e "I try my best to."
    j "Your brightness is blinding me."
    e "I'm sure you'd find your way if you put more efort into it."
    j "I don't know about that. At least, when you fail without trying much, you can blame it on your lack of preparation."
    e "Isn't it a waste to not see your full potential?"
    j "People will expect more from you and you will expect more from yourself. An endless circle. Expectations are heavy."
    e "And life is light."
    j "Yeah. Do I say it that often?"

    "Elise tied her hair into a bun, switching it to study mode."

    e "You're just missing a trigger. A trigger to make that first step."

    #transition

    scene black with dissolve 
    show jeanne smile at center
    "Spring rolled up with a new shine. Jeanne's smile couldn't get wider. It had been three weeks since she had completed her midterm finals, submitted her reports and performed her presentations. She had been finally relieved from her student duty and was now committing fully to her sofa and bed."
    "However, today, she changed from her pajamas to a random tracksuit. Going out once in a while to somewhere other than the library and treating herself with a delicious meal would do her good. A look in the mirror was enough to understand how much she needed that outing. Her already white skin had become paler and her muscles had lost their vigor. Even her butt which she was proud of, had flattened from sitting on the chair and laying on the bed all day."

    scene bg Street_Summer_Evening

    "On the road, she met her brother who was taking his daily walk."

    show arthur smile at right

    a "Don't tell me you're going to meet friends"

    "He said with a shocked face."

    j "Not your business, ciao."

    a "Are you eating dinner at home?"

    "She said no."

    a "I'll give you some money. I should have change on me."

    "She refused."

    j "I've got the money I earned at my part-time job."

    "Her brother's eyes were watering."

    j "What the hell is wrong with you?"

    a "She's growing up so fast. Go ahead, free spirit."

    "She rolled her eyes as an interesting thought struck her."

    j "I saw that you bought fresh ingredients for dinner. Invite Elise, I'm sure she'd be happy to join you for a meal. And, she doesn't work tonight. Otherwise, she'd eat some crappy food. Later."

    hide jeanne with moveoutleft

    "He waved her goodbye as she quickened her pace."

    menu:

        "Invite Elise.": 

            if affinity_with_arthur == 2:
                jump suite5_1_1 

            else:
                jump suite5_1_2
                

        "No, that could lead to misunderstandings.": 

            jump suite5_1_2

    label suite5_1_1:

        "Arthur took out his phone and sent a small text."

            scene black with dissolve


        scene lise smile at center
        
        "Elise had decided to properly wash her hair, but it was taking hours. It had gotten much longer. It reached her waist now. She was rinsing it thoroughly after using her new conditioner when her phone rang in the kitchen."
        "After enveloping her hair in a towel, and her body in another, she treaded carefully to not bump into her trash bin or her piles of study books."

        "“Jeanne is eating out. I planned food for two. Do you want to come over for dinner at eight?” Arthur had messaged."

        " It was only three short and clear sentences. Yet, Elise needed a minute to process the information. She jumped on her bed and dove her head in one of the giant cushions, her legs kicking in the air."   
        "Was that a home date? Good thing she didn't have a shift at the restaurant." 
        "What could she wear? Casual would be the sound option."
        "Elise rummaged in her wardrobe." 
        "Pants? Or a classic dress? What color palette would go well with the season? What color did he like? What was the temperature outside? Her two neurons were playing question-table-tennis at this stage." 
        "Time was ticking. She looked at the mess of knocked-down clothes, and sighed at the idea of folding them later. She put on random black matching underwear, a beige blouse long sleeve, a white shirt, and electric blue jeans. Blue always matched her eyes."
        "She dried off her hair and bolted off to the bus station and caught the bus in extremis. Wiping the sweat off her forehead, a wide grin was placated on her face. She was so thrilled and stressed out at the same time that she couldn't stop her finger from nervously tapping on her leg."
        "Arthur appeared at the door in an red apron over a black shirt, black joggings."

        
        show arthur smile at right
        show lise smile at left

        a "Do you drink?" 
        e "Sure."

        show bg_condo

        "He opened a bottle of wine and poured themselves two glasses."
        "Then, Elise realized she came empty-handed."

        e "Sorry. I forgot to bring something."
        a "No big deal."
        e "Next time, I'll bring over some drinks at least."
        a "Sure. As long it's nothing fancy. I'd feel bad otherwise."

        "He made her sit while he continued cooking. Humming an unfamiliar tune, his soft voice flowed around the kitchen."
        "No need to overthink it."
        "She took a deep breath and reset her mind."
        "It reminded her of their first encounter, the one he didn't remember. The scent of freshly cut tomatoes, the dim lighting and the sound of his voice gently lulled her into peace. Her nervous finger lay down as her eyes followed his back."
        "Obviously, it wasn't a home date. Still, she could enjoy this moment, right?"

        a "Sorry, I was in my thoughts."

        "He laid two bowls on the table for the salad."

        a "The lasagnas will be ready in a few minutes. I'm not used to people arriving on time."

        "He took a sip of wine."

        a "How were your exams?"
        e "Nothing big. Hard work pays off."
        a "That's more than big."

        "Elise tented her fingers."

        menu:

        "Nod and stay silent.": 

            jump suite5_2_1 
                

        "Ask Arthur about his life.": 

            jump suite5_2_2

        label suite5_2_1:

            "They both looked at the red digits of the oven's timer and smiled. 

        
        label suite5_2_2:
            
            affinity_with_arthur += 1

            e "And you?"
            a "Can't say I didn't work hard, but would it be correct to say that it was hard work?"
            e "I'm sure it was."
            a "I didn't know you worked at the restaurant too."
            e "I do some shifts here and there. Nothing too big. I started a while ago. Summer before starting college."
            a "To make pocket money?"
            e "Could say that. It's not as good as funding a successful startup, I have to say."
            
            "Arthur's left brow rose."

            a "Waiting tables is harder."
            e "Why do you say so?"
            a "Because it is physically and mentally demanding. Difficult customers. Running around the whole night. The noise, the smell and the lights. Whereas, building a company with friends around a subject you enjoy is a different matter altogether."
            e "It's tiring some days for sure."

            "The corner of her eyes curved."

            e "It is also rewarding some other days. Birthdays, for example. I love seeing families smile together around a great meal and a beautiful cake."
            a "I see."

        "On cue, the oven and his mobile rang."
        "He served the steaming lasagnas winced."

        a "Sorry. Urgent call. Sorry, really. I hate people who're on their phones during meetings and dinners too."

        "He went into his room, leaving Elise with only her glass and her thoughts."
        "By the time he came back, the lasagnas had gone warm and her glass had gone empty."

        a "Sorry again."
        a "It was faster than I expected."
        e "The call?"
        a "The job interview results."

        "She stood up so fast, the room stood with her."

        e "What? Are you going to join a charity association?"
        a "Charity? I did mention that. But no, I'm going to Paris, to give a hand to a friend, Tom, the one you met at the restaurant."
        a "He's a bit older and has his own company which is currently expanding. He urgently needs new, trustworthy and competent collaborators. Of course, the job in itself is interesting and the offer too, but it means that I'll have to step down from my CEO position at my company."

        "She felt her composure break as she sat back down."

        menu:

        "Ask him what he will be going.": 

            affinity_with_arthur += 1
            jump suite5_3_1 
                

        "Don't ask anything.": 

            jump suite5_3_2

        label suite5_3_1:

            e "When are you going?"
            a "A week after my master's thesis presentations. In a month or so. Well, I don't think I'll miss London."

            "A piece of her heart fell off on her plate."

            a "Don't make that face."
        
        label suite5_3_2:
            
            "She bit her lip in silence."

        "Contradicting thoughts filled her head. She sat back down and nibbled at the lasagna. It was sadly well-made."

        e "Are you set on it?"
        a "I will need to discuss with my board next month, but yes, I guess. One of my colleagues will join too. She was getting tired of London, she was like 'Where are you going like that? Trying to get out of London first, uh?'"

        "Arthur chuckled."

        a "She's quite the competitive one."

        "Arthur gave her a glance."

        a "Hey, are you okay?" 
        e "Yes."

        "The news of him going to work abroad had shaken her."

        e "The lasagna was delicious."

        "Though the last spoons tasted bitter."

        a "A pleasure. Do you want dessert? I've baked a lemon cake."
        e "No, that's fine. I'll go home. It's late."

        "She bit her lips. Her tone came off a little rude."

        e "I think the exams tired me out."

        "She went to get her coat by reflex, but forgot that she didn't bring one."

        a "I'll drive you home. It should be quite chilly outside."

        "She avoided his eyes in a desperate attempt to contain her sudden surge of emotions."

        e "It's fine. It's fine."

        "Elise couldn't tell him it was about him leaving London. Although they had become much closer, she wasn't anybody to him. Even if she was, she would never want him to base his career choices on her personal feelings. It would be too selfish and unfair. Wouldn't it?"
        "His phone rang again."
        
        a "I'm sorry."

        e "I..."

        menu:

        "It's just that... I would have loved to spend more time with you.": 

            if affinity_with_arthur >= 3:
                jump suite5_4_1 

            else:
                jump suite5_4_2
                

        "Nothing.": 

            jump suite5_4_2

        label suite_5_4_1:
            
            a "Me too."
            
            "He slightly smiled."

            a "Paris is not that far. I'll come around once in a while to visit anyways."

            affinity_with_arthur += 1

            jump suite_5_4_2

        label suite_5_4_2: 

            "Elise stayed silent."

            a "I've gotta go. Sorry."

        "She opened the door."

        e "Don't apologize. It's fine. Work is work. I know what it is. I was going to go regardless."

        "Elise tried to smile, but her lips didn't move. She knew that if she didn't go now, she would regret it, they would regret it."

        "'Perhaps, I'm the one who's missing that trigger.'"

        if affinity_with_arthur < 4:

            jump suite5_1_2
        


    label suite5_1_2:
        
        scene black with dissolve
        show text "End A : A" with Pause(8)
        return
        