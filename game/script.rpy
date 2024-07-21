define n = Character('Narrator',color="#c8c8ff"  )
init python:
    def cover_screen(img_width, img_height):
        # Get the game's screen dimensions
        screen_width, screen_height = renpy.config.screen_width, renpy.config.screen_height

        # Calculate zoom factor needed for the image to cover the screen
        zoom_factor = max(screen_width / float(img_width), screen_height / float(img_height))

        # Define the transform with the calculated zoom factor
        return Transform(zoom=zoom_factor)

    class DynamicCharacter:
       def __init__(self, name, emotions, **kwargs):
           self.name = name
           self.emotions = emotions
           self.current_emotion = 'neutral'
           self.color = kwargs.get('color', "#ffffff")
           self.position = kwargs.get('position', None)
           self.character = Character(name, color=self.color)  # Create the Character object here
           self.update_image()

       def update_image(self):
           self.image = self.emotions.get(self.current_emotion, self.emotions['neutral'])

       def set_emotion(self, emotion):
           if emotion in self.emotions:
               self.current_emotion = emotion
           else:
               raise ValueError(f"Emotion '{emotion}' not found for character {self.name}")
           self.update_image()

       def __call__(self, *args, **kwargs):
           return self.character(*args, **kwargs)
# Define characters with their emotion states
### the popular main jock ( main bad influence friend) that love partying and having fun and always mocks adam but try's to bring the player to his group at the beginning of the game he will hate the students if he get to annoying or close to adam but doesn't mind if the player is close to emily
define b = DynamicCharacter('Bryan', emotions={
    'neutral': 'bryan_normal',
    'happy': 'bryan_happy',
    'sad': 'bryan_sad',
}, color="#ff6363",)
### emilu the good influence friend and maybe best friend of the player she trys to be friendly to adam but doesnt have adam as a friend she will be distant with the player if he does push adam studying no break agenda on emily  / very close to the player.She also trust the player that he will make the right choice and not follow the bad influence group
define e = DynamicCharacter('Emily', emotions={
    'neutral': 'emily_normal2',
    'happy': 'emily-smiling3',
    'sad': 'emily_sad2',
}, color="#f71e66",)
### the good influence but overprotective and overeactive friend of the player he will be distant if the player is close to the bad influence or the other bad students . Also distant if the player very close to emily and doesnt
define a = DynamicCharacter('Adam', emotions={
    'neutral': 'adam_smiling',
    'happy': 'adam_happy',
    'sad': 'adam_sad',
}, color="#04B486",)

### the player character he will have a skills and popularity and stress variables that will change depending on the choices he makes in the game
define m = DynamicCharacter('Me', emotions={
    'neutral': 'me_normal',
    'happy': 'me_smiling',
    'sad': 'me_sad',
}, color="#c8c8ff", )

### the main teacher character that will give courses and he will keep an eyes on the students and will have small interactions with the player about his study's status
define t = DynamicCharacter('Mr Jackson', emotions={
    'neutral': 'teacher1_normal',
    'sad': 'teacher1_sad',
}, color="#ffbdbd")

### the 2nd teacher character that will give courses and she will keep an eyes on the students and will have small interactions with the player about his study's status
define t2 = DynamicCharacter('Ms Baker', emotions={
    'neutral': 'teacher2_normal',
    'sad': 'teacher2_sad',
}, color="#ffbdbd")

### the principal of the college he hate troublemakers and will be angry if the player is close to the bad influence group
define p = DynamicCharacter('Principal Stan', emotions={
    'neutral': 'principal_normal',
    'angry': 'principal_angry',
}, color="#ffbdbd")


### the 2nd main character of the bad influence group (bryan and nico ) he will be the one that will be the most angry if the player is close to adam and will be the one that will try to bring the player to the bad influence group.
define ni = DynamicCharacter('Nico', emotions={
    'neutral':'nico_normal',
    'angry': 'nico_angry',
}, color="#ffbdbd")


### group of random students that  will have different reactions
define rg = DynamicCharacter('random_group',emotions={
    'neutral':'random_group_n', ## normal reactions group of rg random students
    'shocked':'random_group_s',## shocked reactions group of rg random students
    }, color="#ffbdbd")
### group of random students that  will have different reactions [those character images shadow mode]
define rb = DynamicCharacter('random_students',emotions={
'neutral':'random_student_b',# shadow of the random students
'neutral2':'random_student_b2',# shadow2 of the random students
},color="#ffbdbd")

### one  random student shadow
define ri = DynamicCharacter('random_student',emotions={
'neutral':'random_student_f', #female student  shadow
'neutral2':'random_student_m',#male student  shadow
},color="#ffbdbd")

### The "3rd main character of the bad influence group (bryan and nico )
define br = DynamicCharacter('Brett', emotions={
    'neutral': 'brett_normal',
    'sad': 'brett_sad',
    'angry' : 'brett_angry',
}, color="#ffbdbd")

### The groups of random students jocks that loves partying and having fun
define jocks = DynamicCharacter('Jocks',emotions={
'neutral':'jocks_group_normal',
'dissapointed':'jocks_group_disappointed',
},color="#ffbdbd")



# Relationship Variables
default adam_friendship = 0
default emily_friendship = 0
default bryan_friendship = 0
default teacher_friendship = 5
default nico_friendship = 0
default brett_friendship = 0
default teacher2_friendship = 0
default principal_friendship = 0




# choices conséquences
default skills = 0 # skills of the player that will unlock some choices in the game
default popularity = 0 # popularity of the player
default stress = 0 # stress of the player that will affect the choices in the game
# 1- Adam classroom
default adamproposition = False

# Unrelated images (no character tags)
image uni = "uniiii.png"
image parisw = "parisweird.png"
image creditt = "creditt.png"
image uniii = "uniii.png"

# All scenes background images
image uni_park_day = "uni_park_day.png" # University park during the day
image uni_park_evening = "uni_park_evening.png" # University park during the evening
image uni_day = "uni_daylight.png" # University during the day
image uni_night = "uni_night.png" # University during the night
image uni_sunset = "uni_sunset.png" # University during the sunset

image uni_hallway1 = "uni_hallway1.png" # University hallway 1
image uni_hallway3 = "uni_hallway3.png" # University hallway 3
image uni_principaloffice = "uni_principaloffice.png" # University principal's office hallway
image uni_library_empty = "uni_library_empty.png"  # University library empty
image uni_library_full = "uni_library_full.png" # University library full
image classroom = "classroom.png" # Classroom
image principaloffice = "principaloffice.png" # Principal's office
image uni_cafeteria = "uni_cafeteria.png" # University cafeteria
image bryan_house = "bryan_mansion.png" # Bryan's house
image player_house_room = "player_house_room.png" # Player's house room
image player_house_room_evening = "player_house_evening.png" # Player's house at evening
image uni_mainbighall = "uni_mainbighall.png" # University main hall where important principal announcement and  graduation would take place
image emily_room = "emily_room.png" # Emily's room
image adam_room = "adam_room.png" # Adam's room
image bryan_dance_room = "bryan_dance_room.png" # Bryan's dance room
image bryan_chill_room = "bryan_chill_room.png" # Bryan's chill room



