# Titulo: Thezap
# Botão de iniciar chat
    # popup (janela na frente da tela)
    # Titulo : bem vindo ao Thezap
    # campo de texto - Escreva seu nome no chat
    # botão: entrar no chat
        # sumir com o titulo 
        # sumir com o botao iniciar chat
        # fechar janela (popup)
        # carregar o chat THPCHAT
            # as mensagens que ja foram enviadas (chat)
            # campo : digite sua mensagem
            # botão de enviar 
# pip install flet

# importar flet
import flet as ft


# criar a função principal da seu aplicativo
def main(pagina : ft.Page):
    # criar todas as funcionalidades 
    # cria o elemento
    titulo = ft.Text('THPCHAT', color=ft.colors.GREEN_900)
    
    titulo_janela =ft.Text('Bem vindo ao THPCHAT')
    campo_texto = ft.TextField(label='Escreva seu nome no chat')
    
    chat = ft.Column()
    
    def enviar_mensagem_tunel(msg):
        texto_chat = ft.Text(msg)
        chat.controls.append(texto_chat)
        pagina.update()
        
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    def enviar_msg(evento):
        nome_usuario = campo_texto.value
        texto_msg = campo.value
        msg = '{}: {}'.format(nome_usuario , texto_msg,)
        pagina.pubsub.send_all(msg)
        campo.value = ''
        campo.focus()
        pagina.update()
       
    campo = ft.TextField(label='Digite sua mensagem', on_submit=enviar_msg , autofocus=True)
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_msg)
    
    linha_msg = ft.Row([campo,botao_enviar])
    
    
    
    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        pagina.add(chat)
        pagina.add(linha_msg)
        msg2 =('~{} entrou no chat~'.format(campo_texto.value))
        pagina.pubsub.send_all(msg2)
        pagina.update()
        
    botao_entrar = ft.ElevatedButton('Entrar no chat',on_click = entrar_chat)
    
    janela = ft.AlertDialog(title=titulo_janela , content=campo_texto , actions=[botao_entrar])
    
    
    def iniciar_chat(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()
        
    botao_iniciar = ft.ElevatedButton('iniciar chat', on_click= iniciar_chat)
    
    # adiciaonar o elemento na pagina
    pagina.add(titulo)
    pagina.add(botao_iniciar)
    pagina.scroll = ft.ScrollMode.AUTO
    pagina.update()
 
# rodar seu aplicativo/site
ft.app(target=main)
    