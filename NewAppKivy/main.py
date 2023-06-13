from kivy.app import App
from kivy.lang import Builder
import requests

UI = Builder.load_file("screen.kv")


def get_quotation(coin):
    link = f"https://economia.awesomeapi.com.br/last/{coin}-BRL"
    response = requests.get(link)

    if response.status_code == 200:
        quotation = response.json()
        return quotation[f"{coin}BRL"]["bid"]
    else:
        print(f"API {link} is unavailable")
        return 0


class MyNewApp(App):
    def build(self):
        return UI

    def on_start(self):
        self.root.ids["mDollar"].text = f"Dollar = R${get_quotation('USD')}"
        self.root.ids["mEuro"].text = f"Euro = R${get_quotation('EUR')}"
        self.root.ids["mBitc"].text = f"Bitcoin = R${get_quotation('BTC')}"
        self.root.ids["mEthe"].text = f"Ethereum = R${get_quotation('ETH')}"


MyNewApp().run()

