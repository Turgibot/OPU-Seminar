from os import wait

from manim.mobject.mobject import T
from manim_slide import *
import cv2

class Header():
    def get(self):
        ou_img = ImageMobject('../images/ou_logo_full_inverted.jpeg').scale(0.4).shift(3*UP+6.3*LEFT)
        nbel_img = ImageMobject('../images/nbel.png').scale(0.18).shift(3*UP+5.8*RIGHT)
        return [ou_img, nbel_img]

class PID_Intro1(SlideScene):
    def construct(self):
        note = "זהו המאמר הנוסף שאסקור בסמינר שנכתב ב2020 על ידי חימינס ואחרים מאוניברסיטת סבייה - שכותרתו:"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        self.add(name, source)
        
        cover = ImageMobject('../images/cover2.png').scale(0.85)
        self.play(FadeIn(cover), run_time=2)
        self.wait(5)

class PID_Intro2(SlideScene):
    def construct(self):
        note = " המאמר מדבר על מימוש נוירומורפי של בקר פי אי די  - פי אי די מסורתי הוא בקר המקבל ככניסה את אות השגיאה אי של טי המחושב כהפרש בין ערך רפרנס למשתנה תהליך. הבקר מוציא פקודת תיקון המבוססת על שלושה רכיבים - פרופורליונלי אינטגרלי ודיפרנציאלי   "
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("Traditional motor controller").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        rec = Rectangle(height=3, width=7.5)
        rec.set_fill(WHITE, opacity=1)
        
        secondary_title = Text("proportional integral derivative (PID) controller", color=BLUE).next_to(model_title, DOWN).scale(0.4)
        secondary_img = ImageMobject("../images/PID.png").scale(0.5)

        pid_eq = Tex(r"$u(t) = K_pe(T)+K_i\int_0^te(\tau)d\tau +K_d\frac{de(t)}{dt}$").scale(0.4).next_to(rec, DOWN)
        pid_s = Tex(r"PID(s) = \frac{X(s)}{E(s)} = K_p + \frac{K_i}{s} + K_ds").scale(0.4).next_to(pid_eq, DOWN)
        self.play(FadeIn(rec, secondary_title, secondary_img, pid_eq, pid_s))


