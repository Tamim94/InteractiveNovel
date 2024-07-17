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
            self.update_image()

        def update_image(self):
            self.image = self.emotions.get(self.current_emotion, self.emotions['neutral'])

        def set_emotion(self, emotion):
            if emotion in self.emotions:
                self.current_emotion = emotion
            else:
                raise ValueError(f"Emotion '{emotion}' not found for character {self.name}")
            self.update_image()

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
}, color="#6370ff",)

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
default teacher_friendship = 0
default nico_friendship = 0





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
image bryan_house = "bryan_house.png" # Bryan's house
image player_house_room = "player_house_room.png" # Player's house room
image player_house_room_evening = "player_house_evening.png" # Player's house at evening
image uni_mainbighall = "uni_mainbighall.png" # University main hall where important principal announcement and  graduation would take place
image emily_room = "emily_room.png" # Emily's room
image adam_room = "adam_room.png" # Adam's room


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
    "Me" "It was interesting! I learned a lot."
    $ a.set_emotion('happy')
    show expression a.image at right with dissolve
    "Adam" "That's great to hear! I'm glad you enjoyed it."
    hide a
    jump continue_conversation

label choice_boring:
    $ adam_friendship -= 2
    $ bryan_friendship += 5
    $ m.set_emotion('neutral')
    show expression m.image at middle with dissolve
    "Me" "It was boring..."
    $ a.set_emotion('sad')
    show expression a.image at right with dissolve
    "Adam" "Oh, that's too bad. Maybe next time it'll be more engaging."
    hide expression a.image
    $ renpy.pause(0.2)
    $ b.set_emotion('neutral')
    hide expression a.image
    show expression b.image at right with dissolve
    "Bryan" "Hey, what's up? You are rightttt this course is boringggg.don't listen to the nerd on the right hehe"
    jump continue_conversation

label choice_not_paying_attention:
    $ adam_friendship -= 5
    $ m.set_emotion('sad')
    show expression m.image at middle
    "Me" "I didn't pay attention..."
    $ a.set_emotion('neutral')
    show expression a.image at right with dissolve
    "Adam" "Well, that's not ideal, but it happens sometimes."
    hide expression a.image
    $ b.set_emotion('neutral')
    hide expression a.image
    show expression b.image at right with dissolve
    "Bryan" "Hey, what's up? You are rightttt this course is boringggg.don't listen to the nerd on the right hehe"
    jump continue_conversation

    hide a
