define n = Character('Narrator',color="#c8c8ff"  )
init python:
    ### trolling screen
    def show_alien_notification():
        renpy.notify("I wish that was true but adding an alien character would be too much work for tamim")
    def cover_screen(img_width, img_height):
        # Get the game's screen dimensions
        screen_width, screen_height = renpy.config.screen_width, renpy.config.screen_height

        # Calculate zoom factor needed for the image to cover the screen
        zoom_factor = max(screen_width / float(img_width), screen_height / float(img_height))

        # Define the transform with the calculated zoom factor
        return Transform(zoom=zoom_factor)

    class DynamicCharacter:
       def __init__(self, name, emotions,male_emotions=None, female_emotions=None, **kwargs):
           self.name = name
           self.emotions = emotions
           self.current_emotion = 'neutral'
           self.male_emotions = male_emotions or emotions
           self.female_emotions = female_emotions or emotions
           self.color = kwargs.get('color', "#ffffff")
           self.position = kwargs.get('position', None)
           self.character = Character(name, color=self.color)
           self.gender = None
           self.update_image()

       #def update_image(self):
           #self.image = self.emotions.get(self.current_emotion, self.emotions['neutral'])
       def update_image(self):
           if self.gender == 'guy':
               self.image = self.male_emotions.get(self.current_emotion, self.male_emotions['neutral'])
           elif self.gender == 'girl':
               self.image = self.female_emotions.get(self.current_emotion, self.female_emotions['neutral'])
           else:
               self.image = self.emotions.get(self.current_emotion, self.emotions['neutral'])

       def set_gender(self, gender):
           self.gender = gender
           self.update_image()

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
    'angry': 'emily_angry',
}, color="#f71e66",)
### the good influence but overprotective and overeactive friend of the player he will be distant if the player is close to the bad influence or the other bad students . Also distant if the player very close to emily and doesnt
define a = DynamicCharacter('Adam', emotions={
    'neutral': 'adam_smiling',
    'happy': 'adam_happy',
    'sad': 'adam_sad',
}, color="#04B486",)

### the player character he will have a skills and popularity and stress variables that will change depending on the choices he makes in the game
define m = DynamicCharacter('Me',
emotions={
    'neutral': 'me_normal',
    'happy': 'me_smiling',
    'sad': 'me_sad',
    'angry': 'me_angry',

},
male_emotions={
    'neutral': 'me_normal',
    'happy': 'me_smiling',
    'sad': 'me_sad',
    'angry': 'me_angry',
    },
female_emotions={
    'neutral': 'me_f_normal',
    'happy': 'me_f_smiling',
    'sad': 'me_f_sad',
    'angry': 'me_f_angry',
    },

color="#c8c8ff", )

### the main teacher character that will give courses and he will keep an eyes on the students and will have small interactions with the player about his study's status
define t = DynamicCharacter('Mr Jackson', emotions={
    'neutral': 'teacher1_normal',
    'sad': 'teacher1_sad',
    'angry': 'teacher1_angry',
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
    'shocked':'random_group_s',## shocked reactions group of rg random students shocked
    }, color="#ffbdbd")

### group of shadow of random students dancing
define rd = DynamicCharacter('Students dancing ' ,emotions={
    'neutral':'random_dancer',
},color="#ffbdbd")
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
default negative_academic_friendship = 0
default jock = 0
default nerd = 0




# choices conséquences
default skills = 0 # skills of the player that will unlock some choices in the game
default popularity = 0 # popularity of the player
default stress = 0 # stress of the player that will affect the choices in the game
# Locked values choices
default adamproposition = False
default emily_hate = False
default bryan_hate = False
default emily_study_group = False
default bryan_study_group = False
default group_alone = False
default choice_talk_to_random_students_used = False
default choice_check_on_bryan_used = False
default choice_quiet_spot_used = False
default choice_stay_with_emily_used = False
default choice_rip_mr_jackson_used = False
default choice_bryan_party = False
default choices_leave_with_emily = False
# Unrelated images (no character tags)
image uni = "uniiii.png"
image parisw = "paris_weird.png"
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
image teacher_office_door = "teacher_office_door.png" # Teacher's office door
image beach_evening = "beach_evening.png" # Beach
image uni_classroom2 = "uni_classroom2.png" # Classroom 2
image uni_mainhall2 = "uni_mainhall2.png" # University main hall 2
image airport_inside = "airport_inside.png" # Airport inside
image airport_field = "airport_field.png" # Airport field
image dance_with_emily = "dance_with_emily.png" # Dance with Emily
image player_house_room_day = "player_house_room_day.png" # Player's house room during the day
image player_house_room_night = "player_house_room_night.png" # Player's house room during the night
image uni_library2_night = "uni_library2_night.png" # University library 2 during the night
image uni_library_outside = "uni_library_outside.png" # University library outside
image building_rooftop = "building_rooftop.png" # Building rooftop
image uni_mainhall3 = "uni_mainhall3.png" # University main hall 3
image nightclub2 = "nightclub2.png" # Nightclub 2
image cozy_restaurant = "cozy_restaurant.png" # Cozy restaurant
image attraction_park_fullofpeoples = "attraction_park_fullofpeoples.png" # Attraction park full of people
#Notifications screen
screen notification(msg):
    frame:
        xalign 0.5
        yalign 0.1
        background Frame("gui/main_menu.png",)
        text msg style "notification_text"

style notification_text is default:
    size 22
    color "#ffffff"

transform right:
    xalign 1.2 yalign 0.9

transform middle:
    xalign 0.1 yalign 0.9

transform right2:
    xalign 1.4 yalign 0.6
transform left3 :
    xalign 1 yalign 0.6
transform right3:
    xalign 1.4 yalign 2.8

transform rightp:
    xalign 1.2 yalign 0.4

transform left2:
    xalign -0.3 yalign 2.8

# Define images for the stats
image skill_icon = "skill_icon.png"
image stress_icon = "stress_icon.png"
image popularity_icon = "popularity_icon.png"




#Gender screen for the player
screen gender_selection():

    vbox :
        xalign 0.5
        yalign 0.5
        spacing 20
        text "You are"  style "window"
        textbutton "A Guy" action [SetVariable("player_gender", "guy"), Return()] style "choice_button"
        textbutton "A Girl" action [SetVariable("player_gender", "girl"), Return()] style "choice_button"
        textbutton "Alien" action [Function(show_alien_notification),] style "choice_button"

label start:
    $ player_gender = None
    scene airport_field at cover_screen(1100, 1380) with dissolve
    n "This is a game made by the group InteractiveNovel in Estiam."
    n "For this project we were suppose to make a game that will be interactive and will have multiple choices that will affect the outcome of the game."
    n "Members of the group are Tamim,  Ilyas (also Maxime but left us on April 2024)."
    scene airport_inside at cover_screen(1100, 1380) with dissolve
    n "You are a student that is moving to New Paris to join a  university to finish your year because your old college closed down after the pandemic."
    n "All your choices will affect the outcome of the game.There are 4 endings and 3 paths you can take."
    n "Your relationship with other students will affect the ending but some choices  will be unlocked depending on your skills , stress , popularity and friendship with the other students. Choose wisely."
    scene paris_weird at cover_screen(800, 800) with dissolve
    n "It's a new bachelor year for you , you are a student in the university (InteractiveNovel), you are discovering New Paris while going to the university. "
label character_creation:
    n "First of all let's create your character."
    n "What is  your character name ?"
    show screen notification("Your name will be used throughout the game")
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip() if player_name else "Me"
    $ m.character = Character(player_name, color=m.color, image=m.image)
    n "Okay ! Your name is [player_name] , now what gender you want your character to be ?"
    show screen notification ("This choice will affect images and dialogues of your character throughout the game")
    call screen gender_selection
    $ m.set_gender(player_gender)
    hide screen notification
    n "Let me confirm this , your name is [player_name] and you are a [player_gender] yes ? "
    menu:
        "Yes":
          "Nice [player_name] let's start the game !"
        "No":
            "Let's restart but i hope you are not trying to choose the alien option"
            jump character_creation
    scene uni_park_day at cover_screen(1100, 1380) with dissolve
    n "You arrive at the university and see the park. Students are sitting on benches, chatting, one student is approaching you."
    show screen notification("All the people you will meet will have different reactions to your choices and will affect the outcome of the game so yeah look out!")
    $ a.set_emotion('happy')
    show expression a.image at right with dissolve
    "Adam" "Hi there! You are a new student from the college that closed down after the pandemic right?"
    hide a
    hide screen notification

    $ m.set_emotion('neutral')
    show expression m.image at middle with dissolve
    "Me" "Yes..."
    $ m.set_emotion('sad')
    show expression m.image at middle with dissolve
    "Me" "I am new here so i will have to get used to this place"
    hide a

    $ a.set_emotion('neutral')
    show expression a.image at right with dissolve
    "Adam" "How was your old college and it's courses?"
    hide a
    hide expression m.image

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
    $ bryan_friendship += 5
    $ stress += 5
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
    hide expression b.image


    $ a.set_emotion('happy')
    show expression a.image at right with dissolve
    a "Don't worry, you'll get the hang of it. I have to go now, but I'll see you around!"
    hide expression a.image

    n "You are looking around the park to find the university building.But you notice someone is approaching you."
    hide a
    $ e.set_emotion('happy')
    show expression e.image at right with dissolve

    e "Hey i'm pretty sure that you are a new [player_gender] here ! My name is Emily ,what's your name?"



    $ m.set_emotion('happy')
    show expression m.image at middle with dissolve
    menu :
     "I'm [player_name], nice to meet you!":
        $ emily_friendship += 5
        jump emily_conv1
     "Please leave me alone i don't care who you are i want to get to class":
        show screen notification("What a start ! You're so focused on your studies that you don't want to make friends . You gained nerd points!")
        $ emily_friendship -= 5
        $ nerd += 5
        $ stress += 5
        $ m.set_emotion('sad')
        m "Please leave me alone i don't care who you are I want to get to class"
        hide screen notification
        $ e.set_emotion('neutral')
        show expression e.image at right with dissolve
        e "Uh oh sure okay bye then"
        $ p.set_emotion('neutral')
        hide expression e.image
        show expression p.image at rightp with dissolve
        p "Hello there i don't think i've seen you around here before are you new here?"
        $ m.set_emotion('neutral')
        show expression m.image at middle with dissolve
        menu:
         "Yes sir ! I'm new here.":
             $ principal_friendship += 5
             $ m.set_emotion('happy')
             show expression m.image at middle with dissolve
             m "Yes, I'm new here."
             $ p.set_emotion('happy')
             show expression p.image at rightp with dissolve
             p "Well, welcome to InteractiveNovel! I hope you enjoy your time here."
             hide expression p.image
             jump hallway
         "(Lie) No, I've been here for a while." :
             $ principal_friendship -= 5
             $ negative_academic_friendship += 1
             $ m.set_emotion('sad')
             show expression m.image at middle with dissolve
             m "No, I've been here for a while."
             $ p.set_emotion('neutral')
             show expression p.image at rightp with dissolve
             p "Oh, sorry for not recognizing you. I hope you're enjoying your time here."
             hide expression p.image
             jump hallway
         "Sorry sir im so much in a hurry i have to go to class to study" if nerd >= 1:
             $ principal_friendship += 5


             $ negative_academic_friendship += 5
             $ m.set_emotion('angry')
             show expression m.image at middle with dissolve
             m "Sorry sir im so much in a hurry i have to go to class to study"
             $ p.set_emotion('neutral')
             show expression p.image at rightp with dissolve
             p "Don't  worry im happy to see that you are so focused on your studies"
             jump hallway

         "I don't have to answer to you" if jock >= 1:
             $ principal_friendship -= 5
             $ negative_academic_friendship += 5
             $ jock += 5
             $ negative_academic_friendship += 5
             $ m.set_emotion('angry')
             show expression m.image at middle with dissolve
             m "I don't have to answer to you"
             $ p.set_emotion('angry')
             show expression p.image at rightp with dissolve
             p "You should be more respectful to your principal !"
             jump hallway


     "Get lost i talk only to people that are worth my time":
        show screen notification("You are triggering the jock path ! You gained jock points!")
        $ emily_friendship -= 5
        $ jock += 5
        $ stress += 5
        $ emily_hate = True
        $ m.set_emotion('sad')
        m "Get lost i talk only to people that are worth my time"
        hide screen notification
        $ e.set_emotion('neutral')
        show expression e.image at right with dissolve
        e "Oh... cool then "
        n "You are on your way to the main building but you notice the principal is coming your way."
        $ p.set_emotion('neutral')
        hide expression e.image
        show expression p.image at rightp with dissolve
        p "Hello there i don't think i've seen you around here before are you new here?"
        $ m.set_emotion('neutral')
        show expression m.image at middle with dissolve
        menu:
         "Yes, I'm new here.":
             $ principal_friendship += 5
             $ m.set_emotion('happy')
             show expression m.image at middle with dissolve
             m "Yes, I'm new here."
             $ p.set_emotion('neutral')
             show expression p.image at rightp with dissolve
             p "Well, welcome to InteractiveNovel! I hope you enjoy your time here."
             hide expression p.image
             jump hallway
         "(Lie) No, I've been here for a while.":
             $ principal_friendship -= 5
             $ negative_academic_friendship += 1
             $ m.set_emotion('neutral')
             show expression m.image at middle with dissolve
             m "No, I've been here for a while."
             $ p.set_emotion('neutral')
             show expression p.image at rightp with dissolve
             p "Oh, sorry for not recognizing you. I hope you're enjoying your time here."
             hide expression p.image
             jump hallway
         "I don't have to answer to you" if jock >= 1:
             $ principal_friendship -= 5
             $ negative_academic_friendship += 5
             $ jock += 5
             $ negative_academic_friendship += 5
             $ m.set_emotion('angry')
             show expression m.image at middle with dissolve
             m "I don't have to answer to you"
             $ p.set_emotion('angry')
             show expression p.image at rightp with dissolve
             p "You should be more respectful to your principal !"
             jump hallway
         "I am sorry sir but i really have to go to class" if nerd >= 1:
             $ principal_friendship += 5
             $ negative_academic_friendship += 5
             $ m.set_emotion('neutral')
             show expression m.image at middle with dissolve
             m "I am sorry sir but i really have to go to class"
             $ p.set_emotion('neutral')
             show expression p.image at rightp with dissolve
             p "Don't worry i understand you have to go to class"
             jump hallway



label emily_conv1 :
    $ emily_friendship += 5
    m "I'm [player_name], nice to meet you!"
    $ e.set_emotion('happy')
    show expression e.image at right with dissolve
    e "Well, [player_name],nice to meet you ! welcome to InteractiveNovel ! I hope you enjoy your time here."
    menu:
     "I'm a bit nervous about being the new kid.":
       $ m.set_emotion('sad')
       show expression m.image at middle   with dissolve
       m "I'm a bit nervous about being the new kid."
       $ e.set_emotion('neutral')
       show expression e.image at right  with dissolve
       e "It's totally normal to feel that way. Just be yourself and you'll find your place."
     "I'm excited to meet new people!":
       $ m.set_emotion('happy')
       show expression m.image at middle with dissolve
       m "I'm excited to meet new people!"
       $ e.set_emotion('happy')
       show expression e.image at right with dissolve
       e "That's the spirit! There are lots of great people here."
       hide expression m.image
       hide expression e.image


    hide expression e.image
    $ p.set_emotion('neutral')
    show expression p.image at rightp with dissolve
    p "Hello , i don't think i've seen you around here before are you new here?"
    $ m.set_emotion('neutral')
    show expression m.image at middle with dissolve
    menu:
        "Yes, I'm new here.":
            $ principal_friendship += 5
            $ m.set_emotion('happy')
            show expression m.image at middle with dissolve
            m "Yes, I'm new here."
            $ p.set_emotion('neutral')
            show expression p.image at rightp with dissolve
            p "Well, welcome to InteractiveNovel! I hope you enjoy your time here."
            hide expression p.image
        "(Lie)No, I've been here for a while.":
            $ principal_friendship -= 5
            $ m.set_emotion('neutral')
            show expression m.image at middle with dissolve
            m "No, I've been here for a while."
            $ p.set_emotion('neutral')
            show expression p.image at rightp with dissolve
            p "Oh, sorry for not recognizing you. I hope you're enjoying your time here."
            hide expression p.image
        "I don't have to answer to you" if jock >= 1:
            $ principal_friendship -= 5
            $ jock += 5
            $ negative_academic_friendship += 5
            $ m.set_emotion('angry')
            show expression m.image at middle with dissolve
            m "I don't have to answer to you"
            $ p.set_emotion('angry')
            show expression p.image at rightp with dissolve
            p "You should be more respectful to your principal !"
        "I am sorry sir but i really have to go to class" if nerd >= 1:
            $ principal_friendship += 5
            $ m.set_emotion('neutral')
            show expression m.image at middle with dissolve
            m "I am sorry sir but i really have to go to class"
            $ p.set_emotion('neutral')
            show expression p.image at rightp with dissolve
            p "Don't worry i understand you have to go to class"

    n "You have met Adam and Emily, two students at InteractiveNovel. Your interactions with them will affect your relationships and the story's outcome."
   ### hallway scene
label hallway:
    scene uni_hallway1 at cover_screen(1100, 1380)
    n "As you walk through the hallway, you see Bryan, another student at InteractiveNovel."

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
    n "You see some student groups chatting and laughing."
    $rb.set_emotion('neutral')
    show expression rb.image at left2 with dissolve
    rb "This year exam better be easy as last year's one"
    $ ri.set_emotion('neutral2')
    show expression ri.image at right with dissolve
    ri"Wanna sneak up and listen to teacher conversation?"
    hide expression rb.image
    hide expression ri.image
    $ m.set_emotion('neutral')
    show expression m.image at middle with dissolve
    m"should i risk and follow them to listen to the teachers conversation or should i just go to the class?"
    show screen notification("Upcoming choices will affect your skills , popularity,stress and  friendship .")
    hide expression m.image
    menu:
        "Follow them and spy on the teachers":

            jump follow_them
        "Go to class":
            jump go_to_class


