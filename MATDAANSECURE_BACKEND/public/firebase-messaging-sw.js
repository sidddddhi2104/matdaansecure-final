importScripts("https://www.gstatic.com/firebasejs/10.7.1/firebase-app-compat.js");
importScripts("https://www.gstatic.com/firebasejs/10.7.1/firebase-messaging-compat.js");

firebase.initializeApp({
  apiKey: "AIzaSyCEoerP_xiqcZMkIc6I83Kka6l3OI9CetQ",
  authDomain: "matdaan-d1486.firebaseapp.com",
  projectId: "matdaan-d1486",
  messagingSenderId: "484649301509",
  appId: "1:484649301509:web:c61b2a4720343cb3dc0e6c"
});

const messaging = firebase.messaging();

// BACKGROUND NOTIFICATION
messaging.onBackgroundMessage(payload => {
  self.registration.showNotification(
    payload.notification.title,
    {
      body: payload.notification.body,
      icon: "/icon.png"
    }
  );
});