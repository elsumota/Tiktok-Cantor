from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.background_color =  "#EDE0C8"

class Cantor1(Scene):
    def construct(self):
        s = Square(4, color = "#00008b", fill_opacity=0.4).move_to([2.5,5,0] )
        l = Line([-5,3,0],[-1,3,0], color = "#FE0000" )
        
        self.play(Create(s),Create(l))

        self.wait(2)
        self.play(s.animate.shift(2.5*LEFT),l.animate.shift(3*RIGHT))
        
        self.play(Rotate(l, PI/2,about_point =[-2,3,0], rate_func =
        rate_functions.ease_in_out_quad ),run_time = 2)
        self.play(Indicate(s, color = "#00008B"))
        
        self.play(Uncreate(s),Uncreate(l,run_time = 1.7))
        
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

        d = Dot([-3,-4,0], color = BLACK)

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


        de = DecimalNumber(0, num_decimal_places=4, include_sign=False, font_size=42, color =  BLACK )
        
        t_6 = MathTex(r"\ldots  ", font_size = 40, color = BLACK)


        t_6.next_to(d,2.4*RIGHT + 0.9*UP)




        def next(object,dir,t):
            def updater(mob):
                mob.next_to(object,dir, buff = t)
            return updater

            

        de.add_updater(next(d,UP,0.2))



        p = MathTex(r"\dfrac{\pi}{4}\, =\, 0.\,7\,8\,5\,3\,9\,8\,...", color = BLACK,font_size = 60).move_to([-1,0,0])



        x = self.camera.frame.get_width()  #ancho de la cámara al principio de la escena



        #ANIMACIONES ------------------------------------------------------------------------------------------------

        self.play(Create(l),Create(s), Create(ax),Create(d_1),
        Create(d_2) ) #Se crean los elementos básicos como el cuadrado, línea y puntos de la linea
        

        self.play(Write(t_1), Write(t_2), Write(t_3), Write(t_4), Write(t_5)) 
        #Se escriben los puntos cartesianos y el 0 y 1 que acompañan a la línea
        
        self.play(Write(de.set_color(BLACK)),FadeIn(d), Write(t_6)) # Se escribe el updater y el punto que se mueve en la linea 
 
        self.play(self.camera.frame.animate.set_width(l.width*1.9).move_to([-0.3,-5,0]))
          
        self.play(d.animate.shift(4*RIGHT),ChangeDecimalToValue(de,1),
        t_6.animate.shift(4*RIGHT),run_time = 3.2,rate_func = smooth) 
        
        self.wait(2)
        
        self.play(self.camera.frame.animate.set_width(x).move_to(ORIGIN)) #Vuelvo a la cámara original


        self.play(d.animate.shift(1.2*LEFT), ChangeDecimalToValue(de,0.7),t_6.animate.shift(1.2*LEFT))

        self.play(d.animate.shift(0.3412*RIGHT), ChangeDecimalToValue(de,0.7853),
        t_6.animate.shift(0.3412*RIGHT))

        c= d.copy() #clona el punto de pi/4

        self.play(Transform(c,p)) #Transforma el punto en texto


        r_1 = Rectangle(width=.4, height=0.65, color = "#4CAF50").shift(1.29*LEFT + 0.05*UP)

        r_2 = Rectangle(width=.4, height=0.65, color = "#4CAF50").shift(0.46*LEFT + 0.05*UP)

        r_3 = Rectangle(width=.4, height=0.65, color = "#4CAF50").shift(.35 *RIGHT + 0.05*UP)

        q_1 = Rectangle(width=.4, height=0.65, color = PINK).shift(0.875*LEFT+ 0.05*UP)

        q_2 = Rectangle(width=.4, height=0.65, color = PINK).shift(0.045*LEFT+ 0.05*UP)

        q_3 = Rectangle(width=.4, height=0.65, color = PINK).shift(0.765*RIGHT+ 0.05*UP)
        # pi/4 = 0.785398... 
        
        self.add(r_1,r_2,r_3)


        self.add(q_1,q_2,q_3)


        self.wait(2)

