__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Based on MindSumo puzzle #22
Print all the dates, in mm/dd/yyyy format, in which every single digit is unique.
'''
months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "12"]  # not 11
days = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
days += [str(x) for x in range(10, 32)]
days.remove("22")  # not 22
for year in range(1000, 9999):
    yearList = list(str(year))
    used = [str(n) for n in range(10)]
    if len(yearList) == len(set(yearList)) and "0" not in yearList:
        used1 = list(set(used).difference(set(yearList)))
        for month in months:  # months have to have 0,1
            if list(month)[0] in used1 and list(month)[1] in used1:
                used2 = list(set(used1).difference(set(list(month))))
                for day in days:  # days have to have 0,1,2
                    if list(day)[0] in used2 and list(day)[1] in used2:
                        print(str(year) + " " + str(month) + " " + str(day))
                        #180