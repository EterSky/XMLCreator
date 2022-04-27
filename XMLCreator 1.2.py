from tkinter import *
from tkinter import messagebox

# It was 141 lines long in 1.2 | 392 in 2.0

### Variables ###

xmlCheckInt=0
gameCheckInt=0
sectionCheckInt=0
optionCheckInt=0
choiceCheckInt=0
folderCheckInt=0
gameNumber=0
memoryPatchesCounter=-1
endMemoryPatches=0
memoryPatchesList=[0]*250
ripPatches=0 # Screw this
noDoubles=0
lang=["EuFrench","EuSpanish","EuItalian","EuDutch","EuGerman","UsFrench","UsSpanish","UsEnglish","JpJapanese"]

### Functions ###

def gameFunc(event):
    global gameNumber
    if gameTk.get()=="1":
        gameNumber=1
    elif gameTk.get()=="2":
        gameNumber=2
    else:
        gameNumber=0
    if gameNumber==1:
        smg1Text.config(state="normal")
        movieData.config(state="normal")
        localizeData.config(state="disabled")
        projectTemplate.config(state="disabled")
        localizeData.deselect()
        projectTemplate.deselect()
    if gameNumber==2:
        localizeData.config(state="normal")
        projectTemplate.config(state="normal")
        smg1Text.config(state="disabled")
        movieData.config(state="disabled")
        smg1Text.deselect()
        movieData.deselect()
    if gameNumber==0:
        smg1Text.config(state="disabled")
        movieData.config(state="disabled")
        smg1Text.deselect()
        movieData.deselect()
        localizeData.config(state="disabled")
        projectTemplate.config(state="disabled")
        localizeData.deselect()
        projectTemplate.deselect()
    gameCheck()
    return gameNumber

def saveGameChangeState():
    if varSaveCustom.get()==0:
        saveGame.config(state="normal")
    if varSaveCustom.get()==1:
        saveGame.config(state="disabled")
        saveGame.deselect()

def patchesChangeState():
    if varPatches.get()==1:
        memoryPatchesTk.config(state="normal")
    if varPatches.get()==0:
        memoryPatchesTk.config(state="disabled")
        if ripPatches==1:
            askMemoryPatches.config(state="disabled")

def memoryPatchesClear():
    memoryPatchesTk.delete(0,len(memoryPatchesTk.get()))

def xmlCheck(event):
    global xmlCheckInt
    while xmlCheckInt==0:
        xmlCheckInt=1
        xmlNameText.config(fg="green")
    if xmlNameTk.get()=="":
        xmlCheckInt=0
        xmlNameText.config(fg="red")
    generateUnlock()

def gameCheck():
    global gameCheckInt
    while gameCheckInt==0:
        gameCheckInt=1
        gameText.config(fg="green")
    if gameTk.get()=="":
        gameCheckInt=0
        gameText.config(fg="red")
    if gameNumber==0:
        gameCheckInt=0
        gameText.config(fg="red")
    generateUnlock()

def sectionCheck(event):
    global sectionCheckInt
    while sectionCheckInt==0:
        sectionCheckInt=1
        sectionNameText.config(fg="green")
    if sectionNameTk.get()=="":
        sectionCheckInt=0
        sectionNameText.config(fg="red")
    generateUnlock()

def optionCheck(event):
    global optionCheckInt
    while optionCheckInt==0:
        optionCheckInt=1
        optionNameText.config(fg="green")
    if optionNameTk.get()=="":
        optionCheckInt=0
        optionNameText.config(fg="red")
    generateUnlock()

def choiceCheck(event):
    global choiceCheckInt
    while choiceCheckInt==0:
        choiceCheckInt=1
        choiceNameText.config(fg="green")
    if choiceNameTk.get()=="":
        choiceCheckInt=0
        choiceNameText.config(fg="red")
    generateUnlock()

def folderCheck(event):
    global folderCheckInt
    while folderCheckInt==0:
        folderCheckInt=1
        folderNameText.config(fg="green")
    if folderNameTk.get()=="":
        folderCheckInt=0
        folderNameText.config(fg="red")
    generateUnlock()

def generateUnlock():
    if xmlCheckInt==1 and gameCheckInt==1 and sectionCheckInt==1 and optionCheckInt==1 and choiceCheckInt==1 and folderCheckInt==1:
        generateButton.config(state="normal")
    else:
        generateButton.config(state="disabled")

################################################