class Cantor3(MovingCameraScene):
    def construct(self):


#--------------------------------- Mobjects -----------------------------------------
     
        # Cuadrados
        s_1 = Square(3.2, color="#00008B", fill_opacity=0.4).move_to([-3.5, 5, 0])
        s_2 = Square(3.2, color="#00008B", fill_opacity=0.4).move_to([2.4, 5, 0])
        s_3 = Square(3.2, color="#00008B", fill_opacity=0.4).move_to([-3.5, -2, 0])
        s_4 = Square(3.2, color="#00008B", fill_opacity=0.4).move_to([2.4, -2, 0])
        
        #lineas
        l_1 = Line([-5.1, 1, 0], [-1.9, 1, 0], color="#FE0000")
        l_2 = Line([0.8, 1, 0],  [4, 1, 0], color="#FE0000")
        l_3 = Line([-5.1, -6, 0], [-1.9, -6, 0], color="#FE0000")
        l_4 = Line([0.8, -6, 0], [4, -6, 0], color="#FE0000")


        #copias

        c_1 = l_1.copy().set_stroke(opacity = 0.4)
        c_2 = l_2.copy().set_stroke(opacity = 0.4)
        c_3 = l_3.copy().set_stroke(opacity = 0.4)
        c_4 = l_4.copy().set_stroke(opacity = 0.4)

#------------------------------ Puntos ----------------------------

        p_1 = np.array([-4.5, -1.5, 0]) 
        p_2 = np.array([-3, -1, 0]) 
        p_3 = np.array([-2, -1.4, 0])
        p_4 = np.array([-4, -5, 0])
        p_5 = np.array([-4.5,-3,0])

        
#------------------------- Transfomraciones --------------------------------


        t_1 = s_1.copy().set_color("#FE0000").set_opacity(1)
        t_2 = Line([0.8,3.4,0],[4,6.6,0],color ="#FE0000") 
        t_3 = bezier([p_1,p_2,p_3,p_4,
        p_5,p_1] )
        ft_3 = ParametricFunction(t_3 ,t_range = (0, 1)
        , fill_opacity =1 ).set_color("#FE0000")
        


        t_4 = Text("Sigueme",font_size = 40, font = "american_typewriter"
                  , color ="#FE0000" ,
                  stroke_color = BLACK ).move_to([2.4, -2, 0]
                    ).set_stroke(width = 0)


#------------------------- Animaciones ------------------------------------

        self.add(s_1,s_2,s_3,s_4, 
        l_1,l_2,l_3,l_4,
        c_1,c_2,c_3,c_4)

        self.wait()

        self.play(Transform(l_1,t_1))

        self.wait(3)
        
        self.play(Transform(l_2,t_2),

        Transform(l_3,ft_3),Transform(l_4,t_4) )


        self.wait(3)

class Cantor4(MovingCameraScene):
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

        d = Dot([-3,-4,0], color = BLACK)

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


        de = DecimalNumber(0, num_decimal_places=4, include_sign=False, font_size=42, color =  BLACK )
        
        t_6 = MathTex(r"\ldots ", font_size = 40, color = BLACK)

        t_6.next_to(d,2.4*RIGHT + 0.9*UP)




        def next(object,dir,t):
            def updater(mob):
                mob.next_to(object,dir, buff = t)
            return updater

            

        de.add_updater(next(d,UP,0.2))



        p = MathTex(r"\dfrac{\pi}{4} = 0.71", color = BLACK)

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

    
class Prueba(Scene):
    def construct(self):
        p0 = LEFT
        p1 = 2 * UP + LEFT
        p2 = 2 * DOWN + RIGHT
        p3 = RIGHT


        bez = bezier([p0, p1, p2, p3,p0])
        pop=ParametricFunction(bez, t_range = (0, 1), fill_opacity=1).set_color("#FE0000")

        # Mostrar la curva en la escena
        
        self.play(Create(pop))

        self.wait(1)