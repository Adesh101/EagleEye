from tkinter import *
from PIL import ImageTk,Image
import os
import json
import openpyxl
from tkinter import messagebox
import requests as reqAPI
import faceRecognition as fr
import cv2
import numpy as np
import excel
import time


root = Tk()
root.title("Eagle Eye")
root.geometry("1070x800")
root.configure(background='white')
root.resizable(False,False)
# e=Entry(root,width=20)
# # e.insert(0,"Enter your name:")
# e.grid(row=0)

global first
first = 1

global managestudents
managestudents=False

global frameManageStudents
frameManageStudents = LabelFrame(root,borderwidth=0,highlightthickness=0)



global requests
requests=False

global trainSystem
trainSystem=False

global lecturesBool
lecturesBool=False


global studentsBool
studentsBool=False











def checkAttendance():
    # os.system("open attendance.xlsx")

    os.startfile("C:/Users/vrush/PycharmProjects/project_new/attendance_files/sheets/")




def trainsystem():
    global studentsBool
    if studentsBool:
        global frameStudents
        frameStudents.grid_forget()
    global lecturesBool
    if lecturesBool:
        global frameLectures
        frameLectures.grid_forget()
    global requests
    if requests:
        global frameMain
        frameMain.grid_forget()

    global managestudents
    if managestudents:
        global frameManageStudents
        frameManageStudents.grid_forget()
    global frameTrainSystem
    frameTrainSystem = LabelFrame(root,borderwidth=0,highlightthickness=0)
    frameTrainSystem.grid(row=2,column=0,columnspan=4)
    print("it'll launch the program to train the system")
    trainimageTK = ImageTk.PhotoImage(Image.open("loading.gif"))
    trainimage = Label(frameTrainSystem,image=trainimageTK,pady=200,padx=120)
    trainimage.image=trainimageTK
    trainimage.grid()


    faces, faceID = fr.labels_for_training_data('C:/Users/vrush/PycharmProjects/project_new/trainingImages')
    # print(faceID)
    # print(faces)
    face_recognizer = fr.train_classifier(faces, faceID)
    face_recognizer.save('trainingData.yml')
    messagebox.showinfo("Title", "Successfully Trained \n Thank You!!")

    global trainSystem
    trainSystem=True







def insertAPI(rollno,semester,facebookURL):
    print(rollno)
    print(semester)
    print(facebookURL)
    print('''----NOTE---------------
    after completion of the project
    this method will store the data in the main server''')
    sem = semester
    rollno = rollno

    take_name = sem + rollno
    cap = cv2.VideoCapture("take_sample.mp4")

    os.mkdir('C:/Users/vrush/PycharmProjects/project_new/trainingImages/' + take_name)

    num = 1
    while True:
        ret, test_img = cap.read()  # captures frame and returns boolean value and captured image

        temp_img = test_img.copy()
        faces_detected, gray_img = fr.faceDetection(test_img)

        # num=num+1
        # if(num<=50):
        #     break
        for (x, y, w, h) in faces_detected:
            cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=7)

        font = cv2.FONT_HERSHEY_SIMPLEX
        for face in faces_detected:
            (x, y, w, h) = face
            roi_gray = gray_img[y:y + h, x:x + h]
            font = cv2.FONT_HERSHEY_SIMPLEX
            if (num == 51):
                break

            if (num <= 50):
                cv2.imwrite(
                    'C:/Users/vrush/PycharmProjects/project_new/trainingImages/' + take_name + '/' + str(num) + '.jpg',
                    roi_gray)
                cv2.putText(test_img, str(num), (x, y), font, 1, (200, 255, 255))
                # time.sleep(1)

            num = num + 1

        resized_img = cv2.resize(test_img, (1000, 700))
        cv2.imshow('face detection Tutorial ', resized_img)
        cv2.waitKey(10)
        if cv2.waitKey(10) == ord('q'):  # wait until 'q' key is pressed
            break
        if num == 51:
            messagebox.showinfo("title","Successfully Added")
            break
    # q
    cap.release()
    cv2.destroyAllWindows()


