import urllib2
def stats(id):
    a = b = c = d = e = 0
    f= urllib2.urlopen('http://acb.com/stsacumjug.php?cod_jugador=%s' % id)
    html = f.readlines()
    count_lines = len(html)
    for i in range(61,count_lines):
        if('12-13' in html[i]):
            if('LR' in html[i+2]):
                a = int(html[i+3][-10:-6].replace('>','').replace('o','').replace('"',''))
                b = int(html[i+29][-10:-6].replace('>','').replace('o','').replace('"',''))            
            else:
                pass
        if('11-12' in html[i]):
            if('LR' in html[i+2]):
                c = int(html[i+3][-10:-6].replace('>','').replace('o','').replace('"',''))
                d = int(html[i+29][-10:-6].replace('>','').replace('o','').replace('"',''))
            else:
                pass
        if('Promedios' in html[i]):
            e = html[i+27][-10:-6].replace('>','').replace('o','').replace('"','')
            try:
                return id , "12-13" , a , b, round(1.00*b/a,2), "11-12" , c, d , round(1.00*d/c,2), "Total" , e
            except ZeroDivisionError:
                return id , "12-13" , 0 , 0, 0, "11-12" , 0, 0 , 0, "Total" , 0
        else:
            pass