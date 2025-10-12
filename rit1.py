a=[1,2,3,4,5,6,7,8]
b=[10,11,12,13,14,15,16,17,18,19,20]
c=[1,2,3,4,5,6,7,8,9]

s=0
t=0
for i in range(792):
  ai=i%8
  bi=i%11
  ci=i%9
  s+=int(str(a[ai])+str(b[bi])+str(c[ci]))
  t+=(a[ai])*(b[bi])*(c[ci])
  #print(s,t)

print(s)
print(t)
print(s/t)