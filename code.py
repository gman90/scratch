import pandas as pd
import math
coeffs = pd.read_table('inputs/logreg_coefficients.txt',quoting = 3,header =None)
data = pd.read_table('inputs/test_movies.txt',quoting = 3,header =None)
#print data
print len(data)
#print coeffs
minimum_calc=[]
results=[]
for d in data[0]:
    crew = d.split()
    crew=list(set(crew))
    hyp=0
    for c in crew:
        if any(coeffs[0]==c):
            hyp=float(float(1*coeffs[coeffs[0]==c][1])+float(hyp))
            #print hyp
            #raw_input()
        else:
            hyp=hyp+1*0
    results.append([d,float(math.exp(hyp))/float(1+float(math.exp(hyp)))])
for r in results:
    current = r[0].split()
    current=list(set(current))
    temp=[]
    for c in current:
        if any(coeffs[0]==c):
            temp.append([c,coeffs[coeffs[0]==c][1]]

for r in results:
    if r[1]>0.5:
        r[1]=1
    else:
        r[1]=0


results = pd.DataFrame(results,index=None, columns=None)
print results
results.to_csv('predicted_values.csv')




