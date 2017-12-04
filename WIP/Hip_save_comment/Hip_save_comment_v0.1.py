import os.path as op
import hou

activeSession = hou.hipFile.name()

# Fetch tuple with index of pressed button and input text.
choice, text = hou.ui.readInput('Type comments message',
                                help='Type comments description.',
                                title='Commented HIP',
                                buttons=('OK', 'Cancel'),
                                default_choice=1,
                                close_choice=1)

# If OK was pressed with some non-empty text.
if choice == 0 and text:
    path = hou.hipFile.path()
    dir, name = op.split(path)

    # Discard extension.
    name = op.splitext(name)[0]

    # Discard one '.anytext' occurence at the end.
    name = name.rsplit('.', 1)[0]

    # Make new name with input text.
    new_name = '%s.%s.hip' % (name, text)

    # Finally, create an absolute path to save file to.
    new = op.normpath(op.join(dir, new_name))

    # Save the file.
    hou.hipFile.save(file_name=new, save_to_recent_files=False)
    hou.hipFile.setName(path)
    print "File saved to - " + (new)
