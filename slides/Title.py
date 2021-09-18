from manim_slide import *

class Header():
    def get(self):
        ou_img = ImageMobject('../images/ou_logo_full_inverted.jpeg').scale(0.4).shift(3*UP+6.3*LEFT)
        nbel_img = ImageMobject('../images/nbel.png').scale(0.18).shift(3*UP+5.8*RIGHT)
        return [ou_img, nbel_img]

class Title(SlideScene):
    def construct(self):
        note = "Hello Everyone, my name is Guy Tordjman and today I'll present my seminar. This seminar reviews articles in 2 fields of neuromorphic engineering in robotics so I'm positive you'll find them very interesting.\n \
            The First topic is neuromorphic stereo vision and the second one is neuromorphic Robot controller.\n In case you have question please feel free to stop me at any time."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        cover = ImageMobject('../images/cover.png').scale(0.85)
        self.add(cover)
        self.wait(0.2)

class Itinerary(SlideScene):
    def construct(self):
        note = "So the first topic that I would represent today is neuromorphic stereo vision. Inorder for me to so, I would like to start by briefly giving you all some background information about the subject of conventional stereo vision.\n \
            I'll also present some slides with information about neuromorphic cameras and then we'll dive for a deeper explanation of the neuromorphic stereo vision model, decribed in the paper I reviewed"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        cover = ImageMobject('../images/cover.png').scale(0.85)
        name = Text("Guy Tordjman", font_size=12).shift(3.2*DOWN+6.3*LEFT)
        self.add(cover)
        self.add(name)

        # self.play(Transform(cover,name), run_time=1.5)
        self.wait(0.2)