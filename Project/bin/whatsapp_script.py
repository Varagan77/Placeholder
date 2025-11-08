import pywhatkit as pwk

try:
    pwk.sendwhatmsg_instantly("+--------------", "Hello World", wait_time=10, tab_close=True)
    print("Message Sent!")
except Exception as e:
    print("Error in sending the message:", e)


