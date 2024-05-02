import tkinter
import os
import time
import csv
#from Klassen import*

global rw,vk,rk,sp

class Buttons():
    def __init__(self):
        global rw
        pass

## Beenden

    def btnBeenden_click(tmp):
        exit()
        
## Speichern
    
    def btnSpeichern_click(tmp):
        rw.Withdraw()
        sp.Deiconify()
        
## Button Zurück
    
    def btnZurück_click(tmp):
        rk.Withdraw()
        vk.Withdraw()
        rw.Deiconify()
        
## Button Zurück aus Speichermenü
        
    def btnZurückSpeichern_click(tmp):
        sp.Withdraw()

## Button Rechnung Vorwärtskalkulation

    def btnBerechnenVK_click(tmp):
        try:
            txtLEP = float (vk.txtLEP.get())
            txtLR = float (vk.txtLR.get())
            txtSkontoL = float (vk.txtSkontoL.get())
            txtBK = float (vk.txtBK.get())
            txtHK = float (vk.txtHK.get())
            txtGe = float (vk.txtGe.get())
            txtSkontoK = float (vk.txtSkontoK.get())
            txtKR = float (vk.txtKR.get())
            
            lblLR = txtLEP * (txtLR/100)
            vk.lblLR["text"] = str(round(float (lblLR), 2))
            
            lblZEP = txtLEP - lblLR
            vk.lblZEP["text"] = str(round(float (lblZEP), 2))
            
            lblSkontoL = lblZEP * (txtSkontoL/100)
            vk.lblSkontoL["text"] = str(round(float (lblSkontoL), 2))
            
            lblBEP = lblZEP - lblSkontoL
            vk.lblBEP["text"] = str(round(float (lblBEP), 2))
            
            lblBPB = lblBEP + txtBK
            vk.lblBPB1["text"] = str(round(float (lblBPB), 2))
            vk.lblBPB2["text"] = str(round(float (lblBPB), 2))
            
            lblHK = lblBPB * (txtHK/100)
            vk.lblHK["text"] = str(round(float (lblHK), 2))
            
            lblSK = lblBPB + lblHK
            vk.lblSK["text"] = str(round(float (lblSK), 2))
            
            lblGe= lblSK * (txtGe/100)
            vk.lblGe["text"] = str(round(float (lblGe), 2))
            
            lblBVK = lblSK + lblGe
            vk.lblBVK["text"] = str(round(float (lblBVK), 2))
            
            lblSkontoK = lblBVK / (1- (txtSkontoK/100)) * (txtSkontoK/100)
            vk.lblSkontoK["text"] = str(round(float (lblSkontoK), 2))
            
            lblZVK = lblBVK + lblSkontoK
            vk.lblZVK["text"] = str(round(float (lblZVK), 2))
            
            lblKR = lblZVK / (1- (txtKR/100)) * (txtKR/100)
            vk.lblKR["text"] = str(round(float (lblKR), 2))
            
            lblLVP = lblZVK + lblKR
            vk.lblLVP["text"] = str(round(float (lblLVP), 2))
            
            active = "vk"
            
        except Exception as e:
            print(e)
            vk.lblLVP["text"] = e
            
