from numpy import number
from manim_slide import *
import cv2
import math
import random


class Header():
    def get(self):
        ou_img = ImageMobject('../images/ou_logo_full_inverted.jpeg').scale(0.4).shift(3*UP+6.3*LEFT)
        nbel_img = ImageMobject('../images/nbel.png').scale(0.18).shift(3*UP+5.8*RIGHT)
        return [ou_img, nbel_img]



class StereoVision(SlideScene):
    def construct(self):
        note = "So the first topic that I would present today is neuromorphic stereo vision. And I would like to start with the definition\
            of stereo vision. So Stereo-vision refers to the method of recovering depth information from both eyes, or in the artificial \
                context, machine stereo vision, also referred to as stereoscopic vision, extracts the data from two visual sensors.\
                    It happends that the past 60 years of research have been devoted to frame based cameras whereas the article that i am introducing to\
                        you today uses a relatively new approach based of bio inspired event stereo camera. Some of you migh ask yourselves - \
                            what is an event camera and what is the difference between an event based to frame based camera?"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        self.add(name)
        
        neuro_title = Text("Neuromorphic Stereo vision").scale(0.7)
        pid = Text("Neuromorphic Robot PID controller").scale(0.7).next_to(neuro_title, DOWN)
        self.add(neuro_title)
        self.play(FadeOut(pid), run_time=1.5)
        self.wait(2)

        title = Text("Stereo Vision").shift(UP*3).scale(0.7)
        self.play(ReplacementTransform(neuro_title, title), run_time=1)
       
        zed = ImageMobject('../images/zed.jpg').shift(2.2*RIGHT+0.7*UP).scale(0.7)
        ec = ImageMobject('../images/stereo_event.png').shift(2.2*LEFT)
        neuro = Text("Event Stereo Camera").scale(0.7).next_to(ec, DOWN)
        classic = Text("Frame based Stereo Camera").scale(0.7).next_to(zed, UP)

        depth = ImageMobject("../images/depth-perception.jpg").scale(1.3)
        definition = Text("Stereo-vision refers to the method of recovering depth information from both eyes.").scale(0.3).next_to(depth, DOWN)
        self.play(FadeIn(depth, definition))
        self.wait(8)
        self.play(FadeOut(depth, definition))
        self.wait(1)
        machine_title = Text("Machine Stereo Vision").shift(UP*3).scale(0.7)
        self.play(ReplacementTransform(title, machine_title))
        self.wait(0.5)
        self.play(FadeIn(zed,classic), run_time=2)
        self.wait(1.5)
        self.play(FadeIn(ec, neuro), run_time=2)



class WhatIsEventCameraPart1(SlideScene):
    def construct(self):
        note = "Known frame based camera algorithms of computer vision suffer from issues like high latency due to redundant data analysis\
            , motion blur which depends on the exposure time of the camera and low dynamic range which causes issues for example when there a strong light source in the camara's field of view.\
            but as we shall see, event cameras provide solutions to these problems."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("http://rpg.ifi.uzh.ch/docs/EventVisionSurvey.pdf", font_size=11).shift(3.2*DOWN+3*RIGHT)
        self.add(name, source)
        machine_title = Text("Machine Stereo Vision").shift(UP*3).scale(0.7)
        self.add(machine_title)
        title_camera = Text("What is an Event camera").shift(UP*3).scale(0.7)
        self.play(ReplacementTransform(machine_title,title_camera))
        self.wait(1)
        frame_img = ImageMobject('../images/framebased.png').scale(0.8)
        frame_txt = Text("Framed base image data").scale(0.3).next_to(frame_img, DOWN)
        grp1 = Group(frame_img, frame_txt)
        self.play(FadeIn(grp1))
        frame_img_c = ImageMobject('../images/framebased.png').scale(0.8).shift(1*DOWN)
        frame_txt_c = Text("Framed base image data").scale(0.3).next_to(frame_img_c, DOWN)
        grp2 = Group(frame_img_c, frame_txt_c)
        self.play(ReplacementTransform(grp1, grp2), run_time=2)

        high_txt = Text("High Latency").scale(0.3).shift(3.3*LEFT+0.7*UP)
        self.play(Write(high_txt))
        self.wait(3)
        blur_txt = Text("Motion Blur").scale(0.3).shift(0.3*LEFT+0.7*UP)
        self.play(Write(blur_txt))
        self.wait(1.5)
        dnr_txt = Text("Low Dynamic Range").scale(0.3).shift(3*RIGHT+0.7*UP)
        self.play(Write(dnr_txt))


