import sys

def ask(question, default="yes"): ##Thanks to TheSunCat for this function
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")

xmlName=str(input("Name your xml file (.xml will be automatically added to the file name)"))
f=open(xmlName+".xml", "w")

gameNumber=0

game=str(input("SMG1 or SMG2 ?"))
for numberTest in game:
    if numberTest=="1":
        gameNumber=1
    elif numberTest=="2":
        gameNumber=2

sectionName=str(input("What is your mod name ? (Short name) [Section name]"))
optionName=str(input("What will be the message that will show up in riivolution on the mod's page ? [Option name]"))
choiceName=str(input("What will be shown when the mod is enabled ? [Choice name]"))
folderName=str(input("What is your mod's folder name ? (For example \"smgtest\")"))

saveGame="Yes"
memoryPatchesCounter=-1
endMemoryPatches=0
memoryPatchesChange=0
memoryPatchesList=[0]*250
memoryPatchXmlStr=""
noDoubles=0
projectTemplate=""
localizeData=""
smg1Text=""
movieData=""
lang=["EuFrench","EuSpanish","EuItalian","EuDutch","EuGerman","UsFrench","UsSpanish","UsEnglish","JpJapanese"]

saveGameCustom=ask("Does your mod use a custom save file ?")
if saveGameCustom == False:
    saveGame=ask("Do you want the mod to use your vanilla save files ?")
stageData=ask("Does your mod use StageData ?")
objectData=ask("Does your mod use ObjectData ?")
audioRes=ask("Does your mod use AudioRes ?")
layoutData=ask("Does your mod use LayoutData ?")
if gameNumber==2:
    localizeData=ask("Does your mod use LocalizeData ?")
elif gameNumber==1:
    smg1Text=ask("Does your mod use custom text ?")
particleData=ask("Does your mod use ParticleData ?")
systemData=ask("Does your mod use SystemData ?")
if gameNumber==2:
    projectTemplate=ask("Does your mod use Project Template ? (If yes, will automatically enable SystemData and ParticleData)")
if gameNumber==1:
    movieData=ask("Does your mod use MovieData ?")
askMemoryPatches=ask("Do you want to use memory patches ?")
if askMemoryPatches==True:
    while endMemoryPatches==0: ## I think I overcomplicated that
        memoryPatches=str(input("Type in your memory offset and its value separated by a \";\" or type \"end\" if you're finishing entering your memory patches"))
        if memoryPatches=="end":
            endMemoryPatches=1
        else:
            memoryPatchesCounter+=1
            memoryPatchesList[memoryPatchesCounter]=memoryPatches
    memoryPatchesCounter=249-memoryPatchesCounter
    for i in range(memoryPatchesCounter):
        memoryPatchesList.remove(0)

if gameNumber==1:
    f.write("<!-- XML created by XMLCreator -->\n<!-- Get XMLCreator at https://github.com/EterSky/XMLCreator/releases -->\n<wiidisc version=\"1\">\n    <id game=\"RMG\"/>\n       <region type=\"E\"/>\n       <region type=\"J\"/>\n       <region type=\"P\"/>\n       <region type=\"K\"/>\n    <options>\n")
elif gameNumber==2:
    f.write("<!-- XML created by XMLCreator -->\n<!-- Get XMLCreator at https://github.com/EterSky/XMLCreator/releases -->\n<wiidisc version=\"1\">\n    <id game=\"SB4\"/>\n       <region type=\"E\"/>\n       <region type=\"J\"/>\n       <region type=\"P\"/>\n       <region type=\"W\"/>\n       <region type=\"K\"/>\n    <options>\n")
f.write("       <section name=\""+sectionName+"\">\n")
f.write("           <option name=\""+optionName+"\">\n")
f.write("               <choice name=\""+choiceName+"\">\n")
f.write("                   <patch id=\""+sectionName+"\"/>\n")
f.write("               </choice>\n           </option>\n       </section>\n    </options>\n")
f.write("    <patch id=\""+sectionName+"\" root=\"/"+folderName+"\">\n")

if saveGameCustom:
    f.write("        <savegame external=\"SaveGame/{$__gameid}{$__region}{$__maker}\" clone=\"false\"/>\n")
elif saveGame == False:
    f.write("        <savegame external=\"SaveGame/{$__gameid}{$__region}{$__maker}\" clone=\"true\"/>\n")
if stageData:
    f.write("        <folder external=\"StageData\" disc=\"/StageData\" create=\"true\"/>\n")
if objectData:
    f.write("        <folder external=\"ObjectData\" disc=\"/ObjectData\" create=\"true\"/>\n")
if audioRes:
    f.write("        <folder external=\"AudioRes\" disc=\"/AudioRes\" create=\"true\"/>\n")
if layoutData:
    f.write("        <folder external=\"LayoutData\" disc=\"/LayoutData\" create=\"true\"/>\n")
if projectTemplate:
    noDoubles=1
    f.write("        <folder external=\"ParticleData\" disc=\"/ParticleData\" create=\"true\"/>\n")
    f.write("        <folder external=\"SystemData\" disc=\"/SystemData\" create=\"true\"/>\n")
if particleData and noDoubles==0:
    f.write("        <folder external=\"ParticleData\" disc=\"/ParticleData\" create=\"true\"/>\n")
if systemData and noDoubles==0:
    f.write("        <folder external=\"SystemData\" disc=\"/SystemData\" create=\"true\"/>\n")
if localizeData:
    f.write("        <folder external=\"LocalizeData\" disc=\"/LocalizeData\" create=\"true\"/>\n")
    for langNbSMG2 in range(9):
        f.write("        <folder external=\"LocalizeData/EuEnglish\" disc=\"/LocalizeData/"+lang[langNbSMG2]+"\" create=\"true\" />\n")
if smg1Text:
    for langNbSMG1 in range(9):
        f.write("        <folder external=\"EuEnglish\" disc=\"/"+lang[langNbSMG1]+"\" create=\"true\" />\n")
if projectTemplate:
    f.write("        <folder external=\"CustomCode\" disc=\"/CustomCode\" create=\"true\"/>\n        <memory offset=\"0x804B7D38\" value=\"4BB4A4D0\"/>\n        <memory offset=\"0x804B7D38\" value=\"4BB4A240\" original=\"4E800020\" target=\"E\"/>\n        <memory offset=\"0x804B7D38\" value=\"4BB4A240\" original=\"4E800020\" target=\"J\"/>\n        <memory offset=\"0x804B7D38\" value=\"4BB4A240\" original=\"4E800020\" target=\"P\"/>\n        <memory offset=\"0x804B7DA8\" value=\"4BB4A1D0\" original=\"4E800020\" target=\"K\"/>\n        <memory offset=\"0x804B7DA8\" value=\"4BB4A1D0\" original=\"4E800020\" target=\"W\"/>\n        <memory offset=\"0x80001800\" valuefile=\"CustomCode/Loader{$__region}.bin\"/>\n")
if movieData:
    f.write("        <folder external=\"MovieData\" disc=\"/MovieData\" create=\"true\"/>\n")
if askMemoryPatches:
    f=open(xmlName+".xml", "a")
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
