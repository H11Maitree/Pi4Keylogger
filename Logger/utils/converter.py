from Logger.utils.mapping import ModifierScanCode, KeyCodesMap

def isModifier(ScanCode):
    return ScanCode in ModifierScanCode

def getKeyCode(ScanCode):
    return KeyCodesMap[ScanCode]