def memoryPatch(event): # 0x80948A1F;0x60000000 (that was for testing but left it in)
    global endMemoryPatches
    global memoryPatchesCounter
    global ripPatches
    if endMemoryPatches==0:
        if memoryPatchesTk.get()=="end":
            endMemoryPatches=1
            memoryPatchesCounter=249-memoryPatchesCounter
            for i in range(memoryPatchesCounter):
                memoryPatchesList.remove(0)
            memoryPatchesTk.config(state="disabled")
            ripPatches=1
            return
        else:
            memoryPatchesCounter+=1
            memoryPatchesList[memoryPatchesCounter]=memoryPatchesTk.get()
            memoryPatchesClear()
    else:
        return

################################################

def generate():
    global noDoubles
    f=open(xmlNameTk.get()+".xml","w")
    if gameNumber==1:
        f.write("<!-- XML created by XMLCreator -->\n<!-- Get XMLCreator at https://github.com/EterSky/XMLCreator/releases/latest -->\n<wiidisc version=\"1\">\n    <id game=\"RMG\"/>\n       <region type=\"E\"/>\n       <region type=\"J\"/>\n       <region type=\"P\"/>\n       <region type=\"K\"/>\n    <options>\n")
    elif gameNumber==2:
        f.write("<!-- XML created by XMLCreator -->\n<!-- Get XMLCreator at https://github.com/EterSky/XMLCreator/releases/latest -->\n<wiidisc version=\"1\">\n    <id game=\"SB4\"/>\n       <region type=\"E\"/>\n       <region type=\"J\"/>\n       <region type=\"P\"/>\n       <region type=\"K\"/>\n    <options>\n")
    f.write("       <section name=\""+sectionNameTk.get()+"\">\n")
    f.write("           <option name=\""+optionNameTk.get()+"\">\n")
    f.write("               <choice name=\""+choiceNameTk.get()+"\">\n")
    f.write("                   <patch id=\""+sectionNameTk.get()+"\"/>\n")
    f.write("               </choice>\n           </option>\n       </section>\n    </options>\n")
    f.write("    <patch id=\""+sectionNameTk.get()+"\" root=\"/"+folderNameTk.get()+"\">\n")

    if varSaveCustom.get()==1:
        f.write("        <savegame external=\"SaveGame/{$__gameid}{$__region}{$__maker}\" clone=\"false\"/>\n")
    elif varSaveVanilla.get()==0:
        f.write("        <savegame external=\"SaveGame/{$__gameid}{$__region}{$__maker}\" clone=\"true\"/>\n")
    if varStage.get()==1:
        f.write("        <folder external=\"StageData\" disc=\"/StageData\" create=\"true\"/>\n")
    if varObject.get()==1:
        f.write("        <folder external=\"ObjectData\" disc=\"/ObjectData\" create=\"true\"/>\n")
    if varAudio.get()==1:
        f.write("        <folder external=\"AudioRes\" disc=\"/AudioRes\" create=\"true\"/>\n")
    if varLayout.get()==1:
        f.write("        <folder external=\"LayoutData\" disc=\"/LayoutData\" create=\"true\"/>\n")
    if varPT.get()==1:
        noDoubles=1
        f.write("        <folder external=\"ParticleData\" disc=\"/ParticleData\" create=\"true\"/>\n")
        f.write("        <folder external=\"SystemData\" disc=\"/SystemData\" create=\"true\"/>\n")
    if varParticle.get()==1 and noDoubles==0:
        f.write("        <folder external=\"ParticleData\" disc=\"/ParticleData\" create=\"true\"/>\n")
    if varSystem.get()==1 and noDoubles==0:
        f.write("        <folder external=\"SystemData\" disc=\"/SystemData\" create=\"true\"/>\n")
    if varLocalize.get()==1:
        f.write("        <folder external=\"LocalizeData\" disc=\"/LocalizeData\" create=\"true\"/>\n")
        for langNbSMG2 in range(9):
            f.write("        <folder external=\"LocalizeData/EuEnglish\" disc=\"/LocalizeData/"+lang[langNbSMG2]+"\" create=\"true\" />\n")
    if varSMG1text.get()==1:
        for langNbSMG1 in range(9):
            f.write("        <folder external=\"EuEnglish\" disc=\"/"+lang[langNbSMG1]+"\" create=\"true\" />\n")
    if varPT.get()==1:
        f.write("        <folder external=\"CustomCode\" disc=\"/CustomCode\" create=\"true\"/>\n        <memory offset=\"0x804B7D38\" value=\"4BB4A4D0\"/>\n        <memory offset=\"0x804B7D38\" value=\"4BB4A240\" original=\"4E800020\" target=\"E\"/>\n        <memory offset=\"0x804B7D38\" value=\"4BB4A240\" original=\"4E800020\" target=\"J\"/>\n        <memory offset=\"0x804B7D38\" value=\"4BB4A240\" original=\"4E800020\" target=\"P\"/>\n        <memory offset=\"0x804B7DA8\" value=\"4BB4A1D0\" original=\"4E800020\" target=\"K\"/>\n        <memory offset=\"0x804B7DA8\" value=\"4BB4A1D0\" original=\"4E800020\" target=\"W\"/>\n        <memory offset=\"0x80001800\" valuefile=\"CustomCode/Loader{$__region}.bin\"/>\n")
    if varMovie.get()==1:
        f.write("        <folder external=\"MovieData\" disc=\"/MovieData\" create=\"true\"/>\n")
    if varCrash.get()==1 and gameNumber==1:
        f.write("        <memory offset=\"0x8039AA2C\" value=\"60000000\" original=\"98040068\"/>\n        <memory offset=\"0x8039AAF0\" value=\"60000000\" original=\"4082FFB8\"/>\n        <memory offset=\"0x804A432C\" value=\"60000000\" original=\"48000160\"/>\n") # American (E)
        f.write("        <memory offset=\"0x8039AA48\" value=\"60000000\" original=\"98040068\"/>\n        <memory offset=\"0x8039AB0C\" value=\"60000000\" original=\"4082FFB8\"/>\n        <memory offset=\"0x804A432C\" value=\"60000000\" original=\"48000160\"/>\n") # European/Australian (P)
        f.write("        <memory offset=\"0x8039AA2C\" value=\"60000000\" original=\"98040068\"/>\n        <memory offset=\"0x8039AAF0\" value=\"60000000\" original=\"4082FFB8\"/>\n        <memory offset=\"0x804A430C\" value=\"60000000\" original=\"48000160\"/>\n") # Japanese (J)
        f.write("        <memory offset=\"0x8039BF80\" value=\"60000000\" original=\"98040068\"/>\n        <memory offset=\"0x8039C044\" value=\"60000000\" original=\"4082FFB8\"/>\n        <memory offset=\"0x804A656C\" value=\"60000000\" original=\"48000160\"/>\n") # Korean (K)
    if varCrash.get()==1 and gameNumber==2 and varPT.get()==0:
        f.write("        <memory offset=\"0x804B7D90\" value=\"60000000\"/>\n        <memory offset=\"0x804B7E54\" value=\"60000000\"/>\n        <memory offset=\"0x805B66B4\" value=\"60000000\"/>\n")
    if varPatches.get()==1:
        f=open(xmlNameTk.get()+".xml", "a")
        for i in range(len(memoryPatchesList)):
            f.write("        <memory offset=\"")
            patch=memoryPatchesList[i]
            c=0
            for offsetValue in patch.split(";"):
                f.write(offsetValue)
                if c==0:
                    f.write("\" value=\"")
                else:
                    f.write("\"/>\n")
                c=1
    f.write("    </patch>\n</wiidisc>")

    f.close()

    messagebox.showinfo(title="Generation complete !", message="Your XML has been generated successfully !")