def scrapAPI():
    print("It'll start scraping for facebook images of the student.")





def managestudents():
    global lecturesBool
    if lecturesBool:
        global frameLectures
        frameLectures.grid_forget()
    global studentsBool
    if studentsBool:
        global frameStudents
        frameStudents.grid_forget()
    global trainSystem

    if trainSystem:
        global frameTrainSystem
        frameTrainSystem.grid_forget()

    global requests

    if requests:
        global frameMain
        frameMain.grid_forget()
        frameMain.grid_forget()
    # root.geometry("800x800")



    global frameManageStudents
    frameManageStudents = LabelFrame(root,borderwidth=0,highlightthickness=0)
    frameManageStudents.grid(row=2, column=0, columnspan=5)

    enrollmentnoText = Label(frameManageStudents,text="Semester:",font=("Aerial",22),padx=20,anchor="w")
    enrollmentnoText.grid(row=0,column=0)

    semesterEntry = Entry(frameManageStudents, width=45)
    semesterEntry.grid(row=0, column=1, sticky="W")

    firstnameText = Label(frameManageStudents,text="Roll no:",font=("Aerial",22),padx=20,anchor="w")
    firstnameText.grid(row=1,column=0)

    rollnoEntry = Entry(frameManageStudents, width=45)
    rollnoEntry.grid(row=1, column=1, sticky="W")

    # middlenameText = Label(frameManageStudents, text="Middle Name:", font=("Aerial", 22), padx=20, anchor="w")
    # middlenameText.grid(row=1, column=0)
    #
    # middlenameEntry = Entry(frameManageStudents, width=20)
    # middlenameEntry.grid(row=1, column=1, sticky="W")
    #
    # lastnameText = Label(frameManageStudents, text="Last Name:", font=("Aerial", 22), padx=20, anchor="w")
    # lastnameText.grid(row=1, column=2)
    #
    # lastnameEntry = Entry(frameManageStudents, width=30)
    # lastnameEntry.grid(row=1, column=4, sticky="W")
    #
    # contactText = Label(frameManageStudents, text="Contact No:", font=("Aerial", 22), padx=20, anchor="w")
    # contactText.grid(row=2, column=0)
    #
    # contactEntry = Entry(frameManageStudents, width=20)
    # contactEntry.grid(row=2, column=1, sticky="W")
    #
    # emailText = Label(frameManageStudents, text="Email ID:", font=("Aerial", 22), padx=20, anchor="w")
    # emailText.grid(row=2, column=2)
    #
    # emailEntry = Entry(frameManageStudents, width=30)
    # emailEntry.grid(row=2, column=4, sticky="W")

    # facebookURLText = Label(frameManageStudents, text="Facebook URL:", font=("Aerial", 22), padx=20, anchor="w")
    # facebookURLText.grid(row=3, column=0)
    #
    # facebookURLEntry = Entry(frameManageStudents, width=45)
    # facebookURLEntry.grid(row=3, column=1, sticky="W",columnspan=4)

    emptyLine = Label(frameManageStudents)
    emptyLine.grid(row=4,column=0,columnspan=5)

    #
    # insert_btn = Button(frameManageStudents, text="Insert Data", font=("Aerial", 20), command=lambda: insertAPI(enrollmentnoEntry.get(),firstnameEntry.get(),middlenameEntry.get(),lastnameEntry.get(),contactEntry.get(),emailEntry.get(),facebookURLEntry.get()), bg="#273c75",fg="white")
    # insert_btn.grid(row=5, column=1, columnspan=1, stick="w")

    take_btn = Button(frameManageStudents, text="Take Photo", font=("Aerial", 20),
                        command=lambda: insertAPI(rollnoEntry.get(), semesterEntry.get()), bg="#273c75",fg="white")
    take_btn.grid(row=5, column=2, columnspan=1, stick="w",padx="20")

    # scrap_btn = Button(frameManageStudents, text="Web Scrap", font=("Aerial", 20), command=lambda: scrapAPI(), bg="#273c75",fg="white")
    # scrap_btn.grid(row=5,column=3,stick="w")





    global managestudents
    managestudents=True







