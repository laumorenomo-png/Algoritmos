def sumatorias(Minimo,Maximo):
  x=0
  suma_numeros= sum(x for x in range(Minimo,Maximo+1))
  suma_cuadrados= sum(x**2 for x in range(Minimo,Maximo+1))
  suma_cubos= sum(x**3 for x in range(Minimo,Maximo+1))
  return f"{suma_numeros} {suma_cuadrados} {suma_cubos}"
  


N = int(input())
for _ in range(N):
    T=list(map(int,input().strip().split()))
    Minimo,Maximo=min(T),max(T)
    resultado=sumatorias(Minimo,Maximo)
    print(resultado)
    
