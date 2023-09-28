import mediapipe as mp
import cv2
import os
import csv
    
mp_holistic = mp.solutions.holistic
holistic = mp_holistic.Holistic(static_image_mode=True, model_complexity=2)

data = []
for p in mp_holistic.PoseLandmark:
        x = str(p)[13:]
        data.append(x + "_x")
        data.append(x + "_y")
        data.append(x + "_z")
        data.append(x + "_visibility")
data.append("NAME_OF_THE_ASANA")

path = 'app/DATASET/TRAIN'

landmarks = []

for asana in os.listdir(path):
    for image in os.listdir(os.path.join(path,asana)):
        image_path = os.path.join(path,asana,image)
        try:
            img = cv2.imread(image_path)
            imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            results = holistic.process(imgRGB)
            if results.pose_landmarks:
                new = []
                for landmark in results.pose_landmarks.landmark:
                    new.append(landmark.x)
                    new.append(landmark.y)
                    new.append(landmark.z)
                    new.append(landmark.visibility)
                new.append(asana)
                landmarks.append(new)
        except Exception as e:
            print(e)

file = open("app/Asana.csv","w")
writer = csv.writer(file)
writer.writerow(data)
writer.writerows(landmarks)
file.close()