label follow_them:
    hide screen notification
    scene teacher_office_door at cover_screen(1100, 1380) with dissolve
    $ popularity += 5
    $ skills += 3
    $ stress += 5

    $ bryan_friendship += 2
    $ nico_friendship += 2
    $ t.set_emotion('neutral')
    show expression t.image at right with dissolve
    t"I think i will mainly focus the long end of the year project exam on quantum computing this year"
    $ t2.set_emotion('neutral')
    show expression t2.image at left with dissolve
    t2 "No i believe only putting 1 subject in the exam is not fair for the students i think the other subjects should IT in general like last year "
    t "No the principal said we should harden the exams to compete against other universities if we put the other subject then we should grade the IT subject way harder to make the student choose quantum computing "
    $ t2.set_emotion('sad')
    show expression t2.image at left with dissolve
    t2 "I know the principal is focusing on the college reputation but i think the students should have a fair chance to pass the exam they already had a hard time with the pandemic the past few years"
    hide expression t2.image
    hide expression t.image
    $ rb.set_emotion('neutral')
    show expression rb.image at left2 with dissolve
    rb "Ouch this doesn't sound let's get out of here and tell everyone about this"
    $ ri.set_emotion('neutral2')
    show expression ri.image at right with dissolve
    ri "Yeah before we get caught let's go guys !"
    hide expression rb.image
    hide expression ri.image
    menu:
        "Leave aswell ":
            jump go_to_class
        "Stay and listen more (WARNING if your stress is high this will have a very bad impact on your paths)":
                $ popularity += 5
                $ skills += 3
                $ stress += 5

                $ bryan_friendship += 3
                $ nico_friendship += 3



    n "You stay and listen more to the teachers conversation "
    $ t.set_emotion('sad')
    show expression t.image at right2 with dissolve
    t "If i don't harden the exam then the principal will put someone else in my place and i can't afford to lose my job while it's already impossible to find a job in this post pandemic economy"
    $ t2.set_emotion('sad')
    show expression t2.image at left with dissolve
    t2"I understand but the students are already struggling with the post pandemic effect , we could negotiate with the principal to make the exam fair for the students"
    t"Listen the principal is already mad at me for a lots of  students not being professional or having  bad grades so i don't think they even deserve a fair exam we getting some new students from another university that closed down because of the pandemic so we need to show them that we are a serious university in exams"
    hide expression t2.image
    hide expression t.image
    if stress >= 15:
        n "Oh man you're losing your cool  because of your stress level so you pop out of nowhere and start arguing'."
        $ popularity = 10
        $ skills -= 10
        $ stress += 20
        $ negative_academic_friendship += 5

        $ bryan_friendship += 1
        $ nico_friendship += 1
        $ m.set_emotion('sad')
        show expression m.image at middle with dissolve
        m "This is not right sir , you should be fair to the students! Just because it's your job doesn't mean you should make the students suffer!"
        $ t.set_emotion('sad')
        show expression t.image at right2 with dissolve
        t "Ok that's none of your business also what is a new student doing sneaking up on the teachers conversation? i will report you to the principal for this!"
        hide expression t.image
        show expression t2.image at right with dissolve
        t2 "That's was a bad move young man please leave before it gets worse we can let it slide this time"


        menu :
            "Leave":
                jump go_to_class
            "Argue with the teacher":
                hide expression t2.image
                $ popularity += 20
                $ skills -= 10
                $ stress += 20
                $ negative_academic_friendship += 5
                $ principal_friendship -= 5

                $ bryan_friendship += 1
                $ nico_friendship += 1
                $ m.set_emotion('sad')
                show expression m.image at middle with dissolve
                m "No you're wrong sir! i don't care if you report me i didn't come to this university to study something that wasn't in the program last year why do i got it harder than the students of last year?"
                $ t.set_emotion('angry')
                show expression t.image at right2 with dissolve
                t "Okay i'm gonna report you to the principal what is your name?"
                hide expression t.image with dissolve
                menu :
                    "Leave":
                        show screen notification("On the jock path ")
                        $ popularity += 10
                        $ jock = 10
                        m "I don't have to give my name to YOU"
                        hide screen notification
                        jump go_to_class
                    "Give your name":
                        $ popularity += 10
                        $ skills += 2
                        $ stress -=5
                        m "My name is [player_name] and i'm new here but i am very  disappointed in this college."
                        show expression t2.image at right with dissolve
                        t2 "Please... "

                        jump go_to_class
    n "yikesss the teacher is coming out of the door it's to late for you to do anything now"
    show expression m.image at middle with dissolve
    m "I'm sorry i was listening but i was just curious and passing by"
    $ t.set_emotion('neutral')
    show expression t.image at right with dissolve
    $ teacher_friendship += 5
    t "It's alright i appreciate your honesty but this is not a good thing to do especially if it was the principal"
    if popularity >= 10:
       t "[player_name] right ? i've been hearing a lots about you in the campus your reputation is already starting to grow"
    t "You should be going to class now i will be coming to the class in a few minutes"






    # New Scene: Classroom
label go_to_class:
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
    n"The teacher entering the classroom and the students start to get quiet."
    if negative_academic_friendship >= 5:
        n"The teacher glaring at you and the students notice it and start to whisper."

        $ popularity += 10
        $ skills -= 5
        $ stress += 5
        $ emily_friendship -= 3
        $ jocks.set_emotion('neutral')
        show expression jocks.image at right2 with dissolve
        jocks "ooooooooooooo [player_name] got in trouble with the teacher"
        hide expression jocks.image
        if adam_friendship >= 7:
            $ adam_friendship -= 10
            $ b.set_emotion('neutral')
            show expression b.image at right with dissolve
            b " I thought you were a nerd like adam but i was wrong hehe "
            hide expression b.image
            $ a.set_emotion('sad')
            show expression a.image at right with dissolve
            a "What did you do [player_name] to the teacher  ? i thought you were better than this "
            hide expression a.image
            $ ni.set_emotion('neutral')
            show expression ni.image at right2 with dissolve
            ni "Adam discovered that not everyone a hypocrite gold student like him haha"
            $ m.set_emotion('sad')
            show expression m.image at middle with dissolve
            menu:
                "I regret it i am sorry Adam":
                   $ adam_friendship += 10
                   $ bryan_friendship -= 5
                   $ nico_friendship -= 5
                   $ popularity -= 5
                   $ b.set_emotion('neutral')
                   show expression b.image at right with dissolve
                   b "You don't have to be sorry [player_name] this is how we deal with the 'teachers' here hehe"
                   hide expression b.image
                   $ a.set_emotion('happy')
                   show expression a.image at right with dissolve
                   a "I'm glad you're sorry [player_name] i hope you learned your lesson"
                   hide expression a.image
                   $ ni.set_emotion('neutral')
                   show expression ni.image at right2 with dissolve
                   ni "blablabla gold student acting like everyone owe him something"

                "I was just defending the students well being":
                  $ popularity += 10
                  $ skills += 4
                  $ popularity += 10
                  $ b.set_emotion('neutral')
                  show expression b.image at right with dissolve
                  b "You're right [player_name] we should all stand up for ourselves right adam ? hehe "
                  hide expression b.image
                  $ a.set_emotion('sad')
                  show expression a.image at right with dissolve
                  a "Im glad you are defending the students but when the teacher give us a hard time we should just stay silent"
                  hide expression a.image
                  $ ni.set_emotion('angry')
                  show expression ni.image at right2 with dissolve
                  ni "wE ShoulD StaY SiLenT aNd Do NoThiNg *sheep noises*"
                  hide expression ni.image
                  hide expression m.image




                "I don't care this year is a mess already":
                 $ popularity += 20
                 $ jock += 10
                 $ adam_friendship -= 5
                 $ bryan_friendship += 10
                 $ nico_friendship += 5
                 $ m.set_emotion('happy')
                 m"I don't care this year is a mess already and i don't really care about what you think adam we just met"
                 show expression a.image at right with dissolve
                 a "I was wrong about meeting you [player_name] you are just like the others"
                 hide expression a.image
                 show expression b.image at right with dissolve
                 b " Nico [player_name] was never gonna be adam bff you lost the bet hehe "



        $ b.set_emotion('neutral')
        show expression b.image at right with dissolve
        b "[player_name] is just like us hehe , Day 1 and already in trouble"
        hide expression b.image


        if emily_hate == False:
         $ e.set_emotion('sad')
         show expression e.image at right with dissolve
         e "Is everything okay [player_name] ? what happened ? You can tell me later "
         hide expression e.image
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
    show expression t.image at right2 with dissolve
    t "i said  SILENCE ! Ms brett you are late again so do not have the odacity to speak out loud!I'm going to report you to the principal if you keep this up!now go sit down and be quiet"
    hide expression t.image

    $ br.set_emotion('sad')
    show expression br.image at right2 with dissolve
    br """jeeez I'm sorry Mr Jackson,**quietly mumbling** chill out man."""
    hide expression br.image
    $ a.set_emotion('happy')
    show expression a.image at right
    a "Maybe stopping  partying and start studying would be a good idea."
    hide expression a.image
    $ e.set_emotion('neutral')
    show expression e.image at right2 with dissolve
    e "Did you really had to say that Adam? What are you trying to prove ?"
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
            br "thank you new [player_gender] for backing me up i appreciate it your name is [player_name] right?"
            hide expression br.image
            hide screen notification
            $ b.set_emotion('neutral')
            show expression b.image at right with dissolve
            if bryan_friendship >= 10:
             b "Hehe right ! [player_name] is a good cool guy you heard that Adam ? nobody like you in this class"
             hide expression b.image
             $ ni.set_emotion('neutral')
             show expression ni.image at right2 with dissolve
             ni "Maybe it's time to stop being a nerd and start having fun like [player_name] and brett"
            else:
                b "Hehe right ! [player_name] is a strange [player_gender] but he can be nice too"
                hide expression b.image
                $ ni.set_emotion('neutral')
                show expression ni.image at right2 with dissolve
                ni "Maybe it's time to stop acting like mr always right and start having fun like [player_name] and brett"

            hide expression ni.image
            hide expression m.image
            $ t.set_emotion('neutral')
            show expression t.image at right with dissolve
            if jock < 0 :
              t "I didn't expected you to talk [player_name] i am really disappointed that you are not silent "
            if jock >= 5 :
                t "You and me will have a real talk after so please for once shut it and focus on the lesson"
                if bryan_friendship >= 10:
                 show expression br.image at left with dissolve
                 br "Wooo scary Mr jackson but you won't do anything to [player_name] "
                 hide expression br.image
                 show expression b.image at left with dissolve
                 b "Yeah you heard that Mr jackson [player_name] is a cool [player_gender]"
                 hide expression b.image
                 t "Whatever you two say, i already reported you to the principal for being late and talking in class"
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
            $ nerd += 10
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
            if adam_friendship >= 15 and bryan_friendship < 5 and nerd >= 10:
                show screen notification("Nerd paths")
                $ b.set_emotion('neutral')
                show expression b.image at right with dissolve
                b "Well, [player_name] so you are a nerd like Adam after all"
                hide screen notification
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
       "Ask your neighbor what they know " if emily_hate == False:
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

        if emily_hate == False:
         $ e.set_emotion('neutral')
         show expression e.image at right with dissolve
         e "Pull yourself together [player_name]!!. This is important for the project exam!"
        else:
            $ e.set_emotion('neutral')
            show expression e.image at right with dissolve
            e " Pfff typical bad [player_gender] behavior"
            hide expression e.image
            menu :
             "I'm sorry Emily about earlier i didn't mean to be rude if that's the reason you're mad at me ":
               $ emily_hate = False
               $ e.set_emotion('happy')
               e "It's alright maybe i had you wrong [player_name] i'm sorry too"
               hide expression e.image
             "Don't say anything":
              n "You decide to stay silent strange you trying to figure out if you should apologize or not?"
             "Please shut the hell up  Emily":
                $ popularity += 10
                $ skills -= 3
                $ stress += 5
                $ e.set_emotion('angry')
                show expression e.image at right with dissolve
                e "Whatever clown"
             "You're just jealous girl that you are not the center of attention " if player_gender == "girl" :
                $ popularity += 10
                $ skills -= 3
                $ stress += 5
                $ e.set_emotion('angry')
                show expression e.image at right with dissolve
                e "Ah you wish [player_gender] ! i don't to become a Mcdonald cashier like you"



        hide expression e.image
        hide expression m.image
        if negative_academic_friendship >= 2:
            $ negative_academic_friendship += 5
            $ jock += 5
            $ t.set_emotion('angry')
            show expression t.image at right2 with dissolve
            t "New student ? I wonder if the reason your old college closed down is because of students like you who don't care about their studies"
        hide screen notification

    if stress >= 20 and popularity >= 20:
        hide expression t.image
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
      "Try to explain it to Bryan" if bryan_friendship >= 5 and jock < 5:
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

      "Admit you're struggling too" if jock < 5:
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
      "I dont understand a single stuff bro" if jock >= 5 and bryan_friendship >= 10 :
        n "ohhh yes the jock path choices looking nice right ? "
        $ skills += 0
        $ popularity += 5
        $ stress += 20
        $ bryan_friendship += 3
        $ teacher_friendship += 1
        $ emily_friendship += 3
        n "You admit to Bryan that you're completely lost, and he nods in understanding. You both share a look of confusion and try to follow along as best you can."
        $ m.set_emotion('sad')
        show expression m.image at middle with dissolve
        m "I'm lost too,i dont understand a single stuff at the moment but the teacher made this harder on purpose"
        $ b.set_emotion('neutral')
        show expression b.image at right with dissolve
        b "I'm glad i'm not the only one lost here, this is really tough "
        hide expression b.image
        hide expression m.image

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
    if jock >= 5 and popularity >= 20 and skills <= 6:
        $ t.set_emotion('sad')
        show expression t.image at right with dissolve
        t" [player_name] i'm giving you a choice  to either give me an apologies or i will report you to the principal for this unnecessary provocations"
        menu :
            "Apologize":
                $ t.set_emotion('neutral')
                $ teacher_friendship += 5
                $ negative_academic_friendship -= 5
                $ jock -= 5
                show expression t.image at right with dissolve
                t "I appreciate your apology [player_name] but you need to focus on your studies and not on provoking other students"
                hide expression t.image

            "Refuse":
                $ teacher_friendship = 0
                $ negative_academic_friendship += 10
                $ jock += 5
                $ principal_friendship -= 5
                $ popularity -= 10
                $ t.set_emotion('sad')
                show expression t.image at right with dissolve
                t "I will report you to the principal [player_name] for your provocations"
                hide expression t.image
                if bryan_friendship >= 20:
                    $ b.set_emotion('neutral')
                    show expression b.image at right with dissolve

                    b "hehe , sir [player_name] doesn't care about any consequences"
                    hide expression b.image
                    $ jocks.set_emotion('neutral')
                    show expression jocks.image at right2 with dissolve
                    jocks "New [player_gender] is so cool"
                    hide expression jocks.image


                hide expression t.image
    hide expression t.image
    n"The bell rings, signaling the end of the class. Students start packing up their things, and you feel a mix of excitement and anxiety about the upcoming project and the vast new field you're just beginning to explore."








if adam_friendship >= 15 or skills >= 10:
        $ a.set_emotion('happy')
        show expression a.image at right
        a "So, [player_name], what do you think about joining my study group?"
        hide expression a.image
        menu:
           "Sure, that sounds great!":
             $ a.set_emotion('happy')
             show expression a.image at right with dissolve
             a "Awesome! We'll meet at the library after school. I'm sure we can help each other out."
             $ adamproposition = True
             jump group_study
           "Sure but i will join you later":
             $ a.set_emotion('neutral')
             show expression a.image at right with dissolve
             a "No problem, just let me know when you're ready to join us."
             jump choice_unsure
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
    if  bryan_friendship >= 15 and adamproposition == False:

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
    if adamproposition == True:
        $ b.set_emotion('neutral')
        show expression b.image at right with dissolve
        b "Oh look at the new [player_gender] not sure if adam is the right choice hehe "
        hide expression b.image

    if jock < 5  and emily_hate == False:
      $ e.set_emotion('neutral')
      show expression e.image at right with dissolve
      e "Hey [player_name], i was wondering if you want to join my project group , i know adam is a work machine and can get irritating  but i think we can make a great study group you and me , if adam get in the way we can just be a duo study group"
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
    if jock >= 5 and emily_hate == False:
        $ e.set_emotion('neutral')
        show expression e.image at right with dissolve
        e "Hey [player_name], are you alright? why you've been acting strange lately"
        hide expression e.image
        menu :
          "Yes i'm fine , i love this college and the people here":
           $ e.set_emotion('sad')
           show expression e.image at right with dissolve
           e"You are lying aren't you ? I didn't thought you were this kind of guy"
           $ emily_hate = True
           jump choice_unsure2

           hide expression e.image
          "I don't know i feel like i'm becoming a different person and i don't like it ":
           $ e.set_emotion('sad')
           show expression e.image at right with dissolve
           e "You can talk to me you know that ?"
           e" I actually wanted to ask you if you wanted to join my study group but your change in attitude is making me think twice..."
           jump choice_unsure2



label choice_unsure2:
    hide expression e.image
    $ m.set_emotion('neutral')
    show expression m.image at middle with dissolve
    show screen notification("This is your last chance to join a study group, choose wisely.it will affect your skills and friendship most importantly the ending")
    m "i have to join a study group but i don't know who to join who should i join ?"
    menu:
        "Join Bryan's study group" if bryan_friendship >= 15 and adamproposition == False:
            $ bryan_study_group = True
            jump bryan_study_group
        "Join Emily's study group" if emily_friendship >= 15 or emily_hate == False:
            $ emily_study_group = True
            jump emily_study_group
        "Join Adam's study group" if adam_friendship >= 15:
            jump adam_study_group
        "Go to the party (On Adam path)" if adamproposition == True:
            $ choice_bryan_party = True
            jump party_scene
        "Who cares about studying, let's go to the party" if jock >= 5:
            jump party_scene




### bryan group choices scenes
label bryan_study_group:
 hide screen notification
 scene uni_sunset at cover_screen(1100, 1380)
 n "You decide to join Bryan's study group. You meet up with Bryan and Nico at the library after school."
 $ m.set_emotion('neutral')
 show expression m.image at middle with dissolve
 m "Hey guys i made up my mind i will join your study group"
 $ b.set_emotion('neutral')
 show expression b.image at right with dissolve
 if jock < 5 :
  $ bryan_study_group = True
  b "I was hoping you would join us [player_name]! We can help each other out and make studying more fun."
  hide expression b.image
  $ ni.set_emotion('neutral')
  show expression ni.image at right2 with dissolve
  ni "Maybe you can help us get better grades [player_name] "
  hide expression ni.image
 if jock >= 5:
  $ bryan_study_group = True
  b "Hehe this year project is going to be a breeze with you in our group [player_name]!"
  hide expression b.image
  $ ni.set_emotion('neutral')
  show expression ni.image at right2 with dissolve
  ni "Yeah never mind the project it won't have to be perfect we can clutch it "
  hide expression ni.image
