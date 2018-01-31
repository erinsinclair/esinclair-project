#Erin J. Sinclair
#110117
#Missile Launch
# Input the username and password for the missile launch.

print ("""Welcome to the Missile Launch! Input the username and the
    password. If you give correct information, the Missile will launch. If you
    give incorrect information, the system will self destruct.""")

Username = "Sinclair Erin"
Password = "Oxyology"
your_username = input ("Username:")

if your_username == Username:
    print ("Username Valid")
    input ("Password:")

    if Password==Password:
        print ("Password Valid. Missile launching in 5")
        time.sleep (1)
        print ("2")

    
else:
    print ("Username Invalid")



