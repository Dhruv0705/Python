from tkinter import * 
import random
import ttkthemes
from tkinter import ttk
from time import sleep
import threading



TotalTime = 60
Time = 0
WrongWords = 0
ElapsedTimeInMinutes = 0

def Start_Timer():
    StartButton.config(state=DISABLED)
    global Time
    TextArea.config(state=NORMAL)
    TextArea.focus()

    for Time in range(1,61):
        Elapsed_Timer_Label.config(text = Time)
        RemainingTime = TotalTime - Time
        Remaining_Timer_Label.config(text = RemainingTime)
        sleep(1)
        root.update()

    TextArea.config(state=DISABLED)
    ResetButton.config(state=NORMAL)

def Stop_Timer():

    StopButton.config(state=DISABLED)
    global Time
    TextArea.config(state=NORMAL)
    TextArea.focus()

    for Time in range(1,61):
        Elapsed_Timer_Label.config(text = Time)
        RemainingTime = TotalTime - Time
        Remaining_Timer_Label.config(text = RemainingTime)
        sleep(0)
        root.update()

    TextArea.config(state=DISABLED)
    ResetButton.config(state=NORMAL)

def Count():

    global WrongWords
    while Time != TotalTime:
        Entered_Paragraph= TextArea.get(1.0,END).split()
        TotalWords=len(Entered_Paragraph)

    TotalWords_Count_Label.config(text=TotalWords)

    Para_Word_List=Label_Paragraph['text'].split()

    for Pair in list(zip(Para_Word_List, Entered_Paragraph)):
        if Pair[0]!= Pair[1]:
            WrongWords+=1

    WrongWords_count_label.config(text=WrongWords)

    ElapsedTimeInMinutes= Time/60
    WPM=(TotalWords-WrongWords)/ElapsedTimeInMinutes
    WPM_Count_Label.config(text=WPM)
    gross_WPM=TotalWords/ElapsedTimeInMinutes
    accuracy=WPM/gross_WPM*100
    accuracy=round(accuracy)
    Accuracy_Percent_Label.config(text=str(accuracy)+'%')


def Start():
    t1=threading.Thread(target = Start_Timer)
    t1.start()

    t2 = threading.Thread(target = Count)
    t2.start()

def Stop():
    t1=threading.Thread(target = Stop_Timer)
    t1.start()

    t2 = threading.Thread(target = Count)
    t2.start()


def Reset():

    global Time, ElapsedTimeInMinutes
    Time = 0
    ElapsedTimeInMinutes = 0
    StartButton.config(state=NORMAL)
    ResetButton.config(state=DISABLED)
    TextArea.config(state=NORMAL)
    TextArea.delete(1.0,END)
    TextArea.config(state=DISABLED)

    Elapsed_Timer_Label.config(text='0')
    Remaining_Timer_Label.config(text='0')
    WPM_Count_Label.config(text='0')
    Accuracy_Percent_Label.config(text='0')
    TotalWords_Count_Label.config(text='0')
    WrongWords_count_label.config(text='0')




########GUI Part

root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('940x735+200+10')
root.resizable(200,200)
root.overrideredirect(True)

mainframe=Frame(root,bd=4)
mainframe.grid()

titleframe=Frame(mainframe,bg='black')
titleframe.grid()

titleLabel=Label(titleframe,text='TypeWriter Speed Test',font=('algerian',28,'bold'),bg='black',fg='white'
                 ,width=38,bd=10)
titleLabel.grid(pady=5)

paragraph_frame=Frame(mainframe)
paragraph_frame.grid(row=1,column=0)