#Notifications screen
screen notification(msg):
    frame:
        xalign 0.5
        yalign 0.1
        background Frame("gui/thoughtbubble.png",)
        text msg style "notification_text"

style notification_text is default:
    size 22
    color "#63ff69"

transform right:
    xalign 1.2 yalign 0.9

transform middle:
    xalign 0.1 yalign 0.9

transform right2:
    xalign 1.4 yalign 0.6

transform right3:
    xalign 1.4 yalign 2.8

transform left2:
    xalign -0.3 yalign 2.8

# Define images for the stats
image skill_icon = "skill_icon.png"
image stress_icon = "stress_icon.png"
image popularity_icon = "popularity_icon.png"




label start:
    show creditt
    n "This is a game made by the group InteractiveNovel in Estiam."
    n " members of the group are Tamim, Maxime, Ilyas."
    show parisw
    n "It's a new bachelor year for you (student 1), you are a student in the university (Estiam), your actions and relationship with other students will affect the ending "
    scene uni_park_day at cover_screen(1100, 1380)
    $ a.set_emotion('happy')
    show expression a.image at right with dissolve
    "Adam" "Hi there! How was class?"
    hide a

    $ m.set_emotion('neutral')
    show expression m.image at middle with dissolve
    "Me" "Good..."
    $ m.set_emotion('sad')
    show expression m.image at middle with dissolve
    "Me" "I can't bring myself to admit that it all went in one ear and out the other."
    hide a

    $ a.set_emotion('neutral')
    show expression a.image at right with dissolve
    "Adam" "How was it?"
    hide a

    menu:
        "It was interesting! I learned a lot.":
            jump choice_interesting
        "It was boring...":
            jump choice_boring
        "I didn't pay attention...":
            jump choice_not_paying_attention

label choice_interesting:
    $ adam_friendship += 5
    $ m.set_emotion('happy')
    show expression m.image at middle with dissolve
    m "It was interesting! I learned a lot."
    $ a.set_emotion('happy')
    show expression a.image at right with dissolve
    a "That's great to hear! I'm glad you enjoyed it."
    hide a
    jump continue_conversation

label choice_boring:
    $ adam_friendship -= 2
    $ bryan_friendship += 5
    $ m.set_emotion('neutral')
    show expression m.image at middle with dissolve
    m "It was boring..."
    $ a.set_emotion('sad')
    show expression a.image at right with dissolve
    a "Oh, that's too bad. Maybe next time it'll be more engaging."
    hide expression a.image
    $ renpy.pause(0.2)
    $ b.set_emotion('neutral')
    hide expression a.image
    show expression b.image at right with dissolve
    b "Hey, how's it going? join our group at the end of the class if you want since adam a boring nerd hehe"
    jump continue_conversation

label choice_not_paying_attention:
    $ adam_friendship -= 5
    $ m.set_emotion('sad')
    show expression m.image at middle
    m "I didn't pay attention..."
    $ a.set_emotion('neutral')
    show expression a.image at right with dissolve
    m "Well, that's not ideal, but it happens sometimes."
    hide expression a.image
    $ b.set_emotion('neutral')
    hide expression a.image
    #b_character = b.get_character(),
    show expression b.image at right with dissolve
    b "Hey, what's up? You are rightttt this course is boringggg.don't listen to the nerd on the right hehe"
    jump continue_conversation

    hide a
