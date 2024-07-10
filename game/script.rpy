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
define b = DynamicCharacter('Bryan', emotions={
    'neutral': 'bryan_normal',
    'happy': 'bryan_happy',
    'sad': 'bryan_sad',
}, color="#ffbdbd")

define e = DynamicCharacter('Emily', emotions={
    'neutral': 'emily_normal2',
    'happy': 'emily-smiling3',
    'sad': 'emily_sad2',
}, color="#ffbdbd")

define a = DynamicCharacter('Adam', emotions={
    'neutral': 'adam_smiling',
    'happy': 'adam_happy',
    'sad': 'adam_sad',
}, color="#c8ffc8")

define m = DynamicCharacter('Me', emotions={
    'neutral': 'me_normal',
    'happy': 'me_smiling',
    'sad': 'me_sad',
}, color="#c8c8ff", )

define t = DynamicCharacter('Teacher', emotions={
    'neutral': 'teacher1_normal',
    'sad': 'teacher1_sad',
}, color="#ffbdbd")

# Relationship Variables
default adam_friendship = 0
default emily_friendship = 0
default bryan_friendship = 0

# Unrelated images (no character tags)
image uni = "uniiii.png"
image uni_park_day = "uni_park_day.png"
image uni_park_evening = "uni_park_evening.png"
image uni_day = "uni_daylight.png"
image uni_night = "uni_night.png"
image uni_sunset = "uni_sunset.png"
image parisw = "parisweird.png"
image creditt = "creditt.png"
image uni_hallway1 = "uni_hallway1.png"
image uni_hallway3 = "uni_hallway3.png"
image uni_principaloffice = "uni_principaloffice.png"
image uni_library_empty = "uni_library_empty.png"
image uni_library_full = "uni_library_full.png"
image classroom = "classroom.png"



transform right:
    xalign 1.2 yalign 0.9

transform middle:
    xalign 0.1 yalign 0.9

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
    show expression a.image at right
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
    show expression m.image at middle
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
    show expression a.image at right
    "Adam" "Well, that's not ideal, but it happens sometimes."
    hide expression a.image
    $ b.set_emotion('neutral')
    hide expression a.image
    show expression b.image at right
    "Bryan" "Hey, what's up? You are rightttt this course is boringggg.don't listen to the nerd on the right hehe"
    jump continue_conversation

label continue_conversation:
    $ a.set_emotion('neutral')
    show expression a.image at right
    "Adam" "Well, I'm new around here."

    $ a.set_emotion('happy')
    show expression a.image at right
    "Adam" "Don't worry, you'll get the hang of it. By the way, this is Emily, my friend."
    hide a

    $ e.set_emotion('happy')
    show expression e.image at right
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
        show expression b.image at right
        "Bryan" "Hey, [player_name], how's it going? join our group at the end of the class if you want  since adam a boring nerd hehe"
    else:
        $ b.set_emotion('neutral')
        show expression b.image at right
        "Bryan" "Hey, [player_name], how's it going? join us if you find Adam boring hehe"


    # New Scene: Classroom
    # New Scene: Classroom
    hide expression e.image
    scene classroom at cover_screen(1100, 1380)
    with dissolve
    $ t.set_emotion ('neutral')
    show expression t.image at right
    "Teacher" "Alright, class, let's get started."
    hide expression t.image
    $ a.set_emotion ('happy')
    show expression a.image at right
    "Adam" "Hey [player_name], do you want to join our study group after class?"

    menu:
        "Sure, that sounds great!":
            jump choice_interesting2
        "I'm not sure, I need to catch up on the material first.":
            jump choice_unsure
        "No thanks, I prefer to study alone.":
            jump choice_decline

label choice_interesting2:
    $ adam_friendship += 3
    $ emily_friendship += 2
    show expression m.image at middle
    "Me" "Sure, that sounds great!"
    show expression a.image at right
    "Adam" "Awesome! We usually meet in the library."
    jump after_study_group_choice

label choice_unsure:
    show expression m.image at middle
    "Me" "I'm not sure, I need to catch up on the material first."
    show expression a.image at right
    "Adam" "No worries, maybe next time."
    jump after_study_group_choice

label choice_decline:
    $ adam_friendship -= 1
    $ emily_friendship -= 1
    $ m.set_emotion('neutral')
    show expression m.image at middle
    "Me" "No thanks, I prefer to study alone."
    $ a.set_emotion('happy')
    show expression a.image at right
    "Adam" "Alright, suit yourself."
    jump after_study_group_choice

label after_study_group_choice:
    show uni_library_empty at cover_screen(1100, 1380)
    with dissolve

    show expression a.image at right
    "Adam" "Alright, let's get started. What do you need help with?"

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
