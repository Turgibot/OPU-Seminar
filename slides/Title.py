from manim_slide import *

class Title(SlideScene):
    def construct(self):
        # title = Tex(r"\bfseries\textsc{Manim slides example}").scale(1.25).shift(3*UP+3*LEFT)
        ou_img = ImageMobject('../media/images/ou_logo_full_inverted.jpeg').scale(0.4).shift(3*UP+6.3*LEFT)
        nbel_img = ImageMobject('../media/images/nbel.png').scale(0.18).shift(3*UP+5.8*RIGHT)
        self.add(ou_img,nbel_img)

        self.play(FadeOut(nbel_img),run_time=0.5)