label continue_conversation:
    $ m.set_emotion('neutral')
    show expression m.image at middle with dissolve
    m "Well, I'm new around here."


    $ a.set_emotion('happy')
    show expression a.image at right with dissolve
    a "Don't worry, you'll get the hang of it. By the way, this is Emily, my friend."
    hide expression a.image

    hide a
    $ e.set_emotion('happy')
    show expression e.image at right with dissolve
    e "Nice to meet you! What's your name?"

    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip() if player_name else "Me"
    $ m.character = Character(player_name, color=m.color, image=m.image)

    $ m.set_emotion('neutral')
    show expression m.image at middle
    m "[player_name]"
    hide expression m.image

    $ e.set_emotion('happy')
    show expression e.image at right
    e "Well, [player_name], welcome to Estiam! I hope you enjoy your time here."

    menu:
        "I'm a bit nervous about being the new kid.":
            $ m.set_emotion('sad')
            show expression m.image at middle
            m "I'm a bit nervous about being the new kid."
            $ e.set_emotion('neutral')
            show expression e.image at right
            e "It's totally normal to feel that way. Just be yourself and you'll find your place."
        "I'm excited to meet new people!":
            $ m.set_emotion('happy')
            show expression m.image at middle
            m "I'm excited to meet new people!"
            $ e.set_emotion('happy')
            show expression e.image at right
            e "That's the spirit! There are lots of great people here."

    n "You have met Adam and Emily, two students at Estiam. Your interactions with them will affect your relationships and the story's outcome."
   ### hallway scene
    scene uni_hallway1 at cover_screen(1100, 1380)
    n "As you walk through the hallway, you see Bryan, another student at Estiam."

    if bryan_friendship >= 5:
        $ b.set_emotion('neutral')
        show expression b.image at right with dissolve
        b "Hey, [player_name], how's it going? join our group at the end of the class if you want since adam a boring nerd hehe"
        hide expression b.image
        $ ni.set_emotion('neutral')
        show expression ni.image at right2 with dissolve
        ni "Hey, [player_name], I heard you're new here and you are already bored haha i like you join us !"
        hide expression ni.image
    else:
        $ b.set_emotion('neutral')
        show expression b.image at right with dissolve
        b "Hey, [player_name], how's it going? join us if you find Adam boring hehe"
        hide expression b.image
        $ ni.set_emotion('neutral')
        show expression ni.image at right2 with dissolve
        ni "Hey, [player_name], I heard you  are getting to friendly with the losers be careful!"
        hide expression ni.image





    # New Scene: Classroom

    scene classroom at cover_screen(1100, 1380)
    with dissolve
    show screen notification("Warning: Upcoming choices will affect your skills , popularity,stress and  friendship .")
    n "You enter the classroom and take a seat. The teacher is setting up the projector, and the students are chatting."
    hide screen notification

    $ rb.set_emotion('neutral')
    show expression rb.image at left2 with dissolve
    rb "Hey, have you heard that we may get a project exam today?"
    $ rb.set_emotion('neutral2')
    show expression rb.image at right3 with dissolve
    rb "I hope not, I didn't study at all!"
    hide expression rb.image



    $ rg.set_emotion('neutral')
    show expression rg.image at right2 with dissolve
    rg "I heard that the teacher will announce it soon, so be prepared!"
    hide expression rg.image
    $ ri.set_emotion('neutral2')
    show expression ri.image at right with dissolve
    ri "I heard Bryan is throwing a party tonight, are you guys coming?"
    hide expression ri.image
    $ jocks.set_emotion('neutral')
    show expression jocks.image at right2 with dissolve
    jocks "Yeah, it's going to be epic! You should all come!"
    hide expression jocks.image
    $ t.set_emotion('neutral')
    show expression t.image at right with dissolve
    t "Be quiet, class! I need silence to see what's wrong with the projector."
    hide expression t.image

    n "The classroom falls silent as everyone watches the teacher struggle with the projector. You glance around and notice the different reactions from your classmates."

    $ rb.set_emotion ('neutral')
    show expression rb.image at left2 with dissolve
    rb " Did you guys also hear we're starting quantum computing today ?"

    n "A girl seem to have come late to the class outta nowhere but heard the conversation and she seems to be a loud mouth and a troublemaker"


    $ br.set_emotion('angry')
    show expression br.image at right2 with dissolve
    br "WHAT ? this is insane we just started regular programming few months ago and now we are diving into quantum computing ??!!"
    hide expression br.image
    hide expression rb.image

    $ t.set_emotion('sad')
    show expression t.image at right with dissolve
    t "i said  SILENCE ! Ms brett you are late again so do not have the odacity to speak out loud!I'm going to report you to the principal if you keep this up!now go sit down and be quiet"
    hide expression t.image

    $ br.set_emotion('sad')
    show expression br.image at right2 with dissolve
    br """jeeez I'm sorry Mr Jackson,**quietly mumbling** chill out man."""
    hide expression br.image
    $ a.set_emotion('happy')
    show expression a.image at right
    a "Maybe stopping the partying and start studying would be a good idea."
    hide expression a.image
    $ e.set_emotion('neutral')
    show expression e.image at right2 with dissolve
    e "Did you really had to say that Adam? trying to heat up the situation?"
    hide expression e.image
    $ br.set_emotion('neutral')
    show expression br.image at right2 with dissolve
    br """Look who's talking Mr. always studying and never having fun! you want to add me in your troublemaker list too? i think you should listen to emily and stop being a nerd"""
    hide expression br.image
    menu:
        "Back up Brett":
            show screen notification("You gained 10 friendship points with Brett and 5 with Emily, but lost 5 with Adam.")

            $ popularity += 7
            $ skills += 5
            $ stress += 1
            $ adam_friendship -= 5
            $ emily_friendship += 5
            $ brett_friendship += 10
            $ bryan_friendship += 5
            $ nico_friendship += 5
            $ teacher_friendship -=1

            $ m.set_emotion('neutral')
            show expression m.image at middle with dissolve


            m "Mr jackson was a bit harsh and you shouldn't be heating up the situation Adam"
            $ a.set_emotion('sad')
            show expression a.image at right with dissolve
            a "I didn't thought you were like this [player_name] , ok i will stop i apologize "
            hide screen notification
            hide expression a.image
            hide screen notification
            $ e.set_emotion('happy')
            show expression e.image at right with dissolve
            e " [player_name] is like what ? He is right Adam you should stop acting like the world greatest student"
            hide expression e.image
            show screen notification("You have [popularity] popularity , [stress] stress points and [skills] skills.")
            $ br.set_emotion('neutral')
            show expression br.image at right2 with dissolve
            br "thank you new guy for backing me up i appreciate it your name is [player_name] right?"
            hide expression br.image
            hide screen notification
            $ b.set_emotion('neutral')
            show expression b.image at right with dissolve
            b "Hehe right ! [player_name] is a good cool guy you heard that Adam ? nobody like you in this class"
            hide expression b.image
            $ ni.set_emotion('neutral')
            show expression ni.image at right2 with dissolve
            ni "Maybe it's time to stop being a nerd and start having fun like [player_name] and brett"
            hide expression ni.image
            hide expression m.image
            $ t.set_emotion('neutral')
            show expression t.image at right with dissolve
            t "I didn't expected you to talk [player_name] i am really dissapointed that you are not silent "
            n "The teacher finally manages to get the projector working and starts the lesson. A slide with complex diagrams appears on the screen."
            hide expression t.image

        "Calm the situation down":
            $ popularity += 3
            $ skills += 10
            $ stress += 1
            $ adam_friendship -= 2
            $ emily_friendship += 6
            $ brett_friendship += 6
            $ bryan_friendship += 3
            $ nico_friendship += 3
            $ teacher_friendship += 3
            $ t.set_emotion('neutral')
            show screen notification("You gained 3 popularity, 7 skills, and 1 stress point you also gained 6 friendship points with Emily, 5 with Brett, 3 with Bryan and Nico, but lost 2 with Adam and gained 3 with the teacher.")
            $ m.set_emotion('neutral')
            show expression m.image at middle with dissolve
            m "Let's all calm down and focus on the lesson, also Mr Jackson is right we should all be quiet maybe he is having a bad day, so adam dont tense up the situation for nothing"
            $ a.set_emotion('neutral')
            show expression a.image at right with dissolve
            a "I guess you're right, [player_name]. I apologize for heating up the situation."
            hide expression a.image
            $ br.set_emotion('neutral')
            show expression br.image at right2 with dissolve
            br "Well atleast [player_name] is a cool unlike you Adam"
            hide expression br.image
            $ e.set_emotion('happy')
            show expression e.image at right with dissolve
            e "[player_name] is right we shouldn't be acting like this in class"
            hide expression e.image
            $ b.set_emotion('neutral')
            show expression b.image at right with dissolve
            b "Yeah, you heard that Adam? [player_name] is right we should all calm down"
            hide expression b.image
            $ ni.set_emotion('neutral')
            show expression ni.image at right2 with dissolve
            ni "I guess we should all calm down and focus on the lesson"
            hide expression ni.image
            $ t.set_emotion('neutral')
            show expression t.image at right with dissolve
            t "I am hearing everything you should be silent and focus on the lesson"

            n"The teacher finally manages to get the projector working and starts the lesson. A slide with complex diagrams appears on the screen."


        "Stay out of it":
            $ popularity += 0
            $ skills += 7
            $ stress += 0
            $ adam_friendship -= 0
            $ emily_friendship -= 3
            $ brett_friendship += 0
            $ bryan_friendship += 0
            $ nico_friendship += 0
            $ teacher_friendship += 10
            show screen notification("You gained 5 skills and 10 friendship points with the teacher, but lost 3 with Emily because she expected more from you ! Remember that.")
            $ e.set_emotion('sad')
            show expression e.image at right with dissolve
            e" [player_name] i wish you would have said something , adam wasn't right to heat up the situation"
            hide expression e.image
            $ t.set_emotion('neutral')
            show expression t.image at right with dissolve
            t "Or [player_name] just want to stay out of it and focus on the lesson? i hear you guys talking!"
            hide expression t.image

        "Back up Adam":
            $ popularity += 2
            $ skills += 3
            $ stress += 1
            $ adam_friendship +=10
            $ emily_friendship -= 1
            $ brett_friendship -= 5
            $ bryan_friendship -= 5
            $ nico_friendship -= 5
            $ teacher_friendship -= 1
            show screen notification("You gained 3 skills and 1 stress point you also gained 10 friendship points with Adam, 5 with the teacher, but lost 1 with Emily, 5 with Brett, Bryan and Nico.")
            $ m.set_emotion('neutral')
            show expression m.image at middle with dissolve
            m "Adam is right, maybe you guys should calm down and focus on the lesson and stop partying if you want to succeed"
            $ a.set_emotion('happy')
            show expression a.image at right with dissolve
            a "Thanks [player_name], I appreciate your support."
            hide expression a.image
            $ br.set_emotion('sad')
            show expression br.image at right2 with dissolve
            br "So adam found a friend to back him up ? I see how it is [player_name] hope you are not who i think you are"
            hide expression br.image
            $ e.set_emotion('neutral')
            show expression e.image at right with dissolve
            e "Why did you back up Adam [player_name] ? i didn't think you could act like a arrogant student as well, im kind of dissapointed"
            hide expression e.image
            if adam_friendship >= 15:
                $ b.set_emotion('neutral')
                show expression b.image at right with dissolve
                b "Well, [player_name] so you are a nerd like Adam after all"
                hide expression b.image
                $ ni.set_emotion('neutral')
                show expression ni.image at right2 with dissolve
                ni "I guess you are not who i thought you were [player_name] "
                hide expression ni.image
            else:
                $ b.set_emotion('neutral')
                show expression b.image at right with dissolve
                b "Well, [player_name] i dont agree with you but i respect your opinion for now "
                hide expression b.image
                $ ni.set_emotion('angry')
                show expression ni.image at right2 with dissolve
                ni "Adam getting in your head [player_name] ?"
                hide expression ni.image
                $ t.set_emotion('neutral')
                show expression t.image at right with dissolve
                t "I didn't expect you to speak [player_name] i am really dissapointed that you are not silent "
                hide expression t.image
                n "The teacher finally manages to get the projector working and starts the lesson. A slide with complex diagrams appears on the screen."
















    menu:
        "Listen to the students":
            $ popularity += 10
            $ stress += 1
            $ skills += 3

            $ b.set_emotion('neutral')
            show screen notification("You gained [popularity] popularity and [stress] stress.")
            show expression b.image at right with dissolve
            b "[player_name], did you hear about the party tonight? It's going to be epic!"
            hide expression b.image
            $ e.set_emotion('neutral')
            show expression e.image at right2 with dissolve
            e "I'm more worried about this project exam. I hope it's not too hard."
            hide screen notification
            hide expression e.image

            n "The teacher finally manages to get the projector working and starts the lesson. A slide with complex diagrams appears on the screen."
        "Pay attention to class":
            $ skills += 15
            $ stress -= 5
            $ adam_friendship += 3
            $ t.set_emotion('neutral')
            show expression t.image at right with dissolve
            t "Pay close attention, as this will be important for your project."

        "Just don't listen":
            $ skills -= 7
            $ stress += 15
            $ adam_friendship -= 3
            $ emily_friendship += 5
            $ popularity += 10
            show screen notification("You lost [skills] skills and gained [stress] stress and [popularity] popularity.")
            $ m.set_emotion('happy')
            show expression m.image at middle with dissolve
            m "I'm going to relax and wait for the teacher to explain everything."
            hide expression m.image


    if popularity >= 20 and stress >= 20:
        n "You are getting more careless and stressed, and it's starting to show. The teacher notices your lack of focus and this is giving you a bad reputation."
    hide expression t.image
    n "The teacher begins to explain the concepts, and you do your best to take notes. You notice that some students are struggling to keep up. Adam however ..."
    $ a.set_emotion('happy')
    show expression a.image at right with dissolve
    a "I feel so motivated !"
    hide expression a.image
    n "The classroom buzzes with a mix of excitement and nervousness. You can feel the anticipation in the air."
    $ rb.set_emotion('neutral')
    show expression rb.image at left2 with dissolve
    rb "oooooof"
    hide expression rb.image
    $ e.set_emotion('neutral')
    show expression e.image at right with dissolve
    e "Ugh this is though , i have to study tonight that's for sure"
    hide expression e.image





    menu:
       "Try to recall what you know about quantum computing":
        $ skills += 7
        $ stress += 2
        $ emily_friendship += 3
        $ adam_friendship += 3
        show screen notification("You gained [skills] skills and [stress] stress.")
        n "You wrack your brain, trying to remember anything you've read about quantum computing. It's a cutting-edge field, you recall, that could revolutionize computing as we know it."
        $ m.set_emotion('neutral')
        show expression m.image at middle with dissolve
        m "I think I remember something about quantum bits and superposition... I'll have to look it up later."
        hide expression m.image
        hide screen notification
        n "dude you are a genius ! because i myself don't know what you the teacher is  talking about"
       "Ask your neighbor what they know ":
        $ popularity += 6
        $ skills += 4
        $ stress -= 3
        $ emily_friendship += 7
        show screen notification("You gained [popularity] popularity, [skills] skills, and calmed down a bit, [stress] stress.")
        n "You lean over to the student next to you, asking if they know anything about quantum computing. They share a few tidbits they've picked up, which helps you feel a bit more prepared."
        $ m.set_emotion('neutral')
        show expression m.image at middle with dissolve
        m "Thanks for the info, I appreciate it."
        $ e.set_emotion('neutral')
        show expression e.image at right with dissolve
        e "I'm glad you're feeling more confident now if you want to study together after class let me know"
        hide expression e.image
        hide expression m.image
        hide screen notification
       "Just don't listen who care about quantum computing":
        $ popularity += 11
        $ skills -= 4
        $ stress += 6
        $ adam_friendship -= 3
        show screen notification("You gained [popularity] popularity, but lost [skills] skills and gained [stress] stress.")
        n "You decide to relax and wait for the teacher to explain everything(but you're not listening wtf?). let's see what happens next."
        $ m.set_emotion('neutral')
        show expression m.image at middle with dissolve
        m "I'm falling asleep, I can't focus on this."
        $ e.set_emotion('neutral')
        show expression e.image at right with dissolve
        e "Pull yourself together [player_name]!!. This is important for the project exam!"
        hide expression e.image
        hide expression m.image
        hide screen notification

    if stress >= 20 and popularity >= 20:
        $ bryan_friendship += 15
        $ m.set_emotion('sad')
        show expression m.image at middle with dissolve
        m "imma pull my phone and play some games to relax"
        n "There is the first consequences of being to stressed and not caring about studying a lot! You pull out your phone and start playing games to relax, but the teacher catches you and gives you a warning."
        $ b.set_emotion('neutral')
        show expression b.image at right with dissolve
        b "Dammmmn, [player_name] being a menace i like that hehe "
        hide expression b.image
        $ t.set_emotion('angry')
        show expression t.image at right with dissolve
        t "I will not tolerate this behavior in my class, [player_name]! You should be ashamed of yourself ! Get this phone off right now ! And listen  ."
        hide expression t.image
        $ jocks.set_emotion('neutral')
        show expression jocks.image at right2 with dissolve
        jocks "[player_name] is right , who cares about quantum computing anyway"
        hide expression jocks.image
        hide expression m.image

    $ t.set_emotion ('neutral')
    show expression t.image at right with dissolve
    t "Let's start with the basics. In classical computing, we use bits - binary digits that can be either 0 or 1. All the programs you've written so far use these bits as their fundamental units of information."
    t "Now, in quantum computing, we use qubits. Unlike classical bits, qubits can exist in a superposition of states, meaning they can be both 0 and 1 simultaneously until observed."
    n "The class erupts in murmurs of confusion."
    $ rg.set_emotion('neutral')
    show expression rg.image at left with dissolve
    rg "But how can something be two things at once? That doesn't make sense!"
    hide expression rg.image
    t "Excellent question! This is where quantum mechanics comes in. At the quantum level, particles can exist in multiple states simultaneously. It's counter-intuitive, but it's how our universe works at the smallest scales."

    t "Now, let's relate this back to programming. In classical programming, you might write an if-else statement like this:"

    n "The teacher types some code on the projector:"
    t """
    if (x == 1) {{
        do_something();
    }} else {{
        do_something_else();
    }}
      """

    t "In this case, the program follows one path or the other. But in quantum computing, it's as if both paths are taken simultaneously!"

    n "The students look both fascinated and bewildered."

    t "Another key concept in quantum computing is entanglement. This is when qubits are connected in such a way that the state of one qubit can instantly affect the state of another, regardless of the distance between them."

    t "This property allows quantum computers to perform certain calculations exponentially faster than classical computers. It's particularly useful in fields like cryptography, optimization, and simulating quantum systems."

    n "As the lecture progresses, you find yourself both excited and overwhelmed by the possibilities of quantum computing."

    t "Now, let's look at how we might represent a simple quantum circuit in code. We'll use Qiskit, a quantum computing framework in Python."

    n "The teacher types more code on the projector:"
    t """
    from qiskit import QuantumCircuit, execute, Aer
    # Create a quantum circuit with 2 qubits
    circuit = QuantumCircuit(2, 2)

    # Apply a Hadamard gate to the first qubit
    circuit.h(0)
    # Apply a CNOT gate with control qubit 0 and target qubit 1
    circuit.cx(0, 1)
    # Measure both qubits
    circuit.measure([0,1], [0,1])

    # Execute the circuit on a simulator
    backend = Aer.get_backend('qasm_simulator')
    job = execute(circuit, backend, shots=1000)
    result = job.result()

    # Print the results
    print(result.get_counts(circuit))
"""
    n"The teacher explains the code step by step, showing how it creates a simple quantum circuit and simulates its execution on a quantum computer simulator. I won't lie i don't understand it myself but i hope you do"
    hide expression t.image
    t "This code creates a simple quantum circuit that demonstrates superposition and entanglement. It's a basic example of what quantum programs look like."

    n "You notice some students furiously typing notes, while others look completely lost."

    $ b.set_emotion('neutral')
    show expression b.image at right with dissolve
    b "Psst, [player_name], are you getting any of this quantum stuff?"
    hide expression b.image

    menu:
      "Try to explain it to Bryan":
        n"I know it's annoying but adam is watching you and he is not happy that you are helping  bryan however you gaining skills because helping others also helps you understand the subject better"
        $ skills += 7
        $ popularity += 5
        $ stress += 3
        $ bryan_friendship += 7
        $ adam_friendship -= 3
        $ teacher_friendship += 5
        $ emily_friendship += 3
        n "You whisper a simplified explanation to Bryan, comparing qubits to spinning coins and entanglement to magical linked coins. Bryan seems to grasp the basics and looks impressed."
        $ m.set_emotion('neutral')
        show expression m.image at middle with dissolve
        m "So basically the code is showing how qubits can be in multiple states at once and how they can be connected to affect each other"
        $ b.set_emotion('neutral')
        show expression b.image at right with dissolve
        b "Thanks for the explanation [player_name] hehe i appreciate it"
        hide expression b.image
        hide expression m.image

      "Admit you're struggling too":
        n"You gained skills too ? why? because admitting you are struggling is a good thing and you are not the only one struggling however Adam did not like that hes watching everybody huh"
        $ skills += 5
        $ bryan_friendship += 4
        $ popularity += 3
        $ stress += 1
        $ adam_friendship -= 2
        $ emily_friendship += 3
        $ teacher_friendship += 7
        n "You shrug and whisper back that you're just as confused. Bryan seems relieved he's not the only one struggling with the complex concepts."
        $ m.set_emotion('sad')
        show expression m.image at middle with dissolve
        m "I'm struggling too, this is really tough."
        $ b.set_emotion('neutral')
        show expression b.image at right with dissolve
        b "So this course really though only that loser over there can enjoy it hehe but i appreciate it [player_name] "
        hide expression b.image
      "Ignore Bryan and focus on the lecture":
        n "Watch out ! ignoring bryan will make him feel left out and he will not like you for that"
        $ bryan_friendship -= 7
        $ skills += 3
        $ teacher_friendship += 3
        $ popularity -= 10
        if adam_friendship >= 15 and bryan_friendship <= 10:
            $ adam_friendship += 5
            $ b.set_emotion('angry')
            show expression b.image at right with dissolve
            b "So you are truly a loser that study all the time and never help others or have fun huh [player_name] ? You are banned from coming to my party tonight"
            hide expression b.image

        n "You pretend not to hear Bryan and try to concentrate on the teacher's words, determined to understand these mind-bending concepts."
        $ b.set_emotion('neutral')
        show expression b.image at right with dissolve
        b "Hey [player_name] are you even listening to me ? i guess i am on my own here that wasn't cool"
        hide expression b.image
        $ br.set_emotion('neutral')
        show expression br.image at right2 with dissolve
        br "Hey player i get that your focused but don't ignore people like that everytime"
        hide expression br.image

    show screen notification("You have [skills] skills, [popularity] popularity, and [stress] stress. teacher_friendship [teacher_friendship] ")
    t "And that brings us to the end of today's introduction to quantum computing. Remember, understanding these concepts is crucial for your upcoming project, where you'll be designing a basic quantum algorithm."

    n "The teacher continues, discussing potential applications of quantum computing in various fields."

    t "Quantum computing has the potential to revolutionize many fields. In cryptography, it could break many of our current encryption methods, but also create unbreakable ones. In drug discovery, it could simulate molecular interactions far more accurately than classical computers."
    hide screen notification

    t "In artificial intelligence and machine learning, quantum computers could process vast amounts of data and recognize patterns far faster than classical computers. This could lead to breakthroughs in areas like natural language processing and computer vision."

    n "The class is a mix of excitement and anxiety as the implications of this technology sink in."
    $ e.set_emotion('neutral')
    show expression e.image at right2 with dissolve
    e "But if quantum computers can break our current encryption, isn't that dangerous? What about our online privacy and security?"
    hide expression e.image

    t "Another excellent question! This is indeed a concern, and it's why there's a lot of research going into post-quantum cryptography - encryption methods that even quantum computers can't break."

    n "The discussion continues, touching on ethical implications and the potential impact on various industries."

    $ t.set_emotion('neutral')
    show expression t.image at right with dissolve
    t "Before we wrap up, I want to remind you all that your project will involve designing a simple quantum algorithm and implementing it using Qiskit. You'll present your results at the end of the month. Make sure you're studying regularly and practicing with the quantum simulators."
    t "I want to see some of you for a talk before you leave the class"

    hide expression t.image

    if teacher_friendship >= 4 and popularity >= 10 and skills >= 6:
        $ t.set_emotion('neutral')
        show expression t.image at right with dissolve
        t "I'm impressed with your focus and dedication, [player_name]. Keep it up, and you'll do great things in this field unlike some other students you help other students and you are not just focused on yourself which is a great trait to have at work"
        hide expression t.image
    if  teacher_friendship < 4 and popularity >= 20 and skills <= 6:
        $ t.set_emotion('sad')
        show expression t.image at right with dissolve
        t "[player_name] i see you are not paying attention and you are not taking this seriously , this is serious even if you pass the exam and graduate you will not be able to work without any knowledge, i am saying this because you seem to be the kind of student only want the degree and not the knowledge you need to look out for your future"

    hide expression t.image
    n"The bell rings, signaling the end of the class. Students start packing up their things, and you feel a mix of excitement and anxiety about the upcoming project and the vast new field you're just beginning to explore."






    $ a.set_emotion('happy')
    show expression a.image at right
    a "So, [player_name], what do you think about joining our study group?"
    hide expression a.image

