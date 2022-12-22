from django.shortcuts import render
import pyrebase

config = {
    "apiKey": "AIzaSyAF88sfZoOLcHpyf8Xyyl3MDSuyT0TRs_g",
    "authDomain": "cpanel-2a6f9.firebaseapp.com",
    "databaseURL": "https://cpanel-2a6f9-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "cpanel-2a6f9",
    "storageBucket": "cpanel-2a6f9.appspot.com",
    "messagingSenderId": "734364346185",
    "appId": "1:734364346185:web:1b073306ef685396b39c98",
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()

def index(request):
    channel_name = database.child('Data').child('Name').get().val()
    channel_subs = database.child('Data').child('Subscribers').get().val()
    channel_type = database.child('Data').child('Type').get().val()

    return render(request, 'index.html', {
        "channel_name" : channel_name,
        "channel_subs" : channel_subs,
        "channel_type" : channel_type,
    })
