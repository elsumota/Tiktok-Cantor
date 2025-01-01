from manim import *
config.pixel_width = 1080
config.pixel_height = 1920
config.background_color =  "#EDE0C8"

class Cantor1(Scene):
    def construct(self):
        s = Square(4, color = "#00008B", fill_opacity=0.4).move_to([2.5,5,0] )
        l = Line([-5,3,0],[-1,3,0], color = "#FE0000" )
        
        self.play(Create(s),Create(l))
        
        self.play(s.animate.shift(2.5*LEFT),l.animate.shift(3*RIGHT))
        
        self.play(Rotate(l, PI/2,about_point =[-2,3,0], rate_func =
        rate_functions.ease_in_out_quad ),run_time = 2)
        
        self.play(Uncreate(s),Uncreate(l,run_time = 1.4))
        
        self.wait()



class Cantor2(MovingCameraScene):
    def construct(self):

        #MOBJECTS ----------------------------------------------------------------------------------------------- 

        ax = Axes(x_range = [0, 1, 1], y_range = [0,1,1], 
        x_length = 4,y_length = 4,
        axis_config={
                "color": BLACK,  
                "include_numbers": True
                },
        ).move_to([-1.1,4.9,0])

        l = Line([-3,-4,0],[1,-4,0], color = "#FE0000" )
        d_1 = Dot([-3,-4,0], color = BLACK)
        d_2 = Dot([1,-4,0], color = BLACK)

        d = Dot([-3,-4,0], color = "#009975")

        t_1 = MathTex(r"(1,1)", font_size=72, color = BLACK   )
        t_2 = MathTex(r"(0,1)", font_size=72, color = BLACK   )
        t_3 = MathTex(r"(1,0)", font_size=72, color = BLACK   )

        t_4 = MathTex(r"0", font_size = 72, color = BLACK )
        t_5 = MathTex(r"1", font_size = 72, color = BLACK )
        

        s = Square(4, color = "#00008B", fill_opacity=0.4).move_to([-1,5,0] )
        
        t_1.next_to(s, UR)
        t_2.next_to(s, UL)
        t_3.next_to(s,DR)
        t_4.next_to(d_1,DL)
        t_5.next_to(d_2,DR)


        de = DecimalNumber(0, num_decimal_places=4, include_sign=False, font_size=42, color =  "#28713E" )
        
        t_6 = MathTex(r"\ldots ", font_size = 40, color = "#28713E" )

        t_6.next_to(d,2.4*RIGHT + 0.9*UP)




        def next(object,dir,t):
            def updater(mob):
                mob.next_to(object,dir, buff = t)
            return updater

            

        de.add_updater(next(d,UP,0.2))



        p = MathTex(r"\dfrac{\pi}{4}", color = BLACK)

        p_1 = MathTex(r"= 0.7853\ldots")
  

        #ANIMACIONES ------------------------------------------------------------------------------------------------

        self.play(Create(l),Create(s), Create(ax),Create(d_1),
        Create(d_2) ) #Se crean los elementos básicos como el cuadrado, línea y puntos de la linea
        
        self.wait(2)

        self.play(Write(t_1), Write(t_2), Write(t_3), Write(t_4), Write(t_5)) 
        #Se escriben los puntos cartesianos y el 0 y 1 que acompañan a la línea
        
        self.play(Write(de),FadeIn(d), Write(t_6)) # Se escribe el updater y el punto que se mueve en la linea 

        
          
        self.play(d.animate.shift(4*RIGHT),ChangeDecimalToValue(de,1),
        t_6.animate.shift(4*RIGHT),run_time = 3.2,rate_func = smooth) 
        
        self.wait(0.3)
        
        self.play(d.animate.shift(2*LEFT), ChangeDecimalToValue(de,0.5),
        t_6.animate.shift(2*LEFT)
        ,run_time =2)
        
        self.play(Write(p))
        self.play(d.animate.shift(0.8*RIGHT),ChangeDecimalToValue(de,0.7),
        t_6.animate.shift(0.8*RIGHT), run_time=1)

        self.play(self.camera.frame.animate.move_to(l).set(width=l.width*1
        ))



        # pi/4 = 0.785398... 
        




        self.wait(2)

class Cantor3(MovingCameraScene):
    def construct(self):
        s_1 = Square(3.2, color = "#00008B", fill_opacity=0.4).move_to([-3.5,5,0] )
        
        l_1 = Line([-5.1,2,0], [-1.9,2,0] , color = "#FE0000" )

        t_1 = Line([-5.1,3.4,0],[-1.9,6.6,0],color ="#FE0000") 

        s_2 = Square(3.2, color = "#00008B", fill_opacity=0.4).move_to([2.4,5,0] )
    
        l_2 =2

        s_3 = Square(3.2, color = "#00008B", fill_opacity=0.4).move_to([-3.5,-2,0] )

        l_3 = 2

        s_4 = Square(3.2, color = "#00008B", fill_opacity=0.4).move_to([2.4,-2,0] )
    
        l_4 = 2

        self.add(s_1,s_2,s_3,s_4, l_1,)

        self.wait()

        self.play(Transform(l_1,t_1))


        self.wait(3)