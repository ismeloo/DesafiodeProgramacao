

password = input("Informe sua senha:" , )
 
if (len(password)<6):
  print (f"Sua senha não atende os requisitos mínimos de segurança, deve ter 6 caracteres ou mais , você digitou {password} e ele tem apenas ", (len(password)), "caracteres ")
else:
  print ("Parabéns sua senha atende os requisitos")
 

'''Uma estrutura de else/if para validar a senha , conforme as caracteristicas necessarias '''