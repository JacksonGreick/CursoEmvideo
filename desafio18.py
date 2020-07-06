co=float(input("digite o valor do cateto oposto"))
ca=float(input("digite o valor do cateto adjacente"))
hi=float(input("digite o valor da  hipotenusa "))

sen=float(co/hi)
cos=float(ca/hi)
ta=float(co/ca)
print("o cateto oposto e o {} o adjacente e o {} sua hipotenusa e o {} sendo que o seno e o {} e o coseno {} e a tangente são {}".format(co, ca, hi, sen, cos, ta))


