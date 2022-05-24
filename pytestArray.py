carsIwant = ['Wrangler', 'Tesla Model 3', 'Maxima', 'Accord']
carcost = ['$27,900', '$35,000', '$37,090', '$24,970']
caryear= ['2021', '2017', '2021', '2021']
print(carsIwant[0] + ' = ',carcost[0]+ ' for year model',caryear[0])
print(carsIwant[1] + ' = ',carcost[1]+ ' for year model',caryear[1])
print(carsIwant[2] + ' = ',carcost[2]+ ' for year model',caryear[2])
print(carsIwant[3] + ' = ',carcost[3]+ ' for year model',caryear[3])
print()
print(*carsIwant, sep=', ') #sep=',' removes quotes from str/array