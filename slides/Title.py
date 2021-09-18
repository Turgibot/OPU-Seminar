from manim_slide import *

class Header():
    def get(self):
        ou_img = ImageMobject('../images/ou_logo_full_inverted.jpeg').scale(0.4).shift(3*UP+6.3*LEFT)
        nbel_img = ImageMobject('../images/nbel.png').scale(0.18).shift(3*UP+5.8*RIGHT)
        return [ou_img, nbel_img]

class Title(SlideScene):
    def construct(self):
        note = "This is a seminat about ..."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        cover = ImageMobject('../images/cover.png').scale(0.85)
        self.add(cover)
        self.wait(0.2)

class Abstract(SlideScene):
    def construct(self):
        for x in Header().get():
            self.add(x)
        cover = ImageMobject('../images/cover.png').scale(0.85)
        self.add(cover)
        self.wait(0.2)