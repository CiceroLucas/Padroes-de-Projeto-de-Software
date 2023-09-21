from terreno.quadrado import TerrenoQuadrado
from terreno.retangular import TerrenoRetangular
from engenheiro import Engenheiro

Engenheiro = Engenheiro('Guilherme')
TerrenoQuadrado = TerrenoQuadrado(4)
TerrenoRetangular = TerrenoRetangular(2, 3)

Engenheiro.medir_area(TerrenoQuadrado)
Engenheiro.medir_perimetro(TerrenoRetangular)
