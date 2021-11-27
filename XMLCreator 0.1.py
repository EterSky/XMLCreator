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

sectionName=str(input("What is your mod name ? (Short name) [Section name]"))
optionName=str(input("What will be the message that will show up in riivolution on the mod's page ? [Option name]"))
choiceName=str(input("What will be shown when the mod is enabled ? [Choice name]"))
folderName=str(input("What is your mod's folder name ? (For example \"smg2test\")"))

saveGame="Yes"
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
projectTemplate=ask("Does your mod use Project Template ?")

print("<!-- XML created by XMLCreator -->\n<wiidisc version=\"1\">\n    <id game=\"SB4\"/>\n       <region type=\"E\"/>\n       <region type=\"J\"/>\n       <region type=\"P\"/>\n       <region type=\"W\"/>\n       <region type=\"K\"/>\n    <options>")
print("       <section name=\"",sectionName,"\"",">",sep="")
print("           <option name=\"",optionName,"\"",">",sep="")
print("               <choice name=\"",choiceName,"\"",">",sep="")
print("                   <patch id=\"",sectionName,"\"","/>",sep="")
print("               </choice>\n           </option>\n       </section>\n    </options>")
print("    <patch id=\"",sectionName,"\" root=\"/",folderName,"\">",sep="")

if saveGameCustom:
    print("        <savegame external=\"SaveGame/{$__gameid}{$__region}{$__maker}\" clone=\"false\"/>")
elif saveGame == False:
    print("        <savegame external=\"SaveGame/{$__gameid}{$__region}{$__maker}\" clone=\"true\"/>")
if stageData:
    print("        <folder external=\"StageData\" disc=\"/StageData\" create=\"true\"/>")
if objectData:
    print("        <folder external=\"ObjectData\" disc=\"/ObjectData\" create=\"true\"/>")
if audioRes:
    print("        <folder external=\"AudioRes\" disc=\"/AudioRes\" create=\"true\"/>")
if layoutData:
    print("        <folder external=\"LayoutData\" disc=\"/LayoutData\" create=\"true\"/>")
if particleData:
    print("        <folder external=\"ParticleData\" disc=\"/ParticleData\" create=\"true\"/>")
if systemData:
    print("        <folder external=\"SystemData\" disc=\"/SystemData\" create=\"true\"/>")
if localizeData:
    print("        <folder external=\"LocalizeData\" disc=\"/LocalizeData\" create=\"true\"/>\n        <folder external=\"LocalizeData/EuEnglish\" disc=\"/LocalizeData/EuFrench\" recursive=\"true\" create=\"true\" />\n        <folder external=\"LocalizeData/EuEnglish\" disc=\"/LocalizeData/EuSpanish\" recursive=\"true\" create=\"true\" />\n        <folder external=\"LocalizeData/EuEnglish\" disc=\"/LocalizeData/EuItalian\" recursive=\"true\" create=\"true\" />\n        <folder external=\"LocalizeData/EuEnglish\" disc=\"/LocalizeData/EuDutch\" recursive=\"true\" create=\"true\" />\n        <folder external=\"LocalizeData/EuEnglish\" disc=\"/LocalizeData/EuGerman\" recursive=\"true\" create=\"true\" />\n        <folder external=\"LocalizeData/EuEnglish\" disc=\"/LocalizeData/UsFrench\" recursive=\"true\" create=\"true\" />\n        <folder external=\"LocalizeData/EuEnglish\" disc=\"/LocalizeData/UsSpanish\" recursive=\"true\" create=\"true\" />\n        <folder external=\"LocalizeData/EuEnglish\" disc=\"/LocalizeData/UsEnglish\" recursive=\"true\" create=\"true\" />\n        <folder external=\"LocalizeData/EuEnglish\" disc=\"/LocalizeData/JpJapanese\" recursive=\"true\" create=\"true\" />")
if projectTemplate:
    print("        <memory offset=\"0x804B7D38\" value=\"4BB4A4D0\"/>\n        <memory offset=\"0x804B7D38\" value=\"4BB4A240\" original=\"4E800020\" target=\"E\"/>\n        <memory offset=\"0x804B7D38\" value=\"4BB4A240\" original=\"4E800020\" target=\"J\"/>\n        <memory offset=\"0x804B7D38\" value=\"4BB4A240\" original=\"4E800020\" target=\"P\"/>\n        <memory offset=\"0x804B7DA8\" value=\"4BB4A1D0\" original=\"4E800020\" target=\"K\"/>\n        <memory offset=\"0x804B7DA8\" value=\"4BB4A1D0\" original=\"4E800020\" target=\"W\"/>\n        <memory offset=\"0x80001800\" valuefile=\"CustomCode/Loader{$__region}.bin\"/>")
print("    </patch>\n</wiidisc>")
