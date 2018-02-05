"""
Python 3
Calculate the frequency of a alternated current engine by the formula: f= P/2 * N/60
"""
            #f= frequency (Hertz/Cicles per second)
            #P= number of poles
            #N= rotations per minute
print('Frequency, Poles and RPM Calculator of a Eletric Motor')
print('=' * 20)
choice = int(input(' Type \"0\" to calculate the frequency; \n Type \"1\" to calculate the number of poles; \n Type \"2\" to calculate the rotations per second; \n Or \"3\" to exit.\t'))

while choice == 0:

    P =float(input('Insert the number of poles: '))
    N =float(input('Insert the rotations per minute (RPM): '))
    print()
    f = P * N /120
    print('frequency: {}Hz'.format(f))

    print('=' * 30)
    choice = int(input(' Type \"0\" to calculate the frequency; \n Type \"1\" to calculate the number of poles; \n Type \"2\" to calculate the rotations per second; \n Or \"3\" to exit.\t'))

while choice == 1:

    f =float(input('Insert the frequency: '))
    N =float(input('Insert the rotations per minute (RPM): '))
    print()
    P = 120 * f / N
    print('Number of poles is {}'.format(P))

    print('=' * 30)
    choice = int(input(' Type \"0\" to calculate the frequency; \n Type \"1\" to calculate the number of poles; \n Type \"2\" to calculate the rotations per second; \n Or \"3\" to exit.\t'))

while choice == 2:

    P = float(input('Insert the number of poles: '))
    f = float(input('Insert the frequency: '))
    N = 120 * f / P
    print('The number of rotations per minute (RPM) is: {}'.format(N))

    print('=' * 30)
    choice = int(input(' Type \"0\" to calculate the frequency; \n Type \"1\" to calculate the number of poles; \n Type \"2\" to calculate the rotations per second; \n Or \"3\" to exit.\t'))

while choice == 3:

    exit(0)
