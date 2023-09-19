def inputyearstu():
    year = int(input('ปีการศึกษา : '))
    return year

def checkyearstu(yearstu):
    if yearstu == 1 :
        return 'Welcome Freshman'
    elif yearstu == 2 :
        return 'Welcome Sophomore'
    elif yearstu == 3 :
        return 'Welcome Junior'
    elif yearstu == 4 :
        return 'Welcome Senior'

def showyearstu(year , yearstu):
    print(f'ปีการศึกษา {year} จะได้ {yearstu}')

yearstu = inputyearstu()
checkyear = checkyearstu(yearstu)
showyearstu(yearstu , checkyear)