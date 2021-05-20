#UEBERSETZUNGSSPIEL FÜR KINDER: "FRAG' DEN FROSCH"

#Actor-images by opengameart.org

import pgzero

WIDTH = 855
HEIGHT = 448

frog = Actor('frog_stand')
frog.topright = 840, 380

abc = []
for i in range(0, 26):
    abc.append(chr(i+97))

letters_actors = []
def make_Actors(letters):
    for letter in letters:
        letters_actors.append(Actor(letter))
    return (letters_actors)
abc_actors = make_Actors(abc)

def position_abc_actors():
    position_x = 32.1
    for i in range(0, 26):
        position_x += 30
        abc_actors[i].topright = position_x, 50
position_abc_actors()

def draw():
    screen.clear()
    screen.blit('background', (0, 0))
    frog.draw()
    for i in range(0, 26):
        abc_actors[i].draw()

import builtins
from unittest.mock import Mock

words = {'cat': 'katze', 'dog': 'hund', 'bird': 'vogel',
         'snake': 'schlange', 'sheep': 'schaf', 'cow': 'kuh',
         'fish': 'fisch', 'frog':'frosch', 'horse': 'pferd', 
         'mouse': 'maus','hamster': 'hamster'}
print(list(words))

def chosen_word():
    word = input("Gib ein Wort ein, das du uebersetzen moechtest: ")
    print("Uebersetze das englische Wort '" + word + "' auf Deutsch: Klicke auf die Buchstaben")
    return words[word]

def test_ultimate_answer(monkeypatch):
        fake_input = Mock(side_effect=['cow'])
        monkeypatch.setattr(builtins, 'input', fake_input)
        assert chosen_word == 'cow'

word_de = chosen_word()

def on_mouse_down(pos):
    i = 0
    while i < len(word_de):
        if abc_actors[abc.index(word_de[i])].collidepoint(pos):
            animate(abc_actors[abc.index(word_de[i])], tween='bounce_start', pos=
            ((WIDTH/2-15*(len(word_de)-1))+30*i, 250)).on_finished = frog_jump
        i += 1

def frog_jump():
    frog.image = 'frog_jump1'
    clock.schedule_unique(frog_jump2, 0.07)
    clock.schedule_unique(frog_jump3, 0.14)
    clock.schedule_unique(frog_stand, 0.21)

def frog_jump2():
    frog.image = 'frog_jump2'

def frog_jump3():
    frog.image = 'frog_jump3'
    frog.right -= 750/len(word_de)

def frog_stand():
    frog.image = 'frog_stand'
