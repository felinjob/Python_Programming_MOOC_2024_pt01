# Write your solution here
def numberslist():
    listnum = []
    for num in range(0, 100):
        listnum.append(num)
    return listnum
    
def textlist():
    textnum = []
    listaunid = ["zero", "one", "two", 
            "three", "four", "five", 
            "six", "seven", "eight", 
            "nine", "ten"
            ]
    listateen = ["eleven", "twelve", "thirteen", 
            "fourteen", "fifteen", "sixteen",
            "seventeen", "eighteen", "nineteen"
            ]            
    
    listadez = ["twenty", "thirty", "forty",
            "fifty", "sixty", "seventy",
            "eighty", "ninety"
            ]
    for item in listaunid:
        textnum.append(item)
    for item in listateen:
        textnum.append(item)
    for item in listadez:
        for tens in listadez:
            textnum.append(tens)
            for unid in listaunid:
                if unid == "zero" or unid == "ten":
                    continue
                textnum.append(tens + "-" + unid)
    return textnum
    
    
def dict_of_numbers():
    numberdict = {}
    numbers = numberslist()
    numbnames = textlist()
    for itens in numbers:
        numberdict[itens] = numbnames[itens]
    return numberdict
    
if __name__ ==  "__main__":
    dict_of_numbers()