## Button Rechnung Rückwärtskalkulation
        
    def btnBerechnenRK_click(tmp):
        try:
            txtLVP = float (rk.txtLVP.get())
            txtKR = float (rk.txtKR.get())
            txtSkontoK = float (rk.txtSkontoK.get())
            txtGe = float (rk.txtGe.get())
            txtHK = float (rk.txtHK.get())
            txtBK = float (rk.txtBK.get())
            txtSkontoL = float (rk.txtSkontoL.get())
            txtLR = float (rk.txtLR.get())
            
            lblKR = txtLVP * (txtKR/100)
            rk.lblKR["text"] = round(float (lblKR), 2)
            
            lblZVP = txtLVP - lblKR
            rk.lblZVP["text"] = round(float (lblZVP), 2)
            
            lblSkontoK = lblZVP * (txtSkontoK/100)
            rk.lblSkontoK["text"] = round(float (lblSkontoK), 2)
            
            lblBVP = lblZVP - lblSkontoK
            rk.lblBVP["text"] = round(float (lblBVP), 2)
            
            #lblGe = lblBVP * (txtGe/100)
            rk.lblGe["text"] = round(float (lblGe), 2)
            
            lblSK = lblBVP - lblGe
            rk.lblSK["text"] = round(float (lblSK), 2)
            
            lblHK = lblSK * (txtHK/100)
            rk.lblHK["text"] = round(float (lblHK), 2)
            
            lblBP= lblSK - lblHK
            rk.lblBP1["text"] = round(float (lblBP), 2)
            rk.lblBP2["text"] = round(float (lblBP), 2)

            lblBEP = lblBP - txtBK
            rk.lblBEP["text"] = round(float (lblBEP), 2)
            
            lblSkontoL = lblBEP * (txtSkontoL/100)
            rk.lblSkontoL["text"] = round(float (lblSkontoL), 2)
            
            lblZEP = lblBEP - lblSkontoL
            rk.lblZEP["text"] = round(float (lblZEP), 2)
            
            lblLR = lblZEP * (txtLR/100)
            rk.lblLR["text"] = round(float (lblLR), 2)
            
            lblLEP = lblZEP - lblLR
            rk.lblLEP["text"] = round(float (lblLEP), 2)
            
        except Exception as e:
            rk.lblLEP["text"] = e
            print(e)

## Button Menüwechsel Vorwärtskalkulation
        
    def btnBezug_click(tmp):
        rw.Withdraw()
        rk.Withdraw()
        vk.Deiconify()
        
## Button Menüwechsel Rückwärtskalkulation
        
    def btnVerkauf_click(tmp):        
        rw.Withdraw()
        vk.Withdraw()
        rk.Deiconify()
        

## Dateien Speichern
        
class DateienSpeichern():
    
    def __init__(self):
        pass
    
## Button Speichern CSV
        
    def btnspeichernCSV_click(tmp):
        try:
            with open("Count.txt", 'r') as F:
                c = int (F.read())
        except:
            c = 0
        with open("Count.txt", 'w') as F:
            F.write (str(c+1))
        Datum = time.ctime()
        name = str(c) + "_" + os.getlogin()+ "_" + Datum.replace(":", "-").replace(" ", "-") + '.csv'
        fields = ['LEP', 'LR', 'ZEP', 'LSko', 'BEP', 'BK', 'BP', 'HK', 'SK', 'Ge', 'BVK', 'KSko', 'ZVK', 'LVP']
        dicCSV = [
                {  'LEP': 	vk.txtLEP.get().replace(".",","),
                   'LR': 	vk.lblLR["text"].replace(".",","),
                   'ZEP': 	vk.lblZEP["text"].replace(".",","),
                   'LSko': 	vk.lblSkontoL["text"].replace(".",","),
                   'BEP': 	vk.lblBEP["text"].replace(".",","),
                   'BK': 	vk.txtBK.get().replace(".",","),
                   'BP': 	vk.lblBPB1["text"].replace(".",","),
                   'HK': 	vk.lblHK["text"].replace(".",","),
                   'SK': 	vk.lblSK["text"].replace(".",","),
                   'Ge': 	vk.lblGe["text"].replace(".",","),
                   'BVK': 	vk.lblBVK["text"].replace(".",","),
                   'KSko': 	vk.lblSkontoK["text"].replace(".",","),
                   'ZVK': 	vk.lblZVK["text"].replace(".",","),
                   'LVP':	vk.lblLVP["text"].replace(".",",")}
                  ]
        with open(name, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields, delimiter=";")
            writer.writeheader()
            writer.writerows(dicCSV)
        sp.Withdraw()
        rk.Withdraw()
        vk.Withdraw()
        rw.Deiconify()
        
## Button Speichern XML
    
    def btnspeichernXML_click(tmp):
        try:
            with open("Count.txt", 'r') as F:
                c = int (F.read())
        except:
            c = 0
        with open("Count.txt", 'w') as F:
            F.write (str(c+1))
        Datum = time.ctime()
        name = str(c) + "_" + os.getlogin()+ "_" + Datum.replace(":", "-").replace(" ", "-") + '.xml'
        datei = open(name,'a')
        datei.write("\nTest")
        datei.close ()
        sp.Withdraw()
        rk.Withdraw()
        vk.Withdraw()
        rw.Deiconify()
        
