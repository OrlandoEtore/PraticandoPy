#Impressoes de Padroes


# print("# ", end='')
# print("# ")
# print("# ", end='')
# print("#")

# for i in range(5):
#     for j in range(5):
#         print("* ",end=" ")
#     print()

# *  *  *  *  *  
# *  *  *  *  *  
# *  *  *  *  *  
# *  *  *  *  *  
# *  *  *  *  *  

for i in range(5):
    for j in range(i+1):
        print("* ",end="")
    print()

# saida :
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 


# for i in range(5):
#     for j in range(5-i):
#         print("* ",end="")
#     print()

# saida :
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 


p = 9 

for a in range(1,(p+1)//2+1):
    for b in range((p+1)//2 - a ):
        print(" ", end ="")
    for c in range((a*2)-1):
        print("*",end="")
    print()

for a in range((p+1)//2+1,p +1):
    for b in range(a - (p+1)//2):
        print(" ", end="")
    for c in range((p+1-a)*2-1):
        print("*",end="")
    print()