def loginbuttonPressed(username,password):
    with open("credentials.JSON") as c:
        credentials = json.load(c)
        try:
            if credentials[username] == password:
                menu1.config(state="normal")
                menu2.config(state="normal")
                menu3.config(state="normal")
                menu4.config(state="normal")
                menu5.config(state="normal")
                load.grid_forget()
                request()
        except:
            messagebox.showinfo("Title", "Wrong credentials")
            print("no such value exists")










def sendAPI():
    # enter the code to send the request to server
    # global frameMain
    # frameMain.grid_forget()
    return






def checkButtonPressed():
    # checkWindow = Toplevel()
    # #checkWindow.geometry("400x400")
    # checkImageTk = ImageTk.PhotoImage(Image.open("default.jpg"))
    # checkImage = Label(checkWindow,image=checkImageTk)
    # checkImage.image=checkImageTk
    # checkImage.grid(row=0,column=0)
    print("check button")
    os.startfile("C:/Users/vrush/PycharmProjects/project_new/attendance_files/undetected_faces/")


def acceptRequest(idValue,rollnoValue,nameValue):
    print(idValue)
    data = {
        "id": idValue,
        "name":nameValue,
        "enroll":rollnoValue
    }
    res = reqAPI.post(url="http://localhost:3000/users/accept_request", data=data)

    resdata = res.text
    if (resdata):
        print("request accepted")
        global frameMain
        frameMain.grid_forget()
        request()

    else:
        print("error")

    return True

def rejectRequest(idValue):
    print(idValue)
    print(idValue)
    data = {
        "id": idValue,
    }
    res = reqAPI.post(url="http://localhost:3000/users/reject_request", data=data)

    resdata = res.text
    if (resdata):
        print("request accepted")
        global frameMain
        frameMain.grid_forget()
        request()

    else:
        print("error")

    return True



def request():
    # maincontent = Label(root,  padx=0, pady=0, font=("Aerial", 22))
    # maincontent.grid(row=1, column=1, rowspan=100)
    #
    #
    #root.geometry("863x800")
    global trainSystem
    if trainSystem:
        global frameTrainSystem
        frameTrainSystem.grid_forget()
    global managestudents
    if managestudents:
        global frameManageStudents
        frameManageStudents.grid_forget()



    global frameMain
    frameMain = LabelFrame(root,borderwidth=0,highlightthickness=0)
    frameMain.grid(row=2,column=0,columnspan=4)


    # fromText = Label(frameMain,text="From: ",font=("Aerial",22),padx=20,anchor="w")
    # fromText.grid(row=2,column=0,sticky=E)
    # #
    #
    # fromEntry = Entry(frameMain,width=30)
    # fromEntry.grid(row=2,column=1,sticky="W")
    #
    # sbmt_btn = Button(frameMain,text="Submit",font=("Aerial",20),command=sendAPI,bg="#273c75")
    # sbmt_btn.grid(row=2,column=2,columnspan=2,stick="w")

    yourRequests = Label(frameMain, text = "Your Requests", font=("Aerial",22))
    yourRequests.grid(row=3,column=0,columnspan=4)

    res = reqAPI.get(url="http://localhost:3000/users/get_student_requests")
    resdata = json.loads(res.text)
    print(resdata)
    temp=4
    for i in range(len(resdata)):
        print(resdata[i]['date'])

        if(resdata[i]['status']=='Pending'):
            frame1 = LabelFrame(frameMain,padx=200,pady=10)
            frame1.grid(row=temp+i,columnspan=4,padx=20,pady=20)

            # date = Label(frame1,text="Date: ",font=("Aerial",12))
            # date.grid(row=0,column=0,columnspan=5,sticky="W")

            dateValue = Label(frame1, text=resdata[i]['date'],font=("Aerial",12))
            dateValue.grid(row=0, column=6, columnspan=5, sticky="W")

            # name = Label(frame1, text="Name: ", font=("Aerial", 12))
            # name.grid(row=0, column=12, columnspan=5, sticky="W")

            nameValue=Label(frame1, text=resdata[i]['name'],font=("Aerial",12))
            nameValue.grid(row=0,column=15)

            semesterValue = Label(frame1, text=resdata[i]['semester'], font=("Aerial", 12))
            semesterValue.grid(row=0, column=17)

            rollnoValue = Label(frame1, text=resdata[i]['enrollment'], font=("Aerial", 12))
            rollnoValue.grid(row=0, column=18)

            name = Label(frame1, text="Lec:", font=("Aerial", 12))
            name.grid(row=0, column=20, columnspan=5, sticky="W")

            lectureValue = Label(frame1, text=resdata[i]['lecture'], font=("Aerial", 12))
            lectureValue.grid(row=0, column=25)

            idValue = Label(frame1, text=resdata[i]['_id'], font=("Aerial", 12))
            idValue.grid(row=0, column=25)
            idValue.grid_forget()

            AcceptButton = Button(frame1,text= "ACCEPT",font=("Aerial",14),bg="#273c75",fg="white",borderwidth=0,command=lambda:acceptRequest(idValue.cget("text"),rollnoValue.cget("text"),nameValue.cget("text")))
            AcceptButton.grid(row=0,column=35,padx=5,sticky="E")

            RejectButton = Button(frame1,text= "REJECT",font=("Aerial",14),bg="#273c75",fg="white",borderwidth=0,command=lambda:rejectRequest(idValue.cget("text")))
            RejectButton.grid(row=0,column=36,padx=5,sticky="E")

            Checkbutton = Button(frame1, text="CHECK", font=("Aerial", 14),bg="#273c75",fg="white",borderwidth=0,command=checkButtonPressed)
            Checkbutton.grid(row=0, column=37, padx=5, sticky="E")



    global requests
    requests = True




