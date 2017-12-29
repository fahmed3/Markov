# CTRL+SHIFT+O -> ControlP5 -> Textfield
# How to paste
# array of filenames to get text?

import lyrics
import getLyrics
import sys
add_library("beads")

ac = AudioContext()
sampleText = ""
state = 0
newLyrics = ""
inputText = ""
useText = ""


def setup():
    size(600, 600)
    #selectInput("Select an audio file:", "fileSelected")

# def fileSelected(selection):
#     if not selection:
#         audioFileName = "C:/Users/fsafa/OneDrive/Documents/1.mp3"
#         sample = SampleManager.sample(audioFileName)
#         player = SamplePlayer(ac, sample)
# And as before...
#         g = Gain(ac, 2, 0.4)
#         g.addInput(player)
#         ac.out.addInput(g)
# print type(audioFileName)
# exit()
#     audioFileName = selection.getAbsolutePath()
#     print audioFileName
#     sample = SampleManager.sample(audioFileName)
#     player = SamplePlayer(ac, sample)
# And as before...
#     g = Gain(ac, 2, 0.4)
#     g.addInput(player)
#     ac.out.addInput(g)


def draw():
    if(state == 0):
        startScreen()
    elif(state == 1):
        nextScreen()

def startScreen():
    x = width / 2
    y = height - 75
    background(50)
    if(mouseX > x - 150
       and mouseX < x + 150
       and mouseY < y + 50
       and mouseY > y - 50):
        fill(200)
        if(mousePressed):
            global newLyrics
            newLyrics = lyrics.generateText(sampleText, 5, 400)
            global state
            state = 1
            # WORKS WITH COLDPLAY BUT NOT WITH ED SHEERAN
            #---select file and print audioFileName again for ed sheeran to check
            # correct path to file
            # print artist
            audioFileName = "C:/Users/fsafa/Desktop/Markov/Markov/artists/" + artist + ".mp3"
            try:
                sample = SampleManager.sample(audioFileName)
                player = SamplePlayer(ac, sample)
                # And as before...
                g = Gain(ac, 2, 0.4)
                g.addInput(player)
                ac.out.addInput(g)
            except:
                pass
    else:
        fill(255)
    rectMode(CENTER)
    rect(x, y, 300, 100, 15)
    textAlign(CENTER)
    textSize(24)
    fill(255)
    text(
        "Create your own lyrics inspired\nby your favorite songs!", width / 2, 30)
    textSize(20)
    text("Type in format:\nArtist - Song", width / 2, 100)
    rect(x, height - 300, 400, 300)
    fill(0)
    textAlign(CENTER)
    textSize(24)
    text("Generate Lyrics", x, y)
    textSize(18)
    text(inputText, width / 2, height - 300, 400, 300)


def nextScreen():
    ac.start()
    background(50)
    fill(255)
    textAlign(LEFT)
    textSize(20)
    text(newLyrics, width / 2, height / 2 + 5, width, height)

    noStroke()
    # scan across the pixels
    xprev = 0
    yprev = height / 2

    fill(color(255, 102, 204))
    # stroke(color(255,102,204))
    # strokeWeight(3)
    for i in range(width):
        # for each pixel work out where in the current audio buffer we are
        buffIndex = i * ac.getBufferSize() / width
        # then work out the pixel height of the audio data at that point
        vOffset = int((1 + 5 * ac.out.getValue(0, buffIndex)) * height / 2)
        vOffset = min(vOffset, height)
        ellipse(i, vOffset, 3, 3)
        # line(xprev,yprev,i,vOffset)
        #xprev = i
        #yprev = vOffset

# def overButton(x, y, w, h):
#     if(mouseX > x - w / 2
#        and mouseX < x + w / 2
#        and mouseY < y + h / 2
#        and mouseY > y - h / 2):
#         fill(200)
#         return True
#     else:
#         fill(255)
#         return False

def keyPressed(): 
    global inputText
    inputText += chr(keyCode)  # what shows up on the screen
    global useText
    useText += chr(keyCode)  # being processed for artist and song
    # print(keyCode)
    if(keyCode == 8):
        inputText = inputText[:-2]
        useText = useText[:-2]
    if(keyCode == 10):
        if "-" in useText:
            newText = useText.split("-")
            global artist
            artist = newText[0]
            artist = re.sub('[^A-Za-z0-9]+', "", artist)
            artist = artist.lower()
            global song
            song = newText[1]
            global sampleText
            sampleText += getLyrics.lyrics_get(artist, song)
        useText = ""

def stop():
    ac.stop()