## Button Speichern JSON
    
    def btnspeichernJSON_click(tmp):
        try:
            with open("Count.txt", 'r') as F:
                c = int (F.read())
        except:
            c = 0
        with open("Count.txt", 'w') as F:
            F.write (str(c+1))
        Datum = time.ctime()
        name = str(c) + "_" + os.getlogin()+ "_" + Datum.replace(":", "-").replace(" ", "-") + '.json'
        datei = open(name,'a')
        datei.write("\nTest")
        datei.close ()
        sp.Withdraw()
        rk.Withdraw()
        vk.Withdraw()
        rw.Deiconify()
        
## Button Speichern SQL
     
    def btnspeichernSQL_click(tmp):
        try:
            with open("Count.txt", 'r') as F:
                c = int (F.read())
        except:
            c = 0
        with open("Count.txt", 'w') as F:
            F.write (str(c+1))
        Datum = time.ctime()
        name = str(c) + "_" + os.getlogin()+ "_" + Datum.replace(":", "-").replace(" ", "-") + '.sql'
        datei = open(name,'a')
        datei.write("\nTest")
        datei.close ()
        sp.Withdraw()
        rk.Withdraw()
        vk.Withdraw()
        rw.Deiconify()


## Hauptmenü

class RechnerWahl():
    global frmMain
    global active

    def __init__(self):
        global frmMain
        global active
        frmMain = tkinter.Tk()
        bt = Buttons()
        frmMain.title("Handelskalkulationsrechner")
        frmMain.wm_geometry("400x250")

        lbl = tkinter.Label(frmMain, text = "Bitte wählen Sie den Rechner aus!", font=('times', 16, 'bold'))
        lbl.pack()

## Buttons

        btnBezug = tkinter.Button(frmMain, text = "Vorwärtskalkulation", command = bt.btnBezug_click)
        btnBezug["height"] = 2
        btnBezug["width"] = 20
        btnBezug.place(x=120,y=50)

        btnVerkauf = tkinter.Button(frmMain, text = "Rückwärtskalkulation", command = bt.btnVerkauf_click)
        btnVerkauf["height"] = 2
        btnVerkauf["width"] = 20
        btnVerkauf.place(x=120,y=120)
        
        btnBeenden = tkinter.Button(frmMain, text = "Beenden", command = bt.btnBeenden_click)
        btnBeenden["height"] = 2
        btnBeenden["width"] = 20
        btnBeenden.place(x=120,y=190)

    def Deiconify(tmp):
        frmMain.deiconify()

    def Withdraw(tmp):
        frmMain.withdraw()
        

## Vorwärtskalkulation    
    
class Vorwärtskalkulation():
    global frmVK
    
    def __init__(self):
        global frmVK
        bt = Buttons()
    
        frmVK = tkinter.Tk()
        frmVK.name="frame"
        frmVK.title("Vorwärtskalkulation")
        frmVK.wm_geometry("1200x600")
        
        lbl = tkinter.Label(frmVK, text = "Vorwärtskalkulation", font=('times', 12, 'bold'))
        lbl.pack()

## VK Buttons

        btnBeenden = tkinter.Button(frmVK, text = "Beenden", command = bt.btnBeenden_click)
        btnBeenden["height"] = 2
        btnBeenden["width"] = 10
        btnBeenden.place(x=420,y=500)

        btnBerechnenVK = tkinter.Button(frmVK, text = "Berechnen", command = bt.btnBerechnenVK_click)
        btnBerechnenVK["height"] = 2
        btnBerechnenVK["width"] = 10
        btnBerechnenVK.place(x=120,y=500)

        btnSpeichern = tkinter.Button(frmVK, text = "Speichern", command = bt.btnSpeichern_click)
        btnSpeichern["height"] = 2
        btnSpeichern["width"] = 10
        btnSpeichern.place(x=220,y=500)

        btnZurück = tkinter.Button(frmVK, text = "Zurück", command = bt.btnZurück_click)
        btnZurück["height"] = 2
        btnZurück["width"] = 10
        btnZurück.place(x=320,y=500)
        
## VK Überschriften 1


        lblPro = tkinter.Label(frmVK, text = "Zuschlagssätze in %")
        lblPro["height"] =2
        lblPro["width"] = 40
        lblPro.place(x=140, y=30)

        lblEur = tkinter.Label(frmVK, text = "Kalkulation in €")
        lblEur["height"] =2
        lblEur["width"] = 40
        lblEur.place(x=340, y=30)
        