class PID_Intro3(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("Traditional motor controller").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        rec = Rectangle(height=3, width=7.5)
        rec.set_fill(WHITE, opacity=1)
        
        secondary_title = Text("proportional integral derivative (PID) controller", color=BLUE).next_to(model_title, DOWN).scale(0.4)
        secondary_img = ImageMobject("../images/PID.png").scale(0.5)

        pid_eq = Tex(r"$u(t) = K_pe(T)+K_i\int_0^te(\tau)d\tau +K_d\frac{de(t)}{dt}$").scale(0.4).next_to(rec, DOWN)
        self.add(rec, secondary_title, secondary_img, pid_eq)

        pid_s = Tex(r"$PID(s) = \frac{X(s)}{E(s)} = K_p + \frac{K_i}{s} + K_ds$").scale(0.4).next_to(pid_eq, DOWN)
        self.play(FadeIn(pid_s))


class PID_Intro3(SlideScene):
    def construct(self):
        note = "החלק הפרופורציונלי מכפיל את אות השגיאה בקבוע קיי פי  - כלומר חלק זה מוציא ערך הנמצא ביחס ישר לשגיאה. החיסרון בשימוש בחלק זה בלבד הוא קבלת שגיאת מצב מתמיד ."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("Traditional motor controller").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        rec = Rectangle(height=3, width=7.5)
        rec.set_fill(WHITE, opacity=1)
        
        secondary_title = Text("The Proportional Term", color=BLUE).scale(0.4)
        term = Tex(r"$K_pe(t)$", color=BLUE).scale(0.52).next_to(secondary_title, RIGHT)
        secondary_title_grp = VGroup(secondary_title, term).next_to(model_title, DOWN)
        secondary_img = ImageMobject("../images/PID_varyingP.jpg").scale(1.1)
        thirdary_title = Text("Produces an output value that is proportional to the current error value").next_to(secondary_img, DOWN).scale(0.33).shift(UP*0.2)
        fourth_title = Text("Might introduce a Steady State Error").scale(0.33).next_to(thirdary_title, DOWN).align_to(thirdary_title, LEFT).shift(UP*0.1)
        self.play(FadeIn(secondary_img, secondary_title_grp, thirdary_title, fourth_title))

class PID_Intro4(SlideScene):
    def construct(self):
        note = "החלק האינטגרלי מבצע אינטגרציה בזמן על אות השגיאה מתחילת המדידה ועד לרגע החישוב, ומכפיל את התוצאה בקבוע קיי איי. חלק זה מתייחס לערכי השגיאה מזמן תחילת המדידה עד לרגע החישוב, ובכך בעצם מושפע מערכי העבר של השגיאה"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("Traditional motor controller").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        rec = Rectangle(height=3, width=7.5)
        rec.set_fill(WHITE, opacity=1)
        
        secondary_title = Text("The Integral Term", color=BLUE).scale(0.4)
        term = Tex(r"$K_i\int_0^te(\tau)d\tau$", color=BLUE).scale(0.52).next_to(secondary_title, RIGHT)
        secondary_title_grp = VGroup(secondary_title, term).next_to(model_title, DOWN)
        secondary_img = ImageMobject("../images/Change_with_Ki.png").scale(1.2).shift(UP*0.2)
        thirdary_title = Text("The integral of a PID controller is the sum of the error e(t) over time").next_to(secondary_img, DOWN).scale(0.33).shift(UP*0.2)
        fourth_title = Text("Might introduce an overshoot if set too high").scale(0.33).next_to(thirdary_title, DOWN).align_to(thirdary_title, LEFT).shift(UP*0.1)
        self.play(FadeIn(secondary_img, secondary_title_grp, thirdary_title, fourth_title))

class PID_Intro5(SlideScene):
    def construct(self):
        note = "החלק הדיפרנציאלי,  מבצע גזירה של אות השגיאה לפי הזמן, ומכפיל את התוצאה בקבוע קיי די, חלק זה כביכול מתייחס להתנהגות העתידית של אות השגיאה על ידי בדיקה של קצב השינוי שלה, או במילים אחרות- באיזו מהירות היציאה מתקרבת או מתרחקת מהערך הרצוי "
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("Traditional motor controller").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        rec = Rectangle(height=3, width=7.5)
        rec.set_fill(WHITE, opacity=1)
        
        secondary_title = Text("The Derivative Term", color=BLUE).scale(0.4)
        term = Tex(r"$D_{out}=K_d\frac{de(t)}{dt}$", color=BLUE).scale(0.52).next_to(secondary_title, RIGHT)
        secondary_title_grp = VGroup(secondary_title, term).next_to(model_title, DOWN)
        secondary_img = ImageMobject("../images/Change_with_Kd.png").scale(1.2).shift(UP*0.2)
        thirdary_title = Text("The derivative of the process is the slope of the error function at a current time").next_to(secondary_img, DOWN).scale(0.33).shift(UP*0.2).shift(LEFT)
        fourth_title = Text("Derivative action predicts system behavior, therefor its effect relates to the future behaviour of the process").scale(0.33).next_to(thirdary_title, DOWN).align_to(thirdary_title, LEFT).shift(UP*0.1)
        self.play(FadeIn(secondary_img, secondary_title_grp, thirdary_title, fourth_title))

class PWMvsPFM1(SlideScene):
    def construct(self):
        note = "בדרך כלל שליטה על עוצמה או מיקום של מנועים מתבצעת באמצעות שינוי המתח אחד החידושים שהחוקרים הציגו במאמר הוא שהם הפעילו ושלטו על המנועים של הרובוט באמצעות פולסים בלבד"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("PWM vs. PFM").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        pwm_title = Text("Pulse Width Modulation (PWM)", color=BLUE).scale(0.4)
        pfm_title = Text("Pulse Frequency Modulation (PFM)", color=GREEN).next_to(pwm_title, RIGHT).scale(0.4)
        titles = VGroup(pwm_title, pfm_title).center().shift(UP*2)
        seperator = Line(UP*2, DOWN*2, color=RED)

        
        self.play(FadeIn(titles, seperator))

class PWMvsPFM2(SlideScene):
    def construct(self):
        note = " פי דבליו אם או פולס וידט מודולאשיין היא שיטה שבה מתח המוצא נקבע לפי יחס הזמן שבו האות גבוה לבין מחזור הדיוטי סייקל של האות. "
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("PWM vs. PFM").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        pwm_title = Text("Pulse Width Modulation (PWM)", color=BLUE).scale(0.4)
        pfm_title = Text("Pulse Frequency Modulation (PFM)", color=GREEN).next_to(pwm_title, RIGHT).scale(0.4)
        titles = VGroup(pwm_title, pfm_title).center().shift(UP*2)
        seperator = Line(UP*2, DOWN*2, color=RED)

        
        self.add(titles, seperator)

        pwm = Tex(r"$V_{DCmotor}\approx\frac{T_h}{T_{PWM}}V_{PS}$").scale(0.4).next_to(pwm_title, DOWN)
        pwm_img = ImageMobject("../images/pwm.gif").scale(1).next_to(pwm, DOWN)

        self.play(FadeIn(pwm, pwm_img))


class PWMvsPFM3(SlideScene):
    def construct(self):
        note = "לעומת זאת פי אכ אם או פולס פריקוונסי מודולאשיין היא שיטה בה מתח המוצע נקבע ביחס ישיר לתדר האות. ככל שהתדר מהיר יותר מתח המוצא גבוה יותר "
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("PWM vs. PFM").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        pwm_title = Text("Pulse Width Modulation (PWM)", color=BLUE).scale(0.4)
        pfm_title = Text("Pulse Frequency Modulation (PFM)", color=GREEN).next_to(pwm_title, RIGHT).scale(0.4)
        titles = VGroup(pwm_title, pfm_title).center().shift(UP*2)
        seperator = Line(UP*2, DOWN*2, color=RED)

        
        self.add(titles, seperator)

        pwm = Tex(r"$V_{DCmotor}\approx\frac{T_h}{T_{PWM}}V_{PS}$").scale(0.4).next_to(pwm_title, DOWN)
        pwm_img = ImageMobject("../images/pwm.gif").scale(1).next_to(pwm, DOWN)

        self.add(pwm, pwm_img)

        pfm = Tex(r"$V_{DCmotor}\approx\frac{T_h}{T_{ISI}}V_{PS} = T_h\cdot Spikes_{rate}\cdot V_{PS}$").scale(0.4).next_to(pfm_title, DOWN)
        pfm_img = ImageMobject("../images/codification.png").scale(0.8).next_to(pfm, DOWN)

        self.play(FadeIn(pfm, pfm_img))

class sPID(SlideScene):
    def construct(self):
        note = "לפנינו שרטוט הבקר המתואר במאמר. כאשר המידע העובר בכל המערכת מבוסס ספייקים. האות שהמערכת מקבלת אינו מהירות סיבוב של מנוע אלא מיקום של מפרק . הפי אייד בעצם יחושב במישור התדר לפי התמרת לפלס של המשוואה המקורית ממישור הזמן.. "
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("Spike-Based PID Position Motor Controller").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)
        secondary_title = Text("The spike-based PID (sPID) Controller Building Blocks", color=BLUE).next_to(model_title, DOWN).scale(0.4)
        blocks_img = ImageMobject("../images/blocks.jpg").scale(1).shift(UP)

        bul0 = Text("Completely designed considering the requirements of the spike paradigm.").scale(0.3).shift(LEFT*1.2)
        bul1 = Text("Both, its reference input signal and its output signal to drive the motor are spike-based signals.").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("The PFM modulation is used along Spike-Signal-Processing (SSP) Building Blocks.").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)
        bul3 = Text("Compute the sPID Laplace domain PID formulation.").scale(0.3).next_to(bul2, DOWN).align_to(bul2, LEFT)
        bul4 = Text("The input signal represents a joint target position").scale(0.3).next_to(bul3, DOWN).align_to(bul3, LEFT)

        bullets = Group(bul0,bul1,bul2,bul3,bul4)
        self.play(FadeIn(secondary_title, bullets, blocks_img))

