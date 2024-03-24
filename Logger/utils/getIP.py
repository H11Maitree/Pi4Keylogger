from subprocess import check_output

def getIP():
    # Get IP address from bash Linux command hostname `-I``
    return check_output(['hostname', '-I']).decode('ascii').split('\n')[0]