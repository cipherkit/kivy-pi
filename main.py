'''

==============

It shows a window with
a buttoned labelled 'play' to turn the camera on and off. Note that
not finding a camera, perhaps because gstreamer or opencv-python is not installed, will
throw an exception during the kv language processing.

'''

from kivy.logger import Logger
import logging
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.lang import Builder
import time
Logger.setLevel(logging.TRACE)
Builder.load_file("doorbell.kv")


class SuspendedMode(Screen):

    def light_off(self):
        pass

    def suspend(self):
        self.sm.current = 'suspended'
        self.light_off()
        # more suspension here


class MenuScreen(Screen):
    pass


class ViewerScreen(Screen):

    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''

        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        Logger.debug("Screen Captured.")


class SettingsMenu(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(ViewerScreen(name='viewer'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsMenu(name='settings'))
sm.add_widget(SuspendedMode(name='suspend'))


class DoorBell(App):

    def build(self):
        return sm


if __name__ == "__main__":
    app = DoorBell()
    app.run()