$ b.set_emotion('neutral')
show expression b.image at right with dissolve
b "Let's go the party hehe we can study later"
jump party_scene


### emily group choices
label emily_study_group:
    hide screen notification
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
    if bryan_study_group == True:
         show screen notification("You are actually on group Bryan paths ")
         n "You , Bryan and Nico arrive at the party, and the music is already blasting. The house is packed with students dancing, chatting, and having a great time."
         hide screen notification
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
        "Find Emily" if emily_friendship >= 15:
            jump find_emily
        "Join the Jocks" if nerd < 4:
            jump join_the_jocks




label talk_to_bryan:
    scene bryan_dance_room at cover_screen(1100, 1380) with dissolve
    if bryan_friendship <= 15:
           n " Your relationship with Bryan is bad why the hell you wanna talk to him lol"
           $ b.set_emotion('angry')
           show expression b.image at right with dissolve
           b "Hey i don't think i invited this loser to my party , if you regret being Adam bestie  wont give  a damn about your apologies"
           $ ni.set_emotion('angry')
           show expression ni.image at left with dissolve
           ni "Yeah, [player_name], you're not welcome here. Go hang out with the nerd.Leave the party unless you want to be trouble with us"
           hide expression ni.image
           if brett_friendship >= 10:
              $ br.set_emotion('angry')
              show expression br.image at right2 with dissolve
              br "Hey, back off! [player_name] can be whoever they want. He was cool earlier so leave him alone"
              hide expression br.image
              ni "Okay okay chill out [player_name] you can stay but don't cause any trouble else you will really regret it"
    else:
        n " You walk over to Bryan, who is surrounded by students dancing and chatting."
    $ b.set_emotion('neutral')
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
    scene bryan_chill_room at cover_screen(1100, 1380) with dissolve
    $ e.set_emotion('neutral')
    show expression e.image at right with dissolve
    e "Hey, [player_name]. Everything okay?"
    menu:
        "Yeah, just checking in.":
            $ emily_friendship += 5
            m "Yeah, just checking in."
            e "Thanks, [player_name]. Try to enjoy the party a bit."
            jump party_continue
        "I'm worried about the exam..." if emily_study_group == True:
            $ emily_friendship += 10
            $ stress += 5
            m "I'm worried about the exam, Emily."
            e "I understand. We'll get through it. I will leave the party early to study if you want to join me"
            m "At the library right?"
            e "Not without you , i rather study at the the coffee shop near the library if im alone"
            m "Oh okay then enjoy the party"

            jump party_continue
        "Have you seen Adam?":
            $ emily_friendship += 5
            m "Have you seen Adam?"
            e "Hmm i don't think adam is the party type, he's probably studying"
            if adamproposition == True:
                e "He consider me to be in his group but i have not checked on him yet however you are his friend you should be aware of his whereabouts"
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





label party_continue:
    scene bryan_dance_room at cover_screen(1100, 1380) with dissolve
    n "The party continues, and you find yourself getting more involved. What do you want to do next?"
    menu:
        "Stay with emily" if emily_friendship >= 60 and  not choice_stay_with_emily_used:
            $ choice_stay_with_emily_used = True
            jump stay_with_emily
        "Talk to random students" if not choice_talk_to_random_students_used:
            $ choice_talk_to_random_students_used = True
            jump talk_to_random_students
        "Check on Bryan" if bryan_friendship >= 25 and not choice_check_on_bryan_used:
            $ choice_check_on_bryan_used = True
            jump check_on_bryan

        "Throw coffee at Mr Jackson" if jock >= 5 and teacher_friendship <= 5:
            $ m.set_emotion('happy')
            show expression m.image at middle with dissolve
            m "Take this Mr Jackson !"
            jump rip_mr_jackson
        "Leave the party" if choice_stay_with_emily_used == True and choice_talk_to_random_students_used == True and choice_check_on_bryan_used == True and choice_find_quiet_spot_used == True:
            jump leave_party
        "Gather proof of bad behavior and objects for the principal " if adamproposition == True :
            $ bryan_proofs = True
            scene bryan_house at cover_screen(1100, 1380) with dissolve
            $ m.set_emotion('happy')
            show expression m.image at middle with dissolve
            n "You start to search bryan house to find anything to use against him and his friends"
            m "Hmmm that's a lots of things adam will love it i will just have to leave the party now and show everything"
            jump after_study_group_choice
        "Ask bryan to leave the party to do the project" if bryan_study_group == True and jock < 5:
                scene bryan_chill_room at cover_screen(1100, 1380) with dissolve
                $ m.set_emotion('neutral')
                show expression m.image at middle with dissolve
                m "Hey bryan i know the party is fun but we should leave now to study for the project we have to finish it before monday"
                $ b.set_emotion('neutral')
                show expression b.image at right with dissolve
                b "Let's try to stay a bit longer [player_name] we can always study later hehe"
                hide expression b.image
                $ br.set_emotion('neutral')
                show expression br.image at right2 with dissolve
                "Come on bryan , we have to finish the project before monday we can't afford to fail this project especially with [player_name] in our group he's a good team player"
                hide expression br.image
                $ ni.set_emotion('neutral')
                show expression ni.image at right2 with dissolve
                ni "Never thought i would say this but i agree with brett we  work on our project now ,[player_name] will give us a chance we can't afford to miss"
                hide expression ni.image
                $ b.set_emotion('neutral')
                show expression b.image at right with dissolve
                b "Alright [player_name] i owe you one for helping me earlier in class let me announce that i am leaving the party"
                b "**megaphone** GUYS  i have to leave the party to work on the project with my new cool friend [player_name] i will see you guys later"
                hide expression b.image
                $ rg.set_emotion('neutral')
                show expression rg.image at left3 with dissolve
                rg "Bryan is about to leave a party for a project ? Did [player_name] use some kind of magic on him ?"
                hide expression rg.image
                $ t.set_emotion('neutral')
                show expression t.image at rightp with dissolve
                t "You should all take notes from this , a party is not more important than your future even a bad student like bryan knows that"
                jump after_study_group_choice2



label leave_party:
    n "You are going home without studying ooof"
    jump go_home
label rip_mr_jackson:
    scene bryan_house at cover_screen(1100, 1380) with dissolve
    $ negative_academic_friendship += 10
    n "You sneak up in the crowwd to Mr Jackson and throw coffee at him and run away"
    $ m.set_emotion('happy')
    show expression m.image at middle with dissolve
    m "Take this Mr Loser !"
    hide expression m.image
    $ rg.set_emotion('shocked')
    show expression rg.image at left3 with dissolve

    $ t.set_emotion('angry')
    show expression t.image at rightp with dissolve
    t "What the hell ?! which immature kid did that I'm gonna report this incident to the principal"
    n "Everybody is laughing but you see bryan and nico knows it was you"
    hide expression rg.image
    hide expression t.image
    $ b.set_emotion('neutral')
    show expression b.image at right with dissolve
    b "hehe [player_name] you are a legend !"
    jump party_continue

label stay_with_emily:
    scene bryan_chill_room at cover_screen(1100, 1380) with dissolve

    $ m.set_emotion('happy')
    show image m.image at middle with dissolve
    m "Mind if i stay there Emily?"
    $ e.set_emotion('happy')
    show expression e.image at right with dissolve
    e "Sure go ahead, [player_name] !"
    hide expression m.image
    hide expression e.image
    n "You sit down next to Emily hearing the music and the people dancing in the background. You both start talking about the exam and the project, sharing your thoughts and concerns."
    n "Somehow the music changes to a classical music"
    $ ni.set_emotion('angry')
    show expression ni.image at right2 with dissolve
    ni " What the ? Since when we blasting some boomer music in a party !"
    $ br.set_emotion('neutral')
    show expression br.image at left3 with dissolve
    br "Ohh Shut up Nico, i like the change of pace"
    hide expression ni.image
    hide expression br.image
    $ jocks.set_emotion('neutral')
    show expression jocks.image at left with dissolve
    jocks "Adam would have loved this music!"
    hide expression jocks.image
    n "Everyone starts laughing and the party continues"

    if player_gender == "girl":
      $ e.set_emotion('happy')
      show expression e.image at right with dissolve
      e "Let's dance [player_name]!"
      n "You and Emily hit the dance floor, laughing and enjoying the music. The energy is infectious, and you both let loose, forgetting about the upcoming exam for a while."
      e "Ugh we've just met and we are already besties , i wish i could stay but i have to prepare for the exam wanna come with me  ?"
      menu:
          "Sure let's go i was getting tired of the party anyway":
                $ popularity += 5
                $ stress -= 5
                m "Sure let's go i was getting tired of the party anyway"
                e "Great! Let's head out to the library."
                $ choices_leave_with_emily = True
                jump after_study_group_choice_e
          "I'm having fun, I'll stay a bit longer":
                $ popularity += 5
                $ stress += 5
                m "I'm having fun, I'll stay a bit longer"
                e "Sure  [player_name].But don't get carried away okay ? "
                n "You and emily hug goodbye she leaves and you continue to enjoy the party"
                jump party_continue


    $ e.set_emotion('neutral')
    show e "I know it's fun but i think i want to leave the party now to study want to join [player_name] ?"
    menu:
        "Sure let's go i was getting tired of the party anyway":
            $ popularity += 5
            $ stress -= 5
            m "Sure let's go i was getting tired of the party anyway"
            e "Great! Let's head out to the library."
            jump after_study_group_choice
        "I'm having fun, I'll stay a bit longer":
            $ emily_friendship += 5
            $ stress -= 5
            m "I'm having fun, I'll stay a bit longer"
            e "Sure  [player_name].But don't get carried away okay ? "
            n"You and emily say goodbye and she leaves the party"
            jump party_continue



label talk_to_random_students:
    scene bryan_dance_room at cover_screen(1100, 1380) with dissolve
    $ rb.set_emotion('neutral')
    show expression rb.image at left with dissolve
    rb "Hey, [player_name]! Great party, right?"
    menu:
        "Yeah, it's awesome!":
            $ popularity += 5
            m "Yeah, it's awesome!"
            rb "Glad you're having fun! Heard any good gossip?"
            menu:
                "Tell them about the overheard conversation.":
                    $ popularity += 10
                    m "Actually, I overheard the teachers talking about making the exam harder this year..."
                    rb "What?! Seriously? That's not fair!"
                    $ stress += 5 # Increased stress due to the news
                "Shrug it off.":
                    m "Not really. Just trying to enjoy the night."
                    jump party_continue
        "I'm worried about the exam...":
            $ stress += 5
            m "I'm worried about the exam, though."
            rb "Don't worry, you'll ace it! Hey, wanna play a drinking game?"
            menu:
                "Sure, why not?":
                    $ popularity += 5
                    $ stress -= 5
                    m "Sure, why not?"
                "I should probably study...":
                    $ skills += 5
                    m "I should probably study..."
                    rb "Suit yourself! But you're missing out on the fun!"
            jump party_continue
        "Seen any teachers around?":
            $ stress += 5
            m "Seen any teachers around?"
            rb "Yeah, they're lurking around like buzzkills. Just ignore them and have fun!"
            jump party_continue

label check_on_bryan:
    scene bryan_dance_room at cover_screen(1100, 1380) with dissolve
    $ b.set_emotion('neutral')
    show expression b.image at right with dissolve
    b "Hey, [player_name]. Enjoying the party?"
    menu:
        "Yeah, it's great!":
            $ bryan_friendship += 5
            $ popularity += 5
            m "Yeah, it's great!"
            b "Awesome! Glad you're part of the crew. Wanna try some of this... special punch?"
            menu:
                "Sure, sounds interesting.":
                    $ popularity += 5
                    $ stress += 10
                    m "Sure, sounds interesting."
                "No thanks, I'm good.":
                    m "No thanks, I'm good."
            jump party_continue
        "I'm worried about the teachers...":
            $ bryan_friendship -= 5
            $ stress += 5
            m "I'm worried about the teachers, though."
            b "Relax, [player_name]. They can't spoil our fun. Just ignore them."
            jump party_continue
        "What's the plan for studying?" if bryan_study_group == True:
            $ skills += 5
            $ stress -= 5
            m "What's the plan for studying?"
            b "We'll figure it out tomorrow. Tonight is for partying!"
            jump party_continue




### scene of bryan study group
label after_study_group_choice2:
   scene uni_library_empty at cover_screen(1100, 1380) with dissolve
   n"You and Bryan and Nico and brett arrive at the library, and the atmosphere is tense until you see Adam noticing you and he is in shock"
   $ a.set_emotion('shocked')
   show expression a.image at right with dissolve
   a "What the hell are you guys doing here ? I don't want to be bothered"
   $ b.set_emotion('neutral')
   show expression b.image at left with dissolve
   b "Nobody care about you loser , we are here to work on the project with our cool friend [player_name] hehe"
   hide expression b.image
   hide expression a.image
   $ ni.set_emotion('neutral')
   show expression ni.image at left2 with dissolve
   ni "Yeah don't cry because we are doing the same thing you are doing but better haha"
   hide expression ni.image
   $ br.set_emotion('neutral')
   show expression br.image at left3 with dissolve
   br "Guys let's not waste our time with him let's go in another place like our favorite rooftop"
   show uni_library_outside at cover_screen(1100, 1380) with dissolve
   n "You and Bryan and Nico and brett leave the library and go to a rooftop int the city  to study"

   $ e.set_emotion('neutral')
   show expression e.image at right with dissolve
   e "Hey you guys were in the library ? i just left it because adam was being an douche because i went to the party"
   $ br.set_emotion('neutral')
   show expression br.image at left3 with dissolve
   br "Yeahh right it just happened to us , i am guessing adam got a personal issue with us duh "
   hide expression e.image
   hide expression br.image
   $ ni.set_emotion('neutral')
   show expression ni.image at left2 with dissolve
   ni "I'm telling you bryan this guy is gonna plot something against us i can feel it"
   hide expression ni.image
   $ b.set_emotion('neutral')
   show expression b.image at right with dissolve
   b "You really think adam is that though hehe and don't worry about it guys we have [player_name] with us we can't fail this project"
   hide expression b.image
   $ br.set_emotion('neutral')
   show expression br.image at left3 with dissolve
   br "Right ! emily you can come with us in the rooftop if you need a nice space "
   if emily_hate == True:
       show screen notification("Emily hate you and she don't want to be near you")
       hide expression br.image
       $ e.set_emotion ('sad')
       show expression e.image at right with dissolve
       e"Thanks for the offer but i rather do it at home , i will see you guys later"
       br "Alright see you later ,let's go to the cool rooftop guys !"
       jump building_rooftop
   $ e.set_emotion('happy')
   show expression e.image at right with dissolve
   e "Sure ! I will come with you guys , i need a quiet place to do the project"
   br "Alright let's go to that cool rooftop guys !"


 ### scene building_rooftop
