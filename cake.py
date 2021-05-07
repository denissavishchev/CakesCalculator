import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
kivy.config.Config.set('graphics', 'resizable', False)
from kivy.core.window import Window
Window.size = (720,1280)#(340,620)
from kivy.properties import ObjectProperty


class Muffin(FloatLayout):

    text_label = ObjectProperty()
    text_result = ObjectProperty()
    text_circle_top = ObjectProperty()
    text_rect_top = ObjectProperty()
    text_circle_bottom = ObjectProperty()
    text_rect_bottom = ObjectProperty()
    squareButtonTop = ObjectProperty()
    rectButtonTop = ObjectProperty()
    circleButtonTop = ObjectProperty()
    squareButtonDown = ObjectProperty()
    rectButtonDown = ObjectProperty()
    circleButtonDown = ObjectProperty()


    def result(self):
        try:
            if self.circleButtonTop.state == 'down' and self.circleButtonDown.state == 'down':
                self.text_label.text = str(round(int(self.text_circle_bottom.text) * (int(self.text_circle_bottom.text))/(int(self.text_circle_top.text) * (int(self.text_circle_top.text))),4))
            elif self.circleButtonTop.state == 'down' and self.squareButtonDown.state == 'down':
                self.text_label.text = str(round((((int(self.text_circle_bottom.text)) * (int(self.text_circle_bottom.text)))/((((int(self.text_circle_top.text))/2) * ((int(self.text_circle_top.text))/2))*3.1415)), 4))
            elif self.circleButtonTop.state == 'down' and self.rectButtonDown.state == 'down':
                self.text_label.text = str(round((((int(self.text_circle_bottom.text)) * (int(self.text_rect_bottom.text)))/((((int(self.text_circle_top.text))/2) * ((int(self.text_circle_top.text))/2))*3.1415)), 4))

            elif self.squareButtonTop.state == 'down' and self.circleButtonDown.state == 'down':
                self.text_label.text = str(round((((((int(self.text_circle_bottom.text))/2) * ((int(self.text_circle_bottom.text))/2))*3.1415))/((int(self.text_circle_top.text)) * (int(self.text_circle_top.text))), 4))
            elif self.squareButtonTop.state == 'down' and self.squareButtonDown.state == 'down':
                self.text_label.text = str(round((((int(self.text_circle_bottom.text)) * (int(self.text_circle_bottom.text)))/((int(self.text_circle_top.text)) * (int(self.text_circle_top.text)))), 4))
            elif self.squareButtonTop.state == 'down' and self.rectButtonDown.state == 'down':
                self.text_label.text = str(round((((int(self.text_circle_bottom.text)) * (int(self.text_rect_bottom.text)))/((int(self.text_circle_top.text)) * (int(self.text_circle_top.text)))), 4))

            elif self.rectButtonTop.state == 'down' and self.circleButtonDown.state == 'down':
                self.text_label.text = str(round((((((int(self.text_circle_bottom.text))/2) * ((int(self.text_circle_bottom.text))/2))*3.1415))/((int(self.text_circle_top.text)) * (int(self.text_rect_top.text))), 4))
            elif self.rectButtonTop.state == 'down' and self.squareButtonDown.state == 'down':
                self.text_label.text = str(round((((int(self.text_circle_bottom.text)) * (int(self.text_circle_bottom.text)))/((int(self.text_circle_top.text)) * (int(self.text_rect_top.text)))), 4))
            elif self.rectButtonTop.state == 'down' and self.rectButtonDown.state == 'down':
                self.text_label.text = str(round((((int(self.text_circle_bottom.text)) * (int(self.text_rect_bottom.text)))/((int(self.text_circle_top.text)) * (int(self.text_rect_top.text)))), 4))
        except ValueError:
            self.text_label.text = '???'

    def circle_textinput_top(self):
        self.text_circle_top.hint_text = 'Diameter'
        self.text_rect_top.hint_text = ' '
        self.text_rect_top.background_color = (215/255, 231/255, 254/255, 0)

    def square_textinput_top(self):
        self.text_circle_top.hint_text = 'Length'
        self.text_rect_top.hint_text = ' '
        self.text_rect_top.background_color = (215/255, 231/255, 254/255, 0)

    def rect_textinput_top(self):
        self.text_circle_top.hint_text = 'Width'
        self.text_rect_top.hint_text = 'Height'
        self.text_rect_top.background_color = (215 / 255, 231 / 255, 254 / 255, 1)

    def circle_textinput_bottom(self):
        self.text_circle_bottom.hint_text = 'Diameter'
        self.text_rect_bottom.hint_text = ' '
        self.text_rect_bottom.background_color = (215/255, 231/255, 254/255, 0)

    def square_textinput_bottom(self):
        self.text_circle_bottom.hint_text = 'Length'
        self.text_rect_bottom.hint_text = ' '
        self.text_rect_bottom.background_color = (215/255, 231/255, 254/255, 0)

    def rect_textinput_bottom(self):
        self.text_circle_bottom.hint_text = 'Width'
        self.text_rect_bottom.hint_text = 'Height'
        self.text_rect_bottom.background_color = (215 / 255, 231 / 255, 254 / 255, 1)

    def circle_button_top(self):
        if self.circleButtonTop.state == 'down':
            self.rectButtonTop.state = 'normal'
            self.squareButtonTop.state = 'normal'
        elif self.circleButtonTop.state == 'normal':
            self.circleButtonTop.state = 'down'
        else:
            self.rectButtonTop.state = 'normal'
            self.squareButtonTop.state = 'normal'

    def rect_button_top(self):
        if self.rectButtonTop.state == 'down':
            self.circleButtonTop.state = 'normal'
            self.squareButtonTop.state = 'normal'
        elif self.rectButtonTop.state == 'normal':
            self.rectButtonTop.state = 'down'
        else:
            self.circleButtonTop.state = 'normal'
            self.squareButtonTop.state = 'normal'

    def square_button_top(self):
        if self.squareButtonTop.state == 'down':
            self.rectButtonTop.state = 'normal'
            self.circleButtonTop.state = 'normal'
        elif self.squareButtonTop.state == 'normal':
            self.squareButtonTop.state = 'down'
        else:
            self.rectButtonTop.state = 'normal'
            self.circleButtonTop.state = 'normal'

    def circle_button_down(self):
        if self.circleButtonDown.state == 'down':
            self.rectButtonDown.state = 'normal'
            self.squareButtonDown.state = 'normal'
        elif self.circleButtonDown.state == 'normal':
            self.circleButtonDown.state = 'down'
        else:
            self.rectButtonDown.state = 'normal'
            self.squareButtonDown.state = 'normal'

    def rect_button_down(self):
        if self.rectButtonDown.state == 'down':
            self.circleButtonDown.state = 'normal'
            self.squareButtonDown.state = 'normal'
        elif self.rectButtonDown.state == 'normal':
            self.rectButtonDown.state = 'down'
        else:
            self.circleButtonDown.state = 'normal'
            self.squareButtonDown.state = 'normal'

    def square_button_down(self):
        if self.squareButtonDown.state == 'down':
            self.rectButtonDown.state = 'normal'
            self.circleButtonDown.state = 'normal'
        elif self.squareButtonDown.state == 'normal':
            self.squareButtonDown.state = 'down'
        else:
            self.rectButtonDown.state = 'normal'
            self.circleButtonDown.state = 'normal'


class Cake(App):
    def build(self):
        Window.clearcolor = (1, .4, 0, 1)
        return Muffin()
if __name__=="__main__":
     Cake().run()