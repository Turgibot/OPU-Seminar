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



class StereoVision1(SlideScene):
    def construct(self):
        note = "Before diving into the first Article I would like to start with a short intro to neuromorphic stereo vision.\
             So Stereo-vision in general, refers to the method of recovering depth information from both eyes, or in the artificial \
                context ...."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        self.add(name)
        
        neuro_title = Text("Neuromorphic Stereo vision").scale(0.7)
        self.add(neuro_title)
        self.wait()

        title = Text("Stereo Vision").shift(UP*3).scale(0.7)
        self.play(ReplacementTransform(neuro_title, title), run_time=1)        

        depth = ImageMobject("../images/depth-perception.jpg").scale(1.3)
        definition = Text("Stereo-vision refers to the method of recovering depth information from both eyes.").scale(0.3).next_to(depth, DOWN)
        self.play(FadeIn(depth, definition))
        


class StereoVision2(SlideScene):
    def construct(self):
        note = "Machine stereo vision, or stereoscopic vision, extracts the data from two visual sensors.\
                    Here you can see 2 types of stereo cameras, the one on the right is a standard stereo camera that consists of two standard cameras, \
                        whereas the one on the left is a mount with pair of bio inspired cameras that are called event cameras ...\
                            As this is a noval neuromorphic hardware - The article that i am introducing to\
                                you today uses a neuromorphic approach, based on input fron an event stereo camera. \
                                    so what is an event camera and what is the difference between a frame based to event based camera?"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        self.add(name)
       
        zed = ImageMobject('../images/zed.jpg').shift(2.2*RIGHT+0.7*UP).scale(0.7)
        ec = ImageMobject('../images/stereo_event.png').shift(2.2*LEFT)
        neuro = Text("Event Stereo Camera").scale(0.7).next_to(ec, DOWN)
        classic = Text("Frame based Stereo Camera").scale(0.7).next_to(zed, UP)

        machine_title = Text("Machine Stereo Vision").shift(UP*3).scale(0.7)
        self.play(FadeIn(machine_title))
        self.wait(0.5)
        self.play(FadeIn(zed,classic,ec, neuro))




class WhatIsEventCameraPart1(SlideScene):
    def construct(self):
        note = "When looking at existing frame data we can say that algorithms of computer vision suffer from issues like high latency - due to redundant data analysis\
            , motion blur  - which depends on the exposure time of the camera,  and low dynamic range - which causes issues for example when there a strong light source in the camera's field of view.\
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

        high_txt = Text("High Latency").scale(0.3).shift(3.3*LEFT+1.7*UP)
 
        blur_txt = Text("Motion Blur").scale(0.3).shift(0.3*LEFT+1.7*UP)

        dnr_txt = Text("Low Dynamic Range").scale(0.3).shift(3*RIGHT+1.7*UP)

        self.play(FadeIn(grp1, high_txt, blur_txt, dnr_txt))



class WhatIsEventCameraPart2(SlideScene):
    def construct(self):
        note = "Event cameras were first commercialized in 2008 by Toby Delbruck from the university of Zurich\
             under the name of DVS which stands for Dynamic Vision Sensor.\
                 An event camera has smart pixels that are all\
                     independent of each other - every time that a single pixel detects motion, in the form of brightness change, that pixel trigers an event.\
                         This means that only motion in measured in the scene. "
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("http://rpg.ifi.uzh.ch/docs/EventVisionSurvey.pdf", font_size=11).shift(3.2*DOWN+3*RIGHT)
        self.add(name, source)
        title_camera = Text("What is an Event camera").shift(UP*3).scale(0.7)
        self.add(title_camera)


        bul0 = Text("First commercialized in 2008 by Toby Delbruck(UZH&ETH under the name of Dynamic Vision Sensor (DVS).)").scale(0.3).shift(LEFT*1.2 + 2*UP)
        bul1 = Text("Novel sensor that measures the motion in the scene.").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("Ultra low power consumption (1 mW instead of 1W in standard ccd camera).").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)
        bul3 = Text("High dynamic range (140 dB instead of 80 dB in a standard ccd camera).").scale(0.3).next_to(bul2, DOWN).align_to(bul2, LEFT)
        bul4 = Text("Low latency (~1 μs)").scale(0.3).next_to(bul3, DOWN).align_to(bul3, LEFT)
        bul5 = Text("No motion blur").scale(0.3).next_to(bul4, DOWN).align_to(bul4, LEFT)
       
        self.play(Write(bul0),Write(bul1),Write(bul2),Write(bul3),Write(bul4),Write(bul5), run_time = 0.75)




