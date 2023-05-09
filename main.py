import vk_api
from kivy.app import App
from kivy.uix.label import Label

import vk_api
from vk_api import audio

class MainApp(App):
    def build(self):
        vk_session = vk_api.VkApi(
            '+79201798938',
            'maksArhipov567',
            api_version='5.81'
        )
        vk_session.auth()
        vk_audio = vk_api.audio.VkAudio(vk_session)

        q = 'Skrillex'
        i = next(vk_audio.search_iter(q=q))

        label = Label(text=i['artist'],
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})

        return label


if __name__ == '__main__':
    app = MainApp()
    app.run()

