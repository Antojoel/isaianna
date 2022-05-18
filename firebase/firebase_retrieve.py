from firebase import firebase
from unittest import result

firebase = firebase.FirebaseApplication('https://peoplecounter-ae29f-default-rtdb.firebaseio.com/', None)
result = firebase.get('/peoplecounter-ae29f-default-rtdb/user/','-MzczM7PV_Y5_Ow5OuZO')
print (result)

