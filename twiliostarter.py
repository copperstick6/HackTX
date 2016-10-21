from twilio.rest import TwilioRestClient

#note this is TEST API. not my real API key lolz.
SSID = AC3e71cbc231ed666dd74383cc98d2897f
AuthToken = 1a64ab97a49199dc4e1c60d93b7dd18c

client = TwilioRestClient(SSID_AuthToken)

client.messages.create(
    to = "+18178072377"
    from_ ="+18176667040"
    body = "This is an automated message from the best CS314 student ever"
)
