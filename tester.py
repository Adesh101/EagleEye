import cv2
import os
import numpy as np
import faceRecognition as fr

# test_img=cv2.imread('C:/Users/vrush/PycharmProjects/project_new/TestImages/group.jpeg');
#
# faces_detected,gray_img=fr.faceDetection(test_img)
# print("faces_detected:",faces_detected)


# for (x,y,w,h) in faces_detected:
#     cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=1)
#
# resized_img=cv2.resize(test_img,(1000,700))
#
# cv2.imshow("test",resized_img)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
faces,faceID=fr.labels_for_training_data('C:/Users/vrush/PycharmProjects/project_new/trainingImages')
face_recognizer=fr.train_classifier(faces,faceID)
face_recognizer.save('trainingData.yml')
# #
# face_recognizer=cv2.face.LBPHFaceRecognizer_create()
# face_recognizer.read('C:/Users/vrush/PycharmProjects/project_new/trainingData.yml')
# name={0: "Donald Trump", 1: "Bill Gates",2: "Elon Musk", 3: "Jeff",4: "Obama",5:"Kirtan",6:"Vrushang",7:"Adesh"}
#
# for face in faces_detected:
#     (x,y,w,h)=face
#     roi_gray=gray_img[y:y+h,x:x+h]
#     label,confidence=face_recognizer.predict(roi_gray)
#     print("confidence:",confidence)
#     print("LABEL:",label)
#     if(confidence<20):
#         fr.draw_rect(test_img, face)
#         predicted_name = name[label]
#         fr.put_text(test_img, predicted_name, x, y)
#     else:
#         fr.draw_rect(test_img, face)
#         # predicted_name = name[label]
#         fr.put_text(test_img, 'unknown', x, y)
#
#
#
#
# resized_img=cv2.resize(test_img,(1000,700))
# cv2.imshow("test",resized_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()