## VK Listeneinkaufspreis

        lblLEP = tkinter.Label(frmVK, text = "Listeneinkaufspreis:", anchor="w")
        lblLEP["height"] =2
        lblLEP["width"] = 20
        lblLEP.place(x=70, y=70)
        
        self.txtLEP = tkinter.Entry(frmVK)
        self.txtLEP.place(x=420, y=75)
        
## VK Liefer-Rabatt

        lblLR = tkinter.Label(frmVK, text = "Liefer-Rabatt:", anchor="w")
        lblLR["height"] = 2
        lblLR["width"] = 20
        lblLR.place(x=70, y=120)
        
        self.lblLR = tkinter.Label(frmVK, text = "0")
        self.lblLR["height"] = 2
        self.lblLR["width"] = 20
        self.lblLR.place(x=410, y=120)

        self.txtLR = tkinter.Entry(frmVK)
        self.txtLR.place(x=220, y=125)
        
## VK Zieleinkaufspreis

        lblZEP = tkinter.Label(frmVK, text = "Zieleinkaufspreis:", anchor="w")
        lblZEP["height"] = 2
        lblZEP["width"] = 20
        lblZEP.place(x=70, y=170)
        
        self.lblZEP = tkinter.Label(frmVK, text = "0")
        self.lblZEP["height"] = 2
        self.lblZEP["width"] = 20
        self.lblZEP.place(x=410, y=170)
        
## VK Liefer-Skonto

        lblSkontoL = tkinter.Label(frmVK, text = "Liefer-Skonto:", anchor="w")
        lblSkontoL["height"] = 2
        lblSkontoL["width"] = 20
        lblSkontoL.place(x=70, y=220)
        
        self.txtSkontoL = tkinter.Entry(frmVK)
        self.txtSkontoL.place(x=220, y=225)
        
        self.lblSkontoL = tkinter.Label(frmVK, text = "0")
        self.lblSkontoL["height"] = 2
        self.lblSkontoL["width"] = 20
        self.lblSkontoL.place(x=410, y=220)
        
## VK Bareinkaufspreis

        lblBEP = tkinter.Label(frmVK, text = "Bareinkaufspreis:", anchor="w")
        lblBEP["height"] = 2
        lblBEP["width"] = 20
        lblBEP.place(x=70, y=270)
        
        self.lblBEP = tkinter.Label(frmVK, text = "0")
        self.lblBEP["height"] = 2
        self.lblBEP["width"] = 20
        self.lblBEP.place(x=410, y=270)
        
## VK Bezugskosten

        lblBK = tkinter.Label(frmVK, text = "Bezugskosten:", anchor="w")
        lblBK["height"] = 2
        lblBK["width"] = 20
        lblBK.place(x=70, y=320)
        
        self.txtBK = tkinter.Entry(frmVK)
        self.txtBK.place(x=420, y=325)
        
        self.lblBK = tkinter.Label(frmVK, text = "Fester Wert in €")
        self.lblBK["height"] = 2
        self.lblBK["width"] = 20
        self.lblBK.place(x=210, y=320)
        
## VK Bezugspreis 1

        lblBP = tkinter.Label(frmVK, text = "Bezugspreis:", anchor="w")
        lblBP["height"] = 2
        lblBP["width"] = 20
        lblBP.place(x=70, y=370)
        
        self.lblBPB1 = tkinter.Label(frmVK, text = "0")
        self.lblBPB1["height"] = 2
        self.lblBPB1["width"] = 20
        self.lblBPB1.place(x=410, y=370)
        
## VK Überschriften 2

        lblEur = tkinter.Label(frmVK, text = "Kalkulation in €")
        lblEur["height"] =2
        lblEur["width"] = 40
        lblEur.place(x=920, y=30)

        lblPro = tkinter.Label(frmVK, text = "Zuschlagssätze in %")
        lblPro["height"] =2
        lblPro["width"] = 40
        lblPro.place(x=720, y=30)
        
## VK Bezugspreis 2

        lblBP = tkinter.Label(frmVK, text = "Bezugspreis:", anchor="w")
        lblBP["height"] =2
        lblBP["width"] = 20
        lblBP.place(x=650, y=70)
        
        self.lblBPB2 = tkinter.Label(frmVK, text = "0")
        self.lblBPB2["height"] = 2
        self.lblBPB2["width"] = 20
        self.lblBPB2.place(x=1000, y=70)
        
