import PySimpleGUI as sg
from cryptography.fernet import Fernet

def encrypt_message(key, message):
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(message.encode())

def decrypt_message(key, encrypted_message):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

# Gere uma chave de criptografia
key = Fernet.generate_key()

sg.theme('DarkBlue')
sg.set_options(font=('Helvetica', 12), element_padding=(5, 5))

layout = [
    [sg.Text('Mensagem'), sg.Input(key='Mensagem')],
    [sg.Button('Criptografar'), sg.Button('Descriptografar')],
    [sg.Output(size=(70, 15))],
]

window = sg.Window('LBK - LockerBox Keeper', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Criptografar':
        mensagem = values['Mensagem']
        mensagem_criptografada = encrypt_message(key, mensagem)
        print(f'Mensagem Criptografada: {mensagem_criptografada}')

    if event == 'Descriptografar' and mensagem_criptografada is not None:
        mensagem_descriptografada = decrypt_message(key, mensagem_criptografada)
        print(f'Mensagem Descriptografada: {mensagem_descriptografada}')

window.close()

