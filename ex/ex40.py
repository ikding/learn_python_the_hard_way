class Song(object):

    def __init__(self, lyrics, title="Unknown"):
        self.lyrics = lyrics
        self.title = title

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

    def tell_me_song_title(self):
        print self.title

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"],
                        title="Bulls on Parade")

happy_bday.sing_me_a_song()
happy_bday.tell_me_song_title()

bulls_on_parade.sing_me_a_song()
bulls_on_parade.tell_me_song_title()