class Block1(SlideScene):
    def construct(self):
        note = "נכיר את החלקים העיקריים שבונים את המערכת. תחילה ה רברסד ... שאחראי על המרה של ערך דיגיטלי לאות פי אכ אם. בקצרה ייצור הספייקים מתבצע באמצעות השוואה בין ערך הקלט לבין היפוך הביטים של שעון עולה. כל פעם שערך הקלט גדול מערך השעון נורה ספייק"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("Spike-Based PID Building Blocks").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        secondary_title = Text("Reversed Bitwise Synthetic Spike Generator", color=BLUE).next_to(model_title, DOWN).scale(0.4)

        bul0 = Text("Responsible for converting a digital value x, respresenting the target link position to a PFM signal.").scale(0.3).next_to(secondary_title, DOWN).shift(DOWN*0.2)

        blocks_img = ImageMobject("../images/spikegen.png").scale(0.6).shift(DOWN)
        
        formula1 = Tex(r"$RBSSG(x)_{SpikeRate} = \frac{F_{clk}}{2^{N-1}(genFD+1)}\cdot x$").scale(0.4).next_to(blocks_img, UP)
        


        self.play(FadeIn(secondary_title, bul0, formula1, blocks_img))


class Block2(SlideScene):
    def construct(self):
        note = "הבלוק הבא אחרי על אינגרציה של ספייקים. הוא מורכב משני חלקים החלק הראשון הוא קאונטר שסוכם ספייקים חיוביים ומחסיר ספייקים שליליים. הקאונטר מחובר לספייק גנראטור שראינו בשקף הקודם שמייצר ספייקים בתדר שתואם את הערך בקאונטר"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("Spike-Based PID Building Blocks").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        secondary_title = Text("Integrate-And-Generate Motor Neuron Model", color=BLUE).next_to(model_title, DOWN).scale(0.4)

        bul0 = Text("This block is composed of a spike counter and an RBSSG.").scale(0.3).next_to(secondary_title, DOWN).shift(DOWN*0.2+LEFT*3)
        bul1 = Text("The spikes counter increases when a positive spike is received, and decreases when a negative spike is received.").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("The spikes counter output is connected to the RBSSG input to generate again a new stream of spikes.").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)


        bullets = Group(bul0,bul1,bul2)

        blocks_img = ImageMobject("../images/integrate.png").scale(0.5).shift(DOWN+LEFT*2.5)
        
        formula1 = Tex(r"$f_{SI\&G}(t) = k_{SI\&G}\cdot \int_0^tf_{inputSpikes}dt = \frac{F_{clk}}{2^{N-1}(genFD+1) } \cdot \int_0^tf_{inputSpikes}dt$").scale(0.4)
        formula2 = Tex(r"$SI\&G(s) = \frac{F_{SI\&G}(S)}{F_{inputSpikes}(S)} = \frac{k_{SI\&G}}{s} =  \frac{F_{clk}}{2^{N-1}(genFD+1)\cdot s}$").scale(0.4).next_to(formula1, DOWN)
        formula3 = Tex(r"$K_i = K_{SI\&G} = \frac{F_{clk}}{2^{N-1}(genFD+1)}$").scale(0.4).next_to(formula2, DOWN)
        
        formulas = VGroup(formula1, formula2, formula3).next_to(blocks_img, RIGHT)

        self.play(FadeIn(secondary_title, bullets, formulas, blocks_img))


