"""
Известно, что амплитуда качающегося маятника с каждым разом затухает
на 8,4% от амплитуды прошлого колебания.
Если качнуть маятник,
то, строго говоря, он не остановится никогда,
просто амплитуда будет постоянно уменьшаться до тех пор,
пока мы не сочтём такой маятник остановившимся.

Напишите программу,
определяющую, сколько раз качнётся маятник, прежде чем он, по нашему мнению, остановится.

Программа получает на вход
начальную амплитуду колебания в сантиметрах
и конечную амплитуду его колебаний,
которая считается остановкой маятника.

Обеспечьте контроль ввода.

Пример:

> Введите начальную амплитуду: 1
> Введите амплитуду остановки: 0.1

> Маятник считается остановившимся через 27 колебаний

"""

start_amplitude = float(input('Enter a starting amplitude (cm): '))
stop_amplitude = float(input('Enter a stopping amplitude (cm): '))
attenuation_coefficient = 8.4

count_fluctuations = 0

while start_amplitude > stop_amplitude:
    count_fluctuations += 1
    # start_amplitude -= start_amplitude * attenuation_coefficient / 100
    start_amplitude *= 1.0 - attenuation_coefficient / 100

print(f'Pendulum will stop in {count_fluctuations} fluctuations')

