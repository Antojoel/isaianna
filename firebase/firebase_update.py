from firebase import firebase
firebase = firebase.FirebaseApplication('https://peoplecounter-ae29f-default-rtdb.firebaseio.com/', None)
firebase.put('/peoplecounter-ae29f-default-rtdb/data', 'name', 'joel')
print("record updated")
