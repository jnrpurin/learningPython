from kivy.app import App
from kivy.lang import Builder
import requests

UI = Builder.load_file("screen.kv")


class MyNewApp(App):
    def build(self):
        return UI

    def on_start(self):
        self.root.ids["mDollar"].text = f"Dollar = R${self.get_values('USD')}"
        self.root.ids["mEuro"].text = f"Euro = R${self.get_values('EUR')}"
        self.root.ids["mBitc"].text = f"Bitcoin = R${self.get_values('BTC')}"
        self.root.ids["mEthe"].text = f"Ethereum = R${self.get_values('ETH')}"

    def get_values(self, coin):
        link = f"https://economia.awesomeapi.com.br/last/{coin}-BRL"
        req = requests.get(link)
        dicreq = req.json()
        return dicreq[f"{coin}BRL"]["bid"]
        


MyNewApp().run()