## VK Handlungskosten

        lblHK = tkinter.Label(frmVK, text = "Handlungskosten:", anchor="w")
        lblHK["height"] = 2
        lblHK["width"] = 20
        lblHK.place(x=650, y=120)
        
        self.txtHK = tkinter.Entry(frmVK)
        self.txtHK.place(x=800, y=125)
        
        self.lblHK = tkinter.Label(frmVK, text = "0")
        self.lblHK["height"] = 2
        self.lblHK["width"] = 20
        self.lblHK.place(x=1000, y=120)
        
## VK Selbstkosten

        lblSK = tkinter.Label(frmVK, text = "Selbstkosten:", anchor="w")
        lblSK["height"] = 2
        lblSK["width"] = 20
        lblSK.place(x=650, y=170)
        
        self.lblSK = tkinter.Label(frmVK, text = "0")
        self.lblSK["height"] = 2
        self.lblSK["width"] = 20
        self.lblSK.place(x=1000, y=170)
        
## VK Gewinn

        lblGe = tkinter.Label(frmVK, text = "Gewinn:", anchor="w")
        lblGe["height"] = 2
        lblGe["width"] = 20
        lblGe.place(x=650, y=220)
        
        self.txtGe = tkinter.Entry(frmVK)
        self.txtGe.place(x=800, y=225)
        
        self.lblGe = tkinter.Label(frmVK, text = "0")
        self.lblGe["height"] = 2
        self.lblGe["width"] = 20
        self.lblGe.place(x=1000, y=220)
        
## VK Barverkaufspreis

        lblBVP = tkinter.Label(frmVK, text = "Barverkaufspreis:", anchor="w")
        lblBVP["height"] = 2
        lblBVP["width"] = 20
        lblBVP.place(x=650, y=270)
        
        self.lblBVK = tkinter.Label(frmVK, text = "0")
        self.lblBVK["height"] = 2
        self.lblBVK["width"] = 20
        self.lblBVK.place(x=1000, y=270)
        
## VK Kundenskonto

        lblSkontoK = tkinter.Label(frmVK, text = "Kundenskonto:", anchor="w")
        lblSkontoK["height"] = 2
        lblSkontoK["width"] = 20
        lblSkontoK.place(x=650, y=320)
        
        self.txtSkontoK = tkinter.Entry(frmVK)
        self.txtSkontoK.place(x=800, y=325)
        
        self.lblSkontoK = tkinter.Label(frmVK, text = "0")
        self.lblSkontoK["height"] = 2
        self.lblSkontoK["width"] = 20
        self.lblSkontoK.place(x=1000, y=320)
        
## VK Zielverkaufspreis

        lblZVK = tkinter.Label(frmVK, text = "Zielverkaufspreis:", anchor="w")
        lblZVK["height"] = 2
        lblZVK["width"] = 20
        lblZVK.place(x=650, y=370)
        
        self.lblZVK = tkinter.Label(frmVK, text = "0")
        self.lblZVK["height"] = 2
        self.lblZVK["width"] = 20
        self.lblZVK.place(x=1000, y=370)
        
## VK Kundenrabatt

        lblKR = tkinter.Label(frmVK, text = "Kundenrabatt:", anchor="w")
        lblKR["height"] = 2
        lblKR["width"] = 20
        lblKR.place(x=650, y=420)
        
        self.txtKR = tkinter.Entry(frmVK)
        self.txtKR.place(x=800, y=425)
        
        self.lblKR = tkinter.Label(frmVK, text = "0")
        self.lblKR["height"] = 2
        self.lblKR["width"] = 20
        self.lblKR.place(x=1000, y=420)
        
## VK Listenverkaufspreis

        lblLVP = tkinter.Label(frmVK, text = "Listenverkaufspreis:", anchor="w")
        lblLVP["height"] = 2
        lblLVP["width"] = 20
        lblLVP.place(x=650, y=470)

        self.lblLVP = tkinter.Label(frmVK, text = "0")
        self.lblLVP["height"] = 2
        self.lblLVP["width"] = 20
        self.lblLVP.place(x=1000, y=470)
    
    def Deiconify(tmp):
        frmVK.deiconify()
    
    def Withdraw(tmp):
        frmVK.withdraw()    


