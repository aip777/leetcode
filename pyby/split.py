msg = 'Hi, How are you doing?'
msg_list = msg.split()
print(msg_list)


msg = 'Hi,How,are,you,doing?'
msg_list = msg.split(sep=',')
print(msg_list)


msg = 'Hi,How,are,you,doing?'
msg_list = msg.split(sep=',', maxsplit=2)
print(msg_list)
