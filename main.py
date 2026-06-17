
from MedicalHistoryManagement import MedicalHistoryManagement
from patient import patient
def main():
    pat1 = patient("A","bn1","stomach ache")
    pat2 = patient("B","bn2","headache")
    pat3 = patient("C","bn3","diarrhea")
    MHM = MedicalHistoryManagement()
    MHM.addrecord(pat1)
    MHM.addrecord(pat2)
    MHM.addrecord(pat3)
    MHM.deleteRecord()
    MHM.display()
    MHM.getHistory("bn3")
if __name__ == "__main__": main()