## Rückwärtskalkulation

class Rückwärtskalkulation():
    global frmRK
    def __init__(self):
        global frmRK
        bt = Buttons()
        
        frmRK = tkinter.Tk()
        frmRK.title("Rückwärtskalkulation")
        frmRK.wm_geometry("1200x600")
        
        lbl = tkinter.Label(frmRK, text = "Rückwärtskalkulation", font=('times', 12, 'bold'))
        lbl.pack()

## RK Buttons

        btnBeenden = tkinter.Button(frmRK, text = "Beenden", command = bt.btnBeenden_click)
        btnBeenden["height"] = 2
        btnBeenden["width"] = 10
        btnBeenden.place(x=980,y=500)

        btnBerechnenRK = tkinter.Button(frmRK, text = "Berechnen", command = bt.btnBerechnenRK_click)
        btnBerechnenRK["height"] = 2
        btnBerechnenRK["width"] = 10
        btnBerechnenRK.place(x=680,y=500)

        btnSpeichern = tkinter.Button(frmRK, text = "Speichern", command = bt.btnSpeichern_click)
        btnSpeichern["height"] = 2
        btnSpeichern["width"] = 10
        btnSpeichern.place(x=780,y=500)

        btnZurück = tkinter.Button(frmRK, text = "Zurück", command = bt.btnZurück_click)
        btnZurück["height"] = 2
        btnZurück["width"] = 10
        btnZurück.place(x=880,y=500)

## RK Überschriften 1

        lblPro = tkinter.Label(frmRK, text = "Zuschlagssätze in %")
        lblPro["height"] =2
        lblPro["width"] = 40
        lblPro.place(x=140, y=30)

        lblEur = tkinter.Label(frmRK, text = "Kalkulation in €")
        lblEur["height"] =2
        lblEur["width"] = 40
        lblEur.place(x=340, y=30)

## RK Listenverkaufspreis

        lblLVP = tkinter.Label(frmRK, text = "Listenverkaufspreis:", anchor="w")
        lblLVP["height"] =2
        lblLVP["width"] = 20
        lblLVP.place(x=70, y=70)
        
        self.txtLVP = tkinter.Entry(frmRK)
        self.txtLVP.place(x=420, y=75)
        
## RK Kundenrabatt
        
        lblKR = tkinter.Label(frmRK, text = "Kundenrabatt:", anchor="w")
        lblKR["height"] = 2
        lblKR["width"] = 20
        lblKR.place(x=70, y=120)
        
        self.lblKR = tkinter.Label(frmRK, text = "0")
        self.lblKR["height"] = 2
        self.lblKR["width"] = 20
        self.lblKR.place(x=410, y=120)
        
        self.txtKR = tkinter.Entry(frmRK)
        self.txtKR.place(x=220, y=125)
        
## RK Zielverkaufspreis
        
        lblZVK = tkinter.Label(frmRK, text = "Zielverkaufspreis:", anchor="w")
        lblZVK["height"] = 2
        lblZVK["width"] = 20
        lblZVK.place(x=70, y=170)
        
        self.lblZVP = tkinter.Label(frmRK, text = "0")
        self.lblZVP["height"] = 2
        self.lblZVP["width"] = 20
        self.lblZVP.place(x=410, y=170)
        
## RK Kundenskonto
        
        lblSkontoK = tkinter.Label(frmRK, text = "Kundenskonto:", anchor="w")
        lblSkontoK["height"] = 2
        lblSkontoK["width"] = 20
        lblSkontoK.place(x=70, y=220)
        
        self.txtSkontoK = tkinter.Entry(frmRK)
        self.txtSkontoK.place(x=220, y=225)
        
        self.lblSkontoK = tkinter.Label(frmRK, text = "0")
        self.lblSkontoK["height"] = 2
        self.lblSkontoK["width"] = 20
        self.lblSkontoK.place(x=410, y=220)
        
## RK Barverkaufspreis
        
        lblBVP = tkinter.Label(frmRK, text = "Barverkaufspreis:", anchor="w")
        lblBVP["height"] = 2
        lblBVP["width"] = 20
        lblBVP.place(x=70, y=270)
        
        self.lblBVP = tkinter.Label(frmRK, text = "0")
        self.lblBVP["height"] = 2
        self.lblBVP["width"] = 20
        self.lblBVP.place(x=410, y=270)
        