### Program ###

gui=Tk()
gui.title("XMLCreator 2.0")
##gui.configure(bg="black") (that's for 2.1)

xmlNameText=Label(gui,text="Name your xml file (.xml will be automatically added to the file name)",fg="red")
xmlNameTk=Entry(gui,width=30)
xmlNameTk.bind("<Return>",xmlCheck)

gameText=Label(gui,text="SMG1 or SMG2 ? (Enter the number)",fg="red")
gameTk=Entry(gui,width=30)
gameTk.bind("<Return>",gameFunc)

sectionNameText=Label(gui,text="What is your mod name ? (Short name) [Section name]",fg="red")
sectionNameTk=Entry(gui,width=30)
sectionNameTk.bind("<Return>",sectionCheck)

optionNameText=Label(gui,text="What will be the message that will show up in riivolution on the mod's page ? [Option name]",fg="red")
optionNameTk=Entry(gui,width=30)
optionNameTk.bind("<Return>",optionCheck)

choiceNameText=Label(gui,text="What will be shown when the mod is enabled ? [Choice name]",fg="red")
choiceNameTk=Entry(gui,width=30)
choiceNameTk.bind("<Return>",choiceCheck)

folderNameText=Label(gui,text="What is your mod's folder name ? (For example \"smgtest\")",fg="red")
folderNameTk=Entry(gui,width=30)
folderNameTk.bind("<Return>",folderCheck)

blank1=Label(gui,text="")
blank2=Label(gui,text="")
blank3=Label(gui,text="")
blank4=Label(gui,text="")
blank5=Label(gui,text="")

# Checkboxes #