if adam_friendship >= 15 or skills >= 10:
    menu:
        "Sure, that sounds great!":
            $ a.set_emotion('happy')
            show expression a.image at right with dissolve
            a "Awesome! We'll meet at the library after school. I'm sure we can help each other out."
            jump group_study
        "I'm not sure, I need to catch up on the material first.":
            $ a.set_emotion('neutral')
            show expression a.image at right with dissolve
            a "No problem, take your time. I will be at the library if you need help."
            n "Adam nods and heads out of the classroom and you are also leaving for the hallway"
            hide expression a.image
            jump choice_unsure
        "No thanks, I prefer to study alone.":
            $ a.set_emotion('sad')
            show expression a.image at right with dissolve
            a "Alright,suit yourself. I'll be at the library if you change your mind."
            hide expression a.image
            $ b.set_emotion('neutral')
            show expression b.image at right with dissolve
            b "hehe will you look at that adam got rejected by [player_name] not a surprise, nobody want your 'carrying the team' attitude"
            hide expression b.image
            $ ni.set_emotion('neutral')
            show expression ni.image at right2 with dissolve
            ni "In your face adam ! that's karma for talking when you dont have to!"
            hide expression ni.image
            $ br.set_emotion('neutral')
            show expression br.image at right2 with dissolve
            br "You are not the team player you think you are adam haha"
            hide expression br.image
            $ a.set_emotion('sad')
            show expression a.image at right with dissolve
            a "You can go partying instead of bashing me guys, i'm out of here"
            hide expression a.image
            n"You leave the classroom and head to the hallway"
            jump choice_unsure