## RK Gewinn
        
        lblGe = tkinter.Label(frmRK, text = "Gewinn:", anchor="w")
        lblGe["height"] = 2
        lblGe["width"] = 20
        lblGe.place(x=70, y=320)
        
        self.txtGe = tkinter.Entry(frmRK)
        self.txtGe.place(x=220, y=325)
        
        self.lblGe = tkinter.Label(frmRK, text = "0")
        self.lblGe["height"] = 2
        self.lblGe["width"] = 20
        self.lblGe.place(x=410, y=320)
        
## RK Selbstkosten
        
        lblSK = tkinter.Label(frmRK, text = "Selbstkosten:", anchor="w")
        lblSK["height"] = 2
        lblSK["width"] = 20
        lblSK.place(x=70, y=370)
        
        self.lblSK = tkinter.Label(frmRK, text = "0")
        self.lblSK["height"] = 2
        self.lblSK["width"] = 20
        self.lblSK.place(x=410, y=370)
        
## RK Handlungskosten
        
        lblHK = tkinter.Label(frmRK, text = "Handlungskosten:", anchor="w")
        lblHK["height"] = 2
        lblHK["width"] = 20
        lblHK.place(x=70, y=420)
        
        self.txtHK = tkinter.Entry(frmRK)
        self.txtHK.place(x=220, y=425)
        
        self.lblHK = tkinter.Label(frmRK, text = "0")
        self.lblHK["height"] = 2
        self.lblHK["width"] = 20
        self.lblHK.place(x=410, y=420)
        
## RK Bezugspreis 1
        
        lblBP1 = tkinter.Label(frmRK, text = "Bezugspreis:", anchor="w")
        lblBP1["height"] = 2
        lblBP1["width"] = 20
        lblBP1.place(x=70, y=470)
        
        self.lblBP1 = tkinter.Label(frmRK, text = "0")
        self.lblBP1["height"] = 2
        self.lblBP1["width"] = 20
        self.lblBP1.place(x=410, y=470)
        
## RK Überschriften 2
        
        lblEur = tkinter.Label(frmRK, text = "Kalkulation in €")
        lblEur["height"] =2
        lblEur["width"] = 40
        lblEur.place(x=920, y=30)
        
        lblPro = tkinter.Label(frmRK, text = "Zuschlagssätze in %")
        lblPro["height"] =2
        lblPro["width"] = 40
        lblPro.place(x=720, y=30)
        
## RK Bezugspreis 2

        lblBP2 = tkinter.Label(frmRK, text = "Bezugspreis:", anchor="w")
        lblBP2["height"] =2
        lblBP2["width"] = 20
        lblBP2.place(x=650, y=70)
        
        self.lblBP2 = tkinter.Label(frmRK, text = "0")
        self.lblBP2["height"] = 2
        self.lblBP2["width"] = 20
        self.lblBP2.place(x=1000, y=70)
        
## RK Bezugskosten
        
        lblBK = tkinter.Label(frmRK, text = "Bezugskosten:", anchor="w")
        lblBK["height"] =2
        lblBK["width"] = 20
        lblBK.place(x=650, y=120)
        
        self.txtBK = tkinter.Entry(frmRK)
        self.txtBK.place(x=800, y=125)
        
        self.lblBK = tkinter.Label(frmRK, text = "Fester Wert in €")
        self.lblBK["height"] = 2
        self.lblBK["width"] = 20
        self.lblBK.place(x=1000, y=120)
        
## RK Bareinkaufspreis
        
        lblBEP = tkinter.Label(frmRK, text = "Bareinkaufspreis:", anchor="w")
        lblBEP["height"] =2
        lblBEP["width"] = 20
        lblBEP.place(x=650, y=170)
        
        self.lblBEP = tkinter.Label(frmRK, text = "0")
        self.lblBEP["height"] = 2
        self.lblBEP["width"] = 20
        self.lblBEP.place(x=1000, y=170)
        
