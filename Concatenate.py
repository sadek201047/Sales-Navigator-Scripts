import csv


with open('book1.csv', 'r') as csv_file:
       csv_reader = csv.reader(csv_file)
       links = list(csv_reader)

text= ''       

for link in links:
        link_0 = link[0]
        text =  text +', '+ str(link_0)

print(text)        
