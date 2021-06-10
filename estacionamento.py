from abc import ABC, abstractmethod, abstractproperty


class Veiculo(ABC):
    def __init__(self, modelo):
        self.modelo = modelo
    
    @abstractproperty
    def quantidade_por_vaga(self):
        pass

    def __str__(self):
        raise NotImplementedError()


class Carro(Veiculo):
    def __str__(self):
        return f"Carro('{self.modelo}')"

    @property
    def quantidade_por_vaga(self):
        return 1


class Moto(Veiculo):
    def __str__(self):
        return f"Moto('{self.modelo}')"

    @property
    def quantidade_por_vaga(self):
        return 2


class Estacionamento:
    def __init__(self, andar, vagas_por_andar):
        self.andar = andar
        self.vagas_por_andar = vagas_por_andar
        self.matriz_vagas = []
        for l in range(self.andar):
            aux = []
            for c in range(self.vagas_por_andar):
                aux.append("vazia")
            self.matriz_vagas.append(aux)
        self.vagas_dict = {}
        self.l = 0
        self.c = 0
    
    def _re_join(self, vaga_atual, novo):
        veiculos = vaga_atual.split(', ')
        veiculos.append(novo)
        return ', '.join(veiculos)
    
    def _get_proxima_vaga(self, quantidade_por_vaga):
        ultima_vaga = self.vagas_dict.get(quantidade_por_vaga)
        if ultima_vaga:
            if len(self.matriz_vagas[ultima_vaga[0]][ultima_vaga[1]].split(', ')) < quantidade_por_vaga:
                return ultima_vaga, True
        result = (self.l, self.c)
        if self.c < self.vagas_por_andar - 1:
            self.c += 1
        elif self.l < self.andar - 1:
            self.c = 0
            self.l += 1
        else:
            raise StopIteration()
        self.vagas_dict[quantidade_por_vaga] = result
        return result, False
    
    def estacionar(self, *args):
        veiculos = [i for i in args]
        for veiculo in veiculos:
            lc, has_re_join = self._get_proxima_vaga(veiculo.quantidade_por_vaga)
            linha = lc[0]
            coluna = lc[1]
            if has_re_join:
                self.matriz_vagas[linha][coluna] = self._re_join(self.matriz_vagas[linha][coluna], str(veiculo))
            else:
                self.matriz_vagas[linha][coluna] = str(veiculo)
        return self.matriz_vagas
