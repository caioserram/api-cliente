from rest_framework import serializers
from clientes.models import Cliente
import re
from validate_docbr import CPF

def celular_valido(celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta

def cpf_valido(cpf):
    cpf_validator = CPF()
    return cpf_validator.validate(cpf)


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, attrs):
        if not cpf_valido(attrs["cpf"]):	
            raise serializers.ValidationError('O CPF deve ser válido')
        if not attrs["nome"].isalpha():
            raise serializers.ValidationError('O nome deve ter apenas letras')
        if len(attrs["rg"]) != 9:
            raise serializers.ValidationError('O RG deve ter 9 dígitos')
        if not celular_valido(attrs["celular"]):
            raise serializers.ValidationError('O celular deve seguir o padrão 99 99999-9999')
        return super().validate(attrs)