### hallway scenes
label choice_unsure:
    scene uni_hallway3 at cover_screen(1100, 1380)
    n "You walk out of the classroom and find yourself in the hallway thinking about the study group offer. You see Bryan and Nico chatting near the lockers."
    if  bryan_friendship >= 15:

       $ b.set_emotion('neutral')
       show expression b.image at right with dissolve
       b "Hey, [player_name], how was the class? I hope you understood the quantum stuff better than me! do you want to join our study group hehe?"
       hide expression b.image
       $ ni.set_emotion('neutral')
       show expression ni.image at right2 with dissolve
       ni "Hey, [player_name], we like you to join our study group we don't often get new people to join us"
       hide expression ni.image
       $ m.set_emotion('happy')
       show expression m.image at middle with dissolve
       m"Thanks for the offer guys, I appreciate it.I am still thinking about it"
       hide expression m.image
    if bryan_friendship >= 15 and brett_friendship >= 5 and teacher_friendship >= 4:
      $ e.set_emotion('neutral')
      show expression e.image at right with dissolve
      e "Hey [player_name], i was wondering if you want to join my study , i know adam is a work machine and can get irritating  but i think we can make a great study group you and me , if adam get in the way we can just be a duo study group"
    menu:
        "I am still thinking about it":
         $ m.set_emotion('neutral')
         show expression m.image at middle with dissolve
         m "I am still thinking about it"
         e "Alright, let me know if you decide to join me i will be not far from here taking a coffee from the vending machine"
         jump choice_unsure2
        "Join Emily's study group":
         e "Great! I'll just take a coffee from the vending machine and we can start studying"
         jump emily_study_group


