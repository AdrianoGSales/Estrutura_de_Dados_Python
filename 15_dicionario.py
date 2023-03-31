"""
    Dicionario é uma estrutura de dados fornecido pela linguagem Python, capaz de ordenar multiplos valores em uma unica
    variavel, por meio de chavrs de chave-valor
"""
#Dicionario é delimitado por chaves{}
#Diferente das listas que tem posições numeradas, os dicionarios possuem posições NOMEADAS. Cada uma da POSIÇÕES nomeadas de 
#um dicionario é chamada PROPRIEDADE

pessoa = {
    "nome": "Grazinho Oliveira Osorio",
    "sexo": "M",
    "idade":71,
    "peso":76,
    "altura":1.60,
    "aposentado" : True

}
#Acessando os valores armazenados no dicionario
print("Nome: ", pessoa ["nome"])
print("Idade: ", pessoa ["idade"])
print("Aposentado: ", pessoa ["aposentado"])

#Calculado o IMC da pessoa
imc=pessoa["peso"]/pessoa["altura"]**2
print(f"O IMC de {pessoa['nome']} é {imc}")

######################################################################3

#Imprimindo formas geometricas planas por meio de dicionario
forma1 = {
    "base" :  7.5,
    "altura":12,
    "tipo": "R" #Retangulo 
}

forma2 = {
    "base" :  6,
    "altura": 2.5,
    "tipo": "T" #Triangulo 
}

forma3 = {
    "base" :  5,
    "altura": 3,
    "tipo": "E" #Elipse
 
}

# forma4 = {
#     "fruta" :  12,
#     "legume": "batata",
#     "tipo": "T" #Elipse
 
# }


from math import pi
def calcular_area(forma):
    if forma["tipo"] =="R":
        return forma["base"] * forma ["altura"]
    elif forma ["tipo"]=="T":
        return forma["base"] * forma["altura"] / 2
    elif forma ["tipo"]=="E":
        return forma["base"]/2 * forma["altura"] / 2 * pi
    else:
        return None
    
########################################################
##Calculando a area das formas
print(f"Base: {forma1['base']}, altura: {forma1['altura']}, tipo: {forma1['tipo']} Area: {calcular_area[forma1]}")

print(f"Base: {forma2['base']}, altura: {forma2['altura']}, tipo: {forma2['tipo']} Area: {calcular_area[forma2]}")

print(f"Base: {forma3['base']}, altura: {forma3['altura']}, tipo: {forma3['tipo']} Area: {calcular_area[forma3]}")

# print(f"Base: {forma4['base']}, altura: {forma4['altura']}, tipo: {forma4['tipo']} Area: {calcular_area[forma4]}")


