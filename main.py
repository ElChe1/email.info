import smtplib
import email.mime.multipart
import email.mime.base
from email.mime.text import MIMEText
import requests
import time
import platform
import psutil
import webbrowser
import json

#Configuración para enviar el correo.
send = 'csh.hkxhtb12854@gmail.com' #Correo que enviará el email
password = 'musx tcvj pdkh tszn' #Contraseña de aplicaciones 
#https://myaccount.google.com/u/4/apppasswords?rapt=AEjHL4PqCbS9OdaTDzN3doCeojp3QS54o3DUyR7fUNIHzf7U_kSJWzF4SEZyvXOra2ZfX3QgIe0WMQYizVUyKvTklqS0mzwZgw
reciver = 'setcomu2005@gmail.com' #Correo que va a recibir el email

body= "Información diaria del dispsitivo." #Asunto
cuerpo = "" #Comentarios


def send_mail():
    # SMTP conexión
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(send, password)
    # Crear el mensaje del correo electrónico
    mensaje = email.mime.multipart.MIMEMultipart()
    mensaje['From'] = send
    mensaje['To'] = reciver
    mensaje['Subject'] = body
    mensaje.attach(email.mime.text.MIMEText(cuerpo, 'plain'))
    # Añadir el archivo
    ruta_archivo = 'RESULT.txt'
    archivo = open(ruta_archivo, 'rb')
    adjunto = email.mime.base.MIMEBase('application', 'octet-stream')
    adjunto.set_payload((archivo).read())
    email.encoders.encode_base64(adjunto)
    adjunto.add_header('Content-Disposition', "attachment; filename= %s" % ruta_archivo)
    mensaje.attach(adjunto)
    # Añadir el archivo 2
    ruta_archivo2 = 'INFO_IP.txt'
    archivo2 = open(ruta_archivo2, 'rb')
    adjunto2 = email.mime.base.MIMEBase('application', 'octet-stream')
    adjunto2.set_payload((archivo2).read())
    email.encoders.encode_base64(adjunto2)
    adjunto2.add_header('Content-Disposition', "attachment; filename= %s" % ruta_archivo2)
    mensaje.attach(adjunto2)
    # Enviar el correo electrónico
    texto = mensaje.as_string()
    server.sendmail(send, reciver, texto)
    server.quit()

def pubip():
    public_ip = requests.get("https://api.ipify.org").text
    with open("INFO_IP.txt", 'a') as f:
        f.write('IP: ' + public_ip)

def system_info(): #Coge la información del sistema
    def get_system_info():
        ptf = platform.platform()
        brw = webbrowser.get().name
        cc = psutil.cpu_count(logical=False)
        ram = psutil.virtual_memory().total
        ren = psutil.cpu_percent(interval=1)
        ht, wd = get_screen_resolution()
        os = platform.system()

        data = {
            "Platform": ptf,
            "Browser": brw,
            "Nucleos": cc,
            "Ram": ram,
            "Render": ren,
            "Height": ht,
            "Width": wd,
            "Os": os,
        }

        return data

    def get_screen_resolution():
        try:
            import tkinter as tk
            root = tk.Tk()
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            root.destroy()
            return screen_height, screen_width
        except ImportError:
            return None, None

    def save_data_to_file(data):
        with open("RESULT.txt", "w") as file:
            json.dump(data, file)

    def main():
        user_data = get_system_info()
        save_data_to_file(user_data)
        
    if __name__ == "__main__":
        main()

def clear(): # Borra el contenido de los archivos RESULT y INFO_IP
    RESULT = 'RESULT.txt'
    INFO_IP = 'INFO_IP.txt'    
    #RESULT
    with open(RESULT, 'w+') as result_file:
        result_file.truncate()
    #INFO_IP
    with open(INFO_IP, 'w+') as info_file:
        info_file.truncate()

a = 1
if __name__ == "__main__":
    while a < 1825: #5 años
        time.sleep(2)
        clear()
        print("Recogiendo información...")
        pubip()
        time.sleep(4)
        print("Se ha cogido la IP correctamente.")
        system_info()
        time.sleep(4)
        print("Se ha cogido la información del sistema correctamente.")
        time.sleep(4)
        print("Enviando correo...")
        send_mail()
        time.sleep(4)
        print("Se ha enviado el correo correctamente.")
        clear()
        time.sleep(86400) # 24h a sec

        a += 1