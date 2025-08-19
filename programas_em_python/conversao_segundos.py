segundos = int(input("Digite os segundos: "))
hora = (segundos//3600)
minutos = int((segundos%3600)/60)
segundos_final = (segundos%60)

mensagem = f"""
  {hora} : {minutos} : {segundos_final}
"""
print(mensagem)