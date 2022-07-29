import firebase_admin
from firebase_admin import credentials, messaging
from flask import Flask, request

app = Flask(__name__)
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# allow both GET and POST requests
@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        token = request.form.get('token')
        title = request.form.get('title')
        body = request.form.get('body')



        # This registration token comes from the client FCM SDKs.
        registration_token = "cRWaEkCLaMI:APA91bEkZA4FUhce1LvfeKElVQ-FZ6hofUdPOpIz8uyeASX1NxSSQOUdJURi0TKjyOH9r-YBhemqJQVxD8bAj47Xh00wVUouFF4UBLe93mKizdmU5lDq70fDsfWtTItzM4-k5z0DNFXm"

        # See documentation on defining a message payload.
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),

            token=token,
        )

        # Send a message to the device corresponding to the provided
        # registration token.
        response = messaging.send(message)
        # Response is a message ID string.
        print('Successfully sent message:', response)
        return '''
                  <h1>The token value is: {}</h1>
                  <h1>The title value is: {}</h1>
                   <h1>The body value is: {}</h1>
                <h1>The response value is: {}</h1>'''.format(token, title,body,response)

    # otherwise handle the GET request
    # This registration token comes from the client FCM SDKs.
    registration_token = "cRWaEkCLaMI:APA91bEkZA4FUhce1LvfeKElVQ-FZ6hofUdPOpIz8uyeASX1NxSSQOUdJURi0TKjyOH9r-YBhemqJQVxD8bAj47Xh00wVUouFF4UBLe93mKizdmU5lDq70fDsfWtTItzM4-k5z0DNFXm"


    return '''
    <h1>The token value is: {}</h1>
           <form method="POST">
               <div><label>token: <input type="text" name="token"></label></div>
               <div><label>title: <input type="text" name="title"></label></div>
                <div><label>body: <input type="text" name="body"></label></div>
               <input type="submit" value="Submit">
           </form>'''.format(registration_token)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)