label continue_conversation:
    $ m.set_emotion('neutral')
    show expression m.image at middle with dissolve
    "Me" "Well, I'm new around here."


    $ a.set_emotion('happy')
    show expression a.image at right with dissolve
    "Adam" "Don't worry, you'll get the hang of it. By the way, this is Emily, my friend."
    hide expression a.image

    hide a
    $ e.set_emotion('happy')
    show expression e.image at right with dissolve
    "Emily" "Nice to meet you! What's your name?"

    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip() if player_name else "Me"
    $ m.character = Character(player_name, color=m.color, image=m.image)

    $ m.set_emotion('neutral')
    show expression m.image at middle
    "Me" "[player_name]"
    hide expression m.image

    $ e.set_emotion('happy')
    show expression e.image at right
    "Emily" "Well, [player_name], welcome to Estiam! I hope you enjoy your time here."

    menu:
        "I'm a bit nervous about being the new kid.":
            $ m.set_emotion('sad')
            show expression m.image at middle
            "Me" "I'm a bit nervous about being the new kid."
            $ e.set_emotion('neutral')
            show expression e.image at right
            "Emily" "It's totally normal to feel that way. Just be yourself and you'll find your place."
        "I'm excited to meet new people!":
            $ m.set_emotion('happy')
            show expression m.image at middle
            "Me" "I'm excited to meet new people!"
            $ e.set_emotion('happy')
            show expression e.image at right
            "Emily" "That's the spirit! There are lots of great people here."

    n "You have met Adam and Emily, two students at Estiam. Your interactions with them will affect your relationships and the story's outcome."
   ### hallway scene
    scene uni_hallway1 at cover_screen(1100, 1380)
    n "As you walk through the hallway, you see Bryan, another student at Estiam."

    if bryan_friendship >= 5:
        $ b.set_emotion('neutral')
        show expression b.image at right with dissolve
        "Bryan" "Hey, [player_name], how's it going? join our group at the end of the class if you want since adam a boring nerd hehe"
        hide expression b.image
        $ ni.set_emotion('neutral')
        show expression ni.image at right2 with dissolve
        "Nico" "Hey, [player_name], I heard you're new here and you are already bored haha i like you join us !"
        hide expression ni.image
    else:
        $ b.set_emotion('neutral')
        show expression b.image at right with dissolve
        "Bryan" "Hey, [player_name], how's it going? join us if you find Adam boring hehe"
        hide expression b.image
        $ ni.set_emotion('neutral')
        show expression ni.image at right2 with dissolve
        "Nico" "Hey, [player_name], I heard you  are getting to friendly with the losers be careful!"
        hide expression ni.image





    # New Scene: Classroom

    scene classroom at cover_screen(1100, 1380)
    with dissolve
    show screen notification("Warning: Upcoming choices will affect your skills , popularity and  level.")
    n "You enter the classroom and take a seat. The teacher is setting up the projector, and the students are chatting."
    hide screen notification
    $ rb.set_emotion('neutral')
    show expression rb.image at left2 with dissolve
    "Random Students" "Hey, have you heard that we may get a project exam today?"
    $ rb.set_emotion('neutral2')
    show expression rb.image at right3 with dissolve
    "Random Students" "I hope not, I didn't study at all!"
    hide expression rb.image
    $ rg.set_emotion('neutral')
    show expression rg.image at right2 with dissolve
    "Random student" "I heard that the teacher will announce it soon, so be prepared!"
    hide expression rg.image
    $ ri.set_emotion('neutral2')
    show expression ri.image at right with dissolve
    "Random student" "I heard Bryan is throwing a party tonight, are you guys coming?"
    hide expression ri.image
    $ jocks.set_emotion('neutral')
    show expression jocks.image at right2 with dissolve
    "Jocks" "Yeah, it's going to be epic! You should all come!"
    hide expression jocks.image
    $ t.set_emotion('neutral')
    show expression t.image at right with dissolve
    "Teacher" "Be quiet, class! I need silence to see what's wrong with the projector."
    hide expression t.image

    n "The classroom falls silent as everyone watches the teacher struggle with the projector. You glance around and notice the different reactions from your classmates."

    menu:
        "Listen to the students":
            $ popularity += 5
            $ stress += 1
            $ b.set_emotion('neutral')
            show screen notification("You gained [popularity] popularity and [stress] stress.")
            show expression b.image at right with dissolve
            "Bryan" "[player_name], did you hear about the party tonight? It's going to be epic!"
            hide expression b.image
            $ e.set_emotion('neutral')
            show expression e.image at right2 with dissolve
            "Emily" "I'm more worried about this project exam. I hope it's not too hard."
            hide screen notification
            hide expression e.image

            n "The teacher finally manages to get the projector working and starts the lesson. A slide with complex diagrams appears on the screen."
        "Pay attention to class":
            $ skills += 1
            $ stress -= 1
            $ t.set_emotion('neutral')
            show expression t.image at right with dissolve
            "Teacher" "Alright, class, let's get started. Today's lesson will cover the fundamentals of quantum mechanics. Pay close attention, as this will be important for your project."

    n "The teacher begins to explain the concepts, and you do your best to take notes. You notice that some students are struggling to keep up."


    $ a.set_emotion('happy')
    show expression a.image at right
    "Adam" "Hey [player_name], since there are rumors about some project, do you want to join our study group after class?"

    hide expression a.image
    $ ni.set_emotion('neutral')
    show expression ni.image at right2 with dissolve
    "Nico" "I can't believe we're diving into quantum mechanics already. This is going to be a tough semester."
    hide expression ni.image

    n "The teacher continues the lecture, covering more advanced topics. You do your best to stay focused, but your mind occasionally drifts to thoughts of the party Bryan mentioned and the study group Adam suggested."

    $ t.set_emotion('neutral')
    show expression t.image at right with dissolve
    "Teacher" "Before we wrap up, I want to remind you all that there will be a project exam at the end of the month. Make sure you're studying regularly."

    hide expression t.image
    n "The bell rings, signaling the end of the class. Students start packing up their things, and you feel a mix of relief and anxiety about the upcoming project."

    $ a.set_emotion('happy')
    show expression a.image at right
    "Adam" "So, [player_name], what do you think about joining our study group?"

    menu:
        "Sure, that sounds great!":
            jump choice_interesting2
        "I'm not sure, I need to catch up on the material first.":
            jump choice_unsure
        "No thanks, I prefer to study alone.":
            jump choice_decline







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
        "Adam" "So now you decide to join Emily, [player_name]? I thought you were joining Bryan or studying alone. What do you need help with?"
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
