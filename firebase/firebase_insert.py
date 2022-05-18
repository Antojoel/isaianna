from unittest import result
from firebase import firebase
from result import Result
firebase = firebase.FirebaseApplication('https://peoplecounter-ae29f-default-rtdb.firebaseio.com/', None)
data = {'name': 'macintosh', 'age': 100}
result = firebase.post('/peoplecounter-ae29f-default-rtdb/user', data)
print(result)