class WhatIsEventCameraPart3(SlideScene):
    def construct(self):
        note = "The animation on the bottom right of the screen from Davide Scaramuzza at the Robotics and perception group\
             in the University of Zurich, compares the outputs of a frame camera with an event camera.\
                    A rotating disk with a black circle is captured by the two camera types.\
                        On top you can see the output of a standard camera which are intensity frames at a constant time interval,\
                            while on the bottom you see the output of an event camera, which relates only to the moving black circle and represented as a spiral of events in space and time \
                                where the red and blue colors represent the polarity of the event."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("http://rpg.ifi.uzh.ch/docs/EventVisionSurvey.pdf", font_size=11).shift(3.2*DOWN+3*RIGHT)
        self.add(name, source)
        title_camera = Text("What is an Event camera").shift(UP*3).scale(0.7)
        self.add(title_camera)

        bul0 = Text("First commercialized in 2008 by Toby Delbruck(UZH&ETH under the name of Dynamic Vision Sensor (DVS).)").scale(0.3).shift(LEFT*1.2 + 2*UP)
        bul1 = Text("Novel sensor that measures the motion in the scene.").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("Ultra low power consumption (1 mW instead of 1W in standard ccd camera).").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)
        bul3 = Text("High dynamic range (140 dB instead of 80 dB in a standard ccd camera).").scale(0.3).next_to(bul2, DOWN).align_to(bul2, LEFT)
        bul4 = Text("Low latency (~1 μs)").scale(0.3).next_to(bul3, DOWN).align_to(bul3, LEFT)
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
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.66).shift(1.25*DOWN + 3*RIGHT)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()

         #include video
        cap = cv2.VideoCapture("../media/videos/basic_operation.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.66).shift(1.25*DOWN + 3*RIGHT)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()
         #include video
        cap = cv2.VideoCapture("../media/videos/basic_operation.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.66).shift(1.25*DOWN + 3*RIGHT)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()


class WhatIsEventCameraPart4(SlideScene):
    def construct(self):
        note = "When the disk stops rotating, there is no motion, hence the event camera does not transmit event\
            which results in a drastic reduction of band width compares to the standard camera that keepts putting out the same frame over and over again. "
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("http://rpg.ifi.uzh.ch/docs/EventVisionSurvey.pdf", font_size=11).shift(3.2*DOWN+3*RIGHT)
        self.add(name, source)
        title_camera = Text("What is an Event camera").shift(UP*3).scale(0.7)
        self.add(title_camera)

        bul0 = Text("First commercialized in 2008 by Toby Delbruck(UZH&ETH under the name of Dynamic Vision Sensor (DVS).)").scale(0.3).shift(LEFT*1.2 + 2*UP)
        bul1 = Text("Novel sensor that measures the motion in the scene.").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("Ultra low power consumption (1 mW instead of 1W in standard ccd camera).").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)
        bul3 = Text("High dynamic range (140 dB instead of 80 dB in a standard ccd camera).").scale(0.3).next_to(bul2, DOWN).align_to(bul2, LEFT)
        bul4 = Text("Low latency (~1 μs)").scale(0.3).next_to(bul3, DOWN).align_to(bul3, LEFT)
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
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.66).shift(1.25*DOWN + 3*RIGHT)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()
         #include video
        cap = cv2.VideoCapture("../media/videos/no_events.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.66).shift(1.25*DOWN + 3*RIGHT)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()
         #include video
        cap = cv2.VideoCapture("../media/videos/no_events.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
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
                            4. a very high dynamic range which is 8 orders of magnitude superior to a standard camera"
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
        bul4 = Text("Low latency (~1 μs)").scale(0.3).next_to(bul3, DOWN).align_to(bul3, LEFT)
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
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.66).shift(1.25*DOWN + 3*RIGHT)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()
         #include video
        cap = cv2.VideoCapture("../media/videos/no_blur.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.66).shift(1.25*DOWN + 3*RIGHT)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()
         #include video
        cap = cv2.VideoCapture("../media/videos/no_blur.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.66).shift(1.25*DOWN + 3*RIGHT)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()

class Football(SlideScene):
    def construct(self):
        note = "This is an example of a real output of an event camera where we have a guy catching a football, taken with a davis camera which is an event camera that outputs both events and frames.\
            In this case the the frame are being output at a rate of 6 Hz while a window of 10 milliseconds of events is shown. A very important fact to notice is that the data rate pick value was measured at 30 kilo Hz\
                 which is that of a microcontroller - \
                So we are talking of faster analysis of the data which is a great benefit especially in real-time applications."
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
        bul4 = Text("Low latency (~1 μs)").scale(0.3).next_to(bul3, DOWN).align_to(bul3, LEFT)
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
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(1.1)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()

class Visualization(SlideScene):
    def construct(self):
        note = "In this slide we see conventional frames on the top and 2 different ways of visualizing the out put of an event camera on the bottom. \
            On the left we see a 3D space time visualization where the events are visualized in an x y t volume. \
                BLUE corresponds to positive changes of intensity and The RED events correspond to negative change of intensity. \
                    On the right we see event in the form of frames, in this case each frame shows the events that were recorded in the last 10 milllseconds, \
                        However, this delta T parameter is configurable and we can go down in time to 1 micro-second.\
                            So how are events generated ???."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("https://drive.google.com/file/d/1w7easbLhcHh-BoMFQq1RRt5RAjGkfk7u/view", font_size=11).shift(3.2*DOWN+3*RIGHT)
        self.add(name, source)
        title_camera = Text("Output of an event camera").shift(UP*3).scale(0.7)
        self.add(title_camera)


       
        self.play(FadeOut(title_camera))
        title_camera = Text("Visualization of an event camera").shift(UP*3).scale(0.7)
        self.play(Write(title_camera, run_time=0.5))
        self.wait(1)
        #include video
        cap = cv2.VideoCapture("../media/videos/visualization.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.95).shift(LEFT*0.6)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()
         #include video
        cap = cv2.VideoCapture("../media/videos/visualization.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.95).shift(LEFT*0.6)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()
         #include video
        cap = cv2.VideoCapture("../media/videos/visualization.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.95).shift(LEFT*0.6)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()

class EventModelPart1(SlideScene):
    def construct(self):
        note = "As We have seen a traditional camera outputs frames at fixed time intervals,\
            By contrast, event camera outputs asynchronous events at microseconds resolution. \
                An event is generated every time a single pixel detects a change in intensity value.\
                    "
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
        self.wait(5)


class EventModelPart2(SlideScene):
    def construct(self):
        note = "each event consists of the following data: \
                        1. The timestamp at the time of the trigering. \
                            2. The x and y pixel coordinates in the sensor. \
                                3. The event polarity (or sign) that get the value  of 1 or -1 for increase or decrease of brightness."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("http://rpg.ifi.uzh.ch/docs/EventVisionSurvey.pdf", font_size=11).shift(3.2*DOWN+3*RIGHT)
        self.add(name, source)
        title_event = Text("Generative Event Model").shift(UP*3).scale(0.7)
        self.add(title_event)
        
 

        pointer = Vector(DOWN, color=RED, stroke_width=1)
        pointer_cp = pointer.copy().shift(LEFT*2+UP*1.5)
        self.play(ReplacementTransform(pointer, pointer_cp))

        formula0 = Tex(r"$event=\left\langle t,  $").next_to(pointer_cp, DOWN)
        self.play(Write(formula0))
        self.wait(2)
        formula1 = Tex(r"$\left\langle x,y \right\rangle $").next_to(formula0, RIGHT)
        self.play(Write(formula1))
        self.wait(2)
        formula2 = Tex(r"$, p \right\rangle $").next_to(formula1, RIGHT)
        self.play(Write(formula2))

class EventModelPart3(SlideScene):
    def construct(self):
        note = "Looking at the circuit diagram of a single pixel we can see that : \
            1. The photoreceptor diode connected to a logritmic calculation module.\
                2. That capacively copuled to a change amplifier that holds the previous signal value and out puts the differnce between the values of the current and previous signals. \
                    Everytime an event is triggered, this subcircuit gets reset and the current value is stored.\
                    3. Then the difference signal is driven into two comparators that detect on and off brigntness changes. \
                        If the signal went up and pass an 'ON' threshold  - an 'ON' event is triggered and viceversa for an 'OFF' event in the bottom comparator."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Lichtsteiner et al. A 128x128 120 dB 15µs Latency Asynchronous Temporal Contrast Vision Sensor, IEEE Journal of Solid-State Circuits, 2008", font_size=11).shift(3.2*DOWN+2*RIGHT).scale(0.8)
        self.add(name, source)
        title_event = Text("Generative Event Model").shift(UP*3).scale(0.7)
        self.add(title_event)
        #add diagram       
        diagram_txt = Text("Event Camera Pixel Circuit Diagram").shift(UP*2+LEFT*2).scale(0.5)
        self.play(Write(diagram_txt), run_time=0.5)
        circuit_img = ImageMobject("../images/DVS_pixel.png")
        self.play(FadeIn(circuit_img), run_time=0.5)

class EventModelPart4(SlideScene):
    def construct(self):
        note = "This graph describes the log Intensity at a Single Pixel x over time. \
            As you can see a POSITIVE RED event was triggered everytime the log intensity increased passed a positive contrast sentitivity threshold -  \
            And a NEGATIVE BLUE event was triggered everytime the log intensity descreased passed a negative contrast sentitivity threshold."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("http://rpg.ifi.uzh.ch/docs/EventVisionSurvey.pdf", font_size=11).shift(3.2*DOWN+3*RIGHT)
        self.add(name, source)
       
        title_event = Text("Generative Event Model").shift(UP*3).scale(0.7)
        self.add(title_event)

        #shrink diagram       
        circuit_img = ImageMobject("../images/DVS_pixel.png")
        diagram_txt = Text("Event Camera Pixel Circuit Diagram").shift(UP*2+LEFT*2).scale(0.5)
        self.add(diagram_txt, circuit_img)
        circuit_img_cp = circuit_img.copy().shift(RIGHT*3.5+UP*1.5).scale(0.5)
        pixel_txt = Text("The Intensity at a Single Pixel").shift(UP+LEFT*2).scale(0.5)
        self.play(ReplacementTransform(circuit_img, circuit_img_cp), Unwrite(diagram_txt))        
        self.play(Write(pixel_txt), run_time=0.5)

        intensity_img = ImageMobject("../images/operation.png").scale(0.85).shift(DOWN+LEFT*1.7)
        self.play(FadeIn(intensity_img), run_time=0.5)

class EventModelPart5(SlideScene):
    def construct(self):
        note = "Here we see a list of Event camera manufacturers and some of their key properties, as you can see, their price is very high compared to a standard camera."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("http://rpg.ifi.uzh.ch/docs/EventVisionSurvey.pdf", font_size=11).shift(3.2*DOWN+3*RIGHT)
        self.add(name, source)
       
        title_event = Text("Generative Event Model").shift(UP*3).scale(0.7)
        self.add(title_event)
        intensity_img = ImageMobject("../images/operation.png").scale(0.85).shift(DOWN+LEFT*1.7)
        circuit_img_cp = ImageMobject("../images/DVS_pixel.png").shift(RIGHT*3.5+UP*1.5).scale(0.5)
        pixel_txt = Text("The Intensity at a Single Pixel").shift(UP+LEFT*2).scale(0.5)
        self.add(pixel_txt, circuit_img_cp,intensity_img)
        self.play(FadeOut(pixel_txt, circuit_img_cp,intensity_img), run_time=0.5)

        available_img = ImageMobject("../images/availability.png").scale(0.8).shift(DOWN*0.2)
        available_txt = Text("Market Available Event Cameras").shift(UP*3).scale(0.7)
        self.play(ReplacementTransform(title_event, available_txt))
        self.play(FadeIn(available_img), run_time=0.5)

class EventModelPart6(SlideScene):
    def construct(self):
        note = "Before I move on to reviewing the algorithm in the article, I just wanted to state that because the output of an event camera is asynchronous\
             and it posseses no intensity information - but only binary intensity changes, traditional vision algorithms that are used on regular frame data \
                 cannot be used on event camera data - \
            Therefor a paradigm shift needs to be applied and example of that is in the article : "
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("http://rpg.ifi.uzh.ch/docs/EventVisionSurvey.pdf", font_size=11).shift(3.2*DOWN+3*RIGHT)
        self.add(name, source)
    
        available_img = ImageMobject("../images/availability.png").scale(0.8).shift(DOWN*0.2)
        available_txt = Text("Market Available Event Cameras").shift(UP*3).scale(0.7)
        self.add(available_txt, available_img)

        self.play(FadeOut(available_txt, available_img))

        dvs_img = ImageMobject('../images/DVS_hand.jpg').scale(0.4).shift(RIGHT*3.8)
        dvs_txt = Text("The Dynamic Vision Sensor (DVS)").scale(0.25).next_to(dvs_img, DOWN)

        txt1 = Text("Because event camera's output data is:").scale(0.5).shift(UP*1.5+LEFT*0.3)
        txt2 = Text("Asynchronous").scale(0.4).next_to(txt1, DOWN).align_to(txt1, LEFT).shift(RIGHT*0.2)
        txt3 = Text("No pixel intensity information").scale(0.4).next_to(txt2, DOWN).align_to(txt1, LEFT).shift(RIGHT*0.2)
        txt4 = Text("Traditional vision algorithms cannot be used", color=RED).scale(0.55).shift(DOWN*1.75)

        self.play(Write(txt1),Write(txt2),Write(txt3),FadeIn(dvs_img,dvs_txt), run_time=0.3)


class EventModelPart7(SlideScene):
    def construct(self):
        note = "Before I move on to reviewing the algorithm in the article, I just wanted to state that because the output of an event camera is asynchronous\
             and it posseses no intensity information - but only binary intensity changes, traditional vision algorithms that are used on regular frame data \
                 cannot be used on event camera data - \
            Therefor a paradigm shift needs to be applied and example of that is in the article : "
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("http://rpg.ifi.uzh.ch/docs/EventVisionSurvey.pdf", font_size=11).shift(3.2*DOWN+3*RIGHT)
        self.add(name, source)
    
        dvs_img = ImageMobject('../images/DVS_hand.jpg').scale(0.4).shift(RIGHT*3.8)
        dvs_txt = Text("The Dynamic Vision Sensor (DVS)").scale(0.25).next_to(dvs_img, DOWN)

        txt1 = Text("Because event camera's output data is:").scale(0.5).shift(UP*1.5+LEFT*0.3)
        txt2 = Text("Asynchronous").scale(0.4).next_to(txt1, DOWN).align_to(txt1, LEFT).shift(RIGHT*0.2)
        txt3 = Text("No pixel intensity information").scale(0.4).next_to(txt2, DOWN).align_to(txt1, LEFT).shift(RIGHT*0.2)
        txt4 = Text("Traditional vision algorithms cannot be used", color=RED).scale(0.55).shift(DOWN*1.75)

        self.add(txt1,txt2,txt3,dvs_img,dvs_txt)
        self.play(FadeIn(txt4))