class WhatIsEventCameraPart2(SlideScene):
    def construct(self):
        note = "Event camears were first commercialized in 2008 by Toby Delbruck from the university of Zurich\
             under the name of DVS which stands for Dynamic Vision Sensor.\
                 The sensor measures only motion in the scene. An event camera has smart pixels that are all\
                     independent of each other - every time that a single pixel detects motion, that pixel trigers an event."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("http://rpg.ifi.uzh.ch/docs/EventVisionSurvey.pdf", font_size=11).shift(3.2*DOWN+3*RIGHT)
        self.add(name, source)
        title_camera = Text("What is an Event camera").shift(UP*3).scale(0.7)
        self.add(title_camera)

        frame_img = ImageMobject('../images/framebased.png').scale(0.8).shift(1*DOWN)
        frame_txt = Text("Framed base image data").scale(0.3).next_to(frame_img, DOWN)
        high_txt = Text("High Latency").scale(0.3).shift(3.3*LEFT+0.7*UP)
        blur_txt = Text("Motion Blur").scale(0.3).shift(0.3*LEFT+0.7*UP)    
        dnr_txt = Text("Low Dynamic Range").scale(0.3).shift(3*RIGHT+0.7*UP)
        self.add(frame_txt,frame_img,high_txt,blur_txt,dnr_txt)
        self.play(FadeOut(frame_txt,frame_img,high_txt,blur_txt,dnr_txt), run_time=2)

        bul0 = Text("First commercialized in 2008 by Toby Delbruck(UZH&ETH under the name of Dynamic Vision Sensor (DVS).)").scale(0.3).shift(LEFT*1.2 + 2*UP)
        bul1 = Text("Novel sensor that measures the motion in the scene.").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("Ultra low power consumption (1 mW instead of 1W in standard ccd camera).").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)
        bul3 = Text("High dynamic range (140 dB instead of 80 dB in a standard ccd camera).").scale(0.3).next_to(bul2, DOWN).align_to(bul2, LEFT)
        bul4 = Text("Low latency (~1 ms)").scale(0.3).next_to(bul3, DOWN).align_to(bul3, LEFT)
        bul5 = Text("No motion blur").scale(0.3).next_to(bul4, DOWN).align_to(bul4, LEFT)
       
        self.play(Write(bul0), run_time = 0.75)
        self.play(Write(bul1), run_time = 0.75)
        self.play(Write(bul2), run_time = 0.75)
        self.play(Write(bul3), run_time = 0.75)
        self.play(Write(bul4), run_time = 0.75)
        self.play(Write(bul5), run_time = 0.75)




