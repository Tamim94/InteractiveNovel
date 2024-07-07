define n = Character('Narrator',color="#c8c8ff"  )
init python:
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
    'neutral': 'emily_normal',
    'happy': 'emily_happy',
    'sad': 'emily_sad',
}, color="#ffbdbd")

define a = DynamicCharacter('Adam', emotions={
    'neutral': 'adam_smiling',
    'happy': 'adam_happy',
    'sad': 'adam_sad',
}, color="#c8ffc8")

define m = DynamicCharacter('Me', emotions={
    'neutral': 'me_normal',
    'happy': 'me_happy',
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
image parisw = "parisweird.png"
image creditt = "creditt.png"



transform right:
    xalign 0.85 yalign 0.9

transform middle:
    xalign 0.1 yalign 0.9

label start:
    show creditt
    n "This is a game made by the group InteractiveNovel in Estiam."
    n " members of the group are Tamim, Maxime, Ilyas."
    show parisw
    n "It's a new bachelor year for you (student 1), you are a student in the university (Estiam), your actions and relationship with other students will affect the ending "
    show uni
    $ a.set_emotion('happy')
    show expression a.image at right with dissolve
    "Adam" "Hi there! How was class?"

    $ m.set_emotion('neutral')
    show expression m.image at middle with dissolve
    "Me" "Good..."
    $ m.set_emotion('sad')
    show expression m.image at middle with dissolve
    "Me" "I can't bring myself to admit that it all went in one ear and out the other."

    $ a.set_emotion('neutral')
    show expression a.image at right
    "Adam" "How was it?"

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
    show expression a.image at right
    "Adam" "That's great to hear! I'm glad you enjoyed it."
    jump continue_conversation

label choice_boring:
    $ adam_friendship -= 2
    $ m.set_emotion('neutral')
    show expression m.image at middle
    "Me" "It was boring..."
    $ a.set_emotion('sad')
    show expression a.image at right
    "Adam" "Oh, that's too bad. Maybe next time it'll be more engaging."
    jump continue_conversation

label choice_not_paying_attention:
    $ adam_friendship -= 5
    $ m.set_emotion('sad')
    show expression m.image at middle
    "Me" "I didn't pay attention..."
    $ a.set_emotion('neutral')
    show expression a.image at right
    "Adam" "Well, that's not ideal, but it happens sometimes."
    $ b.set_emotion('neutral')
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

    $ e.set_emotion('happy')
    show expression e.image at right
    "Emily" "Nice to meet you! What's your name?"

    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip() if player_name else "Me"
    $ m.character = Character(player_name, color=m.color, image=m.image)

    $ m.set_emotion('neutral')
    show expression m.image at middle
    "Me" f"[player_name]"

    $ e.set_emotion('happy')
    show expression e.image at right
    "Emily" f"Well, {player_name}, welcome to Estiam! I hope you enjoy your time here."

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

    $ t.set_emotion('neutral')
    show expression t.image at right
    "Teacher" "Alright, class, let's get started."

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
