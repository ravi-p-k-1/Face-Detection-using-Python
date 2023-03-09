Domain: Deep learning
Topic: Human Face Recognition Using Computer Vision

There are various face recognition algorithms available, such as Eigenfaces, Fisherfaces, and Local Binary Patterns Histograms (LBPH). These algorithms extract features from the face, such as texture, shape, and color, and use machine learning techniques to learn a model that can recognize the person.
The proposed approach mainly focusses on the use of libraries Face Recognition and OpenCV based on the SVM model and LBPH algorithm. dlib and numpy packages are required to use the mentioned libraries. 

HOG algorithm is used for face detection. The database is enhanced by capturing different angles of the same individual. The face embedding is a compact and robust representation in the form of 128 measurements of the face that captures its unique characteristics, such as the shape, texture, and color of the facial features.

The face embeddings of the faces in the database are computed in advance, and when a new face is presented, its face embedding is computed and compared with the embeddings in the database using a similarity metric. The face with the closest embedding is considered to be the match.
The matches are represented as a csv file which can further be used as an employee attendance system at the respective firm.


FRONTEND/UI PAGES:

1. app.py - It is the basic template which helps users to navigate through all the menus of the website.

![1](https://user-images.githubusercontent.com/93720368/222942732-a3620954-9516-4e8d-879a-8d88a2cc7dc2.png)


2. aboutus.html - It contains information about the creators of the website.

![7](https://user-images.githubusercontent.com/93720368/222943289-cf18eb86-0544-4245-88d7-81f063cc2c0e.png)

3. feedback.html - It allows users to provide ratings and reviews.

![4](https://user-images.githubusercontent.com/93720368/222942805-b17f819b-37f7-4beb-b369-a36d52de4d71.png)


BACKEND PAGES:

1. main.py - It allows users to detect and recognize faces from the CCTV footage and also distinguishes between known & unknown faces.

![5](https://user-images.githubusercontent.com/93720368/222942817-6a00cf1e-7838-4b43-82fc-01a8b9556343.png)

2. webcam.py - It allows users to detect and recognize faces through their own webcam and also distinguishes between known & unknown faces. 

![6](https://user-images.githubusercontent.com/93720368/222942821-da3d2f5f-a136-486d-abbd-a53bf5d55391.png)

3. attendance.csv - The recognized faces will be marked in the attendance report consisting of employee ID, date and time of arrival.

![2](https://user-images.githubusercontent.com/93720368/222942766-9fbb62d8-4780-4dea-8798-9f2998f8068b.png)


DATASET:

1. known faces - It consists of images of the known faces (people working in the company)
2. VID_20230302_170157.mp4 - It is the CCTV footage consisting of workers whose faces we will have to recognize and mark in attendance report accordingly. 


PS: Due to Uploading limit of Github, we had to compress the video accordingly. This might have affected the accuracy of our model due to decreased video picture quality. However, it is running perfectly fine on the video that was provided to us by the sponsor
