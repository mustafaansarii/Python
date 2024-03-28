import random
import gradio as gr

class Toss:
    def __init__(self, toss=("Head", "Tail")):
        self.toss = toss

    def Toss_coin(self):
        Tosscoin = random.choice(self.toss)
        return Tosscoin

def coin_toss():
    obj = Toss()
    result = obj.Toss_coin()
    return result

iface = gr.Interface(fn=coin_toss,
                     inputs=None,
                     outputs="text",
                     title="Coin Toss Simulator",
                     description="Click the button to toss a coin.")
iface.launch()
