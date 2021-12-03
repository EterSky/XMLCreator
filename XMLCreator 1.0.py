import sys

def ask(question, default="yes"):
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

sectionName=str(input("What is your mod name ? (Short name) [Section name]"))
optionName=str(input("What will be the message that will show up in riivolution on the mod's page ? [Option name]"))
choiceName=str(input("What will be shown when the mod is enabled ? [Choice name]"))
folderName=str(input("What is your mod's folder name ? (For example \"smg2test\")"))

saveGame="Yes"
noDoubles=0
saveGameCustom=ask("Does your mod use a custom save file ?")
if saveGameCustom == False:
    saveGame=ask("Do you want the mod to use your vanilla save files ?")
stageData=ask("Does your mod use StageData ?")
objectData=ask("Does your mod use ObjectData ?")
audioRes=ask("Does your mod use AudioRes ?")
layoutData=ask("Does your mod use LayoutData ?")
localizeData=ask("Does your mod use LocalizeData ?")
particleData=ask("Does your mod use ParticleData ?")
systemData=ask("Does your mod use SystemData ?")
projectTemplate=ask("Does your mod use Project Template ? (If yes, will automatically enable SystemData and ParticleData")

f.write("<!-- XML created by XMLCreator -->\n<wiidisc version=\"1\">\n    <id game=\"SB4\"/>\n       <region type=\"E\"/>\n       <region type=\"J\"/>\n       <region type=\"P\"/>\n       <region type=\"W\"/>\n       <region type=\"K\"/>\n    <options>\n")
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
    f.write("        <folder external=\"LocalizeData\" disc=\"/LocalizeData\" create=\"true\"/>\n        <folder external=\"LocalizeData/EuEnglish\" disc=\"/LocalizeData/EuFrench\" recursive=\"true\" create=\"true\" />\n        <folder external=\"LocalizeData/EuEnglish\" disc=\"/LocalizeData/EuSpanish\" recursive=\"true\" create=\"true\" />\n        <folder external=\"LocalizeData/EuEnglish\" disc=\"/LocalizeData/EuItalian\" recursive=\"true\" create=\"true\" />\n        <folder external=\"LocalizeData/EuEnglish\" disc=\"/LocalizeData/EuDutch\" recursive=\"true\" create=\"true\" />\n        <folder external=\"LocalizeData/EuEnglish\" disc=\"/LocalizeData/EuGerman\" recursive=\"true\" create=\"true\" />\n        <folder external=\"LocalizeData/EuEnglish\" disc=\"/LocalizeData/UsFrench\" recursive=\"true\" create=\"true\" />\n        <folder external=\"LocalizeData/EuEnglish\" disc=\"/LocalizeData/UsSpanish\" recursive=\"true\" create=\"true\" />\n        <folder external=\"LocalizeData/EuEnglish\" disc=\"/LocalizeData/UsEnglish\" recursive=\"true\" create=\"true\" />\n        <folder external=\"LocalizeData/EuEnglish\" disc=\"/LocalizeData/JpJapanese\" recursive=\"true\" create=\"true\" />\n")
if projectTemplate:
    f.write("        <memory offset=\"0x804B7D38\" value=\"4BB4A4D0\"/>\n        <memory offset=\"0x804B7D38\" value=\"4BB4A240\" original=\"4E800020\" target=\"E\"/>\n        <memory offset=\"0x804B7D38\" value=\"4BB4A240\" original=\"4E800020\" target=\"J\"/>\n        <memory offset=\"0x804B7D38\" value=\"4BB4A240\" original=\"4E800020\" target=\"P\"/>\n        <memory offset=\"0x804B7DA8\" value=\"4BB4A1D0\" original=\"4E800020\" target=\"K\"/>\n        <memory offset=\"0x804B7DA8\" value=\"4BB4A1D0\" original=\"4E800020\" target=\"W\"/>\n        <memory offset=\"0x80001800\" valuefile=\"CustomCode/Loader{$__region}.bin\"/>\n")
f.write("    </patch>\n</wiidisc>")

f.close()