def registerbuttonPressed(username,password):
    print(username)
    print(password)


def startAttendance():
    os.system("python tester_video.py")





def showBTNInLectures(clicked,lectureEntry):
    lectureEntry.delete(0,END)
    value = clicked.get()
    if value == "January":
        index=0
    elif value == "February":
        index=1
    elif value == "March":
        index=2
    elif value == "April":
        index=3
    elif value == "May":
        index=4
    elif value == "June":
        index=5
    elif value == "July":
        index=6
    elif value == "August":
        index=7
    elif value == "September":
        index=8
    elif value == "October":
        index=9
    elif value == "November":
        index=10
    elif value == "December":
        index=11
    lecturesPerMonth = [20, 30, 20, 10, 50, 60, 70, 80, 90, 10, 11, 12]

    lectureEntry.insert(0,str(lecturesPerMonth[index]))

    # print(index)

def updateBTNInLectures(lectureEntry):
    print("Update "+str(lectureEntry.get()))

def lectures():
    global requests
    global studentsBool


    if requests:
        global frameMain
        frameMain.grid_forget()
        frameMain.grid_forget()


    if studentsBool:
        global frameStudents
        frameStudents.grid_forget()


    global trainSystem
    if trainSystem:
        global frameTrainSystem
        frameTrainSystem.grid_forget()
    global managestudents
    if managestudents:
        global frameManageStudents
        frameManageStudents.grid_forget()

    global frameLectures
    frameLectures = LabelFrame(root, borderwidth=0, highlightthickness=0)
    frameLectures.grid(row=2, column=0, columnspan=6)

    clicked = StringVar()

    Label(frameLectures, text="      ").grid(row=0, columnspan=6)

    clicked.set("January")

    drop = OptionMenu(frameLectures,clicked,"January","February","March","April","May","June","July","August","September","October","November","December")
    drop.grid(row=1,column=1,padx=10,sticky="e")

    show_btn = Button(frameLectures, text="Show", font=("Aerial", 20), command=lambda : showBTNInLectures(clicked,lectureEntry), highlightbackground="#273c75")
    show_btn.grid(row=1, column=2, stick="E")


    Label(frameLectures,text="      ").grid(row=2,columnspan=6)


    lectureEntry = Entry(frameLectures, width=20)
    lectureEntry.grid(row=3, column=0, sticky="W",columnspan=5)

    update_btn = Button(frameLectures, text="Update", font=("Aerial", 20), command=lambda : updateBTNInLectures(lectureEntry),
                      highlightbackground="#273c75")
    update_btn.grid(row=3, column=6, stick="w")


    lecturesPerMonth = [20,30,20,10,50,60,70,80,90,10,11,12]




    global lecturesBool
    lecturesBool=True