class Block3(SlideScene):
    def construct(self):
        note = "בגרף ניתן לראות את הסכימה המוצלחת של הספייקים כקשת האדומה. ספייקים חיוביים מוסיפים ערך לסכימה ושליליים מחסירים. "
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("Spike-Based PID Building Blocks").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        secondary_title = Text("Integrate-And-Generate Motor Neuron Model", color=BLUE).next_to(model_title, DOWN).scale(0.4)


        blocks_img = ImageMobject("../images/integrate_example.png").scale(0.55)
        
        bul0 = Text("Example of spikes integration.").scale(0.3).next_to(blocks_img, DOWN)
        


        self.play(FadeIn(secondary_title, bul0, blocks_img))


class Block4(SlideScene):
    def construct(self):
        note = "המעגל המתואר בדיאגרמת הבלוגים מבצע גזירה של אות השגיאה. הוא מורכב מלולאת משוב בין 2 מודולים המודול הראשון נקרא הולד אנד פייר והוא יודע למזג 2 אותות לאות חדש המייצג את ההפרש בינהם ואת הבלוק השני הכרנו כבר בשקף הקודם והוא מבצע אינטגרציה של ההפרשים - \
            מה שמקבלים בסופו של דבר זה שבמוצא יתקבל אות בתדר המתאים לנגזרת השגיאה."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("Spike-Based PID Building Blocks").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        secondary_title = Text("Spike Temporal Derivative Neuron Model", color=BLUE).next_to(model_title, DOWN).scale(0.4)

        bul0 = Text("This block is composed of an Integrate-and-Generate block in a closed loop with a Hold-and-Fire(H&F) module.").scale(0.3).next_to(secondary_title, DOWN).shift(DOWN*0.2+LEFT)
        bul1 = Text("The H&F module merges two spike-based signals into a new spiking signal with a frequency that is the difference of the inputs.").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("The result is that the output rate is the derivative of the input rate.").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)


        bullets = Group(bul0,bul1,bul2)

        blocks_img = ImageMobject("../images/derivative.png").scale(0.8).shift(DOWN+LEFT*2.5)
        
        formula1 = Tex(r"$SpikesOut(s) = SpikesIn(s)-SpikesOut(s)\cdot SI\&G(s)$").scale(0.4)
        formula2 = Tex(r"$STD(s) = \frac{SpikesOut(s)}{SpikesIn(s)} = \frac{1}{1+SI\&G(s)} = \frac{1}{1+\frac{K_{STD}}{s}} = \frac{s}{s+K_{STD}}$").scale(0.4).next_to(formula1, DOWN)
        formula3 = Tex(r"$K_d = K_{STD} = \frac{F_{clk}}{2^{N_d-1}(genFD_d+1)}$").scale(0.4).next_to(formula2, DOWN)
        
        formulas = VGroup(formula1, formula2, formula3).next_to(blocks_img, RIGHT)

        self.play(FadeIn(secondary_title, bullets, formulas, blocks_img))

class Block5(SlideScene):
    def construct(self):
        note = "בגרף ניתן לראות שהגזירה אכן מתבצעת למשל כאשר אין שינוי בתדר הנגזרת שווה לאפס."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("Spike-Based PID Building Blocks").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        secondary_title = Text("Spike Temporal Derivative Neuron Model", color=BLUE).next_to(model_title, DOWN).scale(0.4)


        blocks_img = ImageMobject("../images/derivativResponce.png").scale(0.55)
        
        bul0 = Text("Spikes Temporal derivative response.").scale(0.3).next_to(blocks_img, DOWN)
        


        self.play(FadeIn(secondary_title, bul0, blocks_img))


