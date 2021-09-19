from manim_slide import *

class Header():
    def get(self):
        ou_img = ImageMobject('../images/ou_logo_full_inverted.jpeg').scale(0.4).shift(3*UP+6.3*LEFT)
        nbel_img = ImageMobject('../images/nbel.png').scale(0.18).shift(3*UP+5.8*RIGHT)
        return [ou_img, nbel_img]

class StereoTitle(SlideScene):
    def construct(self):
        note = "Stereo-vision refers to the method of recovering depth information from both eyes,\
             or in the artificial context, machine stereo vision, also referred to as stereoscopic vision, extracts the data from two visual sensors."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        self.add(name)
        
        title = Text("Stereo Vision")
        self.play(FadeIn(title))
        title_copy = Text("Stereo Vision").shift(UP*3).scale(0.5)
        self.play(ReplacementTransform(title,title_copy))
        title_neuro = Text("Neuromorphic Stereo Vision").shift(UP*3).scale(0.5) 
        self.play(ReplacementTransform(title_copy,title_neuro))

class NeuromorphicCamera(SlideScene):
    def construct(self):
        note = "Stereo-vision refers to the method of recovering depth information from both eyes,\
             or in the artificial context, machine stereo vision, also referred to as stereoscopic vision, extracts the data from two visual sensors."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        self.add(name)
        title_neuro = Text("Neuromorphic Stereo Vision").shift(UP*3).scale(0.5) 
        self.add(title_neuro)
        title_camera = Text("Neuromorphic event camera").shift(UP*3).scale(0.5)
        self.play(ReplacementTransform(title_neuro,title_camera))
        self.wait(2)
        
class ConStereoTitle(SlideScene):
    def construct(self):
        note = "Read The Slides!!"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        self.add(name)
        
        title_conventional = Text("Classical Stereo Vision").shift(UP*3).scale(0.5) 
        self.add(title_conventional)

        bul0 = Text("Uses conventional stereo camera").scale(0.3).shift(LEFT*3.5 + UP)
        bul1 = Text("Pixel/feature from one camera corresponds to a pixel/feature in the other camera.").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("This correspondece problem is solved using epipolar constraints.").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)
        bul3 = Text("The depth of in a certain pixel/feature is derived from its disparity.").scale(0.3).next_to(bul2, DOWN).align_to(bul2, LEFT)

        self.play(Write(bul0), run_time = 0.75)
        self.wait(2.5)
        self.play(Write(bul1), run_time = 0.75)
        self.wait(2.5)
        self.play(Write(bul2), run_time = 0.75)
        self.wait(2.5)
        self.play(Write(bul3), run_time = 0.75)
        self.wait(2.5)

class ClassicalExample(SlideScene):
    def construct(self):
        note = "Read The Slides!!"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        self.add(name)
        
        title_conventional = Text("Classical Stereo Vision").shift(UP*3).scale(0.5) 
        self.add(title_conventional)


