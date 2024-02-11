label ch2:
    show text "Chapter 2" with Pause(1.5)
    scene black with dissolve

    scene bg room

    "Seven o'clock rang, Elise propped up in a daze."
    "She flicked her alarm off and drew open the curtains. They fluttered in the breeze as the dark streets of London welcomed its first inhabitants. Nightly light seeped into the simple and neat bedroom."
    "Responsible for the opening of the café, she had to be there at around eight thirty, so without wasting time, she prepared herself and headed out quietly. The café was a thirty minute walk from Jeanne's flat."

    scene bg cafe with dissolve

    "She unlocked the door of the café. The counter, the tables, the floor were itching to be cleaned and the fridges, coffee machines, to be filled."
    "At nine, her morning shift colleague joined her. Though Sebastian always looked indifferent, he was serious and serviable, and he enabled her to rest a little."
    "Time flew at the beginning, but at around ten thirty, it met a slump as there wasn't much activity. When there wasn't much to do, Elise used to read a book or chat with the regulars. But today, she felt too exhausted for anything."
    "Perhaps it was because she wasn't sleeping in her own bed. Or maybe taking a shift at the restaurant yesterday night was too much."

    show sebastian smile at left

    s "Have you had enough sleep? You look slightly off."

    show lise smile at right

    e "Haven't slept well these days."

    "Sebastian glanced at his watch."

    s "There aren't much people today. You can go."
    e "Are you sure? I'm not in a hurry or anything."
    s "Go. Take this with you."

    "He gave her a little blue box."

    s "Merry Christmas Elise."
    e "Really? You didn't have to. Thank you. It's not anything big, innit?"
    s "Just a small present since you gave me one too."
    e "Well, thanks." 
    s "I can't believe I'm going back to Portugal this week. Dama wants to organize a big family meeting."
    e "Sounds good. Like a real grandma."

    "Elise went to fetch her bag."

    e "Please tell her I said hi. Have a nice holiday."
    s "You too!"

    scene bg condo with dissolve

    "As soon as Elise arrived, she could smell the mushrooms and the cooked rice. She took off her brown boots and peeked her head through the hallway."

    show jeanne casual smile at left
    show lise smile at right

    e "I'm home."
    j "Welcome back."

    "Elise beamed. Even though it has been a week now, hearing “welcome back” to her “I'm home” put her in a weirdly good mood. "
    "Jeanne had cooked a mushroom risotto. Proud of it, she described every step of the recipe and how she tweaked it to adapt it to her tasting buds. And indeed, she appeared to love each bite of it."

    j "You're hiding something, aren't you?"
    e "What? How did you know?"
    j "So, what's that blue box?"

    menu:

        "Not telling!":
            jump suite2_1_1

        "What? How did you know?":
            jump suite2_1_2

    label suite2_1_1:

        e "Not telling."
        j "So secretive! So you're not telling me about your plans for Christas either?"
        e "This, I can."

    label suite2_1_2:
        python:
            choixsuite2_1 = True
        
        e "What? How did you know?" 
        j "It was sticking out from the pocket of your coat. So who's it from?"
        e "From Sebastian, but I haven't opened it yet."
        j "You traitor. Didn't you intend to become my step-sister?"

        "Jeanne sniffled."

        j "I lost a friend. A dear friend."
        e "You're so dramatic. Stop it."
        j "You work too much anyway. Like my brother. Wouldn't work out."
        e "I need to put food in my plate."
        j "I can do that."

        "Elise gave a tired smile."

        j "Let's open it then."
        e "Why? You don't need to known what's in there."
        j "Oh, come on."

        "Elise laughed and pulled it out from her coat."

        e "Here."

        "The opened box revealed a light blue braided bracelet."

        j "Blue like your eyes. My brother should take a page from his book."

        "Elise took her phone out."

        j "What are you doing?"
        e "I'm messaging Sebastian to tell him that I'm thankful, and that I'd be wearing it."
        j "How about Arthur?"
        e "It's not such a big deal."
        j "What if he likes you?"
        e "Not happening. So, what do I message him? For thanks?"
        j "Send what you said, it's that simple."

        "Jeanne went to the sink and rinsed the plates with cold water before placing them in the dishwasher."

        j "Do you have anything planned for Christmas?"


    j "If you want to, you can come over."
    e "I'm already sleeping in your brother's bedroom."
    j "So what? It was my brother who suggested you sleep over in case I pass out again like a dead sock. We never finish the food anyway. My mom does too much. My parents would be more than happy to welcome you again."
    e "I'll think about it."

    if choixsuite2_1 == True: 
        "Elise's fingers tapped on her screen, alternating between the delete and the space keys"

        j "Just send that damned text."


    scene black with dissolve
    scene bg condo

    "Jeanne checked again if she didn't forget anything before telling Elise to do the same."

    j "Good. We're going. Don't forget the gift you bought, Elise."
    e "Not like I could forget it."  
    j "Right."

    "Jeanne shook her head helplessly."
        
    j "We could have taken another pair with another color."
    e "No."    
    j "So stubborn."

    "They had gone to the central mall last Friday, the only day Elise didn't have work. And they literally spent a whole afternoon looking for one specific color for this item. Overthinking as always, Elise was Elise after all"

    scene black with dissolve

    "They arrived in Lille in an hour thanks to the efficiency of the Thalys, then with a regional train, they reached Calais where Arthur waited for them."

    scene rain with fade
    show arthur smile

    "They exited the train station and saw him waving his hands. He was wearing a black sweatshirt, jogging, all smiles and all soaked. Jeanne noticed Elise's warm smile at his sight."

    a "I forgot to take an umbrella. We'll have to make a run for it. The car is only a minute away from the entrance of the railway station."

    "His hand pointed at a red family car."

    a "It's this one. Watch for other cars. Let's wait for this one to go. And this one."
    j "Wait, wait, it's not one minute away!"

    "A terrifying icy rain and more than three hundred meters separated them from the car."

    a "If you run, it is. Go!"

    "He sprinted away." 

    a "Go! Go!"

    "Jeanne screamed as she and Elise ran after him."

    scene bg seaside with fade

    "In the car, protected from the hail, they exhaled a sigh of relief. The North's moody weather wasn't a laughing matter. It could go from sunny to a thunderstorm in a minute."

    "Arthur started the engine."

    a "Fasten your seatbelts, the kids at the back. Sorry for the run by the way, Elise."
    e "It's fine, it was fun."
    j "Why don't you say sorry to me too?"

    "Jeanne could see Arthur in the interior mirror smiling. She sighed."

    j "How was the move?"
    a "Done. Wasn't easy to drive a truck, but you know what? Nobody got hurt and we did it in one go. How about you two? How was your week with the dog?"
    j "Slept twelve hours daily, watched whatever shows there were, paradise on earth."
    e "The dog is well-behaved so we didn't have any trouble. Thank you for lending me your bedroom. I'll clean it carefully when you come back."
    a "Don't bother. I'll do the laudry and clean up when I go home, so make yourself comfortable. I should be the one thanking you for taking care of my sister and our newly adopted dog."
    e "No biggie, really."
    j "Is it far? I'm hungry."
    a "The groceries are in the trunk. I bought chips for you."
    j "That's my big bro."

    "Jeanne tried to reach them, but with her seatbelt on, she couldn't get her hands on the yellow bag. If only she could…"

    menu:

        "Try to reach for it.":
            jump suite2_2_1

        "Give up on the chips.":
            j "It's too far. Nevermind. I'll die of hunger."

    label suite2_2_1:

        a "Don't unfasten your seatbelt."

        j "I wasn't going to do it."

        a "Elise, can you please help this shortie? Her arms are too short."

        j "You're the one who's short."

        a "You like walking under the rain, don't you?"

        j "Sorry, big bro."

    scene bg mansion with fade

    "Arthur had called it a modest stone cottage, but it deserved to be called a mansion with its long porch, beautiful yard, and four floors with each of them having a bathroom and three rooms. On the ground floor, there was a large dining hall, a well-equipped kitchen and an enormous living-room."
    "The two upper floors were the bedrooms, and the latest floor was the attic. It kept all the souvenirs Jeanne's parents collected throughout their different jobs."

    scene Livingroom_Night with fade

    show jeanne casual smile at left
    show lise smile at right

    "Elise sank in couch, her puffed out face reflected on the large TV screen. Jeanne told her the truth. Her mother did cook too much."

    j "Found it."

    "Jeanne sat beside her and shared her plaid she just found."

    j "You didn't have to force yourself, you know."
    e "It's not every day that you get the chance to eat home cooked meals."

    "Elise stroked her bloated belly contentedly."

    e "What should I call him?"
    j "How do you know it's a boy?"
    e "Valid point. I should find two names."   
    j "You're wasted. I shouldn't have let you touch the bottle."

    "Elise rested her head on Jeanne's shoulder."

    e "Do you remember how shocked I was to learn that Arthur was your brother. You know, because I met him before."
    j "Yeah, you've never told me about how you met him, you silly secretive meanie beanie. Wait. Is it the flashback arc?"

    "Jeanne gasped."

    scene black with dissolve
    scene park with fade

    "Elise was lying down on the bench, reconsidering her life choices. Her tummy hurt so much, and she couldn't get rid of that hellish headache. Fortunately, it didn't rain. With her light brown jacket and the early morning rays of light, she was able to keep her body barely warm."
    "Drinking on an empty stomach and mixing alcohols, plus clubbing made a dreadful combination. She should have gone home at four like her friends. Instead, she ended up here."

    "Stranger" "Excuse me, are you okay? Do you want me to call 911?"

    "Through her blurry vision, she caught sight of a black-haired guy wearing a blue scarf and a long-sleeved shirt under a long black coat. She wanted to tell him that she was fine and he didn't have to worry, but the words didn't come out."
    "Instead, her throat shook and she threw up."   
    "He cursed in surprise, before taking a deep breath, and laughing it out. She felt sorry for his white shoes. He placed her in the recovery position and gently tapped her back."
    "His eyes looked for witnesses and help as he dialed up the emergency number."

    "Stranger" "Hey. Please, stay with me."

    "Stranger" "I've called an ambulance, they're coming, alright, so stay with me."

    "She felt her hands and feet going cold. Shivers ran through her body. She tried to endure it, but it was soon unbearable."

    e "I'm cold."

    "Stranger" "Where?"

    "He took tissues out of his pocket, wiped his hands and the corners of her mouth."

    "Stranger" "I'm afraid I can't do more in order to avoid any judicial pursuits."

    "Vomit had gone into the obvious neckline of her one-piece dress down to her bra, not to mention the state of her jacket which had turned from brown to yellow."
    "A tremor shook her body and she threw up again in coughs. He was prepared this time and managed to grab her hair while making sure she didn't hit her head. She felt like her stomach was being squeezed out of all its juice."

    e "I'm cold. Hands. Legs."

    "He frowned. He took off his coat and rested it on her legs, and wrapped his scarf around her hands." 

    "Stranger" "Is it better?"

    "She didn't have the strength anymore to answer so she nodded while quivering."

    "Stranger" "Hey. Hey, hey, don't fall unconscious."

    "Stranger." "Come on, Arthur, find something to talk about."

    a "I could talk about last anime I watched with my little sister."

    "Thank you, she tried to say."

    "But only one word out of two came out."

    e "You."
    a "Me?"

    "He huffed out a long sigh and snorted."

    a "First of all, I like it clean."

    "Her mind unconsciously focused on his voice and his laugh, its gentleness, its softness, its mellowness, although she could distinctly hear the rustling leaves and the whistle of the last autumn birds."

    "Slowly, she felt herself drift along the waves of his words."

    scene black with dissolve
    scene bg Livingroom_Night with fade

    show jeanne casual smile at left
    show lise smile at right

    j "You're telling me that the first time you met Arthur, you were hungover, sleeping on a bench all by yourself, threw up on him, and fell unconscious. Way to make a first impression."
    e "I don't think he remembers it."
    j "I don't think so either. He tends to forget a bunch. That's why he writes so much in his journal."
    e "It was during the senior welcome session so it's been a few months. Was he already keeping a journal at that time?"

    "Jeanne shrugged."

    j "You were dating someone at the time too, weren't you?"
    e "Yes. I shouldn't have."   
    e "I was too busy balancing my second job with everything. I'm still trying, it's not always easy. Our breakup was awful. I think I was depressed for an entire week."
    j "Why didn't you call me? I thought you were doing good."
    e "We didn't know each other. And I would have bothered you."
    j "You wouldn't have bothered me."
    e "Would you leave your bed for me?"
    j "Yes, I would." 
    j "First, reach out to your other friends, though."

    "They let out a little laugh"
    "And so, like every time they drank together, Jeanne fell asleep first. Her friend didn't have much resistance to alcohol and tiredness. Training didn't help either."
    "Her throat felt so dry to the point where she thought that the hangover would be fatal without water."

    scene black with dissolve

    menu:

        "Go to the kitchen downstairs.":
            jump suite2_3_1

        "Go to the bathroom.":
            jump suite2_3_2

    label suite2_3_1:
        scene black with dissolve
        "After drinking her fill, she walked to her bed and slept like a log."

    label suite2_3_2:
        scene bg kitchen with fade

        "Elise snuck into the kitchen, but for some reason, the lights were on."
        
        a "Oh? You're not sleeping?"
        
        show arthur smile at left
        show lise smile at right

        "Elise almost drop her glass out of fright. She hadn't seen him and heard him. That was why the lights were on. Stupid."

        a "Haha, sorry."

        "His laptop was on the table."

        a "You should get to sleep."
        e "How about you?"
        a "I'm answering questions from my master's students, and from you."

        "He smiled."

        "She nodded nervously as her heartbeat quickened."
        
        e "I shall accompany you then. Do you want some tea?"
        a "Sure. The tea is in the top right drawer. Mint for me. Thank you."

        "As the water was boiling, her brain was melting."
        "She placed the two teas on the table and sat on the chair opposite"

        a "You know what, I've changed my mind. Let's play a game."
        e "Are you sure? I didn't mean to disturb you."

        "She could feel the traits of her face moving, but couldn't imagine the expression she was making, nor she wanted to."

        a "I was here to get a snack, so might as well take a break. We should have a deck of cards."

        "He found two decks in one of the bottom drawers."

        a "Better two than one. How about a game of Slapjack?"

        "What he didn't know was that Elise was fond of games, especially card games. She might not be a genius player, but she might not be too far from it."
        "Her inner competitiveness took over her previous nervousness."
        "They played for an hour before he finally held his hands up to signify that he was giving up. She was just too good."
        "He refilled their mugs with mint tea."
        "The old clock hung on top of the fridge rang four in the morning. She had gotten so into the game that she didn't notice that it had gotten very late. The adrenaline was still rushing in her veins, erasing any traces of weariness."

        e "Let's change games. One that's easier on the reflexes and on the brain."
        a "I can't tell if you're being considerate or trash talking me."

        "Arthur laughed as his eyes drifted over her hands."
        
        a "Just choose a game where I don't have to worry about hitting your wrist."

        "He pointed at her bracelet."

        a "It suits you."

        "Mixed feelings filled her heart."

        e "Thanks."
        a "Well, if I win the next game, you'll go to sleep."

        "Elise remembered something."

        e "First, actually, I have a gift for you."
        a "Oh, I've got one for you too."
        e "Ah?"
        a "To thank you for taking care of my sister."

        scene black with dissolve
        scene bg kitchen with fade


        "A minute later, they reappeared in the kitchen with their gifts. One was beautifully packed and the other was messily covered in black present wrap."

        show arthur smile at left
        show lise smile at right

        "Arthur scratched his head in embarrassment."

        a "I did my best with packaging. I hope you'll like it."

        "Elise unwrapped it carefully."

        a "Surprise? A dark blue waterproof coat for your family dog."

        "It'd look so cute. 'Can I hug you' was what she wanted to say, but all she could do was nodding with an awkward smile."

        "She gave him the present she prepared."

        "He opened the box."

        a "Reading glasses. A very considerate and useful gift."

        "He put them on."

        a "Do I look good?"

        "He chuckled."

        "Then he brought her into his arms."

        "She could feel his breath on her nape."

        a "Thank you, Elise."

        "He pulled back as her gaze stopped on his lips."


