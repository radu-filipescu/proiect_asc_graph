from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import urllib.request

f = urllib.request.urlopen(httpswww.top500.org)
mybytes = f.read()

html_doc = mybytes.decode(utf8)
f.close()

soup = BeautifulSoup( html_doc , 'html.parser')

main_url = httpswww.top500.org
add_url = liststop500

def str_to_int( x )
   x = x[3040]

   number = 0

   for i in range( len(x) )
       if( x[i] == . ) break
       if( x[i].isdigit() ) number = number  10 + ord( x[i] ) - ord( '0' )

   return number

average = []
years = []
for year in range( 1993, 2021 )

    sum = 0

    for month in [ 06, 11 ]

        url = main_url +  + add_url +  + str(year) +  + month + 

        f = urllib.request.urlopen( url )
        mybytes = f.read()

        html_doc = mybytes.decode(utf8)
        f.close()

        soup = BeautifulSoup(html_doc, 'html.parser')

        lst = str(soup).split(n)

        #( soup )

        if year  2004 value = 15
        else value = 14


        if year  2004 search_string = thRpeak (TFlops)th
        else search_string = thRpeak (GFlops)th

        for i in range(len(lst))
            if lst[i] == search_string

                sum += str_to_int( lst[i + value] )
                sum += str_to_int( lst[i + value  2] )
                sum += str_to_int( lst[i + value  3 ] )

                if value == 14
                    sum = 1000

                break

    average.append( round( sum  3 , 2 ) )

    years.append( year )

progress = 0
for i in range( 1, len(average) )
    progress += average[i] - average[i-1]

progress = 28
print( Progresul mediu realizat pe an este , progress, TFlopssyear )

plt.plot( years, average )

plt.axis([ 1993, 2020 , int(min(average)) , int(max(average))])
plt.show()