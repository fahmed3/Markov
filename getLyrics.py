import string
import time
import re
import urllib

# here we are using AZLyrics as our lyric provider
# we're using AZLyrics because the URL structure is nice and simple:
# <http://azlyrics.com/artist/song> lower alphanumeric only with no spaces
def lyrics_get(artist,song):
    # get artist/song info
    #artist = raw_input("What artist am I covering? ")
    #song = raw_input("What song am I covering? ")
  
    # regex! remove non-alphanumeric characters
    artist = re.sub('[^A-Za-z0-9]+', "", artist)
    song = re.sub('[^A-Za-z0-9]+', "", song)
    # make it all lowercase to work with AZLyrics URL structure
    artist = artist.lower()
    song = song.lower()
    # get the lyrics from the AZLyrics website now
    raw_html = urllib.urlopen("http://azlyrics.com/lyrics/"+str(artist)+"/"+str(song)+".html")
    # throw the HTML page data into a string
    html_copy = str(raw_html.read())
    # now lets parse this ugly HTML document to get the lyrics from it
    # this parsing works on the grounds that AZLyrics doesn't change their webpage structure, ever
    # splitting at the licence warning is okay because I am not a third party lyric provider
    split = html_copy.split('<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->',1)
    split_html = split[1]
    split = split_html.split('</div>',1)
    lyrics = split[0]

    # we have the lyrics now, clean up some leftover HTML ugliness
    lyrics = re.sub('(<.*?>)',"",lyrics)
    # replace common html punctuation, some important sequences/punctuation may be missing
    lyrics = re.sub('&quot;|&#34;|&#x22;|&ldquo;|&#147;|&#x93;|&rdquo;|&#148;|&#x94',"\"",lyrics)
    lyrics = re.sub('&amp;|&#38;|&#x26;', "&", lyrics)
    lyrics = re.sub('&lsquo;|&#145;|&#x91;|&#rsquo;|&#146;|&#x92;|&#39;|&#x27;', "'", lyrics)
    lyrics = re.sub('&#40;|&#x28;', "(", lyrics)
    lyrics = re.sub('&#41;|&#x29;', ")", lyrics)
    lyrics = re.sub('&#33;|&#x21;', "!", lyrics)
    lyrics = re.sub('&#42;|&#x2a;', "*", lyrics)
    lyrics = re.sub('&#44;|&#x2c;', ",", lyrics)
    lyrics = re.sub('&ndash;|&#150;|&#x96;|&mdash;|&#151;|&#x97;|&#45;|&#x2d;', "-", lyrics)
    lyrics = re.sub('&#46;|&#x2e;', ".", lyrics)
    lyrics = re.sub('&#59;|&#x3b;', ";", lyrics)
    lyrics = re.sub('&#63;|&#x3f;', "?", lyrics)
    lyrics = re.sub('&#64;|&#x40;', "@", lyrics)
    lyrics = re.sub('&#35;|&#x23;', "#", lyrics)
    lyrics = re.sub('&#91;|&#x5b;', "[", lyrics)
    lyrics = re.sub('&trade;|&#153;|&#x99;', "TM", lyrics)

    #print lyrics #uncomment if you want the lyrics to be printed to the console as well
    return lyrics

if __name__ == '__main__':
    lyrics_get("Taylor Swift", "Bad Blood")