paragraph_list=[
                
                "I walked through the streets of the small town, taking in the sights and sounds of the bustling market. The sun was shining brightly in the clear blue sky, and the air was filled with the smells of fresh produce and handmade crafts. I stopped to admire a beautiful necklace made of seashells, before continuing on my way to the park at the edge of town. There I found a bench to sit on and watched as children played on the swings and slide. It was a peaceful and idyllic scene, and I couldn't help but feel grateful to be alive and able to experience it all.",

                "The sun was setting behind the mountains, casting a warm glow over the small town nestled in the valley below. The streets were quiet, with only a few people out and about, enjoying the cool evening air. As the last rays of sunlight disappeared behind the peaks, the town was plunged into darkness, with only the glow of streetlights and the occasional window to break up the blackness. Despite the tranquility of the scene, there was a sense of tension in the air, as if something was about to happen. Whether it was good or bad, no one could say.",

                "The jungle was alive with the sounds of wildlife and the distant rumble of thunder. The canopy overhead provided some relief from the sweltering heat, but sweat still dripped down my forehead as I trudged through the dense underbrush. I had been hiking for hours and was beginning to lose track of time. Suddenly, I heard a loud snarling noise and froze. I turned slowly to see a jaguar crouched a few feet away, its golden eyes fixed on me with a hunger that sent shivers down my spine. I knew I had to act fast if I wanted to make it out of this encounter alive.",

                "The wind whipped through the trees, sending a shower of red and gold leaves swirling through the air. I walked along the quiet forest path, the crunch of fallen leaves under my feet the only sound. The peaceful solitude was a welcome break from the hustle and bustle of everyday life. As I breathed in the crisp, clean air, I couldn't help but feel a sense of gratitude and contentment. This was exactly what I needed - a chance to escape the noise and chaos and find some much-needed peace and quiet.",

                "The ocean stretched out before me, a vast expanse of blue and green. The water was calm today, the gentle waves lapping at the shore. Seagulls called to each other, their cries echoing over the water. The salty sea breeze filled my lungs as I took a deep breath, the smell of salt and fish and sun-warmed sand. I closed my eyes and let the peace of the beach wash over me, the worries and stresses of daily life melting away. For a moment, I was completely at ease, free to relax and simply be.",
                
                "The desert stretched out in every direction, a vast expanse of sand and rock. The sun beat down from above, its relentless heat almost palpable. I trudged through the sand, my feet heavy and my throat dry. The only sound was the crunch of my footsteps and the occasional call of a far-off bird. Despite the harsh conditions, there was a certain beauty to the desert - a raw, untamed wilderness that was unlike anything else. As I walked, I couldn't help but feel a sense of awe and respect for this unforgiving landscape.",
                
                "The mountain loomed above me, its peaks kissed by the clouds. I took a deep breath of the thin, cold air and began to climb. The rock was rough under my hands, the slope steep. Sweat beaded on my forehead as I pulled myself up, inch by inch. The view from the top was worth it, I told myself. The sense of accomplishment and the panoramic vista would make it all worth it. And as I reached the summit and saw the world spread out before me, I knew that I was right. The mountain had tested me, pushed me to my limits. And I had conquered it.",
                
                "The winter storm raged outside, the wind howling and the snow swirling through the air. I curled up on the couch, a warm blanket wrapped around me, and let out a contented sigh. There was something so cozy and comforting about a snow day, something about the forced relaxation and the sense of being nestled safely indoors. I picked up my book and settled in, letting the words wash over me as I listened to the storm rage outside. For a moment, all was right with the world.",
            ]   

random.shuffle(paragraph_list)

Label_Paragraph=Label(paragraph_frame,text=paragraph_list[0],wraplength=912,justify=LEFT,font=('arial',14,'bold'))
Label_Paragraph.grid(row=0,column=0)

TextArea_frame=Frame(mainframe)
TextArea_frame.grid(row=2,column=0)

TextArea=Text(TextArea_frame,font=('arial',12,'bold'),width=100,height=7,bd=4,relief=GROOVE,wrap='word'
              ,state=DISABLED)
TextArea.grid()

frame_output=Frame(mainframe)
frame_output.grid(row=3,column=0)

elapsed_time_label=Label(frame_output,text='Elapsed Time',font=('Tahoma',12,'bold'),fg='red')
elapsed_time_label.grid(row=0,column=0,padx=5)

