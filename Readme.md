# <b><u>Asana AI</u></b>

The AsanaAI application is a Virtual Yoga Asana Assistant that uses Machine Learning and Django. The application is built using the Django framework and various Python libraries to accurately identify pre-trained Yoga asanas within the model.

## <u>Steps to use the application:</u>
1. Clone the repository into the system using the command "git clone https://github.com/yaswanthsai002/AsanaAI"
2. Open a terminal in the folder location and create a virtual environment using the command "python -m venv <name-of-environment\>"
3. Activate the environment using the command ".\<name-of-environment\>\Scripts/activate" (windows) or "source <name-of-environmet/>/bin/activate" (macOS or Linux)
4. Install the requirements from requirements.txt using the command "pip install -r requirements.txt --upgrade"
5. Run the Data Collection.py file using the command "python app/data_collection.py"
6. Run the Data Training.py file using the command "python app/data_training.py"
7. Apply makemigrations using the command "python manage.py makemigrations app"
8. Apply migrate using the command "python manage.py migrate"
9. Run Django Server using the command "python manage.py runserver"
10. Wait for the server to start and click on the link (http://127.0.0.1:8000) or copy it and paste it in the browser given in the terminal.

<b><u><i><Note:></u></b> If anyone uses a Linux distribution like ubuntu they have to install the libraries or packages mentioned in Aptfile using command "sudo apt-get update && sudo apt-get install -y $(cat Aptfile)"</i>

## <u>Stages of the Application</u>:

### 1) <i>Data Collection</i>
It is a process of collection of landmarks of joints in a human body. To perform this process we use two modules called OpenCV, Mediapipe.

Image dataset of Yoga Asana is taken from here - https://www.kaggle.com/datasets/niharika41298/yoga-poses-dataset

#### a) <i>OpenCV</i> - It is used to perform operations on images like reading, writing etc. For more information please refer to this - https://opencv.org/

![image](https://user-images.githubusercontent.com/57896227/206229705-4bd49e14-af95-4cab-b230-89347905d041.png)
                                                    
             Fig:- OpenCV Face Detection (Sample Example)

#### b) <i>Mediapipe</i> - It is used to perform landmark detection of keypoints in a human body. For more information please refer to this - https://mediapipe.dev/

![image](https://user-images.githubusercontent.com/57896227/206228479-c8fd39f8-58a1-43de-8539-9c1f6e880caf.png)

             Fig:- Mediapipe Holistic Pipeline Sample
                                                     
After performing all these steps all the landmarks of the body keypoints are stored in a.csv file which is used for further processing.

### 2) <i>Data Training</i>
It is a process of reading, extracting the values from .csv file.These extracted values are used for training our ML model. Here we use Random Forest Algorithm as best optimal solution as it fits our problem. The trained model will be saved by using pickle module which will be used for predicting the asanas in the real time.

### 3) <i>Pose Estimation</i>
Final stage of the process where we use the pre-trained ML model for predicting Yoga asanas in the real time using Webcam feed of the device.It shows the landmarks of the keypoints in red colour if the machine is not able to recognize the asana (Incoorect way of doing) and turns into green colour if the machine recognizes the asana (Correct way of doing).

![Screenshot (22)](https://user-images.githubusercontent.com/57896227/230847947-3c60a91e-5788-4711-992c-b31d66deb1d2.png)

        Fig:- Model detecting the Asana
