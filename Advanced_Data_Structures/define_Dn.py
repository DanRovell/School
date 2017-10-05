# define Dn

#Dn = [(a,b,c) for a in ['A', 'B', 'C'] for b in ['A', 'B', 'C'] for c in ['A', 'B', 'C']]

A = ['A', 'B', 'C', 'D']
Dn = [(a, b, c, d) for a in A for b in A for c in A for d in A]