Elapsed_Timer_Label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
Elapsed_Timer_Label.grid(row=0,column=1,padx=5)

remaining_time_label=Label(frame_output,text='Remaining Time',font=('Tahoma',12,'bold'),fg='red')
remaining_time_label.grid(row=0,column=2,padx=5)

Remaining_Timer_Label=Label(frame_output,text='60',font=('Tahoma',12,'bold'))
Remaining_Timer_Label.grid(row=0,column=3,padx=5)

WPM_Label=Label(frame_output,text='WPM',font=('Tahoma',12,'bold'),fg='red')
WPM_Label.grid(row=0,column=4,padx=5)

WPM_Count_Label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
WPM_Count_Label.grid(row=0,column=5,padx=5)

TotalWords_label=Label(frame_output,text='Total Words',font=('Tahoma',12,'bold'),fg='red')
TotalWords_label.grid(row=0,column=6,padx=5)

TotalWords_Count_Label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
TotalWords_Count_Label.grid(row=0,column=7,padx=5)

WrongWords_label=Label(frame_output,text='Wrong Words',font=('Tahoma',12,'bold'),fg='red')
WrongWords_label.grid(row=0,column=8,padx=5)

WrongWords_count_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
WrongWords_count_label.grid(row=0,column=9,padx=5)

accuracy_label=Label(frame_output,text='Accuracy',font=('Tahoma',12,'bold'),fg='red')
accuracy_label.grid(row=0,column=10,padx=5)

Accuracy_Percent_Label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
Accuracy_Percent_Label.grid(row=0,column=11,padx=5)

buttons_Frame=Frame(mainframe)
buttons_Frame.grid(row=4,column=0)

StartButton=ttk.Button(buttons_Frame,text='Start',command=Start)
StartButton.grid(row=0,column=0,padx=10)

StopButton = ttk.Button(buttons_Frame, text='Stop', command=Stop)
StopButton.grid(row=0,column=1,padx=10)

ResetButton=ttk.Button(buttons_Frame,text='Reset',state=DISABLED,command=Reset)
ResetButton.grid(row=0,column=2,padx=10)

exitButton=ttk.Button(buttons_Frame,text='Exit',command=root.destroy)
exitButton.grid(row=0,column=3,padx=10)

keyboard_frame=Frame(mainframe)
keyboard_frame.grid(row=5,column=0)

frame1to0=Frame(keyboard_frame)
frame1to0.grid(row=0,column=0,pady=3)