label building_rooftop:
    scene uni_night at cover_screen(1100, 1380)
    with dissolve

    n "You find yourself on the rooftop of one of the university buildings, the city lights twinkling below. It's a surprisingly peaceful spot amidst the bustling campus."

    $ b.set_emotion('neutral')
    show expression b.image at left with dissolve
    b "Not bad, huh? This is where we usually hang out when we need a break from the chaos."

    $ ni.set_emotion('neutral')
    show expression ni.image at middle with dissolve
    ni "Yeah, it's got a great view. And it's far away from all the nerds cramming in the library."

    $ br.set_emotion('neutral')
    show expression br.image at right with dissolve
    br "Plus, we can blast our music without anyone complaining."

    menu:
        "It's amazing!":
            $ popularity += 3
            $ bryan_friendship += 2
            $ nico_friendship += 2
            $ brett_friendship += 2
            m "It's amazing! I had no idea this place existed."
            $ b.set_emotion('happy')
            show expression b.image at left with dissolve
            b "See? Told you it was cool. Now, let's get down to business."
            $ ni.set_emotion('happy')
            show expression ni.image at middle with dissolve
            ni "Glad you like it. This spot is our little secret, so feel special!"
            $ br.set_emotion('happy')
            show expression br.image at right with dissolve
            br "Alright, enough chit-chat. Time to focus."

        "It's a bit too... exposed.":
            $ stress += 2
            m "It's a bit too... exposed."
            $ ni.set_emotion('smug')
            show expression ni.image at middle with dissolve
            ni "Come on, [player_name], live a little! Don't be such a worrywart."
            $ br.set_emotion('smug')
            show expression br.image at right with dissolve
            br "Yeah, loosen up. We're not gonna fall off."
            $ b.set_emotion('neutral')
            show expression b.image at left with dissolve
            b "You'll get used to it. Just focus on the view and relax."

        "I prefer the library.":
            $ skills += 2
            $ bryan_friendship -= 2
            $ nico_friendship -= 2
            $ brett_friendship -= 2
            m "I prefer the library, to be honest."
            $ b.set_emotion('annoyed')
            show expression b.image at left with dissolve
            b "Suit yourself, nerd. But don't come crying to us when you fail the exam."
            $ ni.set_emotion('annoyed')
            show expression ni.image at middle with dissolve
            ni "Yeah, good luck trying to focus with all those bookworms around."
            $ br.set_emotion('neutral')
            show expression br.image at right with dissolve
            br "Let's just get started."

    n "The group spreads out, textbooks and laptops scattered across a blanket. The atmosphere is relaxed, but there's an underlying sense of determination."

    $ b.set_emotion('neutral')
    show expression b.image at left with dissolve
    b "Alright, let's tackle this quantum computing monster. Who wants to start?"

    $ ni.set_emotion('neutral')
    show expression ni.image at middle with dissolve
    ni "I'm still struggling with the whole superposition thing. It's like, how can something be in two places at once?"

    $ br.set_emotion('neutral')
    show expression br.image at right with dissolve
    br "Yeah, and don't even get me started on entanglement. It's like quantum voodoo."

    menu:
        "Offer to explain superposition.":
            $ skills += 5
            $ bryan_friendship += 3
            $ nico_friendship += 3
            $ brett_friendship += 3
            m "I think I get superposition. It's like... imagine a coin spinning in the air. It's both heads and tails until you catch it."
            $ b.set_emotion('impressed')
            show expression b.image at left with dissolve
            b "Whoa, that actually makes sense! You're a natural teacher, [player_name]."
            $ ni.set_emotion('surprised')
            show expression ni.image at middle with dissolve
            ni "Yeah, not bad. Maybe you're not so bad after all."
            $ br.set_emotion('happy')
            show expression br.image at right with dissolve
            br "Thanks for that explanation. It definitely helps."

        "Admit you're also confused.":
            $ stress += 3
            m "Honestly, I'm still wrapping my head around it too. It's pretty mind-bending."
            $ br.set_emotion('frustrated')
            show expression br.image at right with dissolve
            br "See? Even [player_name] is struggling. Maybe this stuff is just too advanced for us."
            $ b.set_emotion('determined')
            show expression b.image at left with dissolve
            b "Nah, we can do this. We just need to put in the effort."
            $ ni.set_emotion('neutral')
            show expression ni.image at middle with dissolve
            ni "Let's keep trying. We'll get it eventually."

        "Suggest focusing on the Qiskit code first.":
            $ skills += 3
            m "Maybe we should start with the Qiskit code. Once we understand how to implement the concepts, it might make more sense."
            $ ni.set_emotion('agreeable')
            show expression ni.image at middle with dissolve
            ni "Good idea. Let's see if we can at least get the simulator to do something cool."
            $ b.set_emotion('neutral')
            show expression b.image at left with dissolve
            b "Alright, let's boot up our laptops and dive into the code."
            $ br.set_emotion('neutral')
            show expression br.image at right with dissolve
            br "Sounds like a plan. Let's make some magic happen."

    n "The group dives into the project, discussing concepts, writing code, and occasionally laughing at their own mistakes. The city lights continue to twinkle below, a reminder of the world outside their rooftop haven."


    if skills >= 15:
        menu:
            "Explain a complex concept clearly.":
                $ skills += 5
                $ bryan_friendship += 5
                $ nico_friendship += 5
                $ brett_friendship += 5
                m "Okay, so entanglement is like... imagine you have two dice. When you roll them, they always come up with the same number, no matter how far apart they are."
                $ b.set_emotion('amazed')
                show expression b.image at left with dissolve
                b "Wow, [player_name], you're a genius! I finally get it!"
                $ ni.set_emotion('happy')
                show expression ni.image at middle with dissolve
                ni "That's a great analogy. Thanks for breaking it down for us."
                $ br.set_emotion('impressed')
                show expression br.image at right with dissolve
                br "You're really good at this, [player_name]. Thanks."



    n "As the night deepens, the group starts to wind down. They've made significant progress on the project and feel a sense of accomplishment."

    $ b.set_emotion('happy')
    show expression b.image at left with dissolve
    b "Alright, guys, I think that's enough for tonight. We crushed it!"

    $ ni.set_emotion('neutral')
    show expression ni.image at middle with dissolve
    ni "Yeah, we actually made some headway. Thanks for joining us, [player_name]."

    $ br.set_emotion('neutral')
    show expression br.image at right with dissolve
    $ skills += 270
    br "Definitely. We'll ace this exam, no problem."
    show screen notification("You have completed some task of the project in bryan path ! He is definitely becoming a different person because of you you have [skills] skills now")
    n "You leave the rooftop, the city lights still twinkling below. You feel a mix of exhaustion and satisfaction. Despite the challenges, you're starting to find your place in this new world."

    $ b.set_emotion('neutral')
    show expression b.image at left with dissolve
    b "See you guys tomorrow. We'll finish this project in no time with [player_name] on our gaaang."
    hide screen notification
    jump go_home





### library scenes with adam or emily
label after_study_group_choice:
    scene uni_library_empty at cover_screen(1100, 1380)
    with dissolve
    if adamproposition == True and choice_bryan_party == True:
        scene uni_library2_night at cover_screen(1100, 1380)
        $ adam_friendship += 5
        $ a.set_emotion('sad')
        show expression a.image at right with dissolve
        a "Where were you ? I've been waiting for you for like an hour now"
        hide expression a.image
        $ m.set_emotion('neutral')
        show expression m.image at middle with dissolve
        if bryan_proofs == True:
            $ bryan_hate = True
            m "I was looking for proof to show to the principal about Bryan and his friends"
            $ a.set_emotion('happy')
            show expression a.image at right with dissolve
            a "You did what ?! that's amazing [player_name] give them to me i will show them to the principal  !"
        else:
            m "I was at the party, sorry about that"
        a "Alright, let's get started. Emily will probably be late as usual. Shall we start without her?"
        menu:
            "Yes, let's get started.":
                $ emily_friendship -= 3
                jump choice_start_without_emily
            "No, let's wait for Emily.":
                jump choice_wait_for_emily

    if adamproposition == True and choice_bryan_party == False:
        $ adam_friendship += 5
        $ a.set_emotion('happy')
        show expression a.image at right with dissolve
        a "Alright, let's get started. Emily will probably be late as usual. Shall we start without her?"
        menu:
            "Yes, let's get started.":
                $ emily_friendship -= 3
                jump choice_start_without_emily
            "No, let's wait for Emily.":
                jump choice_wait_for_emily

label choice_start_without_emily:
    $ adam_friendship += 5
    $ a.set_emotion('neutral')
    show expression a.image at right with dissolve
    a "Alright, let's dive into the material. We have a lot to cover, and every minute counts."
    n "You and Adam open your textbooks and start going through the key points of the project. Adam explains some of the more complex concepts with clarity, making sure you understand each step."
    $ a.set_emotion('happy')
    show expression a.image at right with dissolve
    a "I'm glad we're able to start without any distractions. This project is really important for our final grade."
    $ m.set_emotion('neutral')
    show expression m.image at middle with dissolve
    m "I agree. It's nice to focus without interruptions."

label choice_wait_for_emily:
    $ emily_friendship += 5
    $ a.set_emotion('sad')
    show expression a.image at right with dissolve
    a "It's been 2 hours. I hate waiting to start studying. We might miss the chance to get the highest grade."
    hide expression a.image
    $ e.set_emotion('sad')
    show expression e.image at right with dissolve
    e "I heard that, Adam. Sorry I'm late, guys. What are we studying today?"
    $ a.set_emotion('angry')
    show expression a.image at left with dissolve
    a "You dare to be late and ask what we're studying today? I'm guessing you were at Bryan's party. Do us a favor and leave our group. I'm sure [player_name] will agree with me."
    menu:
        "I agree with Adam":
            $ emily_hate = True
            $ emily_friendship -= 5
            $ adam_friendship += 5
            $ e.set_emotion('sad')
            show expression e.image at right with dissolve
            e "You seriously are talking to me like this after all the times I've defended you and been nice to you this year? I'm sorry, [player_name], I will leave you guys to study."
            hide expression e.image
            $ a.set_emotion('happy')
            show expression a.image at right with dissolve
            a "I'm glad at least that you're with me, [player_name]. Let's start studying."
            hide expression a.image

        "I disagree with Adam":
            $ emily_hate = False
            $ emily_friendship += 5
            $ adam_friendship -= 5
            $ e.set_emotion('happy')
            show expression e.image at right with dissolve
            e "Thanks for backing me up, [player_name]. But I will leave you guys to study. I can't stand Adam's attitude. I am sorry."
            hide expression e.image
            $ a.set_emotion('sad')
            show expression a.image at right with dissolve
            a "I can't believe you're taking her side. This is just great. Let's just get this over with."
            hide expression a.image


label studying_without_emily:
    n "With Emily gone, you and Adam dive deep into the study material. Adam's frustration fades as he focuses on explaining the key points."
    $ a.set_emotion('neutral')
    show expression a.image at right with dissolve
    a "Let's break down the first part of the project. We need to understand the core concepts before moving on to the practical applications."
    $ m.set_emotion('happy')
    show expression m.image at middle with dissolve
    m "Agreed. Let's start with the main theories."
    n "Hours pass as you and Adam work through the textbooks, solving problems and discussing theories. Despite the initial tension, you make significant progress."
    $ stress -= 10
    $ skills += 430
    show screen notification("You have gained [skills] skills adam path gives the highest skills of any study group")
    show expression a.image at right with dissolve
    a "Good job today, [player_name]. We made some solid progress."
    $ m.set_emotion('happy')
    show expression m.image at middle with dissolve
    m "Thanks, Adam. Let's keep this momentum going for the next session."
    hide screen notification
    n "You pack up your things and head out of the library, feeling a bit more prepared for the upcoming exam."
    jump go_home


label studying_with_emily2:
    n "After Emily leaves, you and Adam reluctantly start studying. Despite the tension, you manage to focus on the material."
    $ a.set_emotion('neutral')
    show expression a.image at right with dissolve
    a "Alright, let's get through this. We'll start with the first chapter and make sure we cover everything thoroughly."
    $ m.set_emotion('neutral')
    show expression m.image at middle with dissolve
    m "Sounds good. Let's make the most of the time we have."
    n "You and Adam spend the next few hours immersed in your books, taking notes and discussing the key concepts. The library is quiet, allowing you to concentrate fully."
    $ stress -= 5
    $ skills += 430
    show screen notification("You have gained [skills] skills adam path gives the highest skills of any study group")
    n "After a long study session, you and Adam decide to call it a day. Despite the rocky start, you've covered a lot of ground."
    $ a.set_emotion('happy')
    show expression a.image at right with dissolve
    a "Good job today, [player_name]. We made some solid progress."
    hide screen notification
    $ m.set_emotion('happy')
    show expression m.image at middle with dissolve
    m "Thanks, Adam. Let's keep this momentum going for the next session."
    n "You pack up your things and head out of the library, feeling a bit more prepared for the upcoming exam."
    jump go_home


label after_study_group_choice_e:
    ### player and Emily coming from the party
    scene uni_library2_night at cover_screen(1100, 1380)
    $ adam_friendship += 2
    $ emily_friendship += 5
    $ bryan_friendship -= 3
    $ a.set_emotion('sad')
    show expression a.image at right with dissolve
    a "So now you decide to join, Emily and [player_name]? I thought you were joining Bryan or studying alone. What do you need help with?"
    hide expression a.image
    $ e.set_emotion('angry')
    show expression e.image at left3 with dissolve
    e "So what, Adam? This is how you welcome me after all the times I've defended you and been nice to you this year?"
    if emily_study_group == True:
        $ a.set_emotion('sad')
        show expression a.image at right with dissolve
        a "I thought you were a serious student, Emily. That's why I joined your group. I rather do the project exam alone at this point."
        $ e.set_emotion('angry')
        show expression e.image at left with dissolve
        e "Okay, if you wanna argue, then just leave. I don't need your annoying 'I'm perfect' attitude. No kidding, why was I even nice to you in the first place?"
        hide expression a.image
        hide expression e.image
        n "After arguing, Adam goes to another table in the library, and you and Emily start studying."
        $ e.set_emotion('happy')
        show expression e.image at right with dissolve
        e "Sorry about that, [player_name]. Adam is just being Adam. Let's start studying."
        if player_gender == "girl":
            e "I didn't want Adam to ruin the vibes, especially because we've got great chemistry."
            $ m.set_emotion('happy')
            show expression m.image at middle with dissolve
            m "Yeah, don't worry about it. You're right, I feel like we've been friends for a long time."
label studying_with_emily:
    n "You and Emily settle down and start going through the study material. Emily's insights and explanations help you grasp difficult concepts."
    $ e.set_emotion('neutral')
    show expression e.image at right with dissolve
    e "Let's focus on the main points first. We need to understand the theory before we move on to the practical part."
    $ m.set_emotion('neutral')
    show expression m.image at middle with dissolve
    m "Good idea. I'll take notes while you explain."
    n "Emily begins to explain the core concepts in detail, breaking down complex ideas into simpler terms. You find her explanations clear and easy to understand."
    $ e.set_emotion('happy')
    show expression e.image at right with dissolve
    e "This part here is crucial for our project. If we don't get this right, the whole thing falls apart."
    $ m.set_emotion('happy')
    show expression m.image at middle with dissolve
    m "Got it. I'll make sure to write it down properly."
    n "The hours pass by quickly as you and Emily work through the material, discussing and solving problems together. Her enthusiasm for the subject is contagious, making the study session enjoyable despite the initial tension with Adam."
    $ stress -= 10
    $ skills += 350
    $ emily_friendship += 5
    e "I think we've atleast done 3/4 of the project. Well that was one hell of a day partying then studying ugh i'm tired"
    m "Right ? i think we should head home and do the rest next time"
    show screen notification("You have completed 3/4 of the project you have [skills] skills")
    e" Yeah let's go"
    hide expression e.image
    hide expression m.image
    scene uni_library_outside at cover_screen(1100, 1380) with dissolve
    if player_gender == "girl":
        $ e.set_emotion('happy')
        show expression e.image at right with dissolve
        e "Let's finish the project  at the coffee shop near the library tomorrow [player_name] so that we get the weekend off to prepare for the presentation next monday okay ? Have a good night"
        e "Sleep well because i want us to have fun the weekend in a park nearby before the presentation !"
        $ m.set_emotion('happy')
        show expression m.image at middle with dissolve
        m "Ha im up for sure ! Good night Emily !"
        n "You and emily hug goodbye and you head home"
        jump go_home

    $ e.set_emotion('neutral')
    show expression e.image at right with dissolve
    e "Let's finish the project  at the coffee shop near the library tomorrow [player_name] so that we get the weekend off to prepare for the presentation next monday okay ? Have a good night"
    $ m.set_emotion('neutral')
    show expression m.image at middle with dissolve
    m "Sure thing Emily ! Good night"
    n "You and emily say goodbye and you head home"
    jump go_home







label go_home:
    scene player_house_room_night at cover_screen(1100, 1380) with dissolve
    n "You arrive home, feeling exhausted but accomplished. The day was a rollercoaster of emotions, but you managed to make the best of it."

    # Reflect on Party Choices
    if choice_bryan_party:
        if bryan_proofs:
            m "I can't believe I gathered all that evidence against Bryan. Adam's going to flip when he sees this."
            $ stress += 2  # Slight stress from the potential fallout
        else:
            if stress > 10:
                m "That party was wild... maybe a little too wild.  I hope I didn't overdo it."
            else:
                m "That was a blast! I needed a night like that to unwind."

    # Reflect on Study Group Choices
    if emily_study_group:
        if player_gender == "girl":
            m "Emily's awesome.  I can't wait to hang out with her again tomorrow... and hopefully get some studying done too!"
        else:
            m "Studying with Emily tomorrow should be interesting. I hope we can actually focus."
    elif bryan_study_group:
        if jock < 5:
            m "I hope I can handle Bryan and Nico during our study sessions.  They don't seem too motivated..."
        else:
            m "That study session with Bryan and the gang is gonna be legendary!  We'll get work done... eventually."
    elif adamproposition:
        m "I'm glad I chose to study with Adam.  He's intense, but he really knows his stuff."

    # Relationship Hints
    if emily_friendship >= 20:
        n "You smile, remembering Emily's laugh. You're starting to think she might become a good friend."
    if bryan_friendship >= 20:
        n "You wonder if Bryan's all talk or if he's serious about acing this exam.  Either way, he's definitely an interesting character."
    if adam_friendship >= 10:
        n "Adam might be a bit uptight, but you can tell he's a good guy deep down."



    if skills >= 300:

        $ skills += 100  # Bonus for ending the day on a positive note
        $ stress -= 200

        n "You feel good about what you learned today. You're starting to get the hang of this whole quantum computing thing."
        n "Because your skills is higher than 300 you have gained a bonus of 100 skills and you have lost 200 stress now you have [skills] skills and remember skills will affect the grade of the exam!"
    if skill < 300:
        n" You feel so gooood about the day you had and you are ready to face the next day !"
        n" You have [skills] skills and remember skills will affect the grade of the exam!"
    # Setting the Mood
    n "You head to bed, ready to face whatever challenges tomorrow brings."
    jump next_day
## Wake up scene
label next_day:
    scene player_house_room_day at cover_screen(1100, 1380) with dissolve
    n "It's 5AM wakee uppppp !"
    if negative_academic_friendship > 10 or jock > 5:
        $ m.set_emotion('angry')
        show expression m.image at middle with dissolve
        m "RRRRRRRRRRRRRRRRRRRRRAAAAAAAA ! DAMN THIS I WANTED MORE SLEEP"
    else:
        $ m.set_emotion('happy')
        show expression m.image at middle with dissolve
        m "I'm still a bit tired of yesterday but i'm ready to face the day !"
    menu:
            "Get up and start the day":
                jump start_day
            "Snooze for 5 more minutes":
                $ stress += 20
                m "Just 5 more minutes..."
                jump start_day