class Block6(SlideScene):
    def construct(self):
        note = " הבלוק האחרון שנכיר הוא בלוק שמעביר פקודה למנועים - כדי לאפשר תנועה של המנועים על הספייקים להיות רחבים יותר אחרת הם יחשבו כרעש ויסננו על ידי המנועים. הרעיון בגדול הוא להחזיק את הספייק כל עוד דאון קאונטר לא הגיע לאפס. בעצם הרוחב של הספייקים נקבע על ידי הערך בדאון קאונטר ולכן \
            בלוק זה משמש כרכיב הפרופורציונלי של הבקר"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("Spike-Based PID Building Blocks").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        secondary_title = Text("Proportional Spike Expander", color=BLUE).next_to(model_title, DOWN).scale(0.4)

        bul0 = Text("Expands the output spikes to the DC motor in order to allow motor movement.").scale(0.3).next_to(secondary_title, DOWN).shift(DOWN*0.2)
        bul1 = Text("The idea is to hold the spike value as output until a down counter reaches zero.").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("The width of the spike is determined by the value set to the down counter.").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)


        bullets = Group(bul0,bul1,bul2)

        blocks_img0 = ImageMobject("../images/SEcircuit.png")
        blocks_img1 = ImageMobject("../images/expandedSpikes.png").next_to(blocks_img0, LEFT)
        
        blocks_img = Group(blocks_img0, blocks_img1).shift(DOWN+LEFT*0.2)

        formula1 = Tex(r"$T_h = T_{CLK}\cdot SpikeWidth$").scale(0.4)
        formula2 = Tex(r"$K_p = T_h\cdot V_{PS}$").scale(0.4).next_to(formula1, DOWN)
        
        formulas = VGroup(formula1, formula2).next_to(blocks_img, RIGHT)

        self.play(FadeIn(secondary_title, bullets, formulas, blocks_img))


class Block7(SlideScene):
    def construct(self):
        note = "מה שמביא אותנו לקבל נוסחא סופית לבקר  "
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("Spike-Based PID Position Motor Controller").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        secondary_title = Text("The sPID transfer function", color=BLUE).next_to(model_title, DOWN).scale(0.4)

        bul0 = Text("The sPID transfer function.").scale(0.3).next_to(secondary_title, DOWN).shift(DOWN*0.2)

        blocks_img = ImageMobject("../images/blocks.jpg").scale(1).shift(UP*0.5)
        
        formula1 = Tex(r"$sPID(s) = K_p(1+SI\&G(s)+STD(s)) = K_p(1+\frac{K_i}{s}+\frac{s}{s+K_d})$").scale(0.4).next_to(blocks_img, UP)
        


        self.play(FadeIn(secondary_title, formula1, blocks_img))

class BioRob1(SlideScene):
    def construct(self):
        note = "כדי לבדוק את הבקר החוקרים חיברו אותו כחלק ממערכת הכוללת: 1. מחשב כדי לקנפג את המערכת ולקרוא נתונים בעזרת תוכנה שנקראת גיי איי אי אר. 2. זרוע רובוטית שכבר ארחיב עליה. ושני לוחות אפ פי גי אי שעליהם מומש הבקר. "
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("The ED-BioRob Robotic-Arm System").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        secondary_title = Text("The Event Based Hardware Architecture", color=BLUE).next_to(model_title, DOWN).scale(0.4)       
        rob_img = ImageMobject("../images/fnbot.jpg").scale(0.6).shift(3.8*RIGHT+DOWN)

        bul0 = Text("1. A PC for configuration setting and sensors reading using the jAER software.").scale(0.3)
        bul1 = Text("2. A robotic arm named Ed-BioRob.").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("3. AER-Robot, a Spartan-3 FPGA to interface the robotic arm.").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)
        bul3 = Text("4. AER-Node, a Spartan-6 FPGA for sPID block implementation.").scale(0.3).next_to(bul2, DOWN).align_to(bul2, LEFT)

        bullets = Group(bul0,bul1,bul2,bul3).shift(LEFT*2.2+UP*1.5)
        self.play(FadeIn(secondary_title, bullets, rob_img))


class BioRob2(SlideScene):
    def construct(self):
        note = "הרובוט עצמו נקרא אד ניו רוב הוא בעל 4 דרגות חופש .מנועי די סי מורכבים בארבעת הג'וינטס שלו שמחוברים ללינקים באמצעות חבלים וקפיצים כדי לדמות איברים אלסטיים. בנוסף בכל ג'וינט שני חיישנים : 1. אינקודר כחיישן מיקום וחיישן נוסף שמודד את הזוית של אותו הג'וינט.  "
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("The ED-BioRob Robotic-Arm System").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        secondary_title = Text("The Robotic Arm", color=BLUE).next_to(model_title, DOWN).scale(0.4)       
        rob_img = ImageMobject("../images/BioRob.png").scale(0.9).shift(3.8*RIGHT+DOWN)

        bul0 = Text("A 4 DOF, light robotic arm inspired by the biological muscle-tendon elastic system.").scale(0.3)
        bul1 = Text("Each of the four joint of the arm has a DC-motor coupled to ropes and springs as elastic components.").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("Each of the four joint of the arm has two sensors:").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)
        bul3 = Text("An opto-encoder based position sensor, attached to the DC motor.").scale(0.3).next_to(bul2, DOWN).align_to(bul2, LEFT)
        bul4 = Text("An angular sensor to measure the absolute angle of the joint.").scale(0.3).next_to(bul3, DOWN).align_to(bul3, LEFT)

        bullets = Group(bul0,bul1,bul2,bul3,bul4).shift(LEFT*1.4+UP*1.5)
        self.play(FadeIn(secondary_title, bullets, rob_img))