def showBTNInStudents(enrollEntry,clicked1):
    enrollEntry.delete(0,END)

    enrollEntry.insert(0,str(clicked1.get()))

def updateBTNInStudents(enrollmentnoEntry, nameEntry, departmentEntry,semesterEntry,contactEntry,emailEntry,clicked1):
    print("Update")

def students():
    global requests

    if requests:
        global frameMain
        frameMain.grid_forget()
        frameMain.grid_forget()

    global trainSystem
    if trainSystem:
        global frameTrainSystem
        frameTrainSystem.grid_forget()
    global managestudents
    if managestudents:
        global frameManageStudents
        frameManageStudents.grid_forget()

    global lecturesBool
    if lecturesBool:
        global frameLectures
        frameLectures.grid_forget()




    global frameStudents
    frameStudents = LabelFrame(root, borderwidth=0, highlightthickness=0)
    frameStudents.grid(row=2, column=0, columnspan=6)

    clicked1 = StringVar()

    Label(frameStudents, text="      ").grid(row=0, columnspan=6)

    clicked1.set("Select Student")

    dp = OptionMenu(frameStudents, clicked1, "160320107062","160320107060","160320107061")
    dp.grid(row=1, column=1, padx=10, sticky="e")

    show_btn = Button(frameStudents, text="Show", font=("Aerial", 20), highlightbackground="#273c75")
    show_btn.grid(row=1, column=2, stick="E")

    enrollmentnoText = Label(frameStudents, text="Enroll No:", font=("Aerial", 22), padx=20, anchor="w")
    enrollmentnoText.grid(row=2, column=0)

    enrollmentnoEntry = Entry(frameStudents, width=20)
    enrollmentnoEntry.grid(row=2, column=1, sticky="W")

    show_btn.config(command=lambda :showBTNInStudents(enrollmentnoEntry,clicked1))

    nameText = Label(frameStudents, text="Name:", font=("Aerial", 22), padx=20, anchor="w")
    nameText.grid(row=2, column=2)

    nameEntry = Entry(frameStudents, width=30)
    nameEntry.grid(row=2, column=4, sticky="W")

    departmentText = Label(frameStudents, text="Department:", font=("Aerial", 22), padx=20, anchor="w")
    departmentText.grid(row=3, column=0)

    departmentEntry = Entry(frameStudents, width=20)
    departmentEntry.grid(row=3, column=1, sticky="W")

    semesterText = Label(frameStudents, text="Semester:", font=("Aerial", 22), padx=20, anchor="w")
    semesterText.grid(row=3, column=2)

    semesterEntry = Entry(frameStudents, width=30)
    semesterEntry.grid(row=3, column=4, sticky="W")

    contactText = Label(frameStudents, text="Contact No:", font=("Aerial", 22), padx=20, anchor="w")
    contactText.grid(row=4, column=0)

    contactEntry = Entry(frameStudents, width=20)
    contactEntry.grid(row=4, column=1, sticky="W")

    emailText = Label(frameStudents, text="Email ID:", font=("Aerial", 22), padx=20, anchor="w")
    emailText.grid(row=4, column=2)

    emailEntry = Entry(frameStudents, width=30)
    emailEntry.grid(row=4, column=4, sticky="W")

    genderText = Label(frameStudents, text="Gender:", font=("Aerial", 22), padx=20, anchor="w")
    genderText.grid(row=5, column=0)
    #
    # genderEntry = Entry(frameStudents, width=45)
    # genderEntry.grid(row=3, column=1, sticky="W", columnspan=4)



    clicked = StringVar()
    clicked.set("Select Option")

    drop = OptionMenu(frameStudents, clicked, "Male", "Female")
    drop.grid(row=5, column=1, sticky="W", columnspan=4)

    emptyLine = Label(frameStudents)
    emptyLine.grid(row=5, column=0, columnspan=5)

    update_btn = Button(frameStudents, text="Update", font=("Aerial", 20),
                        command=lambda: updateBTNInStudents(enrollmentnoEntry.get(), nameEntry.get(), departmentEntry.get(),
                                                  semesterEntry.get(), contactEntry.get(), emailEntry.get(),
                                                  clicked1.get()), highlightbackground="#273c75")
    update_btn.grid(row=6, column=1, columnspan=1, stick="w")

    global studentsBool
    studentsBool = True