### New day start
label start_day:
    scene uni_park_evening at cover_screen(1100, 1380) with dissolve
    n "You arrive at the university, the sun shining brightly overhead. But the students seem to be in a frenzy, talking and whispering to each other."
    $ ri.set_emotion('neutral')
    show expression ri.image at left with dissolve
    ri "Guys have you heard Adam has exposed last night party to the principal and apparently he has proof that Bryan and his friends were involved in illegal activities"
    $ rg.set_emotion('shocked')
    show expression rg.image at right2 with dissolve
    rg "What ?! I can't believe this this dude is always ruining everything"
    hide expression ri.image
    hide expression rg.image
    n "Every student is going to the main hall to see what's happening"
    scene uni_mainhall3 at cover_screen(1100, 1380) with dissolve
    $ p.set_emotion('neutral')
    show expression p.image at left3 with dissolve
    p "EVERYONE SILENCE ! i have an annoucement to make"
    p "I have received a report that some students were involved in illegal activities last night at the party"
    if adamproposition == True and bryan_proofs == True :
        p "Thanks to our bright student [player_name] and Adam that are doing everything to protect our university reputation  "
    if adamproposition == True and bryan_proofs == False :
        p "Thanks to our bright student Adam who is doing everything to protect our university reputation  "
    if adamproposition == False:
        p "Thanks to our bright student Adam who is doing everything to protect our university reputation  "

    if jock > 5 :
        p " I am also aware that some student has thrown hot coffees to Mr Jackson and i will not tolerate this kind of uneducated behavior in my university"
    p "I am asking the students involved in this to come forward and confess their actions else i will have to believe Adam's proof and take the necessary actions"
    $ b.set_emotion('angry')
    show expression b.image at right with dissolve
    if bryan_proofs == True:
        b "So the losers are trying to frame us for imaginary illegal activities huh ?"
        b "You and Adam are going to regret this especially you [player_name] looking through my house like a creep while i warned you to leave the party !"
    else:
        b "This loser of Adam is trying to frame us for shits we didn't do !"
        b "He is just jealous that almost everybody went to the party while his poor self was crying alone in the library"
    $ p.set_emotion('angry')
    hide expression b.image
    p "Enough ! I know you are a famous troublemaker but im asking you to have some respectful language in my university"
    if bryan_study_group == True or emily_study_group == True:
        p "Adam also told me that one of the new student [player_name] was the number one troublemaker in the party"
    if emily_study_group == True and jock < 5 or bryan_study_group and jock < 5:
        $ e.set_emotion('angry')
        show expression e.image at left3 with dissolve
        if player_gender == "girl":
            e "No way ! [player_name] was with me the whole night she didn't do anything ! Adam is just trying to frame her"
        else:
            e "No way ! [player_name] was with me the whole night he didn't do anything ! Adam is just trying to frame him"
        $ br.set_emotion('angry')
        show expression br.image at right3 with dissolve
        br "Yeah i can confirm that [player_name] didn't do anything wrong last night this loser of adam is probably just jealous of [player_name] popularity among all the students"
        hide expression e.image
        hide expression br.image
        $ b.set_emotion('angry')
        show expression b.image at right with dissolve
        b "Adam you're just done for trying to frame us and [player_name] for things we didn't do !"
        hide expression b.image
        $ ni.set_emotion('angry')
        show expression ni.image at left3 with dissolve
        ni " Yeah everyone knows that [player_name] is a good student and a good person this just shows adam is just a snake scared of losing his perfect student spot !"
        hide expression ni.image
        n "All students are shouting at Adam and he is trying to defend himself"
        $ p.set_emotion('angry')
        show expression p.image at left3 with dissolve
        p "Okay i will investigate this situation it seems maybe adam side of the story isn't adding up "
        $ a.set_emotion('sad')
        show expression a.image at right with dissolve
        a "Sir give me a chance to prove that i am right i have the proof that they were involved in illegal activities"
        p "Enough is enough we've wasted enough time now everybody go to your classes and i will investigate this situation"
        scene uni_hallway3
        n"You are going to your first class of the day but you see bryan group"
        menu:
            "Ignore them and go to your class":
                $ e.set_emotion('happy')
                show expression e.image at right with dissolve
                e "Let's go to class [player_name]"
                jump classroom2
            "Thanks them for defending you":
                $ bryan_friendship += 30
                m "Thanks for defending me guys"
                $ b.set_emotion('neutral')
                show expression b.image at right with dissolve
                b "No problem [player_name] we know you are a good student and a good person"
                hide expression b.image
                $ e.set_emotion('happy')
                show expression e.image at right with dissolve
                e "Let's go to class [player_name]"
                jump classroom2

    if bryan_study_group == True and jock > 10:
        $ b.set_emotion('angry')
        show expression b.image at right with dissolve
        b "I can't believe this loser of Adam is trying to frame us for things we didn't do !"
        b "He is just jealous that almost everybody went to the party while his poor self was crying alone in the library"
        $ p.set_emotion('angry')
        hide expression b.image
        p "Enough ! I know you are a famous troublemaker but im asking you to have some respectful language in my university"
        $ e.set_emotion('angry')
        show expression e.image at left3 with dissolve
        e " Adam is just trying to frame [player_name] i don't think he is genuine in his accusations"
        hide expression e.image
        $ m.set_emotion('angry')
        show expression m.image at middle with dissolve
        m "So what if we did ? Adam is salty because he didn't have any fun last night"
        $ p.set_emotion('angry')
        hide expression m.image
        p "I will investigate this situation this sarcastic isn't helping to believe those accusations"
        n "All students are shouting at Adam and he is trying to defend himself"
        $ a.set_emotion('sad')
        show expression a.image at right with dissolve
        a "Sir you see how he is talking to me ?"
        p "Enough is enough we've wasted enough time now everybody go to your classes and i will investigate this situation"
        scene uni_hallway3
        n"You are going to your first class of the day but you see emily "
        menu:
            "Ignore her and go to your class":
             $ b.set_emotion('neutral')
             show expression b.image at right with dissolve
             b "Let's go to class [player_name]"
             jump classroom2
            "Thank her for defending you":
                 $ emily_friendship += 30
                 m "Thanks for defending me Emily"
                 $ e.set_emotion('neutral')
                 show expression e.image at right with dissolve
                 e "No problem [player_name] i don't think adam is genuine in his accusations but good luck"
                 hide expression e.image
                 $ b.set_emotion('neutral')
                 show expression b.image at right with dissolve
                 b "Let's go to class [player_name]"
                 jump classroom2
    if adamproposition == True :
        $ m.set_emotion('angry')
        show expression m.image at middle with dissolve
        m "Sir we are trusted by the teachers you can see the proof that we have against Bryan and his friends"
        n "The crowd seems to not like you and Adam and they are shouting at you probably because Adam is a good student but he is selfish and arrogant"
        hide expression m.image
        $ a.set_emotion('sad')
        show expression a.image at right with dissolve
        a "They are all against us because we are the only one that are for the new exams changes this year !"
        $ ri.set_emotion('neutral')
        show expression ri.image at left with dissolve
        ri "No we just hate you Adam not because you are better than us but you never help anyone and always act like you are the best that does everything alone !"
        hide expression a.image
        hide expression ri.image
        $ p.set_emotion('angry')
        show expression p.image at left3 with dissolve
        p "Enough ! I will investigate this situation and i will take the necessary actions"
        p "Everybody go to your classes and i will investigate this situation"
        scene uni_hallway3 at cover_screen(1100, 1380) with dissolve
        n "You are going to your first class of the day but you see bryan group and emily in your way"
        if bryan_proofs == True:
            $ b.set_emotion('angry')
            show expression b.image at right with dissolve
            b "If the principal call me his office you two are done for"
            hide expression b.image
        if bryan_proofs == False:
            $ b.set_emotion('angry')
            show expression b.image at right with dissolve
            b " If the principal call me into his office Adam you are done !"
            hide expression b.image
        if emily_hate == True:
            $ e.set_emotion('angry')
            show expression e.image at left3 with dissolve
            e "I don't know what you two are doing but im grateful to not be in your group anymore"

        if emily_hate == False:
            $ e.set_emotion('neutral')
            show expression e.image at left3 with dissolve
            e "[player_name] be careful with Adam if he can backstab other students he can do the same to you"
            $ a.set_emotion('sad')
            show expression a.image at right with dissolve
            a "Don't listen to her [player_name] you are the only one i trust in this university"
            jump classroom2
            hide expression b.image

### Classroom2 scene
label classroom2:
    scene uni_classroom2 at cover_screen(1100, 1380) with dissolve
    n "You enter the classroom, and Ms. Baker greets you with a warm smile."
    if bryan_study_group == True:
        n " You sit next to Bryan "
        $ b.set_emotion('neutral')
        show expression b.image at left with dissolve
        b "Whats up [player_name] ?"
        $ m.set_emotion('neutral')
        show expression m.image at middle with dissolve
        if player_gender == 'girl':
            m "Hey bro !"
            hide expression m.image
            hide expression b.image
        else:
            m "Hey bryan !"
            hide expression m.image
            hide expression b.image
    if emily_study_group == True:
        n " You sit next to Emily "
        $ e.set_emotion('happy')
        show expression e.image at left with dissolve
        e "Hi you !"
        $ m.set_emotion('neutral')
        show expression m.image at middle with dissolve
        if player_gender == 'girl':
            m "Hiiiiii Emily !"
            hide expression m.image
            hide expression e.image
        else:
            m "Hey Emily !"
            hide expression m.image
            hide expression e.image
    if adamproposition == True:
        n "You sit next to Adam"
        $ a.set_emotion('neutral')
        show expression a.image at left with dissolve
        a "Hello [player_name] "
        $ m.set_emotion('neutral')
        show expression m.image at middle with dissolve
        m "Hello Adam..."
        n "I know right Adam has no emotion at all"
        hide expression m.image
        hide expression a.image
    $ t2.set_emotion('neutral')
    show expression t2.image at right with dissolve
    t2 "Good morning, class! I hope you're all ready for an exciting lesson on quantum algorithms."
    hide expression t2.image
    n "You take your seat, noticing the familiar faces of your classmates.  The atmosphere is a bit more subdued than usual, perhaps due to the morning's events."

    # Student chatter about the Adam/Bryan situation
    $ rb.set_emotion('neutral')
    show expression rb.image at left2 with dissolve
    rb "Did you guys hear about what happened in the main hall? Adam tried to get Bryan and his friends expelled!"
    $ rg.set_emotion('neutral')
    show expression rg.image at right2 with dissolve
    rg "Yeah, I can't believe he would do that.  It's so messed up."
    hide expression rb.image
    hide expression rg.image
    $ ri.set_emotion('neutral2')
    show expression ri.image at right with dissolve
    ri "I heard the principal is investigating the whole thing.  Who knows what's gonna happen?"
    hide expression ri.image

    # Reactions based on study group choices
    if bryan_study_group == True:
        $ b.set_emotion('angry')
        show expression b.image at left3 with dissolve
        b "Adam is dead meat, that's what's gonna happen!  He's gonna regret messing with us."
        hide expression b.image
        $ ni.set_emotion('angry')
        show expression ni.image at right3 with dissolve
        ni "Yeah, we're gonna make sure he pays for this."
        hide expression ni.image

    if adamproposition == True:
        $ a.set_emotion('sad')
        show expression a.image at right with dissolve
        a "They'll see.  I have proof, and the principal will believe me. They're just trying to intimidate me."
        hide expression a.image

    # Ms. Baker starts the lesson
    $ t2.set_emotion('neutral')
    show expression t2.image at right with dissolve
    t2 "Okay, everyone, let's settle down and focus on the lesson.  Today, we're going to explore the fascinating world of quantum algorithms."
    hide expression t2.image
    n "Ms. Baker begins her lecture, explaining how quantum algorithms utilize the principles of superposition and entanglement to solve problems that are impossible for classical computers."

    #  Explaining Shor's Algorithm
    $ t2.set_emotion('neutral')
    show expression t2.image at right with dissolve
    t2 "One famous example is Shor's algorithm, which can factor large numbers exponentially faster than any known classical algorithm. This has huge implications for cryptography, as many current encryption methods rely on the difficulty of factoring large numbers."
    hide expression t2.image

    n "You listen intently, trying to absorb the complex information. The implications of this technology are both exciting and daunting.  Ms. Baker continues, delving deeper into the intricacies of Shor's algorithm."

    $ t2.set_emotion('neutral')
    show expression t2.image at right with dissolve
    t2 "Imagine trying to find the prime factors of a really large number - say, one with hundreds of digits.  A classical computer would take an incredibly long time, possibly longer than the age of the universe!  But Shor's algorithm, running on a powerful enough quantum computer, could theoretically do it in a much shorter time frame."
    hide expression t2.image

    $ rg.set_emotion('shocked')
    show expression rg.image at right2 with dissolve
    rg "Wow, that's mind-blowing! So, it could crack all our passwords and security codes?"
    hide expression rg.image

    $ t2.set_emotion('neutral')
    show expression t2.image at right with dissolve
    t2 "That's a simplification, but yes, Shor's algorithm does pose a potential threat to current encryption methods. That's why researchers are actively working on post-quantum cryptography - new encryption schemes that are resistant to attacks from quantum computers."
    hide expression t2.image

    # Choice menu to interact with the lesson
    menu:
        "Ask a question about Shor's algorithm.":
            $ skills += 5
            $ teacher2_friendship += 3
            m "Ms. Baker, can you explain in more detail how Shor's algorithm actually uses quantum phenomena to factor numbers?"
            $ t2.set_emotion('happy')
            show expression t2.image at right with dissolve
            t2 "Excellent question, [player_name]!  Shor's algorithm leverages the principles of quantum superposition and quantum Fourier transform to manipulate qubits in a way that allows for efficient period finding, which is the key to factoring. It's a complex topic, but we can delve into it further after class if you'd like."
            hide expression t2.image
        "Share your thoughts on the ethical implications.":
            $ popularity += 3
            $ stress += 2
            m "This is all incredible, but it also seems a bit scary. What if this technology gets into the wrong hands?  Could it be used for malicious purposes, like mass surveillance or disrupting critical infrastructure?"
            $ t2.set_emotion('neutral')
            show expression t2.image at right with dissolve
            t2 "You raise a valid and important point, [player_name].  The ethical implications of quantum computing are profound.  It's crucial that we, as a society, engage in open dialogue about these issues and establish guidelines for the responsible development and use of this technology.  It's not just about the technical advancements, but also about how we use them and the impact they have on our lives and the world."
            hide expression t2.image
        "Try to relate the concepts to your project.":
            $ skills += 3
            m "I'm trying to wrap my head around how we can apply these complex concepts to our quantum algorithm project.  It's a tough challenge, but also incredibly fascinating."
            $ t2.set_emotion('happy')
            show expression t2.image at right with dissolve
            t2 "That's a great approach, [player_name]!  Keep trying to draw connections between the theoretical concepts we're discussing and the practical application in your project.  It's through that process that you'll deepen your understanding. And remember, don't hesitate to come to me with any questions you have about your project."
            hide expression t2.image

    # Emily's Interaction (Only if in Emily's Study Group)
    if emily_study_group == True:
        $ e.set_emotion('neutral')
        show expression e.image at right2 with dissolve
        e "[player_name], this is amazing, right?  Imagine the possibilities if we could harness this power!"
        if player_gender == "girl":
            $ m.set_emotion('happy')
            show expression m.image at middle with dissolve
            m "I know, right?  It's kind of scary, but also super exciting!  I can't wait to see what we can accomplish with our project."
            hide expression m.image
            $ e.set_emotion('happy')
            show expression e.image at right2 with dissolve
            e "Me too!  We're gonna rock this project.  Let's definitely get together later today to brainstorm some more."
            hide expression e.image
        else:
            menu:
                "Agree enthusiastically":
                    $ emily_friendship += 5
                    $ m.set_emotion('happy')
                    show expression m.image at middle with dissolve
                    m "Totally!  It's mind-blowing.  I think we could come up with some really cool ideas for our project."
                    hide expression m.image
                    $ e.set_emotion('happy')
                    show expression e.image at right2 with dissolve
                    e "I'm glad you're excited too!  Let's definitely make time to work on the project together later. Maybe we can head to that coffee shop near the library again?"
                    hide expression e.image
                "Be cautious but positive":
                    $ emily_friendship += 3
                    $ m.set_emotion('neutral')
                    show expression m.image at middle with dissolve
                    m "Yeah, it's pretty amazing.  But it's also a lot to take in. I'm still trying to wrap my head around it all."
                    hide expression m.image
                    $ e.set_emotion('neutral')
                    show expression e.image at right2 with dissolve
                    e "I get it, it's definitely complex stuff.  But don't worry, we'll figure it out together.  Let's try to meet up later to go over some things, okay?"
                    hide expression e.image
                "Downplay the excitement":
                    $ emily_friendship -= 2
                    $ m.set_emotion('neutral')
                    show expression m.image at middle with dissolve
                    m "It's interesting, I guess.  But I'm not sure how much of this will actually be useful for our project."
                    hide expression m.image
                    $ e.set_emotion('sad')
                    show expression e.image at right2 with dissolve
                    e "Oh, okay.  Well, I still think it's important to understand the broader context.  But sure, we can focus more on the practical aspects later if you want."
                    hide expression e.image

    # More Applications and Quantum Supremacy
    n "The lesson continues, exploring various quantum algorithms and their potential applications in fields like medicine, materials science, and artificial intelligence."
    $ t2.set_emotion('neutral')
    show expression t2.image at right with dissolve
    t2 "Quantum computers are still in their early stages of development, but they hold immense promise.  Some experts believe we're on the verge of achieving 'quantum supremacy' - the point at which quantum computers can outperform classical computers for certain tasks."
    hide expression t2.image
    $ t2.set_emotion('neutral')
    show expression t2.image at right with dissolve
    t2 "Imagine being able to design new drugs and materials at an unprecedented speed, or simulate complex systems like the human brain with incredible accuracy.  The possibilities are truly revolutionary."
    hide expression t2.image
    if bryan_study_group == True :
        menu:
         "Listen to the class so that you get enough knowledge to complete the project to graduate":
            $ skills += 50
            m "Okay i gotta focus a bit more so we can get this project done !"
         "Who care about this i just wanna have fun" if jock > 5:
            m "zzzzzzzzzzzzzzzzzzzzzzzzzzz"
            jump hallway_scene_after_class2
         "I'm stuck in my thought but i need to focus" if jock < 5:
            $ skills += 20
            m "I'm stuck in my thought but i need to focus"

    $ a.set_emotion('happy')
    show expression a.image at right with dissolve
    a "Ms. Baker, what kind of breakthroughs could we see in medicine with quantum computers?"
    hide expression a.image

    $ t2.set_emotion('neutral')
    show expression t2.image at right with dissolve
    t2 "That's an excellent question, Adam.  Quantum computers could revolutionize drug discovery by enabling us to simulate molecular interactions with a level of precision that's simply not possible with classical computers. This could lead to the development of new treatments for diseases like cancer, Alzheimer's, and HIV."
    hide expression t2.image
    $ t2.set_emotion('neutral')
    show expression t2.image at right with dissolve
    t2 "They could also help us understand the complex processes involved in protein folding, which is crucial for developing new therapies for genetic disorders.  And personalized medicine could take a giant leap forward, with quantum computers allowing for the analysis of individual genetic profiles to tailor treatments to specific patients."
    hide expression t2.image

    $ e.set_emotion('neutral')
    show expression e.image at right2 with dissolve
    e "What about materials science?  I read something about quantum computers helping to create super-efficient solar panels."
    hide expression e.image

    $ t2.set_emotion('neutral')
    show expression t2.image at right with dissolve
    t2 "That's another exciting area, Emily.  Quantum computers could lead to the development of new materials with incredible properties.  Imagine materials that are lighter yet stronger than anything we have today, or superconductors that operate at room temperature.  This could revolutionize industries like aerospace, energy, and electronics."
    hide expression t2.image
    $ t2.set_emotion('neutral')
    show expression t2.image at right with dissolve
    t2 "And you're right, Emily, quantum simulations could help us design much more efficient solar panels, leading to a cleaner and more sustainable energy future.  They could also aid in developing better batteries for electric vehicles, and even in creating new catalysts for carbon capture, helping to address climate change."
    hide expression t2.image

    $ ri.set_emotion('neutral2')
    show expression ri.image at right with dissolve
    ri "What about artificial intelligence? Will quantum computers make AI super smart?"
    hide expression ri.image

    $ t2.set_emotion('neutral')
    show expression t2.image at right with dissolve
    t2 "The potential for quantum computing in AI is immense.  Quantum algorithms could significantly speed up machine learning processes, allowing AI systems to learn from data much faster and more efficiently. This could lead to breakthroughs in areas like natural language processing, image recognition, and robotics."
    hide expression t2.image
    $ t2.set_emotion('neutral')
    show expression t2.image at right with dissolve
    t2 "However, we need to be mindful of the potential risks.  More powerful AI also means we need to be even more careful about designing AI systems that are aligned with human values and goals, and that don't pose a threat to our safety and well-being."
    hide expression t2.image

    # Potential Concerns and Responsible Development
    $ br.set_emotion('neutral')
    show expression br.image at right2 with dissolve
    br "This all sounds amazing, but it also kind of makes me nervous. What about job displacement? Will quantum computers take over our jobs?"
    hide expression br.image

    $ t2.set_emotion('neutral')
    show expression t2.image at right with dissolve
    t2 "That's a valid concern, Brett.  It's likely that quantum computing will automate some tasks that are currently done by humans. But it's also important to remember that new technologies often create new jobs and opportunities.  The key is to prepare ourselves for the future by developing the skills and knowledge that will be in demand in a quantum-powered world."
    hide expression t2.image

    $ t2.set_emotion('neutral')
    show expression t2.image at right with dissolve
    t2 "Just like with any powerful technology, there are potential risks and challenges associated with quantum computing.  But by approaching its development and deployment responsibly, ethically, and with a focus on human well-being, we can harness its incredible power to create a better future for all."
    hide expression t2.image

    n "The bell rings, signaling the end of class.  You gather your things, your mind buzzing with possibilities.  You're eager to continue exploring this fascinating field, but also aware of the challenges and ethical considerations that lie ahead."

    jump hallway_scene_after_class2

