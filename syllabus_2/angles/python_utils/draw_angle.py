from pyperclip import copy

class Angle():
    def __init__(self,
                 name="B,A,C",
                 begin_amplitude=0,
                 amplitude=30,
                 side_length=(2, 2),
                 colors=('blue!20', 'blue')):
        self.name = name
        self.sommets = name.split(',')  # une liste avec les sommets
        self.begin = begin_amplitude
        self.amplitude = amplitude
        self.side_length = side_length
        self.colors = colors
        self.fill = self.colors[0]
        self.mark = self.colors[1]

    def create_latex(self):
        balises = ["\\begin{tikzpicture}\n" ,"\n\\end{tikzpicture}"]
        content = [f"\t\\tkzDefPoint(0,0){{{self.sommets[1]}}}",
        f"\t\\tkzDefPoint({self.begin}:{self.side_length[0]}){{{self.sommets[0]}}}",
        f"\t\\tkzDefPoint({self.begin + self.amplitude}:{self.side_length[1]}){{{self.sommets[2]}}}",
        f"\t\\tkzFillAngle[fill={self.fill}]({self.name})",
        f"\t\\tkzMarkAngle[mark=none, color={self.mark}]({self.name})",
        f"\t\\tkzDrawLines({self.sommets[1]},{self.sommets[0]} {self.sommets[1]},{self.sommets[2]})",
        f"\t\\tkzDrawPoints({self.name})",
        f"\t\\tkzLabelPoints({self.name})"]
        latex = "\n".join(content).join(balises)
        return latex

ang = Angle(name='J,K,L', begin_amplitude=120, amplitude=70)
copy(ang.create_latex())
print("== LaTeX code copy to the clipboard ==")


