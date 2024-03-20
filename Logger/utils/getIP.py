from subprocess import check_output

def getIP():
    return check_output(['hostname', '-I']).decode('ascii').split('\n')[0]