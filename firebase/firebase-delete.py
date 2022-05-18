from firebase import firebase
import imp

from numpy import record

firebase = firebase.FirebaseApplication('https://peoplecounter-ae29f-default-rtdb.firebaseio.com/', None)
firebase.delete('/peoplecounter-ae29f-default-rtdb/user',"-MzcvptIKCZnh7-MOf07")
print("record deleted")
