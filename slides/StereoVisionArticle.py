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
        self.play(Write(correspondence_title))
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
        self.wait()
        self.play(Write(line_r), run_time=0.5)

        line_l = DashedLine((-5,1,0), (-0.2, 1,0), color=BLUE)
        line_r = DashedLine((0.2,1,0), (5, 1,0), color=BLUE)
        self.play(Write(line_l), run_time=0.5)
        self.wait()
        self.play(Write(line_r), run_time=0.5)

        line_l = DashedLine((-5,-1,0), (-0.2, -1,0), color=BLACK)
        line_r = DashedLine((0.2,-1,0), (5, -1,0), color=BLACK)
        self.play(Write(line_l), run_time=0.5)
        self.wait()
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

        sad_img = ImageMobject("../images/sad.png").scale(0.6).shift(UP*2.1)
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
        
        sad_img = ImageMobject("../images/sad.png").scale(0.6).shift(UP*2.1)
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
        
        sad_img = ImageMobject("../images/sad.png").scale(0.6).shift(UP*2.1)
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
        
        sad_img = ImageMobject("../images/sad.png").scale(0.6).shift(UP*2.1)
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

        self.wait(5)
        disp = Tex(r"$disparity(0,6) = x_l - x_r = 6 - 4 = 2$").scale(0.6).shift(DOWN)
        self.play(Write(disp), run_time=2)

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

        triangle_1 = Triangle(color=WHITE).scale(2)
        triangle_2 = Triangle(color=RED).scale(1.8)

