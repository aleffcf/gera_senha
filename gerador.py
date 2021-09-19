from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
from random import randint
from datetime import datetime

Builder.load_file('./gerador.kv')
Window.size = (550, 300)

class GeradorWidget(Widget):
    def gerar(self):
        self.dicionario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '!', '@', '#', '$', '%', '&', '*']
        self.pre_senha = [self.dicionario[randint(1, 66)]]
        self.tamanho = int(self.ids.valor_senha.text)
        self.senha = ''
        data_hora_atuais = datetime.now()
        data_hora_texto = data_hora_atuais.strftime('%d/%m/%Y %H:%M')

        for i in range(self.tamanho):
            if (self.pre_senha[-1] == i):
                i = str(self.dicionario[randint(1, 66)])
                self.pre_senha.append(i)
            else:
                i = str(self.dicionario[randint(1, 66)])
                self.pre_senha.append(i)
        
        for x in self.pre_senha:
            self.senha += str(x)

        self.ids.imprime_senha.text = self.senha

        with open('log.txt', 'a') as log:
            log.write(str(data_hora_texto))
            log.write("- Senha gerada --> ")
            log.write(str(self.ids.imprime_senha.text))
            log.write('\n')

class GeradorApp(App):
    def build(self):
        return GeradorWidget()

if __name__ == "__main__":
    GeradorApp().run()