label1=Label(frame1to0,text='1',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label2=Label(frame1to0,text='2',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label3=Label(frame1to0,text='3',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label4=Label(frame1to0,text='4',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label5=Label(frame1to0,text='5',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label6=Label(frame1to0,text='6',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label7=Label(frame1to0,text='7',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label8=Label(frame1to0,text='8',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label9=Label(frame1to0,text='9',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label0=Label(frame1to0,text='0',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)

label1.grid(row=0,column=0,padx=5)
label2.grid(row=0,column=1,padx=5)
label3.grid(row=0,column=2,padx=5)
label4.grid(row=0,column=3,padx=5)
label5.grid(row=0,column=4,padx=5)
label6.grid(row=0,column=5,padx=5)
label7.grid(row=0,column=6,padx=5)
label8.grid(row=0,column=7,padx=5)
label9.grid(row=0,column=8,padx=5)
label0.grid(row=0,column=9,padx=5)

frameqtop=Frame(keyboard_frame)
frameqtop.grid(row=1,column=0,pady=3)
labelQ=Label(frameqtop,text='Q',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelW=Label(frameqtop,text='W',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelE=Label(frameqtop,text='E',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelR=Label(frameqtop,text='R',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelT=Label(frameqtop,text='T',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelY=Label(frameqtop,text='Y',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelU=Label(frameqtop,text='U',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelI=Label(frameqtop,text='I',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelO=Label(frameqtop,text='O',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelP=Label(frameqtop,text='P',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)

labelQ.grid(row=0,column=0,padx=5)
labelW.grid(row=0,column=1,padx=5)
labelE.grid(row=0,column=2,padx=5)
labelR.grid(row=0,column=3,padx=5)
labelT.grid(row=0,column=4,padx=5)
labelY.grid(row=0,column=5,padx=5)
labelU.grid(row=0,column=6,padx=5)
labelI.grid(row=0,column=7,padx=5)
labelO.grid(row=0,column=8,padx=5)
labelP.grid(row=0,column=9,padx=5)

frameatol=Frame(keyboard_frame)
frameatol.grid(row=2,column=0,pady=3)
labelA=Label(frameatol,text='A',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelS=Label(frameatol,text='S',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelD=Label(frameatol,text='D',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelF=Label(frameatol,text='F',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelG=Label(frameatol,text='G',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelH=Label(frameatol,text='H',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelJ=Label(frameatol,text='J',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelK=Label(frameatol,text='K',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelL=Label(frameatol,text='L',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)

labelA.grid(row=0,column=0,padx=5)
labelS.grid(row=0,column=1,padx=5)
labelD.grid(row=0,column=2,padx=5)
labelF.grid(row=0,column=3,padx=5)
labelG.grid(row=0,column=4,padx=5)
labelH.grid(row=0,column=5,padx=5)
labelJ.grid(row=0,column=6,padx=5)
labelK.grid(row=0,column=7,padx=5)
labelL.grid(row=0,column=8,padx=5)

frameztom=Frame(keyboard_frame)
frameztom.grid(row=3,column=0,pady=3)
labelZ=Label(frameztom,text='Z',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelX=Label(frameztom,text='X',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelC=Label(frameztom,text='C',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelV=Label(frameztom,text='V',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelB=Label(frameztom,text='B',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelN=Label(frameztom,text='N',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelM=Label(frameztom,text='M',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)

labelZ.grid(row=0,column=0,padx=5)
labelX.grid(row=0,column=1,padx=5)
labelC.grid(row=0,column=2,padx=5)
labelV.grid(row=0,column=3,padx=5)
labelB.grid(row=0,column=4,padx=5)
labelN.grid(row=0,column=5,padx=5)
labelM.grid(row=0,column=6,padx=5)

spaceFrame=Frame(keyboard_frame)
spaceFrame.grid(row=4,column=0,pady=3)

labelSpace=Label(spaceFrame,bg='black',fg='white',font=('arial',10,'bold'),width=40,height=2,bd=10,relief=GROOVE)
labelSpace.grid(row=0,column=0)

def changeBG(widget):
    widget.config(bg='blue')
    widget.after(100,lambda : widget.config(bg='black'))


label_numbers=[label1,label2,label3,label4,label5,label6,label7,label8,label9,label0]

label_alphabets=[labelA,labelB,labelC,labelD,labelE,labelF,labelG,labelH,labelI,labelJ,labelK,labelL,labelM,labelN,
                 labelO,labelP,labelQ,labelR,labelS,labelT,labelU,labelV,labelW,labelX,labelY,labelZ]

space_label=[labelSpace]

binding_numbers=['1','2','3','4','5','6','7','8','9','0']

binding_capital_alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',
                           'U','V','W','X','Y','Z']

binding_small_alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
                         'u','v','w','x','y','z']

for numbers in range(len(binding_numbers)):
    root.bind(binding_numbers[numbers],lambda event,label=label_numbers[numbers]:changeBG(label))


for capital_alphabets in range(len(binding_capital_alphabets)):
    root.bind(binding_capital_alphabets[capital_alphabets],lambda event,label=label_alphabets[capital_alphabets]:changeBG(label))

for small_alphabets in range(len(binding_small_alphabets)):
    root.bind(binding_small_alphabets[small_alphabets],lambda event,label=label_alphabets[small_alphabets]:changeBG(label))

root.bind('<space>',lambda event:changeBG(space_label[0]))

root.mainloop()