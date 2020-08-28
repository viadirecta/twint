import twint
import pandas as pd
import datetime
import webbrowser
import os

## config pandas screen
pd.options.display.max_rows = 10
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
#pd.set_option("display.colheader_justify","left")

###fecha
hoy = datetime.date.today()
hoy = hoy.strftime( '%Y-%m-%d')
hoyT = hoy + ' 00:00:00'

buscar = input("que quieres buscar? :  ")
desde = input(" fecha? (yyyy-mm-dd):")
##user = input("usuario? : ")
             
c = twint.Config()

###si no hay usuario sólo busqueda
##if user != "":
##    c.Username = user
##else:
##    c.Username = ""
 
c.Search = buscar
c.Limit = 50
# si hay una fecha desde esa fecha, si no hoy desde las 00:00
if desde != "":
    desde  = desde + ' 00:00:00'
    c.Since = desde
else:
    c.Since = hoyT
#custom format
c.Format = " {date} {time} | {username} | {tweet}"
c.Hide_output = True
c.Pandas = True

c.Store_csv = True
c.Output = buscar+".csv"
#c.Lang = "en"
#c.Translate = True
#c.TranslateDest = "it"
twint.run.Search(c)

tweets_df = twint.storage.panda.Tweets_df
tweets_df.set_index(['date'])
#tweets = tweets_df['tweet', 'username']

if c.Output != "":
    data = pd.read_csv(c.Output)
    data = pd.DataFrame(data)
    data = data[['date', 'time', 'name', 'tweet']]
    d = pd.Series(['date'])
    #pd.to_datetime(d, dayFirst, errors= 'coerse')
    data['date']= data.date.astype('datetime64')
    data['time']= data.time.astype('datetime64')
    html= data.to_html(escape=False, border= 1)
    file = (buscar +".html")
    f = open(file,"w",  encoding='utf-8')
    f.write(html)
    f.close()
    filename = 'file:///'+os.getcwd()+'/' + file
    
    webbrowser.open(filename)
    #print("<html><body style='font:10px Verdana, sans serif'>" + html +"</body></html>" )
        

    
else :
    print("nothing found. Try with another dates or phrase search")