class Experiment1(SlideScene):
    def construct(self):
        note = "בניסוי הראשון נבחנה תנועה של כל מפרק ממינוס 90 ל 90 מעלות, הטווח  הפקודות שניתן הוא ממינוס 500 עד 500 בקפיצות של 50 ובכל שניה על השנייה. בגרף ניתן לראות שהפקודות התקבלו באופן תקין "
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("The Experiments").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        secondary_title = Text("Experiment 1: Robot Characterization", color=BLUE).next_to(model_title, DOWN).scale(0.4)       
        rob_img = ImageMobject("../images/commands.png").scale(0.9).shift(DOWN*1.6)
        ticks = Text("Time ticks (x150ms)", color=BLACK).scale(0.25).shift(DOWN*2.5)
        bul0 = Text("Move each joint from −90◦ to 90◦ where 0◦is the vertical home position.").scale(0.3)
        bul1 = Text("The input value range from -500 to 500.").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("The corresponding spike rate are -762.94 Kspikes/s to 762.94 Kspikes/s:").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)
        bul3 = Text("Every second a position command was sent separately to each joint.").scale(0.3).next_to(bul2, DOWN).align_to(bul2, LEFT)
        bul4 = Text("The position commands changed in steps of 50, equivalent to a spike frequency step of 76.3 Kspikes/s.").scale(0.3).next_to(bul3, DOWN).align_to(bul3, LEFT)

        bullets = Group(bul0,bul1,bul2,bul3,bul4).shift(LEFT*1.4+UP*1.6)
        self.play(FadeIn(secondary_title, bullets, rob_img,ticks))

class Experiment2(SlideScene):
    def construct(self):
        note = "תוצאות הניסוי הראשון מראות שהבקר הצליח לגרום לרובוא לבצע את הפקודות בצורה סבירה ובשגיאת אר אם אס איי ממוצאת של 3.3 מעלות"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("The Experiments").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        secondary_title = Text("Experiment 1: Robot Characterization - Results", color=BLUE).next_to(model_title, DOWN).scale(0.4).shift(UP*0.1)     
        img1 = ImageMobject("../images/exp1tab.png").scale(0.62).shift(UP)
        img2 = ImageMobject("../images/positions.png").scale(0.66).next_to(img1, DOWN)
        bul0 = Text("The RMSE after 4 iterations is 3.3◦").scale(0.3).next_to(img2, DOWN)


        self.play(FadeIn(secondary_title, img1,img2, bul0))


class Experiment3(SlideScene):
    def construct(self):
        note = " הניסוי השני בדומה לניבוי הראשון רק שהפעם הפקודות היו להזיז מפרק בודד 4 פעמים מ0 ל90 מעלות ואז 4 פעמים ממינוס 90 ל0 ללא איפוס באמצע. את הזויות הפעם הם בדקו באמצעות ניתוח צילום וידאו ולא על ידי החיישנים כבקרה."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("The Experiments").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        secondary_title = Text("Experiment 2: Controller accuracy of motion", color=BLUE).next_to(model_title, DOWN).scale(0.4)       
        img0 = ImageMobject("../images/exp2.png").scale(0.6).shift(3.8*RIGHT+DOWN*1.4)

        bul0 = Text("Test the accuracy of a the controller when commanding the joint to a specific angle.").scale(0.3)
        bul1 = Text("The input value range from -500 to 0 in steps of 100 (Corresponds to 18◦) for the first run").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul11 = Text("    and from 0 to 500 for the second run.").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)
        bul2 = Text("Each run was repeated 4 consecutive times without resetting the arm to the home position.").scale(0.3).next_to(bul11, DOWN).align_to(bul11, LEFT)
        bul3 = Text("The ground truth angles were measured using a video analysis tool.").scale(0.3).next_to(bul2, DOWN).align_to(bul2, LEFT)

        bullets = Group(bul0,bul1,bul11,bul2,bul3).shift(LEFT*1.4+UP*1.74)
        self.play(FadeIn(secondary_title, bullets, img0))

class Experiment4(SlideScene):
    def construct(self):
        note = "התוצאות שהתקבלו הן שגיאה של 1ץ61 מעלות בטווח 0 עד 90 ו3.3 מעלות ממינוס 90 ל0"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("The Experiments").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        secondary_title = Text("Experiment 2: Controller accuracy of motion - Results", color=BLUE).next_to(model_title, DOWN).scale(0.4)       
        img0 = ImageMobject("../images/exp2grp.png").scale(0.6).shift(DOWN)

        bul0 = Text("The RMSE of the first range (0◦ to 90◦) is 1.61◦(red marks)").scale(0.3).shift(LEFT)
        bul1 = Text("The RMSE of the second range (-90◦ to 0◦) is 3.3◦(blue marks).").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("The standard deviation is higher for the centerpoint (0◦) and for both ends of the experiment (90◦ and -90◦).").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)

        bullets = Group(bul0,bul1,bul2).shift(LEFT*1.4+UP*1.6)
        self.play(FadeIn(secondary_title, bullets, img0))

