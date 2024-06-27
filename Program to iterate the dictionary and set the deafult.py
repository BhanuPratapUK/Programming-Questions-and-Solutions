Dict1={1:'Bhanu',2:'Amit',3:'Akash','class':'ooops'}
Dict1['piyush']= 'kapoor'
Dict1.setdefault('marks',1000)
for i in Dict1.items():
    print(i)
print('The Value of this Key  is--->',Dict1.get('piyush'))


