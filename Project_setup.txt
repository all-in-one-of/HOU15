message=hou.ui.displayMessage("Note: This is a one time scene setup tool to be used only during a fresh start of your shot.", buttons=("Continue", "Cancel"))
if message ==1:
   hou.ui.displayMessage("Cancelled", buttons=('OK',))

if message ==0:

#Set render path
    hou.ui.displayMessage("Please Select a directory for your renders")
    job=hou.hscriptExpression('$JOB')
    renderDir = hou.ui.selectFile(start_directory = job,
    title = "Select render path",
    collapse_sequences = False,
    file_type = hou.fileType.Directory,
    multiple_select = False,
    chooser_mode = hou.fileChooserMode.Read)
    if renderDir == "":
       print "RENDER path: Not set / Unchanged "
    if renderDir != "":
       hou.hscript("setenv RENDER = '%s'" % renderDir)
       print "RENDER path: " + renderDir


#Set cache path
    hou.ui.displayMessage("Now select a directory for your caches")
    job=hou.hscriptExpression('$JOB')
    cacheDir = hou.ui.selectFile(start_directory = job,
    title = "Select cache path",
    collapse_sequences = False,
    file_type = hou.fileType.Directory,
    multiple_select = False,
    chooser_mode = hou.fileChooserMode.Read)
    if cacheDir == "":
       print "CACHE path: Not set / Unchanged "
    if cacheDir != "":
       hou.hscript("setenv CACHE = '%s'" % cacheDir)
       print "CACHE path: " + cacheDir

#Set ifds path
    hou.ui.displayMessage("And finally select a directory for your IFDs")
    job=hou.hscriptExpression('$JOB')
    ifdDir = hou.ui.selectFile(start_directory = job,
    title = "Select IFDs path",
    collapse_sequences = False,
    file_type = hou.fileType.Directory,
    multiple_select = False,
    chooser_mode = hou.fileChooserMode.Read)
    if ifdDir == "":
       print "IFD path: Not set / Unchanged "
    if ifdDir != "":
       hou.hscript("setenv IFD = '%s'" % ifdDir)
       print "IFDs path: " + ifdDir
       hou.ui.displayMessage("Setup complete", buttons=('OK',))