import textwrap
from manim import*
import random

class shot4(ThreeDScene):
    def construct(self):      

        t = random.randint(4,13)
        if random.randint(0,12) == 0:  
            t*=2

        h = min(t,random.randint(0,1+t//3)+5)

        j = t - h 
        k = j
        print("t =", str(t), "h =", str(h), "j =", str(j))

        self.set_camera_orientation(phi = 91 * DEGREES, theta = 0 * DEGREES,zoom=0.26)

        T = str("T(x)")
        txt1 = MathTex(
                r"&\text{if layer} <",
                T,
                r"\text{ - Random(}0\rightarrow3)\text{:}\\",
                r"&\qquad\text{radius} = 2\\",
                r"&\text{else:}\\",
                r"&\qquad\text{radius} = 1\\",
                r"&\text{if } H(x) > 8\ \text{\& layer} < T(x)-H(x) + 4\text{:}\\",
                r"&\qquad\text{radius} = 3"
            )
        txt1[0][2].set_color(YELLOW_E)
        txt1[0][3].set_color(YELLOW_E)
        txt1[0][4].set_color(YELLOW_E)
        txt1[0][5].set_color(YELLOW_E)
        txt1[0][6].set_color(YELLOW_E)

        txt1[6][9].set_color(YELLOW_E)
        txt1[6][10].set_color(YELLOW_E)
        txt1[6][11].set_color(YELLOW_E)
        txt1[6][12].set_color(YELLOW_E)
        txt1[6][13].set_color(YELLOW_E)

        txt1[1].set_color(RED)

        txt1[2][1].set_color(ORANGE)
        txt1[2][2].set_color(ORANGE)  
        txt1[2][3].set_color(ORANGE)  
        txt1[2][4].set_color(ORANGE)  
        txt1[2][5].set_color(ORANGE)  
        txt1[2][6].set_color(ORANGE)
        
        txt1[6][15].set_color(RED)
        txt1[6][16].set_color(RED)  
        txt1[6][17].set_color(RED)  
        txt1[6][18].set_color(RED)

        txt1[6][2].set_color("#00EEFF")
        txt1[6][3].set_color("#00EEFF")
        txt1[6][4].set_color("#00EEFF")
        txt1[6][5].set_color("#00EEFF")
        txt1[6][20].set_color("#00EEFF")
        txt1[6][21].set_color("#00EEFF")
        txt1[6][22].set_color("#00EEFF")
        txt1[6][23].set_color("#00EEFF")     

        txt2 = MathTex(
                r"&\text{if layer} <",
                T,
                r"\text{ - Random(}0\rightarrow3)\text{:}\\",
                r"&\qquad\text{radius} = 2\\",
                r"&\text{else:}\\",
                r"&\qquad\text{radius} = 1\\",
                r"&\text{if } H(x) > 8\ \text{\& layer} < T(x)-H(x) + 4\text{:}\\",
                r"&\qquad\text{radius} = 3"
            )
        txt2.rotate(90 * DEGREES, axis=X_AXIS)
        txt2.rotate(90 * DEGREES, axis=Z_AXIS)
        txt2.shift(DOWN * 14)
        txt2.scale(2.5)

        txt2[0][2].set_color(YELLOW_E)
        txt2[0][3].set_color(YELLOW_E)
        txt2[0][4].set_color(YELLOW_E)
        txt2[0][5].set_color(YELLOW_E) 
        txt2[0][6].set_color(YELLOW_E)

        txt2[6][9].set_color(YELLOW_E)
        txt2[6][10].set_color(YELLOW_E)
        txt2[6][11].set_color(YELLOW_E)
        txt2[6][12].set_color(YELLOW_E)
        txt2[6][13].set_color(YELLOW_E)

        txt2[2][1].set_color(ORANGE)
        txt2[2][2].set_color(ORANGE)  
        txt2[2][3].set_color(ORANGE)  
        txt2[2][4].set_color(ORANGE)  
        txt2[2][5].set_color(ORANGE)  
        txt2[2][6].set_color(ORANGE)

        txt2[1].set_color(RED)
        txt2[6][15].set_color(RED)
        txt2[6][16].set_color(RED)  
        txt2[6][17].set_color(RED)  
        txt2[6][18].set_color(RED)

        txt2[6][2].set_color("#00EEFF")
        txt2[6][3].set_color("#00EEFF")
        txt2[6][4].set_color("#00EEFF")
        txt2[6][5].set_color("#00EEFF")
        txt2[6][20].set_color("#00EEFF")
        txt2[6][21].set_color("#00EEFF")
        txt2[6][22].set_color("#00EEFF")
        txt2[6][23].set_color("#00EEFF")     
        
        txt1.rotate(90 * DEGREES, axis=X_AXIS)
        txt1.rotate(90 * DEGREES, axis=Z_AXIS)
        txt1.shift(DOWN * 14)
        txt1.scale(2.5)
        
        self.play(Write(txt1))
        self.play(ReplacementTransform(txt1, txt2, run_time=0.5))
        
        trunk = Prism(dimensions=[1,1,t], fill_color="#1f7ecc", fill_opacity=1).shift(IN * 0.5)
        self.play(Create(trunk), run_time=0.3)
        self.wait(0.5)       
#loop      
        while(k<=t):
            self.remove(txt2)
            i = random.randint(0,3)
            if k < t - i:
                l = 2
            else: 
                l = 1
            if h > 8 and k < j + 4:
                l = 3
            print("l =", str(l), "k =", str(k), "i =", str(i))
            if k < j + 3:
                layer1 = Prism(dimensions=[2*l+1,2*l+1,1], fill_color="#55A7FA", fill_opacity=0.1).shift(IN * ((t+1)/2) + OUT * (k))
            else:
                layer1 = Prism(dimensions=[2*l+1,2*l+1,1], fill_color="#084678", fill_opacity=1).shift(IN * ((t+1)/2) + OUT * (k))

            txt = MathTex(r"R(" + str(k) + ") = "+ str(l))
            T = str(t)
            txt2 = MathTex(
                r"&\text{if }",
                k,
                r"<",
                T,
                r"\text{ - }",
                str(i),
                r"\text{:}\\",
                r"&\qquad\text{radius} = 2\\",
                r"&\text{else:}\\",
                r"&\qquad\text{radius} = 1\\",
                r"&\text{if }",
                h,
                r" > 8 \text{ \& }",
                k,
                r"<",
                T,
                r"-",
                h,
                r"+4\text{:}\\",
                r"&\qquad\text{radius} = 3"
            )
            txt2.rotate(90 * DEGREES, axis=X_AXIS)
            txt2.rotate(90 * DEGREES, axis=Z_AXIS)
            txt2.shift(DOWN * 17.890, IN * 0.025)
            txt2.scale(2.5)

            txt2[3].set_color(RED)
            txt2[15].set_color(RED)

            txt2[1].set_color(YELLOW_E)
            txt2[13].set_color(YELLOW_E)

            txt2[5][0].set_color(ORANGE)

            txt2[11].set_color("#00EEFF")
            txt2[17].set_color("#00EEFF")   
            
            if l == 1:
                txt.next_to(layer1, UP * 16)
                txt2[9].set_color("#00EE77")
            elif l == 2:
                txt.next_to(layer1, UP * 12)
                txt2[7].set_color("#00EE77")
            else:
                txt.next_to(layer1, UP * 8)
                txt2[19].set_color("#00EE77")
            
            txt.rotate(90 * DEGREES, axis=X_AXIS)
            txt.rotate(90 * DEGREES, axis=Z_AXIS)
            
            self.play(Create(layer1), Write(txt), ReplacementTransform(txt2, txt2), run_time=0.5)          
           
            k+=1

        self.move_camera(theta = 90 * DEGREES)
        self.wait(1)