label choice_unsure2:
    hide expression e.image
    $ m.set_emotion('neutral')
    show expression m.image at middle with dissolve
    show screen notification("This is your last chance to join a study group, choose wisely.it will affect your skills and friendship most importantly the ending")
    m "i have to join a study group but i don't know who to join who should i join ?"
    menu:
        "Join Bryan's study group":
            jump after_study_group_choice2
        "Join Emily's study group":
            jump emily_study_group
        "Join Adam's study group":
            jump adam_study_group
        "Study alone":
            jump study_alone

### emily group choices
hide screen notification
label emily_study_group:

    scene uni_hallway3  at cover_screen(1100, 1380)
    n "You walk over to Emily, who is waiting by the vending machine."
    $ e.set_emotion('happy')
    show expression e.image at right with dissolve
    e "I'm glad you decided to join me, [player_name]. Let's choose a place to study."
    hide expression e.image
    $ m.set_emotion('happy')
    show expression m.image at middle with dissolve
    m "Yeah sure let's go to ..."
    hide expression m.image
    n"You are suddenly interrupted by random students who are talking about the party tonight "
    $ jocks.set_emotion('neutral')
    show expression jocks.image at right2 with dissolve
    jocks "**megaphone** Hey guys don't forget about the party tonight it's going to be epic! you should all come!"
    $ rb.set_emotion('neutral')
    show expression rb.image at left2 with dissolve
    rb "And why should we come to the party when we have to study for the project exam?"
    jocks "Because it's going to be fun! You can study later aswell , come on! it's not like you have to stay all night"
    rb "Well we could go for a bit and then study later"
    if popularity >= 25 and bryan_friendship >= 15:
        show screen notification("Your popularity and relationships with bryan are so high that you are liked by the jocks and they want you to come to the party")
        $ jocks.set_emotion('neutral')
        show expression jocks.image at right2 with dissolve
        jocks "Hey [player_name] you should come to the party tonight it's going to be epic! You really impressed us by helping bryan "
        hide  screen notification
        hide expression jocks.image
        $ rb.set_emotion('neutral')
    if popularity >= 25 and bryan_friendship >= 15 and skills >= 15:
        show screen notification("Your popularity and relationships are so high that you are already popular and liked by EVERYONE in the class you are doing great !!!")
        show expression rb.image at left2 with dissolve
        rb "Yeah [player_name] yeah if you come i think most of us will come aswell he is very skilled and a team player a good example for all of us"
        hide expression rb.image
        hide screen notification
    if popularity >= 25 and bryan_friendship >= 15 and skills >= 15 and teacher_friendship >= 8:
         $ emily_friendship += 15
         $ e.set_emotion('neutral')
         show expression e.image at right with dissolve
         e "Adam wish he was you right now [player_name] huh ? but yeah they are right you are a great team player from what i've seen so far"
         hide expression e.image
    $ e.set_emotion('neutral')
    show expression e.image at right with dissolve
    e "Hmmm maybe we should go to the party for a bit ? and then study later? wouldn't hurt to have some fun what do you think [player_name] ?"
    hide expression e.image
    $ m.set_emotion('neutral')
    show expression m.image at middle with dissolve
    m "Well i think we should ..."
    hide expression m.image
    menu:
     "Go to the party":

        $ popularity += 10
        $ stress -= 5
        $ emily_friendship += 35
        $ e.set_emotion('happy')
        show expression e.image at right with dissolve
        e "Great! Let's go have some fun and then we can study later"
        hide expression e.image
        $ m.set_emotion('neutral')
        show expression m.image at middle with dissolve
        m "Let's not stay too long, we still have to study for the project exam"
        hide expression m.image
        scene uniii at cover_screen(1100, 1380) with dissolve
        n "You and Emily head to the party, and you are wondering if you made the right choice"


        jump party_scene


    hide expression jocks.image
    hide expression rb.image


