import os,base64 
 
with open("D:\\vscode\\project\\PySimpleGUI_Learning\\TxtOfBase64\\test.txt","r") as f:
    imgdata = base64.b64decode(f.read())
    file = open('D:\\vscode\\project\\PySimpleGUI_Learning\\PicForBase64\\test1.png','wb')
    file.write(imgdata)
    file.close()
 
 