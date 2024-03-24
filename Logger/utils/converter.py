from Logger.utils.mapping import ModifierScanCode, KeyCodesMap

def isModifier(ScanCode):
    # Check if ScanCode is in ModifierScanCode
    return ScanCode in ModifierScanCode

def getKeyCode(ScanCode):
    # Return the KeyCode from Map
    return KeyCodesMap[ScanCode]