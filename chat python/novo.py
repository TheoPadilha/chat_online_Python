import flet as ft

class Msg():
    def __init__(self, usuario:str , texto: str):
        self.usuario = usuario
        self.texto = texto 

def main(page:ft.page):
    chat = ft.Column()
    nova_msg = ft.TextField() 
    
    page.update()

    def enviar_click(e):
        page.pubsub.send_all(Msg(usuario = page.session_id , text = nova_msg.value))
        nova_msg.value = ''
        page.update()

    def msg_on(msg:ft.mensagem):
        chat.controls.append(ft.Text('{}: {}'.format(msg.usuario,msg.texto)))
        page.update()
    
    page.pubsub.subscribe(msg_on)
        
        
        
    page.add(chat , ft.Row(controls=[nova_msg , ft.ElevatedButton('enviar', on_click=enviar_click)]))
    
ft.app(main , view=ft.AppView.WEB_BROWSER)