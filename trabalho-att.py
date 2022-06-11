import PySimpleGUI as sg
import requests

lista_dia = []
lista_mes = ['jan.', 'fev.', 'mar.', 'abr.', 'maio', 'jun.', 'jul.', 'ago.', 'set.', 'out.', 'nov.', 'dez.']
lista_ano = []
for i in range(1, 32):
    lista_dia.append(str(i))
for i in range(1940, 2023):
    lista_ano.append(str(i))


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
    ]

    return sg.Window('Janela de login', layout=layout, finalize=True)

def janela_cadastro():
    sg.theme('Reddit')
    layout = [

        

        [sg.Text('Primeiro nome')],
        [sg.Input(key='primeiro_nome')],
        [sg.Text('Ultimo nome')],
        [sg.Input(key='ultimo_nome')],
        [sg.Text('Email')],
        [sg.Input(key='email')],
        [sg.Text('Exemplo: nome@exemplo.com')],
        [sg.Text('Senha')],
        [sg.Input(key='senha')],
        [sg.Text('Confirmar senha')],
        [sg.Input(key='confirmar')],
        [sg.Button('Salvar'), sg.Button('Voltar')]
    ]

    return sg.Window('Janela de cadastro', layout=layout, finalize=True)

def janela_perfil():
    sg.theme("Reddit")

    layout = [

        [sg.Push(), sg.Image(filename='aa.png'), sg.Push()],
        [sg.Push(), sg.Text('Seja Bem Vindo ao Entra21', font=("bold", 25), text_color='black'), sg.Push()],

        [sg.Push(), sg.Text('Diogo Jose Bento', font=("bold", 15), text_color='black'), sg.Push()],
        [sg.Text(key='nome')],

        [sg.Text('Data de Nasc.'),
         sg.Combo(lista_dia, key='dia'),
         sg.Text('/'),
         sg.Combo(lista_mes, key='mes'),
         sg.Text('/'),
         sg.Combo(lista_ano, key='ano'),
         sg.Text('Sexo'),
         sg.Combo(('Masculino', 'Feminino'), key='sexo', size=(10, 1))],
        [sg.Text('Telefone'), sg.InputText(key='telefone', size=(21, 1)),
         sg.Text('Celular'), sg.InputText(key='celular', size=(22, 1))],
        [sg.Text('CEP'), sg.InputText(key='cep', size=(15, 1)), sg.Button('Consultar')],
        [sg.Text('Logradouro')], 
        [sg.InputText(key='logradouro', size=(28, 1)), sg.Text('Número'), sg.InputText(key='numero', size=(8, 1))],
        [sg.Text('Bairro'), sg.InputText(key='bairro', size=(23, 1)), sg.Text('Cidade'), sg.InputText(key='cidadee', size=(23, 1))], 
        [sg.Text('UF')],
        [sg.InputText(key='uf', size=(7, 1))],
        [sg.Button("Voltar")]
    ]

    return sg.Window("Seu perfil", layout=layout, finalize=True)

janela1, janela2, janela3 = janela_login(), None, None

while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    elif window == janela2 and event == sg.WIN_CLOSED:
        break
    elif window == janela3 and event == sg.WIN_CLOSED:
        break

    elif window == janela1 and event == 'Cadastrar':
        janela1.hide()
        janela2 = janela_cadastro()

    elif window == janela2 and event == 'Salvar':
        sg.popup('Cadastro salvo')
        janela2.close()
        janela1.un_hide()
    elif window == janela1 and event == 'Entrar':
        janela1.hide()
        janela3 = janela_perfil()
    if window == janela3 and event == 'Consultar':
        cep = values['cep']
        url = 'https://viacep.com.br/ws/%s/json/' % cep
        response = requests.get(url)
        response_json = response.json()
        janela3.Element('logradouro').Update(response_json['logradouro'])
        janela3.Element('bairro').Update(response_json['bairro'])
        janela3.Element('uf').Update(response_json['uf'])
        janela3.Element('cidadee').Update(response_json['localidade'])
        print(response_json)

    
        



