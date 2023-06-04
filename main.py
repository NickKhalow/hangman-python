from gmsimple import GmSimple
from wdsimple import WdSimple
from wdmistakes import WdMistakes

if __name__ == '__main__':
    GmSimple(
        WdMistakes(
            WdSimple("hello"),
            print,
            5
        ),
        input,
        print
    ).play()
