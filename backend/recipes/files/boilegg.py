
step = 0
message = ''
status = 'idle'
options = []


def start():
    global step, message, options
    step = 1
    runStep()


def stop():
    global step, status, message, options
    step = -1
    status = 'idle'
    message = ''
    options = []


def selectOption(option):
    global step, message, options
    if not option in options:
        return False,'Invalid option ' + option
    else:
        # Can have more complex behaviour here with different goto step 
        # associated with each option
        step = step + 1
        if runStep():
            return True,''
        else:
            return False,message


def runStep():
    global step, status, message, options
    options = []
    status = 'running'
    if step == 1:
        status = 'user_input'
        message = 'Place egg in chamber'
        options = ['Done']
    elif step == 2:
        status = 'user_input'
        message = 'Add enough water to cover egg'
        options = ['Done']
    elif step == 3:
        message = 'Heating water...'
    else:
        status = 'error'
        message = 'Invalid step'
        return False
    return True


