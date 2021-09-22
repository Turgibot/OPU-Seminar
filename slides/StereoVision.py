from manim_slide import *
import cv2

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
        note = "Read the slide."
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
        note = "Read the slide."
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
        note = "Read the slide."
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
        note = "Read the slide."
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


