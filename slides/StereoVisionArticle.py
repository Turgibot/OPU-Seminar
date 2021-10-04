from numpy import number
from manim_slide import *
import cv2
import random


class Header():
    def get(self):
        ou_img = ImageMobject('../images/ou_logo_full_inverted.jpeg').scale(0.4).shift(3*UP+6.3*LEFT)
        nbel_img = ImageMobject('../images/nbel.png').scale(0.18).shift(3*UP+5.8*RIGHT)
        return [ou_img, nbel_img]



class StereoModelTitle(SlideScene):
    def construct(self):
        note = "This 2017 article by Osswald et al. describes a spiking neural network model of 3D perception\
             for event bases neuromorphic stereo vision systems"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        self.add(name)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        cover = ImageMobject('../images/article1.png').scale(0.85)
        
        self.play(FadeIn(source, cover), run_time=0.5)

class StereoCorrespondence1(SlideScene):
    def construct(self):
        note = "To better understand how depth is extracted from stereo data, lets take a look at two images taken by a stereo camera.\
            As you can see the images are of the same scene, taken from a slightly different location, similar to when we humans alternate covering a single eye. \
            To calculate the depth in a certain point in the left image we first must first find the matching point in the right image. This problem is called the correspondence problem\
                For example is this red pointy area in the left image corresponds to this one in the right image or this one?. \
                    and what if we are trying to match a green point on the smooth sureface of the ball? There, the problem is even more complexed...\
                At this point we can assume that the images are rectified which means that they share the same y value. \
                    So the search for a corresponding point is limited to one row which limits the number of operation to the width of the image. \
                        but even if we consentrate on a single row - the solution is not that trivial because there might be more than a single match to a point. \
                            What we can do is to use a cost function like Sum of absolute differences of a window and not a point and return the position with the minimal cost.\
                                but that still might not be enough as we shall see at demo part of the presentation..."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        self.add(name, source)
        correspondence_title = Text("The Correspondence Problem").shift(UP*3).scale(0.7)
        self.play(FadeIn(correspondence_title))
        left_img = ImageMobject("../images/bawlingLeft.png").scale(0.5)
        left_txt = Text("Left Image").scale(0.3).next_to(left_img, UP)
        right_img = ImageMobject("../images/bawlingRight.png").scale(0.5).next_to(left_img, RIGHT)
        right_txt = Text("Right Image").scale(0.3).next_to(right_img, UP)
        stereo_pair = Group(left_img, left_txt, right_img, right_txt).center()
        self.play(FadeIn(stereo_pair))




class StereoCorrespondence2(SlideScene):
    def construct(self):
        note = "To better understand how depth is extracted from stereo data, lets take a look at two images taken by a stereo camera.\
            As you can see the images are of the same scene, taken from a slightly different location, similar to when we humans alternate covering a single eye. \
            To calculate the depth in a certain point in the left image we first must first find the matching point in the right image. This problem is called the correspondence problem\
                For example is this red pointy area in the left image corresponds to this one in the right image or this one?. \
                    and what if we are trying to match a green point on the smooth sureface of the ball? There, the problem is even more complexed...\
                At this point we can assume that the images are rectified which means that they share the same y value. \
                    So the search for a corresponding point is limited to one row which limits the number of operation to the width of the image. \
                        but even if we consentrate on a single row - the solution is not that trivial because there might be more than a single match to a point. \
                            What we can do is to use a cost function like Sum of absolute differences of a window and not a point and return the position with the minimal cost.\
                                but that still might not be enough as we shall see at demo part of the presentation..."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        self.add(name, source)
        correspondence_title = Text("The Correspondence Problem").shift(UP*3).scale(0.7)

        left_img = ImageMobject("../images/bawlingLeft.png").scale(0.5)
        left_txt = Text("Left Image").scale(0.3).next_to(left_img, UP)
        right_img = ImageMobject("../images/bawlingRight.png").scale(0.5).next_to(left_img, RIGHT)
        right_txt = Text("Right Image").scale(0.3).next_to(right_img, UP)
        stereo_pair = Group(left_img, left_txt, right_img, right_txt).center()
        self.add(stereo_pair, correspondence_title)

        rect_left = Rectangle(color=BLACK, height=0.5, width=0.5).shift(LEFT*3.3+UP*0.5)
        rect_right = Rectangle(color=BLACK, height=0.25, width=0.25).shift(LEFT*3.2+UP*0.5)
        rect_right_cp = Rectangle(color=BLACK, height=0.25, width=0.25)
        self.play(Create(rect_left))
        self.play(rect_left.animate.scale(0.5))
        self.wait(3)
        self.play(rect_right.animate.shift(RIGHT*4.57))
        self.wait(2)
        rect_right_cp = rect_right.copy()
        self.play(rect_right_cp.animate.shift(LEFT*0.25))

class StereoCorrespondence3(SlideScene):
    def construct(self):
        note = "To better understand how depth is extracted from stereo data, lets take a look at two images taken by a stereo camera.\
            As you can see the images are of the same scene, taken from a slightly different location, similar to when we humans alternate covering a single eye. \
            To calculate the depth in a certain point in the left image we first must first find the matching point in the right image. This problem is called the correspondence problem\
                For example is this red pointy area in the left image corresponds to this one in the right image or this one?. \
                    and what if we are trying to match a green point on the smooth sureface of the ball? There, the problem is even more complexed...\
                At this point we can assume that the images are rectified which means that they share the same y value. \
                    So the search for a corresponding point is limited to one row which limits the number of operation to the width of the image. \
                        but even if we consentrate on a single row - the solution is not that trivial because there might be more than a single match to a point. \
                            What we can do is to use a cost function like Sum of absolute differences of a window and not a point and return the position with the minimal cost.\
                                but that still might not be enough as we shall see at demo part of the presentation..."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        self.add(name, source)
        correspondence_title = Text("The Correspondence Problem").shift(UP*3).scale(0.7)

        left_img = ImageMobject("../images/bawlingLeft.png").scale(0.5)
        left_txt = Text("Left Image").scale(0.3).next_to(left_img, UP)
        right_img = ImageMobject("../images/bawlingRight.png").scale(0.5).next_to(left_img, RIGHT)
        right_txt = Text("Right Image").scale(0.3).next_to(right_img, UP)
        stereo_pair = Group(left_img, left_txt, right_img, right_txt).center()
        self.add(stereo_pair, correspondence_title)

        circ_left = Circle(radius=0.3).shift(LEFT*2.5)
        circ_right = Circle(radius=0.15).shift(LEFT*2.5)
        
        self.play(Create(circ_left))
        self.play(circ_left.animate.scale(0.5))
        # self.wait(3)
        self.play(circ_right.animate.shift(RIGHT*4.6))

        circ_path = Circle(radius=0.15).shift(RIGHT*2)
        self.play(MoveAlongPath(circ_right, circ_path), run_time = 3)
        self.play(MoveAlongPath(circ_right, circ_path), run_time = 3)
        self.play(MoveAlongPath(circ_right, circ_path), run_time = 3)

class StereoCorrespondence4(SlideScene):
    def construct(self):
        note = "To better understand how depth is extracted from stereo data, lets take a look at two images taken by a stereo camera.\
            As you can see the images are of the same scene, taken from a slightly different location, similar to when we humans alternate covering a single eye. \
            To calculate the depth in a certain point in the left image we first must first find the matching point in the right image. This problem is called the correspondence problem\
                For example is this red pointy area in the left image corresponds to this one in the right image or this one?. \
                    and what if we are trying to match a green point on the smooth sureface of the ball? There, the problem is even more complexed...\
                At this point we can assume that the images are rectified which means that they share the same y value. \
                    So the search for a corresponding point is limited to one row which limits the number of operation to the width of the image. \
                        but even if we consentrate on a single row - the solution is not that trivial because there might be more than a single match to a point. \
                            What we can do is to use a cost function like Sum of absolute differences of a window and not a point and return the position with the minimal cost.\
                                but that still might not be enough as we shall see at demo part of the presentation..."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        self.add(name, source)
        correspondence_title = Text("The Correspondence Problem").shift(UP*3).scale(0.7)

        left_img = ImageMobject("../images/bawlingLeft.png").scale(0.5)
        left_txt = Text("Left Image").scale(0.3).next_to(left_img, UP)
        right_img = ImageMobject("../images/bawlingRight.png").scale(0.5).next_to(left_img, RIGHT)
        right_txt = Text("Right Image").scale(0.3).next_to(right_img, UP)
        stereo_pair = Group(left_img, left_txt, right_img, right_txt).center()
        self.add(stereo_pair, correspondence_title)

        line_l = DashedLine((-5,0,0), (-0.2, 0,0))
        line_r = DashedLine((0.2,0,0), (5, 0,0))
        self.play(Write(line_l), run_time=0.5)
        self.play(Write(line_r), run_time=0.5)
        self.wait()

        line_l = DashedLine((-5,1,0), (-0.2, 1,0), color=BLUE)
        line_r = DashedLine((0.2,1,0), (5, 1,0), color=BLUE)
        self.play(Write(line_l), run_time=0.5)
        self.play(Write(line_r), run_time=0.5)


        line_l = DashedLine((-5,-1,0), (-0.2, -1,0), color=BLACK)
        line_r = DashedLine((0.2,-1,0), (5, -1,0), color=BLACK)
        self.play(Write(line_l), run_time=0.5)
        self.play(Write(line_r), run_time=0.5)