## RK Liefer-Skonto
        
        lblSkontoL = tkinter.Label(frmRK, text = "Liefer-Skonto:", anchor="w")
        lblSkontoL["height"] =2
        lblSkontoL["width"] = 20
        lblSkontoL.place(x=650, y=220)
        
        self.txtSkontoL = tkinter.Entry(frmRK)
        self.txtSkontoL.place(x=800, y=225)
        
        self.lblSkontoL = tkinter.Label(frmRK, text = "0")
        self.lblSkontoL["height"] = 2
        self.lblSkontoL["width"] = 20
        self.lblSkontoL.place(x=1000, y=220)
        
## RK Zieleinkaufspreis
        
        lblZEP = tkinter.Label(frmRK, text = "Zieleinkaufspreis:", anchor="w")
        lblZEP["height"] =2
        lblZEP["width"] = 20
        lblZEP.place(x=650, y=270)
        
        self.lblZEP = tkinter.Label(frmRK, text = "0")
        self.lblZEP["height"] = 2
        self.lblZEP["width"] = 20
        self.lblZEP.place(x=1000, y=270)
        
## RK Liefer-Rabatt
        
        lblLR = tkinter.Label(frmRK, text = "Liefer-Rabatt:", anchor="w")
        lblLR["height"] =2
        lblLR["width"] = 20
        lblLR.place(x=650, y=320)
        
        self.txtLR = tkinter.Entry(frmRK)
        self.txtLR.place(x=800, y=325)
        
        self.lblLR = tkinter.Label(frmRK, text = "0")
        self.lblLR["height"] = 2
        self.lblLR["width"] = 20
        self.lblLR.place(x=1000, y=320)
        
## RK Listeneinkaufspreis
        
        lblLEP = tkinter.Label(frmRK, text = "Listeneinkaufspreis:", anchor="w")
        lblLEP["height"] =2
        lblLEP["width"] = 20
        lblLEP.place(x=650, y=370)
        
        self.lblLEP = tkinter.Label(frmRK, text = "0")
        self.lblLEP["height"] = 2
        self.lblLEP["width"] = 20
        self.lblLEP.place(x=1000, y=370)
        

    
    def Deiconify(tmp):
        frmRK.deiconify()

    def Withdraw(tmp):
        frmRK.withdraw()
        
## Menü Speichern
        

class Speichern():
    global frmSP
    def __init__(self):
        global frmSP
        bt = Buttons()
        
        frmSP = tkinter.Tk()
        frmSP.title("Speichern")
        frmSP.wm_geometry("400x200")
        
        lbl = tkinter.Label(frmSP, text = "\nIn welchem Format soll gespeichert werden?", font=('times', 12, 'bold'))
        lbl.pack()
        
## Buttons

        btnSpeichernCSV = tkinter.Button(frmSP, text = "CSV", command = ds.btnspeichernCSV_click)
        btnSpeichernCSV["height"] = 2
        btnSpeichernCSV["width"] = 10
        btnSpeichernCSV.place(x=10,y=80)

        btnSpeichernXML = tkinter.Button(frmSP, text = "XML", command = ds.btnspeichernXML_click)
        btnSpeichernXML["height"] = 2
        btnSpeichernXML["width"] = 10
        btnSpeichernXML.place(x=110,y=80)

        btnSpeichernJSON = tkinter.Button(frmSP, text = "JSON", command = ds.btnspeichernJSON_click)
        btnSpeichernJSON["height"] = 2
        btnSpeichernJSON["width"] = 10
        btnSpeichernJSON.place(x=210,y=80)

        btnSpeichernSQL = tkinter.Button(frmSP, text = "SQL", command = ds.btnspeichernSQL_click)
        btnSpeichernSQL["height"] = 2
        btnSpeichernSQL["width"] = 10
        btnSpeichernSQL.place(x=310,y=80)
        
        btnZurückSpeichern = tkinter.Button(frmSP, text = "Zurück", command = bt.btnZurückSpeichern_click)
        btnZurückSpeichern["height"] = 2
        btnZurückSpeichern["width"] = 10
        btnZurückSpeichern.place(x=160,y=150)
        
    def Deiconify(tmp):
        frmSP.deiconify()

    def Withdraw(tmp):
        frmSP.withdraw()
        
        
## Objekte

rw = RechnerWahl()
vk = Vorwärtskalkulation()
rk = Rückwärtskalkulation()
ds = DateienSpeichern()
sp = Speichern()
sp.Withdraw()
rk.Withdraw()
vk.Withdraw()
tkinter.mainloop()