label hallway_scene_after_class2:
    scene uni_hallway3 at cover_screen(1100, 1380) with dissolve
    if emily_study_group == True:
        $ e.set_emotion('happy')
        show expression e.image at right with dissolve
        e "That was an amazing class, [player_name]! Even though I barely understood anything, let's go to the college cafeteria and talk about the project."
        $ m.set_emotion('happy')
        show expression m.image at middle with dissolve
        m "Yeah, let's go to the college cafeteria and talk about the project."
        jump uni_cafeteria_scene
    if bryan_study_group == True and jock < 5:
        $ b.set_emotion('neutral')
        show expression b.image at right with dissolve
        b "That was a good class [player_name]. Let's go to the college cafeteria, I heard there is a hugeee burger on the menu today."
        $ m.set_emotion('neutral')
        show expression m.image at middle with dissolve
        m "Yeah, let's go to the college cafeteria and talk about the project as well."
        jump uni_cafeteria_scene
    if bryan_study_group == True and jock > 5 and negative_academic_friendship > 1:
        $ b.set_emotion('neutral')
        show expression b.image at right with dissolve
        b "What a trashy class! Let's go to the college cafeteria and have some funnn!"
        $ m.set_emotion('happy')
        show expression m.image at middle with dissolve
        m "Yeah, let's go to the college cafeteria. I am bored of studying."
        jump uni_cafeteria_scene
    if adamproposition == True:
        $ a.set_emotion('sad')
        show expression a.image at right with dissolve
        a "I can't believe this class is over. I was so into it!"
        $ m.set_emotion('neutral')
        show expression m.image at middle with dissolve
        m "Yeah, I was enjoying it so much, but let's go to the college cafeteria and talk about the project."
        jump uni_cafeteria_scene




label uni_cafeteria_scene:
    scene uni_cafeteria at cover_screen(1100, 1380) with dissolve
    n "The cafeteria is buzzing with students grabbing lunch and chatting about their classes. You find a table with your chosen study group and settle in."

    # Group-Specific Interactions:
    if emily_study_group == True:
        $ e.set_emotion('happy')
        show expression e.image at right with dissolve
        e "Okay, [player_name], let's brainstorm some ideas for our project. I was thinking maybe we could focus on exploring quantum teleportation. It's a mind-blowing concept where information is transmitted instantly between two entangled qubits, regardless of distance! Imagine the possibilities!"
        hide expression e.image
        $ m.set_emotion('happy')
        show expression m.image at middle with dissolve
        m "That sounds incredibly cool, Emily! But how would we even begin to demonstrate that in our project?"
        hide expression m.image
        $ e.set_emotion('neutral')
        show expression e.image at right with dissolve
        e "Well, we could use Qiskit to simulate the process.  We'd need to create a circuit that entangles two qubits, then apply specific gates to teleport the state of one qubit to the other.  It'll be challenging, but I think we can do it!"
        hide expression e.image
        $ m.set_emotion('happy')
        show expression m.image at middle with dissolve
        m "Alright, let's give it a shot!  I'm ready to dive into Qiskit and start experimenting."
        hide expression m.image

    elif bryan_study_group == True:
        if jock < 5:
            $ b.set_emotion('neutral')
            show expression b.image at right with dissolve
            b "Alright, guys, let's try to focus for a bit.  [player_name], you seem to have a good grasp on this stuff. What do you think we should focus on for our project?  Maybe something related to quantum cryptography? I heard that's how they keep secrets safe from hackers."
            hide expression b.image
            $ ni.set_emotion('neutral')
            show expression ni.image at right2 with dissolve
            ni "Yeah, quantum cryptography sounds cool.  Like, unbreakable codes! That'd be useful for keeping our online gaming accounts secure, right?"
            hide expression ni.image
            $ m.set_emotion('neutral')
            show expression m.image at middle with dissolve
            m "Quantum cryptography is definitely an interesting area, but it might be a bit complex for our project.  We could start with something simpler, like designing a quantum random number generator.  It's a good way to understand superposition and measurement."
            hide expression m.image

        else:
            $ b.set_emotion('neutral')
            show expression b.image at right with dissolve
            b "Man, that burger was epic!  Alright, [player_name], what's the plan for this project?  We gotta make sure we don't totally flunk it. Maybe we can do something easy, like a quantum game or something? I bet we could make a killer quantum version of 'Rock, Paper, Scissors!'"
            hide expression b.image
            $ ni.set_emotion('neutral')
            show expression ni.image at right2 with dissolve
            ni "Yeah, a quantum game sounds fun!  We could code it in Qiskit and then challenge other students to play."
            hide expression ni.image
            $ m.set_emotion('happy')
            show expression m.image at middle with dissolve
            m "A quantum game could be cool, but let's not get ahead of ourselves.  We need to make sure our project demonstrates a solid understanding of quantum principles.  How about we focus on building a simple quantum circuit that showcases superposition and entanglement?"
            hide expression m.image

    elif adamproposition == True:
        $ a.set_emotion('happy')
        show expression a.image at right with dissolve
        a "Okay, [player_name], I've been doing some research on potential quantum algorithms we could implement.  I think the most promising one is Grover's algorithm.  It's a search algorithm that can find a specific item in an unsorted database much faster than classical algorithms. Imagine searching through a massive library in seconds!"
        hide expression a.image
        $ m.set_emotion('neutral')
        show expression m.image at middle with dissolve
        m "Grover's algorithm sounds fascinating, Adam.  But wouldn't implementing it require a lot of qubits and complex gates?  I'm not sure if we can handle that level of complexity for our project."
        hide expression m.image
        $ a.set_emotion('neutral')
        show expression a.image at right with dissolve
        a "You're right, it might be ambitious.  But I believe we can simplify it for our project.  We could focus on a smaller search space and use a reduced number of qubits.  The key is to demonstrate the core principles of the algorithm."
        hide expression a.image
        $ m.set_emotion('happy')
        show expression m.image at middle with dissolve
        m "Okay, I'm willing to give it a try.  Let's see if we can make Grover's algorithm work for us."
        hide expression m.image

    # Principal Enters and Calls for Bryan
    n "Suddenly, the cafeteria doors swing open, and Principal Stan strides in, his expression grim. He scans the room, his gaze lingering for a moment on your table before he fixes his attention on Bryan."
    $ p.set_emotion('neutral')
    show expression p.image at left3 with dissolve
    p "Bryan, a word in my office. Now."
    hide expression p.image
    n "A hush falls over the cafeteria as everyone watches Bryan nervously get up and follow the principal out.  You can practically feel the weight of every eye in the room on Bryan's back.  There's a palpable tension in the air. You glance over at Adam and see a smug look of satisfaction on his face."

    # Group-Specific Reactions and Confrontation:
    if emily_study_group == True:
        $ e.set_emotion('neutral')
        show expression e.image at right with dissolve
        e "Oh, no.  I hope Bryan's okay. This is probably about Adam's accusations."
        hide expression e.image
        $ m.set_emotion('neutral')
        show expression m.image at middle with dissolve
        m "Yeah, this doesn't look good. Adam, do you really think Bryan and his friends did something illegal?  Was it really necessary to report them to the principal? This seems a bit extreme."
        hide expression m.image
        $ a.set_emotion('sad')
        show expression a.image at right with dissolve
        a "I just presented the evidence I found. It's up to the principal to decide. And what are you even implying, [player_name]? Are you defending them? Are you on their side now?  I thought you were serious about your studies and this project."
        hide expression a.image
        menu:
            "I'm just concerned about Bryan. This whole situation seems blown out of proportion.":
                $ emily_friendship += 3
                $ adam_friendship -= 2
                $ m.set_emotion('neutral')
                show expression m.image at middle with dissolve
                m "Look, Adam, I understand that you're trying to uphold the university's standards. But Bryan's a good guy, and I don't think he'd do anything truly harmful. This whole thing just feels like a witch hunt."
                hide expression m.image
                $ e.set_emotion('happy')
                show expression e.image at right with dissolve
                e "I agree, [player_name].  Adam's being a bit too self-righteous.  Let's not jump to conclusions before we know all the facts."
                hide expression e.image
            "Maybe you're right, Adam. Bryan and his friends do seem like troublemakers.":
                $ emily_friendship -= 2
                $ adam_friendship += 3
                $ m.set_emotion('neutral')
                show expression m.image at middle with dissolve
                m "You know, Adam, you might have a point.  I've seen Bryan and his friends acting a bit recklessly. Maybe they did cross the line at the party."
                hide expression m.image
                $ a.set_emotion('happy')
                show expression a.image at right with dissolve
                a "I'm glad you're seeing things clearly, [player_name].  It's important to hold people accountable for their actions, even if they're popular."
                hide expression e.image
            "This isn't any of our business. Let's focus on our project.":
                $ stress -= 2
                $ m.set_emotion('neutral')
                show expression m.image at middle with dissolve
                m "Look, I don't want to get involved in this drama.  It's between Bryan and the principal.  Let's just focus on our project."
                hide expression m.image
                $ e.set_emotion('neutral')
                show expression e.image at right with dissolve
                e "Yeah, you're right.  This isn't our fight.  Let's just try to stay out of it."
                hide expression e.image

    elif bryan_study_group == True:
        if jock < 5:
            $ b.set_emotion('sad')
            show expression b.image at left3 with dissolve
            b "[player_name], this is all my fault.  I should never have invited them to the party.  Adam's gonna get us all in trouble.  I just wanted to have some fun, and now it's all going to blow up in my face."
            hide expression b.image
            $ ni.set_emotion('angry')
            show expression ni.image at right3 with dissolve
            ni "Don't worry, Bryan. We'll figure this out.  Adam's a lying snake, and we'll expose him. He's just trying to make himself look good and ruin our reputation."
            hide expression ni.image
            $ m.set_emotion('neutral')
            show expression m.image at middle with dissolve
            m "Hey, guys, calm down.  We don't know what the principal's going to say yet.  Bryan, just try to stay calm and explain your side of the story.  Don't let Adam get to you."
            hide expression m.image
        else:
            $ b.set_emotion('angry')
            show expression b.image at left3 with dissolve
            b "This is such BS! Adam's trying to ruin my life because he's jealous.  He wants to be the star student, so he's trying to take me down.  [player_name], you saw what happened, right? You'll back me up, won't you?"
            hide expression b.image
            $ ni.set_emotion('angry')
            show expression ni.image at right3 with dissolve
            ni "Yeah, [player_name], you were there. You know Adam's making a big deal out of nothing! Tell everyone the truth!"
            hide expression ni.image
            menu:
                "Defend Bryan":
                    $ bryan_friendship += 5
                    $ adam_friendship -= 5
                    $ popularity += 3
                    $ m.set_emotion('angry')
                    show expression m.image at middle with dissolve
                    m "Yeah, I was at the party, and Adam's exaggerating everything.  Bryan wasn't doing anything illegal!  Adam's just trying to stir up trouble because he's got a stick up his..."
                    hide expression m.image
                "Stay neutral":
                    $ stress += 3
                    $ m.set_emotion('neutral')
                    show expression m.image at middle with dissolve
                    m "Guys, I don't want to get involved in this.  Let's just wait and see what the principal decides."
                    hide expression m.image
                "Side with Adam":
                    $ bryan_friendship -= 5
                    $ adam_friendship += 5
                    $ popularity -= 3
                    $ m.set_emotion('neutral')
                    show expression m.image at middle with dissolve
                    m "Sorry, Bryan, but I can't lie for you.  Adam might have a point.  You guys were being pretty wild at the party."
                    hide expression m.image

    elif adamproposition == True:
        $ a.set_emotion('neutral')
        show expression a.image at right with dissolve
        a "I told you they were trouble. The principal will see the truth now.  It's about time someone stood up to those bullies.  I'm just doing what's right for the university."
        hide expression a.image
        menu:
            "I'm not sure about this, Adam. Maybe you went too far.":
                $ adam_friendship -= 3
                $ m.set_emotion('neutral')
                show expression m.image at middle with dissolve
                m "Adam, I appreciate you trying to keep things in order, but this seems a bit harsh.  Maybe you could have talked to Bryan directly instead of going straight to the principal."
                hide expression m.image
            "You did the right thing, Adam. Someone had to put them in their place.":
                $ adam_friendship += 3
                $ m.set_emotion('happy')
                show expression m.image at middle with dissolve
                m "I totally agree, Adam.  Bryan and his friends needed a wake-up call. They can't just get away with breaking the rules."
                hide expression m.image
            "Let's not talk about this, Adam. I'm trying to eat.":
                $ stress -= 2
                $ m.set_emotion('neutral')
                show expression m.image at middle with dissolve
                m "Look, I'm not interested in discussing this right now.  I'm trying to enjoy my lunch.  Can we talk about the project instead?"
                hide expression m.image


    #  Cafeteria Reactions
    n "Murmurs ripple through the cafeteria as students whisper about the situation. Some students shoot you and your group curious glances, while others seem to relish the drama unfolding before them.  A few students even start taking pictures with their phones, eager to capture the spectacle."
    $ rg.set_emotion('shocked')
    show expression rg.image at left2 with dissolve
    rg "Whoa, this is intense!  It's like a real-life soap opera!"
    hide expression rg.image
    $ rb.set_emotion('neutral')
    show expression rb.image at right2 with dissolve
    rb "I can't believe this is happening.  I wonder what the principal will do? Do you think Bryan will get expelled?"
    hide expression rb.image
    $ ri.set_emotion('neutral')
    show expression ri.image at left with dissolve
    ri "This is insane!  I wonder what Adam's proof is. Maybe there's video evidence from the party?"
    hide expression ri.image



    n "You can't help but feel a knot of anxiety in your stomach.  You try to focus on your food, but it's hard to swallow with all the tension hanging in the air. The situation is spiraling, and you're caught right in the middle of it.  What will happen to Bryan?  And what about your own reputation and future at the university?"
    if emily_study_group == True:
        $ e.set_emotion('happy')
        show expression e.image at right with dissolve
        e " [player_name] let's go to the coffee shop near the library to finish the project then we will have the whole weekend to relax and have fun"
        if player_gender == 'girl' :
            $ m.set_emotion('happy')
            show expression m.image at middle with dissolve
            m "Suree girl let's finish this project so that we go to that park we talked about"
            hide expression m.image
            hide expression e.image
        else:
            $ m.set_emotion('neutral')
            show expression m.image at middle with dissolve
            m "Alright let's finish this project so that we get the whole weekend to relax"
            hide expression m.image
            hide expression e.image
            jump emily_coffee_scene
     ### suit of the uni_cafeteria_scene
    elif bryan_study_group == True:
            if jock < 5:
                 $ b.set_emotion('neutral')
                 show expression b.image at right with dissolve
                 b "I'm sorry guys, I don't know what's gonna happen.  I hope I didn't mess things up too much.  Thanks for sticking by me, [player_name]."
                 $ m.set_emotion('neutral')
                 $ ni.set_emotion('neutral')
                 show expression ni.image at right2 with dissolve
                 ni "We are never afraid of anything Bryan, i noticed that you've become more aware of your actions since [player_name] joined the group i am not saying it's a bad thing but you gotta keep your head up"
                 hide expression ni.image
                 hide expression b.image
                 $ br.set_emotion('neutral')
                 show expression br.image at right2 with dissolve
                 br "I like the way you guys are supporting each other, i've never seen this before [player_name] joined the group. And i do like you for that [player_name]"
                 show expression m.image at middle with dissolve
                 m "Don't worry, Bryan.  We'll figure this out together.  Let's focus on our project and try to stay positive. "
                 hide expression m.image
                 hide expression b.image
                 jump hallway_scene_after_cafeteria
            else:

                $ b.set_emotion('angry')
                show expression b.image at right with dissolve
                b "This snake gonna pay for what he did. I am not gonna let him ruin my life. [player_name] you saw what happened at the party, you know i didn't do anything wrong"
                $ m.set_emotion('neutral')
                show expression m.image at middle with dissolve
                m "This nerd gonna regret it we will make sure he don't pass the project"
                hide expression m.image
                hide expression b.image
                $ ni.set_emotion('angry')
                show expression ni.image at right2 with dissolve
                ni "[player_name] right we gonna destroy his project and make sure he don't pass the project"
                hide expression ni.image
                $ br.set_emotion('neutral')
                show expression br.image at right2 with dissolve
                br "I am sorry guys but i think i will join emily's group i don't want to be part of this especially that i am not sure if i am gonna pass the project"
                hide expression br.image
                $ b.set_emotion('sad')
                show expression b.image at right with dissolve
                b "It's alright Brett i understand, good luck never im gonna let this nerd ruin my life so im gonna ruin his"

                hide expression ni.image
                jump hallway_scene_after_cafeteria

    elif adamproposition == True:
        $ a.set_emotion('sad')
        show expression a.image at right with dissolve
        a "I hope Bryan learns his lesson.  He can't just get away with breaking the rules.  I'm glad I did the right thing by reporting him."
        $ m.set_emotion('neutral')
        show expression m.image at middle with dissolve
        m "I hope this all gets resolved soon.  Let's focus on our project and try to stay out of the drama."
        hide expression m.image
        hide expression a.image
        jump hallway_scene_after_cafeteria



