def IDHandle(type):
    if type == "start":
        print "IDHandler activated!"
    elif type == "resourcePackChange":
        print "Updating the blocks and stuff for the resource pack..."
    elif type == "reloadID":
        print "Reloading the blocks and stuff..."
    else:
        print "What are you talking about?"
    if type in "start resourcePackChange reloadID".split():
        print "Loading blocks..."
        blocks = []
        blocks.append(vanillaBlocks)
        blocks.append(modBlocks)
        print "Loading entities..."
        entities = []
        entities.append(vanillaEntities)
        entities.append(modEntities)
        print "Loading GUI..."
        gui = []
        gui.append(vanillaGui)
        gui.append(modGui)
        print "Loading regular scripts. These are regular scripts that do basic stuff, and don't do too much change."
        miscScript = []
        miscScript.append(vanillaScripts)
        miscScript.append(modScripts)
        print "Loading Python scripts. These scripts do a lot of change. and stuff."
        pyScript = []
        print "Loading vanilla Python scripts. These scripts are necessary for the game to work."
        pyScript.append(vanillaPyScripts)
        print "Loading mod Python scripts. These scripts are more capable than regular mod scripts. They add functionality or change that isn't possible in regular scripts, or too difficult to do in regular scripts.
        pyScript.append(modPyScripts)
        return True
    else:
        return False
