from ROOT import TFile, TTree

def openFile(inFile,histo):
    fi = TFile.Open(inFile)
    histo = fi.Get(histo)
    return fi, histo


