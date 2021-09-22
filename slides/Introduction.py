from os import wait
from manim_slide import *

class Header():
    def get(self):
        ou_img = ImageMobject('../images/ou_logo_full_inverted.jpeg').scale(0.4).shift(3*UP+6.3*LEFT)
        nbel_img = ImageMobject('../images/nbel.png').scale(0.18).shift(3*UP+5.8*RIGHT)
        return [ou_img, nbel_img]

class Title(SlideScene):
    def construct(self):
        note = "Hello Everyone, my name is Guy Tordjman and today I'll present my seminar. This seminar reviews articles in 2 fields of neuromorphic engineering. \
            The First topic is neuromorphic stereo vision and the second one is neuromorphic Robot PID controller.\
                 In case you have question please feel free to stop me at any time."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        cover = ImageMobject('../images/cover.png').scale(0.85)
        self.add(cover)
        self.play(FadeIn(cover), run_time=2)
        self.wait(5)
        name = Text("Guy Tordjman", font_size=11).shift(1*DOWN)
        self.add(name)
        self.play(FadeOut(cover), name.animate.shift(2.2*DOWN+6.3*LEFT), run_time=2)
        neuro = Text("Neuromorphic Stereo vision").scale(0.7)
        pid = Text("Neuromorphic Robot PID controller").scale(0.7).next_to(neuro, DOWN)
        self.play(Write(neuro), run_time=1.5)
        self.wait(2)
        self.play(Write(pid), run_time=1.5)