varSaveCustom=IntVar() # Those are not in the "Variables" part otherwise they cause an error
varSaveVanilla=IntVar()
varStage=IntVar()
varObject=IntVar()
varAudio=IntVar()
varLayout=IntVar()
varParticle=IntVar()
varSystem=IntVar()
varCrash=IntVar()
varSMG1text=IntVar()
varMovie=IntVar()
varLocalize=IntVar()
varPT=IntVar()
varPatches=IntVar()


saveGame = Checkbutton(gui,text="Do you want the mod to use your vanilla save files ?",variable=varSaveVanilla)
saveBothUnchecked=Label(gui,text="← If both of those are unchecked, your mod will use its own save files →")
saveGameCustom = Checkbutton(gui,text="Does your mod use a custom save file ?",command=saveGameChangeState,variable=varSaveCustom)
##while saveGameCustom==1:
##    saveGame = Checkbutton(gui,text="Do you want the mod to use your vanilla save files ?",variable=varSaveVanilla)

stageData=Checkbutton(gui,text="Does your mod use StageData ?",variable=varStage)
objectData=Checkbutton(gui,text="Does your mod use ObjectData ?",variable=varObject)
audioRes=Checkbutton(gui,text="Does your mod use AudioRes ?",variable=varAudio)
layoutData=Checkbutton(gui,text="Does your mod use LayoutData ?",variable=varLayout)
particleData=Checkbutton(gui,text="Does your mod use ParticleData ?",variable=varParticle)
systemData=Checkbutton(gui,text="Does your mod use SystemData ?",variable=varSystem)
crashDebug=Checkbutton(gui,text="Do you wish to use the crash debugger ?",variable=varCrash)

LabelSMG1=Label(gui,text="--------------- SMG1 Only ---------------")

smg1Text=Checkbutton(gui,text="Does your mod use custom text ?",state="disabled",variable=varSMG1text)
movieData=Checkbutton(gui,text="Does your mod use MovieData ?",state="disabled",variable=varMovie)

LabelSMG2=Label(gui,text="--------------- SMG2 Only ---------------")

localizeData=Checkbutton(gui,text="Does your mod use LocalizeData ?",state="disabled",variable=varLocalize)
projectTemplate=Checkbutton(gui,text="Does your mod use Project Template ?",state="disabled",variable=varPT)

askMemoryPatches=Checkbutton(gui,text="Do you want to use memory patches ?",command=patchesChangeState,variable=varPatches)

memoryPatchesText1=Label(gui,text="Type in your memory offset and its value separated by a \";\"")
memoryPatchesText2=Label(gui,text=" or type \"end\" if you're finishing entering your memory patches")
memoryPatchesTk=Entry(gui,width=30,state="disabled")
memoryPatchesTk.bind("<Return>",memoryPatch)

generateButton=Button(gui,text="Generate",command=generate,state="disabled")

# GUI appearance stuff #

xmlNameText.grid(row=0,column=1)
xmlNameTk.grid(row=1,column=1)

gameText.grid(row=2,column=1)
gameTk.grid(row=3,column=1)

sectionNameText.grid(row=4,column=1)
sectionNameTk.grid(row=5,column=1)

optionNameText.grid(row=6,column=1)
optionNameTk.grid(row=7,column=1)

choiceNameText.grid(row=8,column=1)
choiceNameTk.grid(row=9,column=1)

folderNameText.grid(row=10,column=1)
folderNameTk.grid(row=11,column=1)

blank1.grid(row=12)

saveGameCustom.grid(row=13,column=0)
saveBothUnchecked.grid(row=13,column=1)
saveGame.grid(row=13,column=2)

blank2.grid(row=14)

stageData.grid(row=15,column=0)
objectData.grid(row=15,column=1)
audioRes.grid(row=15,column=2)
layoutData.grid(row=16,column=0)
particleData.grid(row=16,column=1)
systemData.grid(row=16,column=2)
crashDebug.grid(row=17,column=1)
askMemoryPatches.grid(row=18,column=1)

blank3.grid(row=19)

memoryPatchesText1.grid(row=20,column=1)
memoryPatchesText2.grid(row=21,column=1)
memoryPatchesTk.grid(row=22,column=1)

blank4.grid(row=23)

LabelSMG1.grid(row=24,column=1)
smg1Text.grid(row=25,column=1)
movieData.grid(row=26,column=1)

LabelSMG2.grid(row=27,column=1)
localizeData.grid(row=28,column=1)
projectTemplate.grid(row=29,column=1)

blank5.grid(row=30)

generateButton.grid(row=31,column=1)

# Menu bar #

menubar=Menu(gui)
filemenu=Menu(gui,tearoff=0)
filemenu.add_command(label="Exit",command=gui.destroy)
menubar.add_cascade(label="File",menu=filemenu)

gui.config(menu=menubar)
gui.mainloop()