class StereoCorrespondence5(SlideScene):
    def construct(self):
        note = "Looking at a single line at the same y value, from both images , we can improve our algorithm by minimizing a SAD cost function. \
            Looking for a match for the BLACK point at x index equal to 6, on the left image is done by calculating the sum of absolute differences between each pixel in a window \
                of certain size"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        self.add(name, source)
        correspondence_title = Text("The Correspondence Problem").shift(UP*3).scale(0.7)

        left_img = ImageMobject("../images/bawlingLeft.png").scale(0.5)
        left_txt = Text("Left Image").scale(0.3).next_to(left_img, UP)
        right_img = ImageMobject("../images/bawlingRight.png").scale(0.5).next_to(left_img, RIGHT)
        right_txt = Text("Right Image").scale(0.3).next_to(right_img, UP)
        stereo_pair = Group(left_img, left_txt, right_img, right_txt).center()
        self.add(stereo_pair, correspondence_title)

        # replace images with lines
        left_img_line = ImageMobject("../images/bawlingLeftLine.png").scale(0.5)
        right_img_line = ImageMobject("../images/bawlingRightLine.png").scale(0.5).next_to(left_img_line, RIGHT)
        stereo_line_pair = Group(left_img_line, right_img_line).center().shift(UP*0.5)
        left_row_txt = Text("Left Row").scale(0.3).next_to(left_img_line, UP*1.5)
        right_row_txt = Text("Right Row").scale(0.3).next_to(right_img_line, UP*1.5)
        self.play(FadeOut(left_img, right_img),FadeIn(stereo_line_pair), ReplacementTransform(right_txt, right_row_txt), ReplacementTransform(left_txt, left_row_txt), run_time=2)
        
       
        
        rect_left = Rectangle(color=BLACK, height=0.61, width=0.61, grid_xstep=0.2, grid_ystep=0.2, stroke_width=1).shift(LEFT*3.27+UP*0.5).scale(0.5)
       
        x = Text("6").scale(0.3).next_to(rect_left, DOWN)
        y = Text("10").scale(0.3).next_to(left_img_line, LEFT)
        y_axis = Vector(UP).next_to(y, LEFT)
        x_axis = Vector().align_to(y_axis, LEFT).shift(RIGHT*0.1)
        y_axis_txt = Text("Y").scale(0.3).next_to(y_axis, LEFT)
        x_axis_txt = Text("X").scale(0.3).next_to(x_axis, DOWN)
        self.play(FadeIn(x, y, x_axis, y_axis, x_axis_txt, y_axis_txt))
        dot_src = Dot(radius=0.1, color=BLACK).shift(LEFT*3.27+UP*0.5).scale(0.3)
        self.play(FadeIn(dot_src))

        sad_img = Tex(r"$SAD(x,y,d) = \sum_{(i,j)\in W}|I_1(x+i,y+j)-I_2(x+i+d,y+j)|$").scale(0.6).shift(UP*2.1)
        self.wait(3)
        self.play(FadeIn(sad_img))

class StereoCorrespondence6(SlideScene):
    def construct(self):
        note = ">>>"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        self.add(name, source)
        correspondence_title = Text("The Correspondence Problem").shift(UP*3).scale(0.7)
        self.add(name, source, correspondence_title)



        # replace images with lines
        left_img_line = ImageMobject("../images/bawlingLeftLine.png").scale(0.5)
        right_img_line = ImageMobject("../images/bawlingRightLine.png").scale(0.5).next_to(left_img_line, RIGHT)
        stereo_line_pair = Group(left_img_line, right_img_line).center().shift(UP*0.5)
        self.add(stereo_line_pair)
        left_row_txt = Text("Left Row").scale(0.3).next_to(left_img_line, UP*1.5)
        right_row_txt = Text("Right Row").scale(0.3).next_to(right_img_line, UP*1.5)
        self.add(left_row_txt, right_row_txt)
        
        sad_img = Tex(r"$SAD(x,y,d) = \sum_{(i,j)\in W}|I_1(x+i,y+j)-I_2(x+i+d,y+j)|$").scale(0.6).shift(UP*2.1)
        self.add(sad_img)
        
        rect_left = Rectangle(color=BLACK, height=0.61, width=0.61, grid_xstep=0.2, grid_ystep=0.2, stroke_width=1).shift(LEFT*3.27+UP*0.5).scale(0.5)
        x = Text("6").scale(0.3).next_to(rect_left, DOWN)
        y = Text("10").scale(0.3).next_to(left_img_line, LEFT)
        y_axis = Vector(UP).next_to(y, LEFT)
        x_axis = Vector().align_to(y_axis, LEFT).shift(RIGHT*0.1)
        y_axis_txt = Text("Y").scale(0.3).next_to(y_axis, LEFT)
        x_axis_txt = Text("X").scale(0.3).next_to(x_axis, DOWN)
        self.add(x, y, x_axis, y_axis, x_axis_txt, y_axis_txt)
        self.play(Create(rect_left))
        


class StereoCorrespondence7(SlideScene):
    def construct(self):
        note = "After calculating the SAD value for every point on the right row we can see that the minimum cost is at index 4"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        correspondence_title = Text("The Correspondence Problem").shift(UP*3).scale(0.7)
        self.add(name, source, correspondence_title)



        # replace images with lines
        left_img_line = ImageMobject("../images/bawlingLeftLine.png").scale(0.5)
        right_img_line = ImageMobject("../images/bawlingRightLine.png").scale(0.5).next_to(left_img_line, RIGHT)
        stereo_line_pair = Group(left_img_line, right_img_line).center().shift(UP*0.5)
        self.add(stereo_line_pair)
        left_row_txt = Text("Left Row").scale(0.3).next_to(left_img_line, UP*1.5)
        right_row_txt = Text("Right Row").scale(0.3).next_to(right_img_line, UP*1.5)
        self.add(left_row_txt, right_row_txt)
        
        sad_img = Tex(r"$SAD(x,y,d) = \sum_{(i,j)\in W}|I_1(x+i,y+j)-I_2(x+i+d,y+j)|$").scale(0.6).shift(UP*2.1)
        self.add(sad_img)

        rect_left = Rectangle(color=BLACK, height=0.61, width=0.61, grid_xstep=0.2, grid_ystep=0.2, stroke_width=1).shift(LEFT*3.27+UP*0.5).scale(0.5)
        rect_right = Rectangle(color=BLACK, height=0.61, width=0.61, grid_xstep=0.2, grid_ystep=0.2, stroke_width=1).shift(RIGHT*0.2+UP*0.5).scale(0.5)
        x = Text("6").scale(0.3).next_to(rect_left, DOWN)
        y = Text("10").scale(0.3).next_to(left_img_line, LEFT)
        y_axis = Vector(UP).next_to(y, LEFT)
        x_axis = Vector().align_to(y_axis, LEFT).shift(RIGHT*0.1)
        y_axis_txt = Text("Y").scale(0.3).next_to(y_axis, LEFT)
        x_axis_txt = Text("X").scale(0.3).next_to(x_axis, DOWN)
        self.add(rect_left, x, y, x_axis, y_axis, x_axis_txt, y_axis_txt)
        i = 0.2
        x_r = 0
        d = 0
        diffs = VDict()
        while i < 5.2:
            rect_right.move_to((i, 0.5, 0))
            self.play(FadeIn(rect_right), run_time=0.15)
            self.add(Text(str(x_r)).scale(0.3).next_to(rect_right, DOWN))
            if x_r == 4:
                sad_val = 32
            else:
                sad_val = 33 + int(20*random.random())
            diff_tmp = Text(str(sad_val-30), color=RED).scale(0.3).next_to(rect_right, UP*0.75)
            diffs.add([(i, diff_tmp)])
            self.add(diffs[i])
            self.wait(0.15)
            i += 0.3
            x_r += 1
        
        self.play(FadeOut(rect_right), run_time=0.3)
        

class StereoCorrespondence8(SlideScene):
    def construct(self):
        note = "This means that the disparity of the point at position y = 10 x = 6 is the differnce in the x values and equal to 2"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        correspondence_title = Text("The Correspondence Problem").shift(UP*3).scale(0.7)
        self.add(name, source, correspondence_title)



        # replace images with lines
        left_img_line = ImageMobject("../images/bawlingLeftLine.png").scale(0.5)
        right_img_line = ImageMobject("../images/bawlingRightLine.png").scale(0.5).next_to(left_img_line, RIGHT)
        stereo_line_pair = Group(left_img_line, right_img_line).center().shift(UP*0.5)
        self.add(stereo_line_pair)
        left_row_txt = Text("Left Row").scale(0.3).next_to(left_img_line, UP*1.5)
        right_row_txt = Text("Right Row").scale(0.3).next_to(right_img_line, UP*1.5)
        self.add(left_row_txt, right_row_txt)
        
        sad_img = Tex(r"$SAD(x,y,d) = \sum_{(i,j)\in W}|I_1(x+i,y+j)-I_2(x+i+d,y+j)|$").scale(0.6).shift(UP*2.1)
        self.add(sad_img)

        rect_left = Rectangle(color=BLACK, height=0.61, width=0.61, grid_xstep=0.2, grid_ystep=0.2, stroke_width=1).shift(LEFT*3.27+UP*0.5).scale(0.5)
        rect_right = Rectangle(color=BLACK, height=0.61, width=0.61, grid_xstep=0.2, grid_ystep=0.2, stroke_width=1).shift(RIGHT*0.2+UP*0.5).scale(0.5)
        x = Text("6").scale(0.3).next_to(rect_left, DOWN)
        y = Text("10").scale(0.3).next_to(left_img_line, LEFT)
        y_axis = Vector(UP).next_to(y, LEFT)
        x_axis = Vector().align_to(y_axis, LEFT).shift(RIGHT*0.1)
        y_axis_txt = Text("Y").scale(0.3).next_to(y_axis, LEFT)
        x_axis_txt = Text("X").scale(0.3).next_to(x_axis, DOWN)
        self.add(rect_left, x, y, x_axis, y_axis, x_axis_txt, y_axis_txt)

        i = 0.2
        x_r = 0
        while i < 5.2:
            rect_right.move_to((i, 0.5, 0))
            self.add(Text(str(x_r)).scale(0.3).next_to(rect_right, DOWN))
            i += 0.3
            x_r += 1
        diff = Text(str("2"), color=RED).scale(0.3).next_to(rect_right, UP*0.75).shift(LEFT*3.6)
        self.add(rect_right.next_to(diff, DOWN*0.75).shift(LEFT*0.01))
        self.play(Write(diff), run_time=0.1)

        disp = Tex(r"$disparity(10,6) = x_l - x_r = 6 - 4 = 2$").scale(0.6).shift(DOWN)
        self.play(FadeIn(disp))

