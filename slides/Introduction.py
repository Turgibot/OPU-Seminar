from os import wait
from manim_slide import *

class Header():
    def get(self):
        ou_img = ImageMobject('../images/ou_logo_full_inverted.jpeg').scale(0.4).shift(3*UP+6.3*LEFT)
        nbel_img = ImageMobject('../images/nbel.png').scale(0.18).shift(3*UP+5.8*RIGHT)
        return [ou_img, nbel_img]

class Title1(SlideScene):
    def construct(self):
        note = "..."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        opu = Text("THE OPEN UNIVERSITY OF ISRAEL").scale(0.6).shift(UP*1.5)
        seminar = Text("SEMINAR PRESENTATION").scale(0.6).next_to(opu, DOWN)
        guy = Text("Guy Tordjman").scale(0.3).next_to(seminar, DOWN)
        self.play(FadeIn(opu, seminar, guy))
        
       

class Title2(SlideScene):
    def construct(self):
        note = "Hello Everyone, my name is Guy Tordjman and today I'll present my seminar. This seminar reviews articles in 2 fields of neuromorphic engineering."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        
        cover = ImageMobject('../images/cover.png').scale(0.85)
        self.play(FadeIn(cover))
        self.wait()
        name = Text("Guy Tordjman", font_size=11).shift(1*DOWN)
        self.add(name)
        self.play(FadeOut(cover), name.animate.shift(2.2*DOWN+6.3*LEFT))
        

class Title3(SlideScene):
    def construct(self):
        note = "The First topic is neuromorphic stereo vision and the second one is neuromorphic Robot PID controller."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        self.add(name)
        
        neuro = Text("Neuromorphic Stereo vision").scale(0.7)
        pid = Text("Neuromorphic Robot PID controller").scale(0.7).next_to(neuro, DOWN)
        self.play(Write(neuro), run_time=1.5)
        self.wait(1)
        self.play(Write(pid), run_time=1.5)