class WhatIsEventCameraPart3(SlideScene):
    def construct(self):
        note = "The animation on the bottom right of the screen from Davide Scaramuzza at the Robotics and perception group\
             in the University of Zurich, compares the outputs of an event camera with a frame camera.\
                    A rotating disk with a black circle is captured by the two camera types.\
                        On top you can see the output of a standard camera which are intensity frames at a constant time interval,\
                            while on the bottom you see the output of an event camera, which relates only to the moving black circlt and represented as a spiral of events in space and time \
                                where the red and blue colors represent the polarity of the event."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("http://rpg.ifi.uzh.ch/docs/EventVisionSurvey.pdf", font_size=11).shift(3.2*DOWN+3*RIGHT)
        self.add(name, source)
        title_camera = Text("What is an Event camera").shift(UP*3).scale(0.7)
        self.add(title_camera)

        dvs_img = ImageMobject('../images/DVS_hand.jpg').scale(0.5).shift(LEFT*3)
        dvs_txt = Text("The Dynamic Vision Sensor (DVS)").scale(0.3).next_to(dvs_img, DOWN)

        bul0 = Text("First commercialized in 2008 by Toby Delbruck(UZH&ETH under the name of Dynamic Vision Sensor (DVS).)").scale(0.3).shift(LEFT*1.2 + 2*UP)
        bul1 = Text("Novel sensor that measures the motion in the scene.").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("Ultra low power consumption (1 mW instead of 1W in standard ccd camera).").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)
        bul3 = Text("High dynamic range (140 dB instead of 80 dB in a standard ccd camera).").scale(0.3).next_to(bul2, DOWN).align_to(bul2, LEFT)
        bul4 = Text("Low latency (~1 ms)").scale(0.3).next_to(bul3, DOWN).align_to(bul3, LEFT)
        bul5 = Text("No motion blur").scale(0.3).next_to(bul4, DOWN).align_to(bul4, LEFT)

        bullets = Group(bul0,bul1,bul2,bul3,bul4,bul5)
        self.add(bullets)


        #include video
        cap = cv2.VideoCapture("../media/videos/basic_operation.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame_img = ImageMobject(frame).scale(0.66).shift(1.25*DOWN + 3*RIGHT)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()


class WhatIsEventCameraPart4(SlideScene):
    def construct(self):
        note = "When the disk stops rotating, there is no motion, hence the event camera does not transmit event\
            which results in a drastic reduction of band width caompares to the standard camera that keepts putting out the same frame over and over again. "
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("http://rpg.ifi.uzh.ch/docs/EventVisionSurvey.pdf", font_size=11).shift(3.2*DOWN+3*RIGHT)
        self.add(name, source)
        title_camera = Text("What is an Event camera").shift(UP*3).scale(0.7)
        self.add(title_camera)

        dvs_img = ImageMobject('../images/DVS_hand.jpg').scale(0.5).shift(LEFT*3)
        dvs_txt = Text("The Dynamic Vision Sensor (DVS)").scale(0.3).next_to(dvs_img, DOWN)

        bul0 = Text("First commercialized in 2008 by Toby Delbruck(UZH&ETH under the name of Dynamic Vision Sensor (DVS).)").scale(0.3).shift(LEFT*1.2 + 2*UP)
        bul1 = Text("Novel sensor that measures the motion in the scene.").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("Ultra low power consumption (1 mW instead of 1W in standard ccd camera).").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)
        bul3 = Text("High dynamic range (140 dB instead of 80 dB in a standard ccd camera).").scale(0.3).next_to(bul2, DOWN).align_to(bul2, LEFT)
        bul4 = Text("Low latency (~1 ms)").scale(0.3).next_to(bul3, DOWN).align_to(bul3, LEFT)
        bul5 = Text("No motion blur").scale(0.3).next_to(bul4, DOWN).align_to(bul4, LEFT)

        bullets = Group(bul0,bul1,bul2,bul3,bul4,bul5)
        self.add(bullets)

        #include video
        cap = cv2.VideoCapture("../media/videos/no_events.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame_img = ImageMobject(frame).scale(0.66).shift(1.25*DOWN + 3*RIGHT)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()


class WhatIsEventCameraPart5(SlideScene):
    def construct(self):
        note = "When the disk rotates really fast, the standard camera undersamples and also blurs the images,\
            while an ideal event camera outputs is a tighter spiral of events. \
                so as we can see , Although Event camera have been around only for a few years, it posesses outstanding properties \
            that have the potential of making strong impact in computer vision and robotics applications:\
                1. a very low latency with a resolution of microsecond\
                    2. no motion blur.\
                        3. ultra low power consumption - an event camera on average consumes 1 milliWatt instead of 1 Watt in standard camera.\
                            4. a very high dynamic range which is 8 orders of magnitude superior of standard cameras "
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("http://rpg.ifi.uzh.ch/docs/EventVisionSurvey.pdf", font_size=11).shift(3.2*DOWN+3*RIGHT)
        self.add(name, source)
        title_camera = Text("What is an Event camera").shift(UP*3).scale(0.7)
        self.add(title_camera)

        dvs_img = ImageMobject('../images/DVS_hand.jpg').scale(0.5).shift(LEFT*3)
        dvs_txt = Text("The Dynamic Vision Sensor (DVS)").scale(0.3).next_to(dvs_img, DOWN)

        bul0 = Text("First commercialized in 2008 by Toby Delbruck(UZH&ETH under the name of Dynamic Vision Sensor (DVS).)").scale(0.3).shift(LEFT*1.2 + 2*UP)
        bul1 = Text("Novel sensor that measures the motion in the scene.").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("Ultra low power consumption (1 mW instead of 1W in standard ccd camera).").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)
        bul3 = Text("High dynamic range (140 dB instead of 80 dB in a standard ccd camera).").scale(0.3).next_to(bul2, DOWN).align_to(bul2, LEFT)
        bul4 = Text("Low latency (~1 ms)").scale(0.3).next_to(bul3, DOWN).align_to(bul3, LEFT)
        bul5 = Text("No motion blur").scale(0.3).next_to(bul4, DOWN).align_to(bul4, LEFT)

        bullets = Group(bul0,bul1,bul2,bul3,bul4,bul5)
        self.add(bullets)

        #include video
        cap = cv2.VideoCapture("../media/videos/no_blur.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame_img = ImageMobject(frame).scale(0.66).shift(1.25*DOWN + 3*RIGHT)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()

class Football(SlideScene):
    def construct(self):
        note = "Here we have a recording of a guy catching a football, taken with a davis camera which is an event camera that outputs both events and frames.\
            In this case the the frame are being output at a rate of 6 Hz while a window of 10 milliseconds of events is shown. The frame data rate pick value mesured at th 30 kilo Hz which mean that\
                So we are talking of faster analysis of the data which is a great benefit especially in real-time applications. \
                    So I said the word event many times, I would like to finish this introduction by talking about the event generation process."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("https://drive.google.com/file/d/1w7easbLhcHh-BoMFQq1RRt5RAjGkfk7u/view", font_size=11).shift(3.2*DOWN+3*RIGHT)
        self.add(name, source)
        title_camera = Text("What is an Event camera").shift(UP*3).scale(0.7)
        self.add(title_camera)


        bul0 = Text("First commercialized in 2008 by Toby Delbruck(UZH&ETH under the name of Dynamic Vision Sensor (DVS).)").scale(0.3).shift(LEFT*1.2 + 2*UP)
        bul1 = Text("Novel sensor that measures the motion in the scene.").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("Ultra low power consumption (1 mW instead of 1W in standard ccd camera).").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)
        bul3 = Text("High dynamic range (140 dB instead of 80 dB in a standard ccd camera).").scale(0.3).next_to(bul2, DOWN).align_to(bul2, LEFT)
        bul4 = Text("Low latency (~1 ms)").scale(0.3).next_to(bul3, DOWN).align_to(bul3, LEFT)
        bul5 = Text("No motion blur").scale(0.3).next_to(bul4, DOWN).align_to(bul4, LEFT)

        bullets = Group(bul0,bul1,bul2,bul3,bul4,bul5)
        self.add(bullets)
        self.play(FadeOut(bullets, title_camera))
        title_camera = Text("Output of an event camera").shift(UP*3).scale(0.7)
        self.play(Write(title_camera, run_time=0.5))
        self.wait(1)
        #include video
        davis_txt = Text("DAVIS Camera output. Frames @ 6Hz events window of 10ms").scale(0.3).shift(2.5*DOWN)
        self.add(davis_txt)
        cap = cv2.VideoCapture("../media/videos/football.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame_img = ImageMobject(frame).scale(1.1)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()

class EventModelPart1(SlideScene):
    def construct(self):
        note = "As We have seen a traditional camera outputs frames at fixed time intervals,\
            By contrast, event camera outputs asynchronous events at microseconds resolution. \
                An event is generated every time a single pixel detects a change in intensity value.\
                    each event consists of the following data: \
                        1. The timestamp at the time of the trigering. \
                            2. The x and y pixel coordinates in the sensor. \
                                3. The event polarity (or sign) that get the value  of 1 or -1 for increase or decrease of brightness."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("http://rpg.ifi.uzh.ch/docs/EventVisionSurvey.pdf", font_size=11).shift(3.2*DOWN+3*RIGHT)
        self.add(name, source)

        title_camera = Text("Output of an event camera").shift(UP*3).scale(0.7)
        self.add(title_camera)
        title_event = Text("Generative Event Model").shift(UP*3).scale(0.7)
        self.play(ReplacementTransform(title_camera, title_event))
        
        #Clock
        num = DecimalNumber(number=0, num_decimal_places=4).shift(RIGHT*3+UP*1.5).scale(0.7)
        unit = Tex("$sec$").next_to(num, RIGHT*0.5).scale(0.7)
        clock = VGroup(num, unit)
        border = Rectangle(fill_opacity=1, fill_color=BLACK, stroke_color=BLUE)
        border.round_corners().surround(clock)
        self.add(border, clock)

        #Graph for frames
        x_start = 0
        x_finish = 4
        x_axis = NumberLine(x_range=[x_start, x_finish, 1], length=7, color=GREEN, include_numbers=True).shift(DOWN*0.5)
        axis_txt = Text("Traditional camera outputs frames at fixed time intervals.").scale(0.3).next_to(x_axis, DOWN)
        self.play(Create(x_axis), Write(axis_txt))
        poligons = VGroup()
        def add_image_to_axis(axis, p, poligons=poligons):
            image = Polygon([0, 0, 0], [0, 0.4, 0], [0.3, 0.6, 0], [0.3, 0.2, 0], color=RED)
            p = axis.n2p(p)
            p[0]+=0.1    
            image.next_to(p, UP)
            self.add(image)
            poligons += image

        num.add_updater(lambda m, dt: m.set_value(m.get_value()+dt))
        num.add_updater(lambda m, dt: add_image_to_axis(x_axis, m.get_value()) if (m.get_value()%0.3)<0.01667 and (m.get_value()%0.3)>=0.0166 else None)
        self.wait(x_finish)
        num.clear_updaters()
        
        #replace graph with event graph
        
        x_finish = 2
        x_axis_event = NumberLine(x_range=[x_start, x_finish, 1], length=7, color=PURPLE, include_numbers=True).shift(DOWN*0.5)
        self.play(FadeOut(poligons, axis_txt), ReplacementTransform(x_axis, x_axis_event))
        axis_txt = Text("Event camera outputs asynchronous events at microseconds resolution.").scale(0.3).next_to(x_axis_event, DOWN*3.1)
        self.play(Write(axis_txt))
        pointers = VGroup()
        def add_event_to_axis(axis, time, pointers=pointers):
            p = axis.n2p(time)
            p[0]+=0.1    
            num = random.random()
            if num < 0.4:
                pointer = Vector(UP, color=DARK_BLUE, stroke_width=1).next_to(p, UP)
            elif num < 0.76:
                pointer = Vector(DOWN, color=RED, stroke_width=1).next_to(p, DOWN)
            else:
                return
            self.add(pointer)
            pointers += pointer

        num.set_value(0)
        num.add_updater(lambda m, dt: m.set_value(m.get_value()+dt))
        num.add_updater(lambda m, dt: add_event_to_axis(x_axis_event, m.get_value()) if (m.get_value())<1.5 or (m.get_value())>=1.85 else None)
        self.wait(x_finish)
        num.clear_updaters()
        self.wait(3)

        pointer = Vector(DOWN, color=RED, stroke_width=1)
        pointer_cp = pointer.copy().shift(LEFT*2+UP*1.5)
        self.play(FadeOut(x_axis_event, axis_txt, pointers), FadeIn(pointer))
        self.play(ReplacementTransform(pointer, pointer_cp), run_time=2)

        formula0 = Tex(r"$event=\left\langle t,  $").next_to(pointer_cp, DOWN)
        self.play(Write(formula0))
        self.wait(2)
        formula1 = Tex(r"$\left\langle x,y \right\rangle $").next_to(formula0, RIGHT)
        self.play(Write(formula1))
        self.wait(2)
        formula2 = Tex(r"$, p \right\rangle $").next_to(formula1, RIGHT)
        self.play(Write(formula2))