class StereoCorrespondence9(SlideScene):
    def construct(self):
        note = "This means that the disparity of the point at position y = 10 x = 6 is the differnce in the x values and equal to 2"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        correspondence_title = Text("The Correspondence Problem").shift(UP*3).scale(0.7)
        self.add(name, source, correspondence_title)



        # replace images with lines
        left_img_line = ImageMobject("../images/bawlingLeftLine.png").scale(0.5)
        right_img_line = ImageMobject("../images/bawlingRightLine.png").scale(0.5).next_to(left_img_line, RIGHT)
        stereo_line_pair = Group(left_img_line, right_img_line).center().shift(UP*0.5)
        self.add(stereo_line_pair)
        left_row_txt = Text("Left Row").scale(0.3).next_to(left_img_line, UP*1.5)
        right_row_txt = Text("Right Row").scale(0.3).next_to(right_img_line, UP*1.5)
        self.add(left_row_txt, right_row_txt)
        
        sad_img = Tex(r"$SAD(x,y,d) = \sum_{(i,j)\in W}|I_1(x+i,y+j)-I_2(x+i+d,y+j)|$").scale(0.6).shift(UP*2.1)
        self.add(sad_img)

        rect_left = Rectangle(color=BLACK, height=0.61, width=0.61, grid_xstep=0.2, grid_ystep=0.2, stroke_width=1).shift(LEFT*3.27+UP*0.5).scale(0.5)
        rect_right = Rectangle(color=BLACK, height=0.61, width=0.61, grid_xstep=0.2, grid_ystep=0.2, stroke_width=1).shift(RIGHT*0.2+UP*0.5).scale(0.5)
        x = Text("6").scale(0.3).next_to(rect_left, DOWN)
        y = Text("10").scale(0.3).next_to(left_img_line, LEFT)
        y_axis = Vector(UP).next_to(y, LEFT)
        x_axis = Vector().align_to(y_axis, LEFT).shift(RIGHT*0.1)
        y_axis_txt = Text("Y").scale(0.3).next_to(y_axis, LEFT)
        x_axis_txt = Text("X").scale(0.3).next_to(x_axis, DOWN)
        self.add(rect_left, x, y, x_axis, y_axis, x_axis_txt, y_axis_txt)
       
        diff = Text(str("2"), color=RED).scale(0.3).next_to(rect_right, UP*0.75).shift(LEFT*3.6)
        self.add(rect_right.next_to(diff, DOWN*0.75).shift(LEFT*0.01))
        disp = Tex(r"$disparity(10,6) = x_l - x_r = 6 - 4 = 2$").scale(0.6).shift(DOWN)
        self.add(diff, disp)

        self.play(FadeOut(left_img_line, right_img_line,diff, disp, rect_left, sad_img,left_row_txt,right_row_txt, x, y, x_axis, y_axis, x_axis_txt, y_axis_txt ))


        difficult_txt = Text("Is Difficult").scale(0.7).next_to(correspondence_title, DOWN)
        self.play(Write(difficult_txt), run_time=0.3)

        prob1 = Text("Occlusions").scale(0.4).shift(LEFT*4.3+UP)
        prob2 = Text("Homogeneous regions").scale(0.4).next_to(prob1, DOWN).align_to(prob1, LEFT)
        prob3 = Text("Repetitive patterns").scale(0.4).next_to(prob2, DOWN).align_to(prob1, LEFT)

        self.play(Write(prob1),Write(prob2),Write(prob3), run_time=0.3)

class StereoCorrespondence10(SlideScene):
    def construct(self):
        note = "This means that the disparity of the point at position y = 10 x = 6 is the differnce in the x values and equal to 2"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        correspondence_title = Text("The Correspondence Problem").shift(UP*3).scale(0.7)
        difficult_txt = Text("Is Difficult").scale(0.7).next_to(correspondence_title, DOWN)
        self.add(name, difficult_txt, source, correspondence_title)

        prob1 = Text("Occlusions").scale(0.4).shift(LEFT*4.3+UP)
        prob2 = Text("Homogeneous regions").scale(0.4).next_to(prob1, DOWN).align_to(prob1, LEFT)
        prob3 = Text("Repetitive patterns").scale(0.4).next_to(prob2, DOWN).align_to(prob1, LEFT)

        self.add(prob1, prob2, prob3)
        bot_holder = Dot(radius=0.01).next_to(difficult_txt, DOWN*16)
        seperator = Line(difficult_txt.get_bottom(), bot_holder, color=BLUE).shift(DOWN*0.5+LEFT)
        global_title = Text("Global Constraint must be applied:", color=RED).scale(0.45).shift(RIGHT*2.5+UP*1.5)

        self.play(FadeIn(global_title), FadeIn(seperator))

        const1_title = Text("Uniqueness", color=BLUE).scale(0.4).next_to(global_title, DOWN).align_to(global_title, LEFT)
        const1_txt = Text("For any point in one image, there should be at most ").scale(0.3).next_to(const1_title, DOWN).align_to(global_title, LEFT).shift(RIGHT*0.2)
        const11_txt = Text("one matching point in the other image").scale(0.3).next_to(const1_txt, DOWN).align_to(global_title, LEFT).shift(RIGHT*0.2)
        # const2_title = Text("Ordering", color=BLUE).scale(0.4).next_to(const11_txt, DOWN).align_to(global_title, LEFT)
        # const2_txt = Text("Corresponding points should be in the same order in ").scale(0.3).next_to(const2_title, DOWN).align_to(global_title, LEFT).shift(RIGHT*0.2)
        # const21_txt = Text("both views").scale(0.3).next_to(const2_txt, DOWN).align_to(global_title, LEFT).shift(RIGHT*0.2)
        # const3_title = Text("Smoothness", color=BLUE).scale(0.4).next_to(const21_txt, DOWN).align_to(global_title, LEFT)
        const3_title = Text("Smoothness", color=BLUE).scale(0.4).next_to(const11_txt, DOWN).align_to(global_title, LEFT)
        const3_txt = Text("Disparity is typically a smooth function of x").scale(0.3).next_to(const3_title, DOWN).align_to(global_title, LEFT).shift(RIGHT*0.2)
        const31_txt = Text("(except in occluding boundaries)").scale(0.3).next_to(const3_txt, DOWN).align_to(global_title, LEFT).shift(RIGHT*0.2)

        self.play(FadeIn(const1_title,const1_txt,const11_txt), run_time=0.3)
        # self.play(Write(const2_title), Write(const2_txt), Write(const21_txt), run_time=0.3)
        self.play(FadeIn(const3_title,const3_txt,const31_txt), run_time=0.3)

        