label hallway_scene_after_cafeteria:
    scene uni_principaloffice at cover_screen(1100, 1380) with dissolve
    n "You and your study group decide to leave the cafeteria, the atmosphere now thick with tension. As you walk down the hallway, you see a cluster of students huddled near the principal's office, whispering amongst themselves."

    # Curiosity and Tension
    $ rb.set_emotion('neutral')
    show expression rb.image at left2 with dissolve
    rb "Did you hear? Bryan's still in there with the principal. I wonder what's going on?"
    hide expression rb.image

    $ ri.set_emotion('neutral2')
    show expression ri.image at right with dissolve
    ri "I heard Adam's in there too. Maybe they're confronting each other! This is going to be epic!"
    hide expression ri.image



    if bryan_study_group == True:
        if jock < 5:
            $ b.set_emotion('sad')
            show expression b.image at right with dissolve
            b "I'm really scared, guys. What if I get expelled? My parents are going to kill me."
            hide expression b.image
            $ ni.set_emotion('angry')
            show expression ni.image at right2 with dissolve
            ni "Don't worry, Bryan. We won't let that happen. We'll stick by you, no matter what."
            hide expression ni.image
            $ m.set_emotion('neutral')
            show expression m.image at middle with dissolve
            m "Yeah, Bryan, we're here for you. Just stay strong."
            hide expression m.image

        else:
            $ b.set_emotion('angry')
            show expression b.image at right with dissolve
            b "That little snitch is in there trying to get me in trouble. I swear, if I get expelled because of him..."
            hide expression b.image
            $ ni.set_emotion('angry')
            show expression ni.image at right2 with dissolve
            ni "We'll make him pay, Bryan. Don't you worry."
            hide expression ni.image
            $ m.set_emotion('neutral')
            show expression m.image at middle with dissolve
            m "Guys, let's not make things worse.  Let's just wait and see what happens."
            hide expression m.image

    if adamproposition == True:
            $ a.set_emotion('neutral')
            show expression a.image at right with dissolve
            a "This is what they deserve. Actions have consequences.  I'm just waiting to see what kind of punishment the principal will give them."
            hide expression a.image
            $ m.set_emotion('neutral')
            show expression m.image at middle with dissolve
            m "I hope this doesn't drag on forever. This drama is really stressing me out."
            hide expression m.image

    # The Door Opens
    n "Suddenly, the door to the principal's office swings open, and Adam steps out, his face pale and his eyes downcast."
    $ a.set_emotion('sad')
    show expression a.image at right with dissolve
    a "... I can't believe this is happening."
    hide expression a.image
    n "Everyone stares at Adam in shock. You can feel the anticipation building. What happened in there? What did the principal decide?"
    $ m.set_emotion('neutral')
    show expression m.image at middle with dissolve
    m "Adam, what happened? What did the principal say?"
    hide expression m.image
    n "Adam hesitates for a moment, glancing back at the closed office door before turning to face you, his expression a mixture of anger and disbelief."





label principal_office_scene:
    scene principaloffice at cover_screen(1100, 1380) with dissolve
    n "You follow Adam hesitantly into the principal's office, your heart pounding. The principal, Mr. Stan, sits behind his imposing desk, his face unreadable. Bryan is nowhere to be seen."

    $ p.set_emotion('neutral')
    show expression p.image at right with dissolve
    p "[player_name], have a seat. We need to talk."
    hide expression p.image

    $ m.set_emotion('neutral')
    show expression m.image at middle with dissolve
    m "Sir, what happened?  Where's Bryan?"
    hide expression m.image

    # Dialogue Based on Study Group and Choices:
    if adamproposition == True:
        if bryan_proofs == True:
            $ p.set_emotion('sad')
            show expression p.image at right with dissolve
            p "Adam presented evidence suggesting that Bryan was involved in some serious misconduct at that party. However, upon further investigation, it turned out the so-called 'proof' was fabricated. Doctored images, misleading videos... It seems Adam was determined to see Bryan punished, even if it meant resorting to dishonesty."
            hide expression p.image
            $ a.set_emotion('sad')
            show expression a.image at right2 with dissolve
            a "But... but they were breaking the rules! Drinking, fireworks, and... and..."
            hide expression a.image
            $ p.set_emotion('angry')
            show expression p.image at right with dissolve
            p "Enough, Adam! I'm deeply disappointed in your behavior.  Integrity is paramount in this institution, and your actions have undermined that trust.  You will face disciplinary action for your attempt to frame another student."
            hide expression p.image
            $ m.set_emotion('shocked')
            show expression m.image at middle with dissolve
            m "I... I can't believe Adam would do that."
            hide expression m.image
            $ p.set_emotion('neutral')
            show expression p.image at right with dissolve
            p "[player_name], I commend you for bringing this information to my attention, even if you were initially misled. However, I must also caution you.  Choose your friends wisely. And always seek the truth, even if it's uncomfortable."
            hide expression p.image
            # Adam's Fate and Player's Choice
            n "You watch as Adam, head bowed in shame, is escorted out of the office. The principal turns back to you, his expression softening slightly."
            $ p.set_emotion('neutral')
            show expression p.image at right with dissolve
            p "As for Bryan, I've given him a stern warning.  He understands the seriousness of his actions and has assured me that such behavior will not be repeated.  I believe in second chances, [player_name]. Do you?"
            hide expression p.image
            menu:
                "Yes, sir. Everyone deserves a chance to redeem themselves.":
                    $ principal_friendship += 5
                    $ m.set_emotion('neutral')
                    show expression m.image at middle with dissolve
                    m "Yes, sir. I believe everyone deserves a chance to learn from their mistakes."
                    hide expression m.image
                "I'm not so sure.  Bryan seems like a bad influence.":
                    $ principal_friendship -= 2
                    $ bryan_hate = True
                    $ m.set_emotion('sad')
                    show expression m.image at middle with dissolve
                    m "I appreciate your leniency, sir. But I'm not convinced Bryan will change his ways."
                    hide expression m.image

        else: # Adam's accusations were false but he didn't fabricate evidence
            show screen notification ("You didn't gather real evidence during the party so you will take bryan side no matter what since you are on adam path don't worry even if you did the proofs doesn't show a really prove the  incident")
            $ p.set_emotion('sad')
            show expression p.image at right with dissolve
            p "[player_name], it seems Adam's accusations against Bryan were greatly exaggerated. While there was some inappropriate behavior at the party, there's no evidence to support the more serious claims.  It appears Adam was driven by personal animosity rather than genuine concern for the university's reputation."
            hide expression p.image
            $ a.set_emotion('sad')
            show expression a.image at right2 with dissolve
            a "But sir, they were being reckless!  Drinking, fireworks... It was dangerous!"
            hide expression a.image
            $ p.set_emotion('neutral')
            show expression p.image at right with dissolve
            p "Adam, I understand your concerns. However, making false accusations is not the way to address them.  You will be placed on disciplinary probation. Any further incidents will result in more severe consequences."
            hide expression p.image
            $ m.set_emotion('neutral')
            show expression m.image at middle with dissolve
            m "I knew Adam was being too harsh..."
            hide expression m.image

            n "Just then, the office door opens, and Bryan steps out, looking relieved."
            $ b.set_emotion('neutral')
            show expression b.image at right2 with dissolve
            b "Thanks for having my back, [player_name].  I knew you wouldn't believe those lies."
            hide expression b.image
            $ m.set_emotion('neutral')
            show expression m.image at middle with dissolve
            m "Don't mention it, Bryan.  Glad you're okay."
            hide expression m.image

    elif bryan_study_group == True:
        if jock < 5:
            $ p.set_emotion('neutral')
            show expression p.image at right with dissolve
            p "[player_name], Bryan has admitted to some rule violations at the party.  He's genuinely remorseful and has assured me that this won't happen again.  I've placed him on probationary status, but I believe he can learn from this experience.And Adam accusations were over exaggerated so i gave him a warning for that"
            hide expression p.image
            $ b.set_emotion('sad')
            show expression b.image at right2 with dissolve
            b "Thanks for giving me another chance, sir. I won't let you down."
            hide expression b.image
            $ m.set_emotion('happy')
            show expression m.image at middle with dissolve
            m "I'm glad to hear that, Bryan. Just try to make better choices from now on, okay?"
            hide expression m.image
            jump principal_office_scene_aftermath
        else:
            $ p.set_emotion('angry')
            show expression p.image at right with dissolve
            p "[player_name], you're here because Adam has implicated you in some serious misconduct at that party. He claims you were involved in vandalizing university property, instigating a dangerous fireworks display, and providing alcohol to underage students.  These are very serious allegations."
            hide expression p.image
            $ m.set_emotion('neutral')
            show expression m.image at middle with dissolve
            m "That's ridiculous! Adam's lying! "
            hide expression m.image
            $ p.set_emotion('neutral')
            show expression p.image at right with dissolve
            p "I have statements from other students corroborating some of Adam's claims. They say they saw you participating in these activities."
            hide expression p.image
            menu:
                "Lie and deny everything":
                    $ negative_academic_friendship += 10
                    $ jock += 5
                    $ m.set_emotion('angry')
                    show expression m.image at middle with dissolve
                    m "Those witnesses are lying! I didn't do anything wrong!  Adam making this all up because he's mad that im more popular than him"
                    hide expression m.image
                    $ p.set_emotion('angry')
                    show expression p.image at right with dissolve
                    p "I'm not convinced by your denial, [player_name]. Your disrespectful attitude only reinforces the negative reports I've received about you. "
                    hide expression p.image
                "Admit to some involvement but downplay it":
                    $ negative_academic_friendship += 5
                    $ jock += 3
                    $ m.set_emotion('neutral')
                    show expression m.image at middle with dissolve
                    m "Okay, maybe I was hanging out with Bryan and his friends, but I wasn't the one vandalizing anything or starting fires!  I just had a couple of drinks. It was a party!"
                    hide expression m.image
                    $ p.set_emotion('sad')
                    show expression p.image at right with dissolve
                    p "[player_name], even being present and participating in such activities is unacceptable.  This university has a code of conduct, and you are expected to uphold it."
                    hide expression p.image
                "Blame it all on peer pressure":
                    $ negative_academic_friendship += 3
                    $ jock += 2
                    $ m.set_emotion('sad')
                    show expression m.image at middle with dissolve
                    m "Look, sir, I was just trying to fit in.  Bryan and his friends are really popular, and I didn't want to be the lame one who didn't join in. I know I made some bad choices, but I'm not a bad person."
                    hide expression m.image
                    $ p.set_emotion('neutral')
                    show expression p.image at right with dissolve
                    p "[player_name], blaming your actions on peer pressure is a weak excuse.  You are responsible for your own choices."
                    hide expression p.image

            # Consequences and Warning
            $ p.set_emotion('neutral')
            show expression p.image at right with dissolve
            p "Both you and Bryan will receive a formal warning for your misconduct.  This warning will be placed on your permanent academic record.  Any further violations of the university's code of conduct will result in suspension or expulsion.  Do I make myself clear?"
            hide expression p.image
            $ m.set_emotion('neutral')
            show expression m.image at middle with dissolve
            m "Yes, sir.  I understand."
            hide expression m.image

            # Bryan's Reaction
            n "Bryan smirks at you from across the room, a look of smug satisfaction on his face. It's clear he's enjoying seeing you squirm."
            $ b.set_emotion('neutral')
            show expression b.image at right2 with dissolve
            b "Don't worry, [player_name].  We're in this together now. Partners in crime!"
            hide expression b.image
            n "You glare at Bryan, feeling a surge of anger and regret. You realize that aligning yourself with him was a huge mistake.  But it's too late to back out now. "

    jump principal_office_scene_aftermath
    n "You leave the principal's office, feeling a mix of relief and uncertainty. The drama with Bryan and Adam has left you shaken, but you're determined to focus on your project and navigate the rest of the semester with integrity."



label principal_office_scene_aftermath:
    scene uni_principaloffice at cover_screen(1100, 1380) with dissolve
    n "You step out of the principal's office, the hallway seeming strangely quiet after the intensity of the meeting.  You take a deep breath, trying to process everything that just happened."

    # Group-Specific Reactions and Transitions
    if adamproposition == True:
        if bryan_hate == True:
            $ a.set_emotion('sad')
            show expression a.image at right with dissolve
            a "[player_name], I... I'm sorry for everything.  I let my anger get the best of me. I was wrong to try to frame Bryan.  I just wanted... I don't know what I wanted.  I guess I felt threatened by his popularity and the way he challenged my ideas."
            hide expression a.image
            $ m.set_emotion('neutral')
            show expression m.image at middle with dissolve
            m "Adam, it's okay. We all make mistakes.  The important thing is that you're taking responsibility for your actions.  Just promise me you'll try to be more honest and less judgmental in the future."
            hide expression m.image
            $ a.set_emotion('happy')
            show expression a.image at right with dissolve
            a "I promise, [player_name]. I'll try to be better.  I still want to finish that project with you, if you'll have me."
            hide expression a.image
            $ m.set_emotion('happy')
            show expression m.image at middle with dissolve
            m "Of course, Adam.  Let's go get this project done."
            hide expression m.image
            jump adam_project_scene

        else:
            $ b.set_emotion('happy')
            show expression b.image at right with dissolve
            b "Hey [player_name] thanks for believing me, i knew adam was gonna regret it"
            hide expression b.image
            $ m.set_emotion('happy')
            show expression m.image at middle with dissolve
            m "Dont worry Bryan i knew he was over reacting, i have to catch up with adam to finish the project"
            hide expression m.image
            jump adam_project_scene

    elif bryan_study_group == True:
        if jock < 5:
            $ b.set_emotion('happy')
            show expression b.image at right with dissolve
            b "Whew, that was close!  Thanks for the pep talk, [player_name].  I guess I dodged a bullet this time.  Come on, let's go grab some coffee and get back to work on that project."
            hide expression b.image
            $ m.set_emotion('happy')
            show expression m.image at middle with dissolve
            m "Sounds good, Bryan.  I could really use a caffeine boost right now."
            hide expression m.image
            jump low_jock_project_scene

        else:
            $ b.set_emotion('neutral')
            show expression b.image at right with dissolve
            b "Man, that was intense!  Old Stan almost had us there.  But hey, at least we're both still in the game.  To celebrate our survival, let's hit up Club Quantum tonight!  I hear they've got a killer DJ and the drinks are flowing."
            hide expression b.image
            $ ni.set_emotion('happy')
            show expression ni.image at right2 with dissolve
            ni "Yeah, Club Quantum!  Let's blow off some steam and forget about all this school drama."
            hide expression ni.image
            $ m.set_emotion('happy')
            show expression m.image at middle with dissolve
            m "Sounds like a plan!  I'm in. Let's go wild!"
            hide expression m.image
            jump nightclub_scene



## Finishing project with adam
label adam_project_scene:
    scene uni_library_full at cover_screen(1100, 1380) with dissolve
    n "You and Adam head to the library to work on your project. The tension from the earlier drama still lingers between you, but you both try to focus on the task at hand. The library is packed with students, all diligently preparing for the upcoming exam. You find a small, quiet corner and set up your laptops."

    $ a.set_emotion('neutral')
    show expression a.image at right with dissolve
    a "Okay, [player_name], let's pick up where we left off. We need to finalize our implementation of Grover's algorithm and prepare for the presentation. Are you ready to focus?"
    hide expression a.image
    $ m.set_emotion('happy')
    show expression m.image at middle with dissolve
    m "Absolutely, Adam.  Let's get this done."
    hide expression m.image

    #  Working on the Project
    n "You spend the next few hours immersed in the project, working through the code, running simulations, and refining your presentation.  Adam's meticulous attention to detail and your collaborative spirit create a productive, if slightly awkward, working environment."

    # Adam's Reflection and Apology (Only if Bryan was hated)
    if bryan_hate == True:
        $ a.set_emotion('sad')
        show expression a.image at right with dissolve
        a "[player_name], I... I want to apologize again for what happened with Bryan. I know I messed up.  I've been so focused on getting ahead that I lost sight of what really matters - honesty and integrity.  I'm going to try to be a better person. A better friend."
        hide expression a.image
        $ m.set_emotion('happy')
        show expression m.image at middle with dissolve
        m "I appreciate that, Adam. It takes courage to admit when you're wrong. Just focus on being yourself, and things will work out."
        hide expression m.image
        $ a.set_emotion('happy')
        show expression a.image at right with dissolve
        a "Thanks, [player_name]. That means a lot to me. Now, let's finish this project.  I have a feeling we're going to nail it."
        hide expression a.image

    # Project Completion and Adam's Change
    n "As you wrap up the final touches on the project, you notice a change in Adam.  He seems less tense, more relaxed. He even cracks a few jokes, surprising you with his dry sense of humor."

    $ a.set_emotion('happy')
    show expression a.image at right with dissolve
    a "You know, [player_name], this project has been a real learning experience, and I don't just mean the quantum computing part. I've learned that it's okay to rely on others, to ask for help, and to admit when I'm wrong.  Thanks for being patient with me."
    a "Rest well this weekend, we need to be at our best on Monday for the presentation"
    hide expression a.image
    $ m.set_emotion('happy')
    show expression m.image at middle with dissolve
    m "You too, Adam.  We make a pretty good team."
    hide expression m.image

    # End Scene and Success
    n "You pack up your things, feeling a sense of accomplishment and a newfound respect for Adam.  Despite the challenges and conflicts, you've managed to complete the project, learn some valuable life lessons, and maybe even forge a genuine friendship along the way."


    $ skills += 200
    show screen notification("You have gained 200 skills you have [skills] now! you and adam finished the project! good job!")

    hide screen notification
    jump go_home2
