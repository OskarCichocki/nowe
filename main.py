waga = input ('Siema, oblicze twoje bmi, Podaj swoją wage')
wzrost = input ('jaki masz wzrost? wpisz wartosc liczbowa wyrażona w metrach')
imie = input ('imie poprosze!')
BMI = float(waga) /  float(wzrost)**2
print ('siema',(imie),'twoje BMI to',(BMI) ,'NARA, spierdalaj')
if (BMI) >= 18.5 and (BMI) < 25:
    print('mmm super bmi pozdrawiam')
elif (BMI) >= 25 and (BMI) < 29.9:
    print('mmm no troche prosze schudnac')
elif (BMI) >= 30 and (BMI) < 50:
    print('mam zła wiadomość, trzeba schudnąc!')
elif (BMI) < 18.5 and (BMI) > 1:
    print('chudziak z cb prosze przytyć natychmiast')
else:
    print ('no chyba coś źle wpisano, pewnie kurwa metry z przecinkiem zamiast kropki, spróboj ponownie')
print ('siema',(imie),'twoje BMI to',(BMI) ,'NARA, spierdalaj' 'pozdro')
