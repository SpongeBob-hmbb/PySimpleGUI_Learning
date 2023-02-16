#img to base64
import base64
with open(r"D:\\vscode\\project\\PySimpleGUI_Learning\\PicForBase64\\test.png","rb") as f: # 路径
    base64_data = base64.b64encode(f.read())#使用base64进行加密
    print(base64_data)
    file=open("D:\\vscode\\project\\PySimpleGUI_Learning\\TxtOfBase64\\test.txt","wb")#写成文本格式
    file.write(base64_data)
    file.close()