## bryan group project scene
label low_jock_project_scene:
    n"You and Bryan head to Brett's favorite rooftop to finish the project."
    scene building_rooftop at cover_screen(1100, 1380) with dissolve
    $ br.set_emotion('sad')
    show expression br.image at right2 with dissolve
    br "Hey guys, everything went alright? [player_name], you look tired?"
    hide expression br.image
    $ m.set_emotion('neutral')
    show expression m.image at middle with dissolve
    m "Yeah, it was a bit intense. But Bryan's okay, so that's what matters."
    hide expression m.image
    $ b.set_emotion('neutral')
    show expression b.image at right with dissolve
    b "Yeah, thanks to [player_name].  That pep talk helped a lot. Old Stan gave me a warning, but at least I'm not expelled.  Let's just finish this project and try to stay out of trouble, right?"
    hide expression b.image

    # Nico's Doubts
    $ ni.set_emotion('angry')
    show expression ni.image at right2 with dissolve
    ni "I don't know, man. I still think Adam's a jerk for reporting us.  And this quantum computing stuff is way over my head. I'm not sure I can even pass this exam."
    hide expression ni.image

    # Player Encouragement
    menu:
        "Come on, Nico, you can do it! We'll help you understand.  Let's just focus on one concept at a time.":
            $ skills += 5
            $ ni.set_emotion('neutral')
            show expression ni.image at right2 with dissolve
            ni "Thanks, [player_name].  I appreciate that.  Maybe with your help, I can actually get this."
            hide expression ni.image
        "We're all feeling the pressure, Nico.  But we'll get through this together.  It's not just about passing the exam, it's about learning something new.":
            $ bryan_friendship += 5
            $ ni.set_emotion('neutral')
            show expression ni.image at right2 with dissolve
            ni "Yeah, I guess you're right. It's just tough to stay motivated when it feels like everything's going wrong."
            hide expression ni.image
        "Don't worry about it, Nico. If you fail, you fail.  It's not the end of the world.":
            $ ni.set_emotion('neutral')
            show expression ni.image at right2 with dissolve
            ni "Easy for you to say, [player_name]. You're smart.  I'm just gonna end up flipping burgers for the rest of my life."
            hide expression ni.image

    #  Project Progress and Brett's Support
    n "You all settle down and start working on the project. You guide Bryan and Nico through the concepts, patiently explaining the code and helping them with the simulations. ."

    $ br.set_emotion('neutral')
    show expression br.image at right2 with dissolve
    br "Hey, guys, you're doing great! I'm impressed with how much progress you're making.  See, Nico, you're getting this!"
    hide expression br.image
    $ b.set_emotion('neutral')
    show expression b.image at right with dissolve
    b "Yeah, thanks to [player_name]. They're a real lifesaver.  I think we might actually pull this off!"
    hide expression b.image

    #  Overcoming Challenges and Teamwork
    n "As you work through the project, you face challenges and setbacks, but you work together to overcome them.  You realize that even though Bryan and Nico aren't the most academically inclined, they have strengths that contribute to the team."

    $ b.set_emotion('neutral')
    show expression b.image at right with dissolve
    b "Man, this entanglement stuff is making my brain hurt.  I'm glad you're here to explain it, [player_name]."
    hide expression b.image
    $ ni.set_emotion('neutral')
    show expression ni.image at right2 with dissolve
    ni "Yeah, you're a real quantum wizard, [player_name]. I still don't fully understand it, but I'm starting to see how it all works."
    hide expression ni.image

    # Project Completion and a Sense of Pride
    n "After hours of work, you finally finish the project.  It might not be perfect, but it represents a solid effort from the team.  You all feel a sense of accomplishment and even a bit of pride."

    $ skills += 100
    show screen notification("Good Job! you and your group finished the project and you gained 100 skills you have [skills] now! ")
    hide screen notification
    $ b.set_emotion('neutral')
    show expression b.image at right with dissolve
    b "We did it!  I can't believe we actually finished this thing.  High five, team!"
    hide expression b.image
    $ ni.set_emotion('neutral')
    show expression ni.image at left2 with dissolve
    ni "Yeah, we make a pretty good team, huh?  Thanks for sticking with us, [player_name]."
    hide expression ni.image
    n "You all exchange high fives, celebrating your success.  You realize that this project has been more than just an academic exercise.  It's been a test of teamwork, resilience, and the power of supporting each other through tough times."
    $ br.set_emotion('neutral')
    show expression br.image at right2 with dissolve
    br "Thanks, [player_name]. I don't think if the group could have done it without you. I was thinking of going to the park to relax and have some fun this weekend , what do you think?"
    hide expression br.image
    $ m.set_emotion('happy')
    show expression m.image at middle with dissolve
    m "That sounds like a great idea, Brett.  We all deserve a break after this.  Let's go have some fun this weekend !"

    #  Transition
    n "As the moon is casting a warm glow over the city, you pack up your things and head back to campus. You're tired but satisfied, knowing that you've helped Bryan and Nico achieve something they didn't think was possible. And maybe, just maybe, you've helped them see that there's more to life than just partying and popularity."
    jump go_home2

## Nightclub Scene
label nightclub_scene:
    scene nightclub2 at cover_screen(1100, 1380) with dissolve
    n "The pulsing rhythm of the music vibrates through your chest as you enter Club Quantum.  Laser lights slice through the darkness, illuminating a sea of dancing bodies.  The air is thick with the scent of sweat, perfume, and something a bit stronger."

    $ rd.set_emotion('neutral')
    show expression rd.image at left2 with dissolve
    hide expression rd.image

    $ b.set_emotion('neutral')
    show expression b.image at right with dissolve
    b "Welcome to the real world, [player_name]! No stuffy professors, no boring textbooks, just pure, unadulterated fun!"
    hide expression b.image

    $ ni.set_emotion('neutral')
    show expression ni.image at right2 with dissolve
    ni "Yeah! Let's forget about that old geezer Stan and his lame warnings. Tonight, we're gonna party like there's no tomorrow!"
    hide expression ni.image

    # Choices at the Nightclub
    menu:
        "Head straight to the dance floor":
            $ popularity += 5
            $ stress -= 10
            $ jock += 5
            n "You lose yourself in the rhythm, letting the music move your body. The stress of the day melts away as you dance with reckless abandon, surrounded by other students caught in the same euphoric trance."
        "Grab a drink at the bar":
            $ popularity += 3
            $ stress += 5
            $ jock += 3
            n "You push your way through the crowd to the bar, flashing your fake ID to the bartender.  The music is deafening, but you manage to order a drink.  You take a sip, the alcohol hitting you fast.  It's not the best drink you've ever had, but it does the trick."
            #  Potential Encounter:
            n "As you're about to take another sip, you bump into someone. You turn to apologize, and your eyes meet those of..."
            n "Into me? AH just kidding! Sorry  but if you thought emily or brett was gonna be there AND liking you, you are wrong! "
        "Find a quieter spot to chill":
            $ stress -= 5
            n "You escape the throbbing heart of the dance floor and find a quieter lounge area.  You sink into a plush couch, taking in the scene from a distance.  The music is still loud, but it's less overwhelming here. You watch the swirling lights and dancing bodies, feeling a sense of detachment."
            # Potential Reflection:
            n "You start to wonder if this is really the life you want.  The thrill of rebellion is fading, replaced by a nagging sense of emptiness.  Is this all there is?  Partying, drinking, running from responsibility?"

    # Bryan's Influence and Temptation
    $ b.set_emotion('neutral')
    show expression b.image at right with dissolve
    b "Hey, [player_name], loosen up! This is what freedom feels like! Forget about quantum algorithms and project deadlines! Tonight, we're living in the moment!"
    hide expression b.image
    menu:
        "Embrace the moment and let go":
            $ jock += 5
            $ negative_academic_friendship += 5
            $ m.set_emotion('happy')
            show expression m.image at middle with dissolve
            m "You're right, Bryan! Let's make tonight legendary!"
            hide expression m.image
            n "You let it go and lose yourself ... someone bought you back home"
            jump go_home2

        "Enjoy the night but set boundaries and leave alone early ":
            $ stress += 5
            $ m.set_emotion('neutral')
            show expression m.image at middle with dissolve
            m "I'm having fun, Bryan, but I still need to keep my head on straight.  We have that exam coming up, remember?"
            hide expression m.image
            $ b.set_emotion('sad')
            show expression b.image at right with dissolve
            b "Fine, suit yourself.  But don't blame me if you miss out on all the fun!"
            hide expression b.image
            jump go_home2

        "Suggest leaving early to study":
            $ bryan_friendship -= 5
            $ skills += 5
            $ m.set_emotion('neutral')
            show expression m.image at middle with dissolve
            m "Actually, Bryan, I think I'm gonna head out soon.  I need to get some rest and study for the exam."
            hide expression m.image
            $ b.set_emotion('angry')
            show expression b.image at right with dissolve
            b "Seriously, [player_name]? You're gonna ditch us for some boring textbook?  What a buzzkill!"
            hide expression b.image
            $ ni.set_emotion('angry')
            show expression ni.image at right2 with dissolve
            ni "Yeah, [player_name], you're becoming a real nerd! What happened to the cool [player_gender] we met at the party?"
            hide expression ni.image
            jump go_home2


## Emily's group  Coffee Scene for the project
label emily_coffee_scene:
    scene emily_room at cover_screen(1100, 1380) with dissolve
    n "The aroma of freshly brewed coffee fills Emily's cozy room as you arrive for your final project session.  Sunlight streams through the window, casting a warm glow on the scattered textbooks and notes."

    $ e.set_emotion('happy')
    show expression e.image at right with dissolve
    e "Hey, [player_name]!  I'm so glad you made it!  Grab a coffee and get comfy.  We've got a lot to cover before the presentation."
    hide expression e.image
    $ m.set_emotion('happy')
    show expression m.image at middle with dissolve
    m "Thanks, Emily.  This place smells amazing. What kind of coffee is this?"
    hide expression m.image
    $ e.set_emotion('happy')
    show expression e.image at right with dissolve
    e "It's a special blend from a local roaster. I discovered it a few weeks ago, and I'm hooked!  It's perfect for late-night study sessions."
    hide expression e.image
    n "You settle into a comfortable chair, sipping the aromatic coffee and feeling a sense of calm.  Despite the pressure of the upcoming exam, Emily's relaxed demeanor and the cozy atmosphere of her room help to ease your anxiety."

    # Catching Up and Discussing the Principal Situation
    $ m.set_emotion('neutral')
    show expression m.image at middle with dissolve
    m "So, Emily, what happened with Bryan and Adam? I heard there was some drama with the principal."
    hide expression m.image
    $ e.set_emotion('sad')
    show expression e.image at right with dissolve
    e "It was a mess, [player_name].  Adam tried to get Bryan in serious trouble, but it turned out he'd exaggerated everything and even fabricated some evidence.  The principal was furious.  Adam's on probation now, and Bryan got a warning.  It's all so ridiculous. "
    hide expression e.image
    $ m.set_emotion('sad')
    show expression m.image at middle with dissolve
    m "Wow, I can't believe Adam would do that.  I guess I misjudged him.  I'm just glad Bryan's okay."
    hide expression m.image
    if player_gender == "girl":
      $ e.set_emotion('happy')
      show expression e.image at right with dissolve
      e "Me too!  I always knew he was a jerk, but this is next level.  I'm glad we decided to work together, [player_name].  You're way more trustworthy and fun to be around!"
      hide expression e.image
      $ m.set_emotion('happy')
      show expression m.image at middle with dissolve
      m "Thanks, Emily.  I feel the same way about you.  Now, let's focus on our project and show everyone what we've got!"
      hide expression m.image
    else:
        $ e.set_emotion('happy')
        show expression e.image at right with dissolve
        e "Me too.  It's a shame, because Adam's really smart, but he lets his ego get in the way.  Anyway, let's not dwell on it.  We've got our own amazing project to focus on!"
        hide expression e.image

    # Finalizing the Project
    n "You and Emily spend the next few hours polishing your presentation, reviewing the code, and ensuring you have a solid understanding of the concepts. Emily's enthusiasm is contagious, and you find yourself getting excited about presenting your work."

    $ e.set_emotion('neutral')
    show expression e.image at right with dissolve
    e "I think we're in really good shape, [player_name]!  Our simulation of quantum teleportation is impressive, and our presentation is clear and engaging. I'm really proud of what we've accomplished."
    hide expression e.image
    $ m.set_emotion('happy')
    show expression m.image at middle with dissolve
    m "Me too, Emily.  We make a great team."
    hide expression m.image

    # A Moment of Connection (Optional Romantic Path)
    if emily_friendship >= 60:
        if player_gender == "girl":
            n "As you're packing up your things, you catch Emily's eye.  She smiles at you, a warm, genuine smile that makes your heart skip a beat. You realize that you've developed a strong connection with her, a connection that goes beyond just friendship."
            $ e.set_emotion('happy')
            show expression e.image at right with dissolve
            e "I'm really glad we decided to work together, [player_name].  I've had so much fun with you.  Maybe we can celebrate after the presentation? Just the two of us?"
            hide expression e.image
            menu:
                "That sounds amazing, Emily! I'd love to.":
                    $ emily_friendship += 10
                    $ m.set_emotion('happy')
                    show expression m.image at middle with dissolve
                    m "I'd love that, Emily.  I feel like we have a lot to celebrate."
                    hide expression m.image
                "I'd like that, but maybe we should invite the others too?":
                    $ emily_friendship += 5
                    $ m.set_emotion('happy')
                    show expression m.image at middle with dissolve
                    m "I'd like that, Emily.  But maybe we should invite Bryan, Nico, and Brett too?  It's been a tough week for everyone."
                    hide expression m.image
        else:
            n "As you're packing up your things, you catch Emily's eye.  She smiles at you, a warm, genuine smile that makes your heart skip a beat.  You realize that you've developed a strong connection with her, a connection that might be something more than just friendship."
            $ e.set_emotion('happy')
            show expression e.image at right with dissolve
            e "[player_name], I've had so much fun working with you.  You're incredibly smart and kind, and... well, I was wondering if you'd like to grab dinner with me after the presentation? Just the two of us?"
            hide expression e.image
            menu:
                "I'd love to, Emily.  I feel the same way about you.":
                    $ emily_friendship += 10
                    $ m.set_emotion('happy')
                    show expression m.image at middle with dissolve
                    m "I'd love to, Emily. I feel the same way about you."
                    hide expression m.image
                "That's really nice of you, Emily, but I'm not sure if I'm ready for that.":
                    $ emily_friendship -= 5
                    $ m.set_emotion('neutral')
                    show expression m.image at middle with dissolve
                    m "That's really nice of you, Emily, but I'm not sure if I'm ready for that right now.  Maybe we can just hang out as friends for a while?"
                    hide expression m.image
                "Sorry, Emily, but I'm not interested.":
                    $ emily_friendship -= 10
                    $ m.set_emotion('neutral')
                    show expression m.image at middle with dissolve
                    m "I appreciate the offer, Emily, but I'm not interested. I just want to focus on my studies right now."
                    hide expression m.image

    # Ending the Scene
    n "You leave Emily's room feeling energized and confident.  You're ready to face the project exam head-on, knowing that you have a strong partner by your side.  And maybe, just maybe, you have a chance at something more than just a study buddy."

    $ skills += 250
    show screen notification("You have completed the project and gained 250 skills! you have [skills] skills now! You are ready for the presentation! Good Job!")
    hide screen notification



label go_home2:
    scene player_house_room_night at cover_screen(1100, 1380) with dissolve
    n "You arrive home, exhausted but satisfied with the week's progress. The project is complete, and the drama with Adam and Bryan seems to be settling down (for now).  You collapse onto your bed, letting out a sigh of relief."

    # Weekend Plans and Reflections
    if emily_friendship >= 65 and player_gender == "girl" :
        n "Your thoughts drift to Emily and the plans you made to spend the weekend together. A smile spreads across your face as you imagine exploring the amusement park with her.  You can't wait to have some fun and get to know her better."
        jump weekend_with_emily
    elif emily_friendship >= 65:
        n "Your thoughts drift to Emily and the plans you made to spend the weekend together.  A flutter of excitement fills your stomach. This could be the start of something special. Or maybe it'll just be a fun day out with a friend. Either way, you're looking forward to it."
        jump weekend_with_emily
    elif bryan_study_group == True and jock < 5:
        n "You think about Brett's invitation to the park.  It'll be good to get some fresh air and unwind after the stressful week.  And maybe you can even use the opportunity to help Bryan and Nico stay focused on their studies."
        jump weekend_with_brett
    else:
        n "You close your eyes, letting the exhaustion wash over you. You don't have any big plans for the weekend, but you're looking forward to some much-needed rest and relaxation.  The project presentation looms on Monday, but for now, you're content to simply enjoy the quiet."
        jump presentation_day

# Weekend Scenes

label weekend_with_emily:
    scene amusement_park_day at cover_screen(1100, 1380) with dissolve
    n "The bright lights and cheerful music of the amusement park fill the air as you and Emily arrive, ready for a day of fun and excitement.  The scent of popcorn and cotton candy wafts through the air, making your stomach rumble."

    $ e.set_emotion('happy')
    show expression e.image at right with dissolve
    e "This is awesome, [player_name]!  I haven't been to an amusement park in ages!  What do you want to do first? Rollercoaster? Ferris wheel? Bumper cars?"
    hide expression e.image

    # ...  Continue the scene with choices for amusement park activities, interactions with Emily, and potential romantic moments...

label weekend_with_brett:
    scene amusement_park_day at cover_screen(1100, 1380) with dissolve
    n "You meet up with Brett, Bryan, and Nico at the amusement park. The energy is high, and everyone seems excited to be there."

    $ br.set_emotion('neutral')
    show expression br.image at right with dissolve
    br "Alright, guys, let's hit the rollercoasters first! Who's up for a thrill ride?"
    hide expression br.image

    # ... Continue the scene with choices for amusement park activities, interactions with the group, and potential for the player to influence Bryan and Nico in a positive direction...

# Presentation Day

label presentation_day:
    scene uni_mainbighall at cover_screen(1100, 1380) with dissolve
    n "The day of the project presentation arrives, bringing a mix of anticipation and nervousness.  You take a deep breath, reminding yourself of all the hard work you've put in.  You're ready to showcase your project and face the judges."

    # ... Continue the scene with the presentation, feedback from the judges, and the outcome of the project exam...