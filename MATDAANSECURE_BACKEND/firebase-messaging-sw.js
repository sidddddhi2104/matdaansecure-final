importScripts("https://www.gstatic.com/firebasejs/9.23.0/firebase-app-compat.js");
importScripts("https://www.gstatic.com/firebasejs/9.23.0/firebase-messaging-compat.js");

firebase.initializeApp({
  apiKey: "AIzaSyCEoerP_xiqcZMkIc6I83Kka6l3OI9CetQ",
  projectId: "matdaan-d1486",
  messagingSenderId: "484649301509",
  appId: "1:484649301509:web:c61b2a4720343cb3dc0e6c"
});

const messaging = firebase.messaging();

messaging.onBackgroundMessage(payload => {
  self.registration.showNotification(
    payload.notification.title,
    {
      body: payload.notification.body,
      icon: "/static/images/logo.png"
    }
  );
});