headerframe = LabelFrame(root)
headerframe.grid(columnspan=100,sticky="nsew")


header = Label(headerframe,text="Eagle Eye for Faculty",padx=83,font=("Times New Roman",44),bg="#192a56",fg="white")
header.grid(row=0,column=0,columnspan=3,sticky="w")

menu1 = Button(root,text="Requests",padx=51,font=("Aerial",22), bg="#273c75",fg="white",command=request,state="disabled")
menu1.grid(row=1,column=0,sticky="nsew")

menu2 = Button(root,text="Add Photo",padx=22,font=("Aerial",22), bg="#273c75",fg="white",command=managestudents,state="disabled")
menu2.grid(row=1,column=1,sticky="nsew")

menu3 = Button(root,text="Train System",padx=30,font=("Aerial",22), bg="#273c75",fg="white",command=trainsystem,state="disabled")
menu3.grid(row=1,column=2,sticky="nsew")

menu4 = Button(root,text="Check Attendance",padx=7,font=("Aerial",22), bg="#273c75",fg="white",command=checkAttendance,state="disabled")
menu4.grid(row=1,column=3,sticky="nsew")
menu6 = Button(root,text="Lectures",padx=36,font=("Aerial",22), highlightbackground="#273c75",fg="white",state="disabled",command=lectures)
menu6.grid(row=1,column=4,sticky="nsew")


menu7 = Button(root,text="Update Students",padx=36,font=("Aerial",22), highlightbackground="#273c75",fg="white",state="disabled",command=students)
menu7.grid(row=1,column=5,sticky="nsew")

menu5 = Button(headerframe,text="Start Taking Attendance",padx=7,font=("Aerial",22), bg="#192a56",fg="white",state="disabled",command=startAttendance)
menu5.grid(row=0,column=3,sticky="nsew")


Label(root).grid(row=3,column=0,pady=75)


global load
load = LabelFrame(root,borderwidth=0,highlightthickness=0)
load.grid(row=5,column=0,columnspan=4)
facultylogin = Label(load,text="Faculty Login",padx=205,width=21,font=("Aerial",30))
facultylogin.grid(row=5,columnspan=4,column=0,sticky="nsew")
Label(load).grid(row=6,pady=10)
username = Label(load,text="Username:",font=("Aerial",22),padx=20,anchor="w")
username.grid(row=7,column=1)
usernameEntry = Entry(load, width=30)
usernameEntry.grid(row=7, column=2, sticky="W")
password = Label(load,text="Password:",font=("Aerial",22),padx=20,anchor="w")
password.grid(row=8,column=1)
passwordEntry = Entry(load, width=30,show="*")
passwordEntry.grid(row=8, column=2, sticky="W")
Label(load).grid(row=9,pady=10)
innerload = LabelFrame(load)
innerload.grid(row=10,column=2,sticky="w")
innerload.config(width=20,borderwidth=0,highlightthickness=0)

login_btn = Button(innerload,text="Login",font=("Aerial",22),width=6, bg="#273c75",fg="white",command=lambda: loginbuttonPressed(usernameEntry.get(),passwordEntry.get()))
login_btn.grid(row=0,column=0,sticky="w")
Label(innerload,text="\t").grid(row=0,column=1)
register_btn = Button(innerload,text="Register",font=("Aerial",22),width=6, bg="#273c75",fg="white",command=lambda : registerbuttonPressed(usernameEntry.get(),passwordEntry.get()))
register_btn.grid(row=0,column=2,sticky="e")
Label(root).grid(row=6,column=0,pady=75)



root.mainloop()