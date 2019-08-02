import time
import cv2
import label_image
import os,random
import subprocess
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
mp = 'C:/Program Files (x86)/Windows Media Player/wmplayer.exe'
randomfile = random.choice(os.listdir("F:/Music_player_with_Emotions_recognition-master/songs/fear/"))
print('You are angry !!!! please calm down:) ,I will play song for you :' + randomfile)
file = ('F:/Music_player_with_Emotions_recognition-master/songs/fear/' + randomfile)
subprocess.call([mp, file])