class Experiment5(SlideScene):
    def construct(self):
        note = "בניסוי השלישי נבדק דייוק של הבקר לאורך מסלול בתלת מימד כאשר כל המפרקים של הרובוט קיבלו פקודת תנוע בטווח מינוס 200 ל200 בקפיצות של 1"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("The Experiments").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        secondary_title = Text("Experiment 3: Accuracy along a 3D trajectory", color=BLUE).next_to(model_title, DOWN).scale(0.4)       
        rob_img = ImageMobject("../images/trajectory.png").scale(0.9).shift(DOWN*1.6)
        ticks = Text("Time ticks (x170ms)", color=BLACK).scale(0.25).shift(DOWN*2.5)
        bul0 = Text("Test performing a trajectory by moving all the joints simultaneously.").scale(0.3)
        bul1 = Text("The input value range from -200 to 200 with unitary steps.").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("The experiment was repeated without resetting the arm.").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)
        
        bullets = Group(bul0,bul1,bul2).shift(LEFT*1.4+UP*1.6)
        self.play(FadeIn(secondary_title, bullets, rob_img, ticks))

class Experiment6(SlideScene):
    def construct(self):
        note = "תוצאות הניסוי מסוכמות לפניכם מעידות על שגיאה מצטברת של 2.39 אחוז במיקום של האנד אפקטור של הרובוט וב6.6 מעלות בממוצע בכל מפרק  - כל 10 איטרציות מצד לצד "
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("The Experiments").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        secondary_title = Text("Experiment 3: Accuracy along a 3D trajectory - Results", color=BLUE).next_to(model_title, DOWN).scale(0.4).shift(UP*0.1)     
        img1 = ImageMobject("../images/exp3tbl.png").scale(0.62)
        img2 = ImageMobject("../images/exp33d.png").scale(0.66).next_to(img1, RIGHT)

        imgs = Group(img1, img2).center()
        bul0 = Text("An incremental error of 2.39% in the end effector position over every 10 iterations.").scale(0.3).next_to(imgs, DOWN)
        bul1 = Text("The average error over 10 iterations is 6.6◦ .").scale(0.3).next_to(bul0, DOWN)

        self.play(FadeIn(secondary_title, img1, bul0, bul1))
         #include video
        cap = cv2.VideoCapture("../media/videos/traj.mp4")
        flag, frame = cap.read()
        i = 0
        while not flag:
            pass
        while flag and i<600:
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.66).next_to(img1, RIGHT)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            i+=1
        cap.release()

class Experiment7(SlideScene):
    def construct(self):
        note = "בניסוי הרביעי מתוך 5 נבדקה תנועה מעגלית בין 4 נקודות על מישור. לשם כך נוטרל מפרק הבסיס של הרובוט. "
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("The Experiments").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        secondary_title = Text("Experiment 4: Accuracy along a 2D trajectory", color=BLUE).next_to(model_title, DOWN).scale(0.4)       
        rob_img = ImageMobject("../images/exp4input.png").scale(0.8).shift(DOWN*1.6)

        bul0 = Text("The base joint of the arm was not used, which limited the end-effector movement to a 2D plane.").scale(0.3)
        bul1 = Text("Each of the remaining joints was given a different set of 4 digital reference inputs as its trajectory.").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("The trajectory was commanded point by point in a cyclic way , from point 1 through point 4 and back to point 1.").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)
        bul3 = Text("Commands were sent at 0.25 Hz and measurements were taken at 6.5 Hz.").scale(0.3).next_to(bul2, DOWN).align_to(bul2, LEFT)

        bullets = Group(bul0,bul1,bul2,bul3).shift(LEFT*1.4+UP*1.74)
        self.play(FadeIn(secondary_title, bullets, rob_img))

class Experiment8(SlideScene):
    def construct(self):
        note = "גם פה התוצאות מראות שהבקר מתפקד ומניע את הרובוט מנקודה לנקודה בהצלחה."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("The Experiments").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        secondary_title = Text("Experiment 4: Accuracy along a 2D trajectory - Results", color=BLUE).next_to(model_title, DOWN).scale(0.4)       
        img1 = ImageMobject("../images/exp4tbl.png").scale(0.62)
        img2 = ImageMobject("../images/exp4output.png").scale(0.66).next_to(img1, RIGHT)

        imgs = Group(img1, img2).center()
        bul0 = Text("(left) Measurements average of 4 iteration of trajectories for each joint. (right) Joints mean response (colored) and Std. (black) to the commands.").scale(0.25).next_to(imgs, DOWN)

        self.play(FadeIn(secondary_title, imgs, bul0))
        

