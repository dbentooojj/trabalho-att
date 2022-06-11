import PySimpleGUI as sg

def janela_login():
    sg.theme('Reddit')
    layout = [
        
        [sg.Image(filename='entra.png')],
        [sg.HSeparator(pad=((0,0),(0,0)))],
        [sg.Text('Email')],
        [sg.InputText(key='email')],
        [sg.Text('Senha')],
        [sg.InputText(key='senha', password_char='*')],
        [sg.Checkbox('Salvar Login?', key='lembrar')],
        [sg.Button('Entrar', size=(10, 1)), sg.Button('Cadastrar', size=(10, 1))],
        [sg.Text('', size=(10, 1), key='mensagem')],
        [sg.HSeparator(pad=((0,0),(0,0)))]
aaa
    ]

    return sg.Window('Janela de login', layout=layout, finalize=True)

janela = janela_login()
sg.read_all_windows()
janela.close()
