import nfc_lib
import music_lib

while True:
    uid = nfc_lib.get_uid()
    if uid:
        print('Playing music')
        music_lib.play_music()