class DepthFromDisparity1(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        correspondence_title = Text("The Correspondence Problem").shift(UP*3).scale(0.7)
        self.add(name, source, correspondence_title)

        depth_title = Text("Depth from disparity").shift(UP*3).scale(0.7)
        self.play(ReplacementTransform(correspondence_title, depth_title))


        left_len = Rectangle(color=BLUE).scale(0.7)
        right_len = Rectangle(color=BLUE).next_to(left_len, RIGHT).scale(0.7)
        lens = VGroup(left_len, right_len).center()
        left_len_txt = Text("Left len").scale(0.2).next_to(left_len, UP).align_to(left_len, LEFT)
        right_len_txt = Text("Right len").scale(0.2).next_to(right_len, UP).align_to(right_len, RIGHT)
        self.play(Create(lens), Write(left_len_txt), Write(right_len_txt))

        y_axis = Vector(UP).shift(LEFT*5.5)
        x_axis = Vector().align_to(y_axis, LEFT).shift(RIGHT*0.1)
        z_axis = Vector().align_to(y_axis, LEFT).shift(UP*0.4+LEFT*0.08).rotate(55*DEGREES)
        y_axis_txt = Text("y").scale(0.3).next_to(y_axis, LEFT*0.3)
        x_axis_txt = Text("x").scale(0.3).next_to(x_axis, DOWN*0.3)
        z_axis_txt = Text("z").scale(0.3).next_to(z_axis, RIGHT*0.1)
        self.play(FadeIn(x_axis, y_axis, z_axis, x_axis_txt, y_axis_txt, z_axis_txt))

        left_sens = Dot(radius=0.05, color=GREEN).next_to(left_len, DOWN*1.3)
        right_sens = Dot(radius=0.05, color=GREEN).next_to(right_len, DOWN*1.3)
        o_left = Tex(r"$O_l$").next_to(left_sens, DOWN).scale(0.4)
        o_right = Tex(r"$O_r$").next_to(right_sens, DOWN).scale(0.4)
        sensors_txt = Text("Sensors").scale(0.2).next_to(left_sens, LEFT).align_to(left_len, LEFT)
        self.play(Create(left_sens),Create(right_sens), Write(sensors_txt), Write(o_right), Write(o_left))

        


class DepthFromDisparity2(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        depth_title = Text("Depth from disparity").shift(UP*3).scale(0.7)

        self.add(name, source, depth_title)

        left_len = Rectangle(color=BLUE).scale(0.7)
        right_len = Rectangle(color=BLUE).next_to(left_len, RIGHT).scale(0.7)
        lens = VGroup(left_len, right_len).center()
        left_len_txt = Text("Left len").scale(0.2).next_to(left_len, UP).align_to(left_len, LEFT)
        right_len_txt = Text("Right len").scale(0.2).next_to(right_len, UP).align_to(right_len, RIGHT)
        left_sens = Dot(radius=0.05, color=GREEN).next_to(left_len, DOWN*1.3)
        right_sens = Dot(radius=0.05, color=GREEN).next_to(right_len, DOWN*1.3)
        o_left = Tex(r"$O_l$").next_to(left_sens, DOWN).scale(0.4)
        o_right = Tex(r"$O_r$").next_to(right_sens, DOWN).scale(0.4)
        sensors_txt = Text("Sensors").scale(0.2).next_to(left_sens, LEFT).align_to(left_len, LEFT)
        self.add(lens,left_len_txt,right_len_txt, left_sens,right_sens, o_left,o_right, sensors_txt)

        y_axis = Vector(UP).shift(LEFT*5.5)
        x_axis = Vector().align_to(y_axis, LEFT).shift(RIGHT*0.1)
        z_axis = Vector().align_to(y_axis, LEFT).shift(UP*0.4+LEFT*0.08).rotate(55*DEGREES)
        y_axis_txt = Text("y").scale(0.3).next_to(y_axis, LEFT*0.3)
        x_axis_txt = Text("x").scale(0.3).next_to(x_axis, DOWN*0.3)
        z_axis_txt = Text("z").scale(0.3).next_to(z_axis, RIGHT*0.1)
        self.add(x_axis, y_axis, z_axis, x_axis_txt, y_axis_txt, z_axis_txt)

        target = Dot(radius=0.05, color=RED).move_to((0.5,2,0))

        left_target = Dot(radius=0.05, color=RED).shift(LEFT)
        right_target = Dot(radius=0.05, color=RED).shift(RIGHT*1.34)
        self.play(Create(left_target), Create(right_target),Create(target))

        left_epip = DashedLine(left_len.get_left(), left_len.get_right())
        right_epip = DashedLine(right_len.get_right(), right_len.get_left())
        x_left = Tex(r"$x_l$").next_to(left_target, UP*0.3).shift(LEFT*0.2).scale(0.4)
        x_right = Tex(r"$x_r$").next_to(right_target, UP*0.3).shift(RIGHT*0.2).scale(0.4)
        self.play(Create(left_epip), Create(right_epip), Write(x_left), Write(x_right))
        

class DepthFromDisparity3(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        depth_title = Text("Depth from disparity").shift(UP*3).scale(0.7)

        self.add(name, source, depth_title)

        left_len = Rectangle(color=BLUE).scale(0.7)
        right_len = Rectangle(color=BLUE).next_to(left_len, RIGHT).scale(0.7)
        lens = VGroup(left_len, right_len).center()
        left_len_txt = Text("Left len").scale(0.2).next_to(left_len, UP).align_to(left_len, LEFT)
        right_len_txt = Text("Right len").scale(0.2).next_to(right_len, UP).align_to(right_len, RIGHT)
        left_sens = Dot(radius=0.05, color=GREEN).next_to(left_len, DOWN*1.3)
        right_sens = Dot(radius=0.05, color=GREEN).next_to(right_len, DOWN*1.3)
        o_left = Tex(r"$O_l$").next_to(left_sens, DOWN).scale(0.4)
        o_right = Tex(r"$O_r$").next_to(right_sens, DOWN).scale(0.4)
        sensors_txt = Text("Sensors").scale(0.2).next_to(left_sens, LEFT).align_to(left_len, LEFT)
        self.add(lens,left_len_txt,right_len_txt, left_sens,right_sens, o_left,o_right, sensors_txt)
        
        y_axis = Vector(UP).shift(LEFT*5.5)
        x_axis = Vector().align_to(y_axis, LEFT).shift(RIGHT*0.1)
        z_axis = Vector().align_to(y_axis, LEFT).shift(UP*0.4+LEFT*0.08).rotate(55*DEGREES)
        y_axis_txt = Text("y").scale(0.3).next_to(y_axis, LEFT*0.3)
        x_axis_txt = Text("x").scale(0.3).next_to(x_axis, DOWN*0.3)
        z_axis_txt = Text("z").scale(0.3).next_to(z_axis, RIGHT*0.1)
        self.add(x_axis, y_axis, z_axis, x_axis_txt, y_axis_txt, z_axis_txt)

        target = Dot(radius=0.05, color=RED).move_to((0.5,2,0))
        left_target = Dot(radius=0.05, color=RED).shift(LEFT)
        right_target = Dot(radius=0.05, color=RED).shift(RIGHT*1.34)
        left_epip = DashedLine(left_len.get_left(), left_len.get_right())
        right_epip = DashedLine(right_len.get_right(), right_len.get_left())
        x_left = Tex(r"$x_l$").next_to(left_target, UP*0.3).shift(LEFT*0.2).scale(0.4)
        x_right = Tex(r"$x_r$").next_to(right_target, UP*0.3).shift(RIGHT*0.2).scale(0.4)
        self.add(target, left_target, right_target, left_epip, right_epip, x_left, x_right)

        left_ray = DashedLine(target, left_sens)
        right_ray = DashedLine(target, right_sens)
        self.play(Create(left_ray),Create(right_ray))


class DepthFromDisparity4(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        depth_title = Text("Depth from disparity").shift(UP*3).scale(0.7)

        self.add(name, source, depth_title)

        left_len = Rectangle(color=BLUE).scale(0.7)
        right_len = Rectangle(color=BLUE).next_to(left_len, RIGHT).scale(0.7)
        lens = VGroup(left_len, right_len).center()
        left_len_txt = Text("Left len").scale(0.2).next_to(left_len, UP).align_to(left_len, LEFT)
        right_len_txt = Text("Right len").scale(0.2).next_to(right_len, UP).align_to(right_len, RIGHT)
        left_sens = Dot(radius=0.05, color=GREEN).next_to(left_len, DOWN*1.3)
        right_sens = Dot(radius=0.05, color=GREEN).next_to(right_len, DOWN*1.3)
        o_left = Tex(r"$O_l$").next_to(left_sens, DOWN).scale(0.4)
        o_right = Tex(r"$O_r$").next_to(right_sens, DOWN).scale(0.4)
        sensors_txt = Text("Sensors").scale(0.2).next_to(left_sens, LEFT).align_to(left_len, LEFT)
        self.add(lens,left_len_txt,right_len_txt, left_sens,right_sens, o_left,o_right, sensors_txt)
        
        y_axis = Vector(UP).shift(LEFT*5.5)
        x_axis = Vector().align_to(y_axis, LEFT).shift(RIGHT*0.1)
        z_axis = Vector().align_to(y_axis, LEFT).shift(UP*0.4+LEFT*0.08).rotate(55*DEGREES)
        y_axis_txt = Text("y").scale(0.3).next_to(y_axis, LEFT*0.3)
        x_axis_txt = Text("x").scale(0.3).next_to(x_axis, DOWN*0.3)
        z_axis_txt = Text("z").scale(0.3).next_to(z_axis, RIGHT*0.1)
        self.add(x_axis, y_axis, z_axis, x_axis_txt, y_axis_txt, z_axis_txt)

        target = Dot(radius=0.05, color=RED).move_to((0.5,2,0))
        left_target = Dot(radius=0.05, color=RED).shift(LEFT)
        right_target = Dot(radius=0.05, color=RED).shift(RIGHT*1.34)
        left_epip = DashedLine(left_len.get_left(), left_len.get_right())
        right_epip = DashedLine(right_len.get_right(), right_len.get_left())
        x_left = Tex(r"$x_l$").next_to(left_target, UP*0.3).shift(LEFT*0.2).scale(0.4)
        x_right = Tex(r"$x_r$").next_to(right_target, UP*0.3).shift(RIGHT*0.2).scale(0.4)
        self.add(target, left_target, right_target, left_epip, right_epip, x_left, x_right)

        left_ray = DashedLine(target, left_sens)
        right_ray = DashedLine(target, right_sens)
        self.add(left_ray,right_ray)
        
        foc_length = DashedLine(left_sens, left_epip.get_center())
        f = Tex(r"$f$").next_to(foc_length, LEFT).scale(0.4)


        base_line = DashedLine(left_sens, right_sens)
        T = Tex(r"$T$").next_to(base_line, DOWN).scale(0.4)
        
        marker = Dot(radius=0.01).move_to(target).align_to(base_line, DOWN)
        height = DashedLine(target, marker, color=PURPLE)
        z = Tex(r"$Z$", color=PURPLE).next_to(height, RIGHT*0.5).scale(0.4)
        base_line_epip = DashedLine(left_target, right_target, color=LIGHT_BROWN)

        self.play(Create(base_line_epip),Create(foc_length), Write(f),Create(base_line), Write(T),Create(height), Write(z))

class DepthFromDisparity5(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        depth_title = Text("Depth from disparity").shift(UP*3).scale(0.7)

        self.add(name, source, depth_title)

        left_len = Rectangle(color=BLUE).scale(0.7)
        right_len = Rectangle(color=BLUE).next_to(left_len, RIGHT).scale(0.7)
        lens = VGroup(left_len, right_len).center()
        left_len_txt = Text("Left len").scale(0.2).next_to(left_len, UP).align_to(left_len, LEFT)
        right_len_txt = Text("Right len").scale(0.2).next_to(right_len, UP).align_to(right_len, RIGHT)
        left_sens = Dot(radius=0.05, color=GREEN).next_to(left_len, DOWN*1.3)
        right_sens = Dot(radius=0.05, color=GREEN).next_to(right_len, DOWN*1.3)
        o_left = Tex(r"$O_l$").next_to(left_sens, DOWN).scale(0.4)
        o_right = Tex(r"$O_r$").next_to(right_sens, DOWN).scale(0.4)
        sensors_txt = Text("Sensors").scale(0.2).next_to(left_sens, LEFT).align_to(left_len, LEFT)
        self.add(lens,left_len_txt,right_len_txt, left_sens,right_sens, o_left,o_right, sensors_txt)
        
        y_axis = Vector(UP).shift(LEFT*5.5)
        x_axis = Vector().align_to(y_axis, LEFT).shift(RIGHT*0.1)
        z_axis = Vector().align_to(y_axis, LEFT).shift(UP*0.4+LEFT*0.08).rotate(55*DEGREES)
        y_axis_txt = Text("y").scale(0.3).next_to(y_axis, LEFT*0.3)
        x_axis_txt = Text("x").scale(0.3).next_to(x_axis, DOWN*0.3)
        z_axis_txt = Text("z").scale(0.3).next_to(z_axis, RIGHT*0.1)
        self.add(x_axis, y_axis, z_axis, x_axis_txt, y_axis_txt, z_axis_txt)

        target = Dot(radius=0.05, color=RED).move_to((0.5,2,0))
        left_target = Dot(radius=0.05, color=RED).shift(LEFT)
        right_target = Dot(radius=0.05, color=RED).shift(RIGHT*1.34)
        left_epip = DashedLine(left_len.get_left(), left_len.get_right())
        right_epip = DashedLine(right_len.get_right(), right_len.get_left())
        x_left = Tex(r"$x_l$").next_to(left_target, UP*0.3).shift(LEFT*0.2).scale(0.4)
        x_right = Tex(r"$x_r$").next_to(right_target, UP*0.3).shift(RIGHT*0.2).scale(0.4)
        self.add(target, left_target, right_target, left_epip, right_epip, x_left, x_right)

        left_ray = DashedLine(target, left_sens)
        right_ray = DashedLine(target, right_sens)
        self.add(left_ray,right_ray)
        
        foc_length = DashedLine(left_sens, left_epip.get_center())
        f = Tex(r"$f$").next_to(foc_length, LEFT).scale(0.4)
        base_line = DashedLine(left_sens, right_sens)
        T = Tex(r"$T$").next_to(base_line, DOWN).scale(0.4)
        marker = Dot(radius=0.01).move_to(target).align_to(base_line, DOWN)
        height = DashedLine(target, marker, color=PURPLE)
        z = Tex(r"$Z$", color=PURPLE).next_to(height, RIGHT*0.5).scale(0.4)
        base_line_epip = DashedLine(left_target, right_target, color=LIGHT_BROWN)

        self.add(foc_length, f, base_line, T, height, z, base_line_epip)


        self.play(FadeOut(sensors_txt, o_left, o_right, left_len, right_len, left_len_txt, right_len_txt, left_epip, right_epip), f.animate.shift(RIGHT), foc_length.animate.shift(RIGHT))

        for1 = Tex(r"$\frac{T}{Z} = \frac{T-(x_l-x_r)}{Z-f}  = \frac{T-d}{Z-f}$").scale(0.6).shift(RIGHT*3.5+UP*2)
        for2 = Tex(r"$\longrightarrow ZT-fT = ZT-Zd$").scale(0.5).next_to(for1, DOWN).align_to(for1, LEFT)
        for3 = Tex(r"$\longrightarrow Z = \frac{fT}{d}$").scale(0.5).next_to(for2, DOWN).align_to(for1, LEFT)
        self.play(Write(for1),Write(for2),Write(for3), run_time=0.3)

class DepthMap1(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        depth_title = Text("Depth from disparity").shift(UP*3).scale(0.7)

        self.add(name, source, depth_title)

        
        left_len = Rectangle(color=BLUE).scale(0.7)
        right_len = Rectangle(color=BLUE).next_to(left_len, RIGHT).scale(0.7)
        lens = VGroup(left_len, right_len).center()
        left_len_txt = Text("Left len").scale(0.2).next_to(left_len, UP).align_to(left_len, LEFT)
        right_len_txt = Text("Right len").scale(0.2).next_to(right_len, UP).align_to(right_len, RIGHT)
        left_sens = Dot(radius=0.05, color=GREEN).next_to(left_len, DOWN*1.3)
        right_sens = Dot(radius=0.05, color=GREEN).next_to(right_len, DOWN*1.3)
        o_left = Tex(r"$O_l$").next_to(left_sens, DOWN).scale(0.4)
        o_right = Tex(r"$O_r$").next_to(right_sens, DOWN).scale(0.4)
        sensors_txt = Text("Sensors").scale(0.2).next_to(left_sens, LEFT).align_to(left_len, LEFT)
        self.add(lens,left_len_txt,right_len_txt, left_sens,right_sens, o_left,o_right, sensors_txt)
        
        y_axis = Vector(UP).shift(LEFT*5.5)
        x_axis = Vector().align_to(y_axis, LEFT).shift(RIGHT*0.1)
        z_axis = Vector().align_to(y_axis, LEFT).shift(UP*0.4+LEFT*0.08).rotate(55*DEGREES)
        y_axis_txt = Text("y").scale(0.3).next_to(y_axis, LEFT*0.3)
        x_axis_txt = Text("x").scale(0.3).next_to(x_axis, DOWN*0.3)
        z_axis_txt = Text("z").scale(0.3).next_to(z_axis, RIGHT*0.1)
        self.add(x_axis, y_axis, z_axis, x_axis_txt, y_axis_txt, z_axis_txt)

        target = Dot(radius=0.05, color=RED).move_to((0.5,2,0))
        left_target = Dot(radius=0.05, color=RED).shift(LEFT)
        right_target = Dot(radius=0.05, color=RED).shift(RIGHT*1.34)
        left_epip = DashedLine(left_len.get_left(), left_len.get_right())
        right_epip = DashedLine(right_len.get_right(), right_len.get_left())
        x_left = Tex(r"$x_l$").next_to(left_target, UP*0.3).shift(LEFT*0.2).scale(0.4)
        x_right = Tex(r"$x_r$").next_to(right_target, UP*0.3).shift(RIGHT*0.2).scale(0.4)
        self.add(target, left_target, right_target, left_epip, right_epip, x_left, x_right)

        left_ray = DashedLine(target, left_sens)
        right_ray = DashedLine(target, right_sens)
        self.add(left_ray,right_ray)
        
        foc_length = DashedLine(left_sens, left_epip.get_center()).shift(RIGHT)
        f = Tex(r"$f$").next_to(foc_length, LEFT).scale(0.4).shift(RIGHT)
        base_line = DashedLine(left_sens, right_sens)
        T = Tex(r"$T$").next_to(base_line, DOWN).scale(0.4)
        marker = Dot(radius=0.01).move_to(target).align_to(base_line, DOWN)
        height = DashedLine(target, marker, color=PURPLE)
        z = Tex(r"$Z$", color=PURPLE).next_to(height, RIGHT*0.5).scale(0.4)
        base_line_epip = DashedLine(left_target, right_target, color=LIGHT_BROWN)

        self.add(foc_length, f, base_line, T, height, z, base_line_epip)


        self.remove(sensors_txt, o_left, o_right, left_len, right_len, left_len_txt, right_len_txt, left_epip, right_epip)

        for1 = Tex(r"$\frac{T}{Z} = \frac{T-(x_l-x_r)}{Z-f}  = \frac{T-d}{Z-f}$").scale(0.6).shift(RIGHT*3.5+UP*2)
        for2 = Tex(r"$\longrightarrow ZT-fT = ZT-Zd$").scale(0.5).next_to(for1, DOWN).align_to(for1, LEFT)
        for3 = Tex(r"$\longrightarrow Z = \frac{fT}{d}$").scale(0.5).next_to(for2, DOWN).align_to(for1, LEFT)
        self.add(for1, for2, for3)

        map_title = Text("Depth map").shift(UP*3).scale(0.7)
        self.play(ReplacementTransform(depth_title, map_title), FadeOut(for1, for2, for3, target, left_target, right_target,x_left, x_right, left_sens, right_sens,foc_length, f, base_line, T, height, z, base_line_epip,left_ray,right_ray, x_axis, y_axis, z_axis, x_axis_txt, y_axis_txt, z_axis_txt))

        left_img = ImageMobject("../images/bawlingLeft.png").scale(0.5)
        left_txt = Text("Left Image").scale(0.3).next_to(left_img, UP)
        right_img = ImageMobject("../images/bawlingDisp.png").scale(0.5).next_to(left_img, RIGHT)
        right_txt = Text("Depth Map").scale(0.3).next_to(right_img, UP)
        stereo_pair = Group(left_img, left_txt, right_img, right_txt).center()
        self.play(FadeIn(stereo_pair))

class SNNModel1(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        map_title = Text("Depth map").shift(UP*3).scale(0.7)

        self.add(name, source, map_title)

        left_img = ImageMobject("../images/bawlingLeft.png").scale(0.5)
        left_txt = Text("Left Image").scale(0.3).next_to(left_img, UP)
        right_img = ImageMobject("../images/bawlingDisp.png").scale(0.5).next_to(left_img, RIGHT)
        right_txt = Text("Depth Map").scale(0.3).next_to(right_img, UP)
        stereo_pair = Group(left_img, left_txt, right_img, right_txt).center()
        self.add(stereo_pair)
        model_title = Text("The spiking stereo neural network model").shift(UP*3).scale(0.65)
        self.play(ReplacementTransform(map_title, model_title), FadeOut(stereo_pair))
        coor_img = ImageMobject("../images/coordinate1.png").scale(1.3).center()
        coordinate_title = Text("The coordinate system of the network:", color=BLUE).next_to(model_title, DOWN).scale(0.4)
        x_def = Tex(r"$x = x_R+x_L$").next_to(coor_img, LEFT).scale(0.5)
        d_def = Tex(r"$d = x_R-x_L$").next_to(x_def, DOWN).scale(0.5)
        self.play(FadeIn(coordinate_title, coor_img, x_def, d_def))

class SNNModel2(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("The spiking stereo neural network model").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        coor_img = ImageMobject("../images/coordinate1.png").scale(1.3).center()
        coordinate_title = Text("The coordinate system of the network:", color=BLUE).next_to(model_title, DOWN).scale(0.4)
        x_def = Tex(r"$x = x_R+x_L$").next_to(coor_img, LEFT).scale(0.5)
        d_def = Tex(r"$d = x_R-x_L$").next_to(x_def, DOWN).scale(0.5)
        self.add(coordinate_title, coor_img, x_def, d_def)

        m_1 = Tex(r"$\mathbb{M}:\hspace{1.5cm} \mathbb{N}^3\hspace{0.5cm} \longrightarrow \hspace{0.5cm}\mathbb{D}^3$").next_to(coor_img, RIGHT).scale(0.4).shift(LEFT*1.4)
        m_2 = Tex(r"$(\Bar{x}_L,\Bar{x}_R,\Bar{y})\longrightarrow(x,y,d)=(\Bar{x}_R+\Bar{x}_L,\Bar{y},\Bar{x}_R-\Bar{x}_L)$").next_to(m_1, DOWN).scale(0.4)
        
        self.play(FadeIn(m_1, m_2))

class SNNModel3(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("The spiking stereo neural network model").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        abstract_title = Text("Abstract view of the network’s architecture", color=BLUE).next_to(model_title, DOWN).scale(0.4)
        abstract_img = ImageMobject("../images/high.png").scale(0.7)
        self.play(FadeIn(abstract_title, abstract_img))

class SNNModel4(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("The spiking stereo neural network model").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        secondary_title = Text("Detailed view of a horizontal layer of the network", color=BLUE).next_to(model_title, DOWN).scale(0.4)
        secondary_img = ImageMobject("../images/low.png").scale(0.7)
        self.play(FadeIn(secondary_title, secondary_img))

class SNNModel5(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("The spiking stereo neural network model").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        secondary_title = Text("Simple Coincidence Detectors", color=BLUE).next_to(model_title, DOWN).scale(0.4)
        secondary_img = ImageMobject("../images/low.png").scale(0.7)
        rect = Rectangle(color=BLUE, width=3.5, height=3).shift(LEFT*0.5)
        self.add(secondary_title, secondary_img)
        self.play(FadeIn(rect))

class SNNModel6(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("The spiking stereo neural network model").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        secondary_title = Text("Simple Coincidence Detectors", color=BLUE).next_to(model_title, DOWN).scale(0.4)
        secondary_img = ImageMobject("../images/leaky.tif").scale(0.4)
        secondary_img_title = Text("Leaky Integrate and fire neuron model").next_to(secondary_img, DOWN).scale(0.3)

        
        leaky_formula0 = Tex(r"$\tau_c\frac{dv_c(t)}{dt} = -v_c(t)+I_c(t),\hspace{0.5cm}  v_c(t)<\theta_c$").scale(0.4).shift(LEFT*5+UP*0.5)
        leaky_formula1 = Tex(r"$v_c(t)=0,\hspace{1cm}  v_c(t)\geq\theta_c$").scale(0.4).next_to(leaky_formula0, DOWN)
        self.play(FadeIn(secondary_title, secondary_img,secondary_img_title, leaky_formula0, leaky_formula1))

class SNNModel7(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("The spiking stereo neural network model").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        secondary_title = Text("Simple Coincidence Detectors", color=BLUE).next_to(model_title, DOWN).scale(0.4)
        secondary_img = ImageMobject("../images/leaky.tif").scale(0.4)
        secondary_img_title = Text("Leaky Integrate and fire neuron model").next_to(secondary_img, DOWN).scale(0.3)

        
        leaky_formula0 = Tex(r"$\tau_c\frac{dv_c(t)}{dt} = -v_c(t)+I_c(t),\hspace{0.5cm}  v_c(t)<\theta_c$").scale(0.4).shift(LEFT*5+UP*0.5)
        leaky_formula1 = Tex(r"$v_c(t)=0,\hspace{1cm}  v_c(t)\geq\theta_c$").scale(0.4).next_to(leaky_formula0, DOWN)
        self.add(secondary_title, secondary_img,secondary_img_title, leaky_formula0, leaky_formula1)

        spikes_formula = Tex(r"$I_c(t) = w\sum_i\delta_{\Bar{x}_L}(t-t_i)+ w\sum_j\delta_{\Bar{x}_R}(t-t_j)$").scale(0.4).next_to(secondary_img,RIGHT).shift(UP*0.5)
        self.play(FadeIn(spikes_formula))

class SNNModel8(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("The spiking stereo neural network model").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        secondary_title = Text("Simple Coincidence Detectors", color=BLUE).next_to(model_title, DOWN).scale(0.4)
        secondary_img = ImageMobject("../images/leaky.tif").scale(0.4)
        secondary_img_title = Text("Leaky Integrate and fire neuron model").next_to(secondary_img, DOWN).scale(0.3)

        
        leaky_formula0 = Tex(r"$\tau_c\frac{dv_c(t)}{dt} = -v_c(t)+I_c(t),\hspace{0.5cm}  v_c(t)<\theta_c$").scale(0.4).shift(LEFT*5+UP*0.5)
        leaky_formula1 = Tex(r"$v_c(t)=0,\hspace{1cm}  v_c(t)\geq\theta_c$").scale(0.4).next_to(leaky_formula0, DOWN)
        self.add(secondary_title, secondary_img,secondary_img_title, leaky_formula0, leaky_formula1)

        spikes_formula = Tex(r"$I_c(t) = w\sum_i\delta_{\Bar{x}_L}(t-t_i)+ w\sum_j\delta_{\Bar{x}_R}(t-t_j)$").scale(0.4).next_to(secondary_img,RIGHT).shift(UP*0.5)
        self.add(spikes_formula)

        delta_formula = Tex(r"$S_{\Delta T} = \tau_c\ln(\frac{1}{\frac{\theta_c}{w}-1}) \hspace{0.25cm}, \hspace{1cm}1<\frac{\theta_c}{w}\leq2 $").scale(0.4).next_to(spikes_formula,DOWN)
        
        self.play(FadeIn(delta_formula))

class SNNModel9(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("The spiking stereo neural network model").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        secondary_title = Text("Complex disparity detectors", color=BLUE).next_to(model_title, DOWN).scale(0.4)
        secondary_img = ImageMobject("../images/low.png").scale(0.7)
        rect = Rectangle(color=BLUE, width=3.5, height=3).shift(LEFT*0.5)
        self.add(secondary_title, secondary_img, rect)
        self.play(rect.animate.shift(RIGHT*3))

class SNNModel10(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("The spiking stereo neural network model").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        secondary_title = Text("Complex disparity detectors", color=BLUE).next_to(model_title, DOWN).scale(0.4)
        secondary_img = ImageMobject("../images/low_cut.png").scale(0.7).shift(LEFT*0.5)
        leaky_formula0 = Tex(r"$\tau_d\frac{dv_d(t)}{dt} = -v_d(t)+I_d(t),\hspace{0.5cm}  v_d(t)<\theta_d$").scale(0.4).shift(LEFT*5+UP*0.5)
        leaky_formula1 = Tex(r"$v_d(t)=0,\hspace{1cm}  v_d(t)\geq\theta_d$").scale(0.4).next_to(leaky_formula0, DOWN)
        self.play(FadeIn(secondary_title, secondary_img,leaky_formula0, leaky_formula1))

class SNNModel11(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("The spiking stereo neural network model").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        secondary_title = Text("Complex disparity detectors", color=BLUE).next_to(model_title, DOWN).scale(0.4)
        secondary_img = ImageMobject("../images/low_cut.png").scale(0.7).shift(LEFT*0.5)
        leaky_formula0 = Tex(r"$\tau_d\frac{dv_d(t)}{dt} = -v_d(t)+I_d(t),\hspace{0.5cm}  v_d(t)<\theta_d$").scale(0.4).shift(LEFT*5+UP*0.5)
        leaky_formula1 = Tex(r"$v_d(t)=0,\hspace{1cm}  v_d(t)\geq\theta_d$").scale(0.4).next_to(leaky_formula0, DOWN)
        self.add(secondary_title, secondary_img,leaky_formula0, leaky_formula1)
        
        spikes_formula = Tex(r"$I_c(t) = w_{exc}\sum_{c\in C^+}\sum_k\delta_c(t-t_k) - w_{inh}\sum_{c\in C^-}\sum_k\delta_c(t-t_k)$").scale(0.33).next_to(secondary_img,RIGHT).shift(UP*0.5)
        self.play(FadeIn(spikes_formula))

        c_plus_formula = Tex(r"$C^+ = \{c\in C|(|x_c-x_d|\leq w)\land (|y_c-y_d|\leq w)\land(d_c =d_d)$").scale(0.33).next_to(spikes_formula,DOWN).shift(DOWN*0.3)
        c_minus_formula = Tex(r"$C^- = \{c\in C|(x_c = x_d)\land (|y_c-y_d|\leq w)\land(|d_c-d_d|\leq w)$").scale(0.33).next_to(c_plus_formula,DOWN)
        
        self.play(FadeIn(c_plus_formula, c_minus_formula))

class SNNModel12(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("The spiking stereo neural network model").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        secondary_title = Text("Mutual inhibition of disparity detectors", color=BLUE).next_to(model_title, DOWN).scale(0.4)
        secondary_img = ImageMobject("../images/low_disp.png").scale(0.9)
        leaky_formula0 = Tex(r"$\tau_d\frac{dv_d(t)}{dt} = -v_d(t)+I_d(t),\hspace{0.5cm}  v_d(t)<\theta_d$").scale(0.4).shift(LEFT*5+UP*0.5)
        leaky_formula1 = Tex(r"$v_d(t)=0,\hspace{1cm}  v_d(t)\geq\theta_d$").scale(0.4).next_to(leaky_formula0, DOWN)
        self.play(FadeIn(secondary_title, secondary_img,leaky_formula0, leaky_formula1))


class SNNModel13(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("The spiking stereo neural network model").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        secondary_title = Text("Mutual inhibition of disparity detectors", color=BLUE).next_to(model_title, DOWN).scale(0.4)
        secondary_img = ImageMobject("../images/low_disp.png").scale(0.9)
        leaky_formula0 = Tex(r"$\tau_d\frac{dv_d(t)}{dt} = -v_d(t)+I_d(t),\hspace{0.5cm}  v_d(t)<\theta_d$").scale(0.4).shift(LEFT*5+UP*0.5)
        leaky_formula1 = Tex(r"$v_d(t)=0,\hspace{1cm}  v_d(t)\geq\theta_d$").scale(0.4).next_to(leaky_formula0, DOWN)
        self.add(secondary_title, secondary_img,leaky_formula0, leaky_formula1)

        leaky_formula0_updated = Tex(r"$\tau_d\frac{dv_d(t)}{dt} = -v_d(t)+I_d(t)-I_{d-}(t),\hspace{0.5cm}  v_d(t)<\theta_d$").scale(0.4).shift(LEFT*4.5+UP*0.5)
        leaky_formula1_updated = Tex(r"$v_d(t)=0,\hspace{0.5cm}  v_d(t)\geq\theta_d \lor v_d(t) < 0$").scale(0.4).next_to(leaky_formula0_updated, DOWN)
        self.play(ReplacementTransform(leaky_formula0, leaky_formula0_updated), ReplacementTransform(leaky_formula1, leaky_formula1_updated))

class SNNModel14(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("The spiking stereo neural network model").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        secondary_title = Text("Mutual inhibition of disparity detectors", color=BLUE).next_to(model_title, DOWN).scale(0.4)
        secondary_img = ImageMobject("../images/low_disp.png").scale(0.9)
        self.add(secondary_title, secondary_img)

        leaky_formula0_updated = Tex(r"$\tau_d\frac{dv_d(t)}{dt} = -v_d(t)+I_d(t)-I_{d-}(t),\hspace{0.5cm}  v_d(t)<\theta_d$").scale(0.4).shift(LEFT*4.5+UP*0.5)
        leaky_formula1_updated = Tex(r"$v_d(t)=0,\hspace{0.5cm}  v_d(t)\geq\theta_d \lor v_d(t) < 0$").scale(0.4).next_to(leaky_formula0_updated, DOWN)
        self.add(leaky_formula0_updated, leaky_formula1_updated)

        i_d = Tex(r"$I_{d-}(t) = w_{rec}\sum_{d\in D^-}\sum_n\delta_d(t-t_n)$").scale(0.4).next_to(secondary_img,RIGHT).shift(UP*0.5)
        d_minus = Tex(r"$D^- = \{d \in D|(x_d-d_d = 2\Bar{x}_L)\lor (x_d+d_d = 2\Bar{x}_R)$").scale(0.4).next_to(i_d,DOWN).align_to(i_d, LEFT)

        self.play(FadeIn(i_d, d_minus))

class SNNModel15(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("The spiking stereo neural network model").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        secondary_title = Text("Representation and coding of disparity - The Output", color=BLUE).next_to(model_title, DOWN).scale(0.4)
        self.add(secondary_title)

        event_d = Tex(r"$e^+_d = (\textbf{d},t)$").scale(0.45).shift(LEFT*4.5+UP)
        event_d_txt = Text("- a unipolar disparity event that occurred at time t, at location d, in").scale(0.35).next_to(event_d, RIGHT)
        d3 = Tex(r"$\mathbb{D}^3$").scale(0.45).next_to(event_d_txt, RIGHT)

        
        
        self.play(FadeIn(event_d, event_d_txt, d3))

class SNNModel16(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("The spiking stereo neural network model").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        secondary_title = Text("Representation and coding of disparity - The Output", color=BLUE).next_to(model_title, DOWN).scale(0.4)
        self.add(secondary_title)

        event_d = Tex(r"$e^+_d = (\textbf{d},t)$").scale(0.45).shift(LEFT*4.5+UP)
        event_d_txt = Text("- a unipolar disparity event that occurred at time t, at location d, in").scale(0.35).next_to(event_d, RIGHT)
        d3 = Tex(r"$\mathbb{D}^3$").scale(0.45).next_to(event_d_txt, RIGHT)

        event_c = Tex(r"$e^+_c = (\textbf{c},t)$").scale(0.45).next_to(event_d, DOWN).align_to(event_d, LEFT).shift(DOWN*0.3)
        event_c_txt = Text("- a unipolar disparity event that occurred at time t, at location c, in").scale(0.35).next_to(event_c, RIGHT)
        c3 = Tex(r"$\mathbb{C}^3$").scale(0.45).next_to(event_c_txt, RIGHT)
        
        self.add(event_d, event_d_txt, d3)

        self.play(FadeIn(event_c, event_c_txt, c3))

class SNNModel17(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("The spiking stereo neural network model").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        secondary_title = Text("Representation and coding of disparity - The Output", color=BLUE).next_to(model_title, DOWN).scale(0.4)
        self.add(secondary_title)

        event_d = Tex(r"$e^+_d = (\textbf{d},t)$").scale(0.45).shift(LEFT*4.5+UP)
        event_d_txt = Text("- a unipolar disparity event that occurred at time t, at location d, in").scale(0.35).next_to(event_d, RIGHT)
        d3 = Tex(r"$\mathbb{D}^3$").scale(0.45).next_to(event_d_txt, RIGHT)

        event_c = Tex(r"$e^+_c = (\textbf{c},t)$").scale(0.45).next_to(event_d, DOWN).align_to(event_d, LEFT).shift(DOWN*0.3)
        event_c_txt = Text("- a unipolar disparity event that occurred at time t, at location c, in").scale(0.35).next_to(event_c, RIGHT)
        c3 = Tex(r"$\mathbb{C}^3$").scale(0.45).next_to(event_c_txt, RIGHT)
        
        self.add(event_d, event_d_txt, d3, event_c, event_c_txt, c3)

        c_plus = Tex(r"$C^+ = \{e^+_c\}$").scale(0.45).next_to(event_c, DOWN)
        d_plus = Tex(r"$D^+ = \{e^+_d\}$").scale(0.45).next_to(c_plus, RIGHT)
        sets = VGroup(c_plus, d_plus).center().shift(DOWN*0.5)
        cap = Tex(r"$O^+ = C^+\cap D^+$").scale(0.45).next_to(sets, DOWN)

        self.play(FadeIn(c_plus, d_plus, cap))

class SNNModel18(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("The spiking stereo neural network model").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        secondary_title = Text("Representation and coding of disparity - The Output", color=BLUE).next_to(model_title, DOWN).scale(0.4)
        self.add(secondary_title)

        event_d = Tex(r"$e^+_d = (\textbf{d},t)$").scale(0.45).shift(LEFT*4.5+UP)
        event_d_txt = Text("- a unipolar disparity event that occurred at time t, at location d, in").scale(0.35).next_to(event_d, RIGHT)
        d3 = Tex(r"$\mathbb{D}^3$").scale(0.45).next_to(event_d_txt, RIGHT)

        event_c = Tex(r"$e^+_c = (\textbf{c},t)$").scale(0.45).next_to(event_d, DOWN).align_to(event_d, LEFT).shift(DOWN*0.3)
        event_c_txt = Text("- a unipolar disparity event that occurred at time t, at location c, in").scale(0.35).next_to(event_c, RIGHT)
        c3 = Tex(r"$\mathbb{C}^3$").scale(0.45).next_to(event_c_txt, RIGHT)
        

        c_plus = Tex(r"$C^+ = \{e^+_c\}$").scale(0.45).next_to(event_c, DOWN)
        d_plus = Tex(r"$D^+ = \{e^+_d\}$").scale(0.45).next_to(c_plus, RIGHT)
        sets = VGroup(c_plus, d_plus).center().shift(DOWN*0.5)
        cap = Tex(r"$O^+ = C^+\cap D^+$").scale(0.45).next_to(sets, DOWN)
        self.add(event_d, event_d_txt, d3, event_c, event_c_txt, c3, c_plus, d_plus, cap)

        e_c = Tex(r"$e_c = (\textbf{c},s,t), \hspace{0.25cm} s \in [\text{-}1,1]$").scale(0.45).next_to(cap, DOWN)
        o_final = Tex(r"$O =\{e_c \in C | [e_c]^+ \in D^+\}$").scale(0.45).next_to(e_c, DOWN)
        self.play(FadeIn(e_c, o_final))


class Results1(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("Results and model evaluation").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        secondary_title = Text("Ground Truth using the Microsoft Kinnect", color=BLUE).next_to(model_title, DOWN).scale(0.4)
        secondary_img = ImageMobject("../images/kinect.jpeg").scale(1.2)
        self.play(FadeIn(secondary_title, secondary_img))

class Results2(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("Results and model evaluation").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        
        secondary_title = Text("Network simulation", color=BLUE).next_to(model_title, DOWN).scale(0.4)

        bul0 = Text("Input source from 2 DVS cameras with 180X180 pixels resolution.").scale(0.3).shift(LEFT*1.2 + UP)
        bul1 = Text("The SNN model incorporated a total of more than 4 million neurons.").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("Simulation run time of about 30 seconds on a single core of an i7 CPU running at 3.40 GHz.").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)
        bul3 = Text("3 different scenes were tested.").scale(0.3).next_to(bul2, DOWN).align_to(bul2, LEFT)
        bul4 = Text("The disparity was limited to the range (0, 40)").scale(0.3).next_to(bul3, DOWN).align_to(bul3, LEFT)
        bul5 = Text("In the 4 seconds walking scene, roughly 1.2 million input events were processed.").scale(0.3).next_to(bul4, DOWN).align_to(bul4, LEFT)

        bullets = Group(bul0,bul1,bul2,bul3,bul4,bul5)

        self.play(FadeIn(secondary_title, bullets))

class Results3(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("Results and model evaluation").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        
        secondary_title = Text('Qualitative and quantitative results of the "Moving Face" scene', color=BLUE).next_to(model_title, DOWN).scale(0.4)
        secondary_img = ImageMobject("../images/head.png").scale(0.75).shift(DOWN*0.5)
        self.play(FadeIn(secondary_title, secondary_img))


class Results4(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("Results and model evaluation").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        
        secondary_title = Text('Qualitative and quantitative results of the "People" scene', color=BLUE).next_to(model_title, DOWN).scale(0.4)
        secondary_img = ImageMobject("../images/walk.png").scale(0.75).shift(DOWN*0.5)
        self.play(FadeIn(secondary_title, secondary_img))


class Results5(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("Results and model evaluation").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        
        secondary_title = Text('Qualitative and quantitative results of the "Martial Arts" scene', color=BLUE).next_to(model_title, DOWN).scale(0.4)
        secondary_img = ImageMobject("../images/arts.png").scale(0.75).shift(DOWN*0.5)
        self.play(FadeIn(secondary_title, secondary_img))


class Results6(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("Results and model evaluation").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        
        secondary_title = Text('Summary of Results', color=BLUE).next_to(model_title, DOWN).scale(0.4).shift(UP*0.2)
        secondary_img = ImageMobject("../images/hist.png").scale(0.8).shift(UP*0.4)
        thirdary_img = ImageMobject("../images/summary.png").scale(1).shift(DOWN*2.2)
        self.play(FadeIn(secondary_title, secondary_img, thirdary_img) )


class Results7(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("Results and model evaluation").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        
        secondary_title = Text('Response to dynamic random dot stereograms', color=BLUE).next_to(model_title, DOWN).scale(0.4)
        secondary_img = ImageMobject("../images/rds.png").scale(1).shift(UP*0.4)
        self.play(FadeIn(secondary_title, secondary_img) )


class Results8(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("Results and model evaluation").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        
        secondary_title = Text('Response to dynamic random dot stereograms', color=BLUE).next_to(model_title, DOWN).scale(0.4)
        secondary_img = ImageMobject("../images/cube.png").scale(1)
        thirdary_img = ImageMobject("../images/cuberes.png").scale(1).next_to(secondary_img, RIGHT)
        grp = Group(secondary_img, thirdary_img).center()
        self.add(secondary_title)
        self.play(FadeIn(grp) )


class Results9(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("Results and model evaluation").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        
        secondary_title = Text("Neuromorphic hardware implementation", color=BLUE).next_to(model_title, DOWN).scale(0.4)

        bul0 = Text("The Disparity detecetion was implemented on the Reconfigurable On-Line Learning Spiking (ROLLS) neuromorphic processor.").scale(0.3).shift(1.5*UP)
        bul1 = Text("The Coincidence detecetion was implemented on a Field Programmable Gate Array (FPGA) device. ").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("An RDS stimulus was printed on a chart and moved across multiple depths.").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)
        bul3 = Text("The stimulus was presented at equally spaced disparities ranging from -10 to 10.").scale(0.3).next_to(bul2, DOWN).align_to(bul2, LEFT)
        
        bullets = Group(bul0,bul1,bul2,bul3)
        secondary_img = ImageMobject("../images/neuro.png").scale(0.7)
        thirdary_img = ImageMobject("../images/neuro2.png").scale(0.9).next_to(secondary_img, RIGHT)
        grp = Group(secondary_img, thirdary_img).center().shift(DOWN*1.5)
        self.play(FadeIn(grp, secondary_title, bullets))


class Results10(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("Results and model evaluation").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        
        secondary_title = Text("Comparing stereo correspondence performance of traditional and neuromorphic hardware", color=BLUE).next_to(model_title, DOWN).scale(0.4)

        bul0 = Text("The Disparity detecetion was implemented on the Reconfigurable On-Line Learning Spiking (ROLLS) neuromorphic processor.").scale(0.3).shift(1.5*UP)
        bul1 = Text("The Coincidence detecetion was implemented on a Field Programmable Gate Array (FPGA) device. ").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("An RDS stimulus was printed on a chart and moved across multiple depths.").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)
        bul3 = Text("The stimulus was presented at equally spaced disparities ranging from -10 to 10.").scale(0.3).next_to(bul2, DOWN).align_to(bul2, LEFT)
        
        bullets = Group(bul0,bul1,bul2,bul3)
        secondary_img = ImageMobject("../images/neuro.png").scale(0.7)
        thirdary_img = ImageMobject("../images/neuro2.png").scale(0.9).next_to(secondary_img, RIGHT)
        grp = Group(secondary_img, thirdary_img).center().shift(DOWN*1.5)
        self.play(FadeIn(grp, secondary_title, bullets))

class Results10(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("Results and model evaluation").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        
        secondary_title = Text("Comparing stereo correspondence performance of traditional and neuromorphic hardware", color=BLUE).next_to(model_title, DOWN).scale(0.4)

        bul0 = Text("A SAD based stereo correspondenc algorithm implemented on a low power microcontroller.").scale(0.3).shift(1.5*UP+0.8*LEFT)
        bul1 = Text("The number of SAD operations grows with the the camera frame-rate.").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("In SNN model, the equivalent operational primitive is a coincidence detection followed by a spike integration.").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)
        bul3 = Text("The rate of these operations depends on the response of the DVS to the contents of the scene.").scale(0.3).next_to(bul2, DOWN).align_to(bul2, LEFT)
        bul4 = Text("In the RDS scene the operation rate was calculated as 151 Hz.").scale(0.3).next_to(bul3, DOWN).align_to(bul3, LEFT)

        bullets = Group(bul0,bul1,bul2,bul3,bul4)

        secondary_img = ImageMobject("../images/compare.png").scale(0.7).shift(DOWN*1.5)
        self.play(FadeIn(secondary_img, secondary_title, bullets))


class Summary1(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Osswald et al. A spiking neural network model of 3D perception for event-based neuromorphic stereo vision systems (2017).", font_size=11).shift(3.2*DOWN+2*RIGHT)
        model_title = Text("Summary").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        
        secondary_title = Text("The researchers succeeded in:", color=BLUE).next_to(model_title, DOWN).scale(0.4)

        bul0 = Text("Use stereo event camera spikes as input to the SNN model.").scale(0.3).shift(1.5*UP+2*LEFT)
        bul1 = Text("Implement the SNN model and solve the correspondence problem for multiple scenes and with high PCM.").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("Implement the SNN model on a neuromorphic hardware").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)
        bul3 = Text("Compare power consumption on the neuromorphic hardware Vs. a traditional one.").scale(0.3).next_to(bul2, DOWN).align_to(bul2, LEFT)

        bullets = Group(bul0,bul1,bul2,bul3)

        self.play(FadeIn(secondary_title, bullets))