#### party scene
label party_scene:
    scene bryan_house at cover_screen(1100, 1380)
    with dissolve

    if emily_friendship >= 56:
         show screen notification("You are actually on group Emily paths ")
         n "You and Emily arrive at the party, and the music is already blasting. The house is packed with students dancing, chatting, and having a great time."
         hide screen notification
         $ e.set_emotion('happy')
         show expression e.image at right with dissolve
         e "This party is kind of huge for an end of the year party, we should be watching the time as well. Text me if you want to leave."
         $ m.set_emotion('neutral')
         show expression m.image at middle with dissolve
         m "Yeah, we should stay for a bit and then head back to study."
         $ e.set_emotion('sad')
         show expression e.image at right with dissolve
         e "Is that Mr. Jackson arguing with some students over there? Looks bad. Try to avoid him, [player_name]."
         hide expression e.image
         $ t.set_emotion('sad')
         show expression t.image at right with dissolve
         t "Are you guys insane? You should be studying for the project exam, not getting drunk and doing fireworks illegally at an unsafe distance from the house!"
         hide expression t.image
         $ e.set_emotion('happy')
         show expression e.image at right with dissolve
         e "See you in a bit, [player_name]."
         hide expression e.image
         hide expression m.image
    else:
        n "You arrive at the party, and the music is already blasting. It seems Mr. Jackson is arguing with some students over there. What is the teacher doing at a student party?"
        $ t.set_emotion('sad')
        show expression t.image at right with dissolve
        t "Are you guys insane? You should be studying for the project exam, not getting drunk and doing fireworks illegally at an unsafe distance from the house!"
        hide expression t.image

    $ jocks.set_emotion('neutral')
    show expression jocks.image at left with dissolve
    jocks "Sir, who invited you to the party?"
    $ t.set_emotion('sad')
    show expression t.image at right with dissolve
    t "Bryan invited me to help him with the exam, and I'm walking into a party?????? But worse, I see some of my students drinking and doing fireworks in an unsafe distance from the house before the project exam?!?!"
    hide expression t.image
    $ ri.set_emotion('neutral')
    show expression ri.image at right2 with dissolve
    ri "Hey guys, that's Ms. Baker over there!"
    jocks "Did Bryan invite the whole college to the party?"
    hide expression ri.image
    hide expression jocks.image
    $ t2.set_emotion('sad')
    show expression t2.image at right with dissolve
    t2 "Is this how Gen-Z studies for exams?! Mr. Jackson, were you called for a 'project' emergency from Bryan too?"
    hide expression t2.image

    menu:
        "Talk to Bryan":
            jump talk_to_bryan
        "Find Emily":
            jump find_emily
        "Join the Jocks":
            jump join_the_jocks
        "Avoid the teachers and blend in":
            jump blend_in
        "Leave the party":
            jump leave_party

label talk_to_bryan:
    scene bryan_party with dissolve
    $ b.set_emotion('happy')
    show expression b.image at right with dissolve
    b "Hey, [player_name]! Glad you could make it. Having fun yet?"
    menu:
        "Yeah, it's great!":
            $ bryan_friendship += 5
            $ popularity += 5
            m "Yeah, it's great! Thanks for inviting me."
            b "Anytime, buddy! Enjoy the party!"
            jump party_continue
        "I'm worried about the exam...":
            $ bryan_friendship -= 5
            $ stress += 5
            m "I'm worried about the exam, though."
            b "Relax, [player_name]! One night of fun won't hurt. We'll study tomorrow."
            jump party_continue
        "Why are the teachers here?":
            $ bryan_friendship -= 5
            $ stress += 5
            m "Why are the teachers here, Bryan?"
            b "I had to convince them to come to keep things under control. But now they're just ruining the vibe."
            jump party_continue

