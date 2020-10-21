'''

==============

It shows a window with
a buttoned labelled 'play' to turn the camera on and off. Note that
not finding a camera, perhaps because gstreamer or opencv-python is not installed, will
throw an exception during the kv language processing.

'''

# Uncomment these lines to see all the messages
from kivy.logger import Logger
import logging

from kivy.uix.floatlayout import FloatLayout

Logger.setLevel(logging.TRACE)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time

Builder.load_file("doorbell.kv")


class DoorBell(BoxLayout):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.capture()

    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''

        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")


class Main(App):

    def build(self):
        return DoorBell()


Main().run()
