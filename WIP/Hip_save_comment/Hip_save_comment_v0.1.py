import os.path as op
import hou

# Fetch tuple with index of pressed button and input text.
choice, text = hou.ui.readInput('Type comments message',
                                help='Type comments description.',
                                title='Commented HIP',
                                buttons=('OK', 'Cancel'),
                                default_choice=1,
                                close_choice=1)

# If OK was pressed with some non-empty text.
if choice == 0:
    path = hou.hipFile.path()

    # Replace existing comment.
    if text:
        dir, name = op.split(path)
        name = op.splitext(name)[0]
        name = name.rsplit('.', 1)[0]
        name = '%s.%s.hip' % (name, text)
        path = op.join(dir, name)
        path = op.normpath(path)

    hou.hipFile.save(path)
    print(path)