label find_emily:
    scene emily_party with dissolve
    $ e.set_emotion('neutral')
    show expression e.image at right with dissolve
    e "Hey, [player_name]. Everything okay?"
    menu:
        "Yeah, just checking in.":
            $ emily_friendship += 5
            m "Yeah, just checking in."
            e "Thanks, [player_name]. Let's try to enjoy ourselves a bit."
            jump party_continue
        "I'm worried about the exam...":
            $ emily_friendship += 10
            $ stress += 5
            m "I'm worried about the exam, Emily."
            e "I understand. We'll get through it. Just don't let the stress get to you."
            jump party_continue
        "Have you seen Adam?":
            $ emily_friendship += 5
            m "Have you seen Adam?"
            e "Not yet, but I think he's avoiding the party. Probably studying."
            jump party_continue

label join_the_jocks:
    scene jocks_party with dissolve
    $ jocks.set_emotion('neutral')
    show expression jocks.image at right with dissolve
    jocks "Hey, [player_name]! Glad you could join us!"
    menu:
        "Let's dance!":
            $ popularity += 10
            m "Let's dance!"
            jocks "That's the spirit!"
            jump party_continue
        "I need a drink.":
            $ popularity += 5
            m "I need a drink."
            jocks "Right this way!"
            jump party_continue
        "What's up with the teachers?":
            $ popularity += 5
            $ stress += 5
            m "What's up with the teachers?"
            jocks "Bryan invited them for some reason. Just ignore them."
            jump party_continue

label blend_in:
    scene blend_in_party with dissolve
    n "You decide to avoid the teachers and blend into the crowd, trying to enjoy the party without attracting attention."
    $ popularity += 5
    jump party_continue

label leave_party:
    scene leave_party with dissolve
    n "You decide that the party isn't worth the risk and leave early. You head home to get some rest and maybe study a bit."
    $ stress -= 5
    $ skills += 5
    jump next_day

label party_continue:
    scene party_continue with dissolve
    n "The party continues, and you find yourself getting more involved. What do you want to do next?"
    menu:
        "Dance with Emily":
            jump dance_with_emily
        "Talk to random students":
            jump talk_to_random_students
        "Check on Bryan":
            jump check_on_bryan
        "Find a quiet spot to study":
            jump quiet_spot

label dance_with_emily:
    scene dance_with_emily with dissolve
    $ e.set_emotion('happy')
    show expression e.image at right with dissolve
    e "Hey, [player_name], want to dance?"
    $ m.set_emotion('happy')
    show expression m.image at middle with dissolve
    m "Sure!"
    n "You and Emily dance together, enjoying the music and the atmosphere. It's a great way to relieve some stress."
    $ stress -= 5
    $ emily_friendship += 10
    jump party_end

label talk_to_random_students:
    scene talk_to_random_students with dissolve
    $ rb.set_emotion('neutral')
    show expression rb.image at right with dissolve
    rb "Hey, [player_name]! Great party, right?"
    menu:
        "Yeah, it's awesome!":
            $ popularity += 5
            m "Yeah, it's awesome!"
            rb "Glad you're having fun!"
            jump party_end
        "I'm worried about the exam...":
            $ stress += 5
            m "I'm worried about the exam, though."
            rb "Don't stress too much. You'll do fine!"
            jump party_end
        "Seen any teachers around?":
            $ stress += 5
            m "Seen any teachers around?"
            rb "Yeah, they're trying to keep an eye on us. Just avoid them."
            jump party_end

label check_on_bryan:
    scene check_on_bryan with dissolve
    $ b.set_emotion('neutral')
    show expression b.image at right with dissolve
    b "Hey, [player_name]. Enjoying the party?"
    menu:
        "Yeah, it's great!":
            $ bryan_friendship += 5
            $ popularity += 5
            m "Yeah, it's great!"
            b "Awesome! Glad you could make it."
            jump party_end
        "I'm worried about the teachers...":
            $ bryan_friendship -= 5
            $ stress += 5
            m "I'm worried about the teachers, though."
            b "Don't let them ruin the fun. We'll deal with them later."
            jump party_end

label quiet_spot:
    scene quiet_spot with dissolve
    n "You find a quiet spot away from the party noise and try to study for a bit. It's not the best environment, but it's better than nothing."
    $ skills += 5
    $ stress -= 5
    jump party_end

label party_end:
    n "As the night goes on, you start feeling tired. It's time to wrap up and head home."
    jump next_day

label next_day:
    scene next_day_morning with dissolve
    n "You wake up the next day, ready to tackle whatever comes next."
    return



label after_study_group_choice2:

label after_study_group_choice:
    show uni_library_empty at cover_screen(1100, 1380)
    with dissolve
    if adamproposition:
        $ adam_friendship += 5
        $ a.set_emotion('happy')
        show expression a.image at right
        "Adam" "Alright, let's get started. Emily will probably be late as usual. Shall we start without her?"
        menu:
            "Yes, let's get started.":
                $ emily_friendship -= 3
                jump choice_start_study_group
            "No, let's wait for Emily.":
                jump choice_wait_for_emily

        label choice_wait_for_emily:
            $ emily_friendship += 5
            $ a.set_emotion('sad')
            show expression a.image at right
            "Adam" "Alright i hate waiting to start studying , let's wait for Emily to arrive before we start."
            hide expression a.image
            $ e.set_emotion('sad')
            show expression e.image at right
            "Emily" "I heard that adam , sorry i'm late guys, what are we studying today?"
            jump choice_start_study_group


    else:
        $ adam_friendship += 2
        $ emily_friendship += 5
        $ bryan_friendship -= 3
        $ a.set_emotion('sad')
        show expression a.image at right
        "Adam" "So now you decide to join Emily and [player_name]? I thought you were joining Bryan or studying alone. What do you need help with?"
        hide expression a.image
        $ e.set_emotion('happy')
        show expression e.image at right
        "Emily" "Why are you in such a bad mood, Adam? Sorry [player_name] I was late aswell. What do you need help with?"
        menu:
            "I need help with the last lecture.":
                jump choice_last_lecture
            "I need help with the homework assignment.":
                jump choice_homework_assignment
            "I need help with both.":
                jump choice_both





label choice_last_lecture:
    # Continue your story from here

label choice_homework_assignment:
    # Continue your story from here

label choice_both:
    # Continue your story from here
    # Later in the game, you can check the friendship level:
    if adam_friendship >= 20:
        "Adam" "Hey, you're becoming a great friend!"
    elif adam_friendship <= -10:
        "Adam" "Look, I don't think we're compatible as friends."
    else:
        "Adam" "We should hang out sometime!"

    if emily_friendship >= 20:
        "Emily" "Hey, you're becoming a great friend!"
    elif emily_friendship <= -10:
        "Emily" "Look, I don't think we're compatible as friends."
    else:
        "Emily" "We should hang out sometime!"