class Experiment9(SlideScene):
    def construct(self):
        note = "בניסוי האחרון החוקרים החליפו את הפי סי ברשת נוירונים המייצרת פקודות לרובוא ישירות בצורה של ספייקים. הרשת מומשה על מעבד נוירומורפי שנקרא דיינאפ אס אי . 4 ערכים שונים נבדקו בניסוי."
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("The Experiments").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        secondary_title = Text("Experiment 5: Dynap-SE Control of the Robot", color=BLUE).next_to(model_title, DOWN).scale(0.4)       
        img1 = ImageMobject("../images/dynap.png").scale(0.7)

        imgs = Group(img1).shift(DOWN*1.5)
        txt = Text("The Dynamic Neuromorphic Asynchronous Processor.").scale(0.2).next_to(imgs, DOWN)
        bul0 = Text("Transmit position commands to each joint using a neuromorphic hardware instead of a PC running jAER software.").scale(0.3)
        bul1 = Text("The reference value is represented by the activity rate of the neural population in the Dynap-SE.").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("The Dynap-SE is transmitting via its AER ports to the AER decoder module in the robot controller.").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)
        bul3 = Text("The AER decoder is connected to the sPID module.").scale(0.3).next_to(bul2, DOWN).align_to(bul2, LEFT)
        bul4 = Text("4 different neuron activities were tested to change the angles of joint 4.").scale(0.3).next_to(bul3, DOWN).align_to(bul3, LEFT)

        bullets = Group(bul0,bul1,bul2,bul3,bul4).shift(LEFT*0.6+UP*1.6)
        self.play(FadeIn(secondary_title, bullets, imgs, txt))

class Experiment10(SlideScene):
    def construct(self):
        note = "התוצאות מראות שרשתות הנוירונים התמשקו בהצלחה למערכת ושהרובוט זז לזזיות הרצויות"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)       
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("The Experiments").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        secondary_title = Text("Experiment 5: Dynap-SE Control of the Robot - Results", color=BLUE).next_to(model_title, DOWN).scale(0.4)       
        img1 = ImageMobject("../images/exp5.jpg").scale(0.85)

        imgs = Group(img1).shift(DOWN*0.4)
        txt = Text("The neural activity on the Dynap-SE changes within the range of the joint. (A)0◦,(B)30◦,(C)90◦,(D)130◦.").scale(0.2).next_to(imgs, DOWN)
        bul0 = Text("The 4 angles required PFM reference signals were successfully represented by the neural activity in the Dynap-SE chip.").scale(0.3)
       

        bullets = Group(bul0).shift(LEFT*0.2+UP*1.6)
        self.play(FadeIn(secondary_title, bullets, imgs, txt))
        


class Summary2(SlideScene):
    def construct(self):
        note = "לסיכום במאמר החוקרים הצליחו: 1. לממש בקר פי איי די מבוסס ספייקים ובאמצעותו לשלוט ברובוט בעל 4 דרגות חופש. 2. להניע מנועים באמצעות פולס פריקוונסי מודוליישן 3. להתמשק לחומרה נוירומורפית בכדיי לקבל פקודות מרשת מוירונים ולא רק מפי סי. דיוק של 3.3 מעלות בתנועה של 90 למינוס 90 מעלות"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        source = Text("Jimenez et al. ED-BioRob: A Neuromorphic Robotic Arm With FPGA-Based Infrastructure for Bio-Inspired Spiking Motor Controllers (2020).", font_size=11).shift(3.2*DOWN+1.7*RIGHT)
        model_title = Text("Summary").shift(UP*3).scale(0.65)

        self.add(name, source, model_title)

        
        secondary_title = Text("The researchers succeeded in:", color=BLUE).next_to(model_title, DOWN).scale(0.4)

        bul0 = Text("Implementing a spike-based PID motor controllers to control the position of the 4 joints of a robotic arm, called ED-BioRob.").scale(0.27).shift(1.5*UP+1.2*LEFT)
        bul1 = Text("Drive DC motors with Pulse Frequency Modulation signals, mimicking the motor-neurons of mammals.").scale(0.27).next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Text("Demonstrating that the robot can be commanded through a population of silicon neurons (DYNAP-SE executing a spiking neural network)").scale(0.27).next_to(bul1, DOWN).align_to(bul1, LEFT)
        bul3 = Text("The sPID offers the worst RMSE of 3.3◦ after several iterations of joint movements from -90◦to 90◦.").scale(0.27).next_to(bul2, DOWN).align_to(bul2, LEFT)

        bullets = Group(bul0,bul1,bul2,bul3)

        self.play(FadeIn(secondary_title, bullets))


class Demo(SlideScene):
    def construct(self):
        note = "......"
        self.create_note(note)
        for x in Header().get():
            self.add(x)
        name = Text("Guy Tordjman", font_size=11).shift(3.2*DOWN+6.3*LEFT)
        model_title = Text("Demo").center()

        self.add(name)

        self.play(FadeIn(model_title))
