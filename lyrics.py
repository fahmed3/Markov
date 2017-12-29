from random import choice
from random import randint
import sys


def generateModel(text, order):
    model = {}
    for i in range(0, len(text) - order):
        fragment = text[i:i+order]
        next_letter = text[i+order]
        if fragment not in model:
            model[fragment] = {}
        if next_letter not in model[fragment]:
            model[fragment][next_letter] = 1
        else:
            model[fragment][next_letter] += 1
    return model

def getNextCharacter(model, fragment):
    letters = []
    for letter in model[fragment].keys():
        for times in range(0, model[fragment][letter]):
            letters.append(letter)
    return choice(letters)

def generateText(text, order, length):
    model = generateModel(text, order)
    x = randint(0,length)
    currentFragment = text[x:x+order]
    output = ""
    for i in range(0, length-order):
        newCharacter = getNextCharacter(model, currentFragment)
        output += newCharacter
        currentFragment = currentFragment[1:] + newCharacter
    return output
    
#def parseTextFile():

    
text = "Is this a dagger which I see before me, The handle toward my hand? Come, let me clutch thee! I have thee not, and yet I see thee still Art thou not, fatal vision, sensible To feeling as to sight? or art thou but A dagger of the mind, a false creation Proceeding from the heat-oppressed brain?I see thee yet, in form as palpable As this which now I draw. Thou marshallst me the way that I was going, And such an instrument I was to use. Mine eyes are made the fools o' th' other senses, Or else worth all the rest. I see thee still, And on thy blade and dudgeon gouts of blood, Which was not so before. Theres no such thing. It is the bloody business which informs Thus to mine eyes. Now oer the one half-world Nature seems dead, and wicked dreams abuse The curtained sleep. Witchcraft celebrates Pale Hecates offerings; and withered murder, Alarumed by his sentinel, the wolf, Whose howls his watch, thus with his stealthy pace, With Tarquins ravishing strides, towards his design Moves like a ghost. Thou sure and firm-set earth, Hear not my steps which way they walk, for fear Thy very stones prate of my whereabout And take the present horror from the time, Which now suits with it. Whiles I threat, he lives; Words to the heat of deeds too cold breath gives."
    
if __name__ == "__main__":
    print generateText(text, int(sys.argv[1]), int(sys.argv[2]))
    