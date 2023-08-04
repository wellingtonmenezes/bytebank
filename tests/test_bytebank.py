from codigo.bytebank import Funcionario
from pytest import mark
import pytest

class TesteClass:
    def test_quando_idade_recebe_23_04_1984_deve_retornar_39(self):
        entrada = '23/04/1984' # Given (Contexto)
        esperado = 39
        
        funcionario_teste = Funcionario('Wellington', entrada, 5000)
        resultado = funcionario_teste.idade() # When (Ação)

        assert  resultado == esperado # Then (Desfecho)

    def test_quando_nome_Wellington_Menezes_deve_retornar_Menezes(self):
        entrada = 'Wellington Menezes'
        esperado = 'Menezes'
        funcionario_teste = Funcionario(entrada, '23/04/1984', 5000)
        resultado = funcionario_teste.sobrenome()

        assert resultado == esperado

    def test_quando_decrescimento_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Luan Marx'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '27/04/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_funcionario_tem_direito_ao_bonus_retorna_valor_bonus(self):
        entrada_salario = 1000
        esperado = 100

        funcionario_teste = Funcionario('Rosimeire', '25/07/1986', entrada_salario)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_funcionario_nao_tem_direito_ao_bonus_retorna_exception(self):
        with pytest.raises(Exception):
            entrada_salario = 100000
            funcionario_teste = Funcionario('Rosimeire', '25/07/1986', entrada_salario)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado
