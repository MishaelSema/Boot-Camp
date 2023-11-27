class song():
    def __init__(self,lyric=[]):
        self.lyric=lyric
    def sing_me_a_song(self):
        for i in self.lyric:
            print(i)
stairway=song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()
