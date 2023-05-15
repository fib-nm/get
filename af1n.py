import RPi.GPIO as gpio
import time
import matplotlib.pyplot as plt

gpio.setmode(gpio.BCM)
leds = [21, 20, 16, 12, 7, 8, 25, 24]
gpio.setup(leds, gpio.OUT)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
gpio.setup(dac, gpio.OUT, initial=gpio.HIGH)
comp = 4
troyka = 17

gpio.setup(comp, gpio.IN)


def d2b(decimal): return [int(bit) for bit in bin(decimal)[2:].zfill(8)]


def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2**i
        gpio.output(dac, d2b(k))
        time.sleep(0.005)
        if gpio.input(comp) == 0:
            k -= 2**i
    return k


try:
    v = 0
    t = 0
    dt = 0.005
    time_experiment = []
    results = []
    start_time = time.time()
    gpio.setup(troyka, gpio.OUT, initial=gpio.LOW)
    print('Начало зарядки конденсатора ')
    while v < 130:
        print(v)
        v = adc()
        results.append(v*3.3/255)
        time_experiment.append(t)
        time.sleep(dt)
        gpio.output(leds, d2b(v))
        t += dt+0.005

    gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
    print('Начало разрядки конденсатора ')
    while v > 70:
        print(v)
        v = adc()
        results.append(v*3.3/255)
        time_experiment.append(t)
        time.sleep(dt)
        gpio.output(leds, d2b(v))
        t += dt+0.005

    end_time = time.time()
    t_0 = end_time-start_time


    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(time_experiment, results, color='black', linewidth=1)
    plt.xlabel('t, с')
    plt.ylabel('U, В')
    plt.grid(visible=True, which='major')
    plt.show()


    with open('data.txt', 'w') as f:
        for i in results:
            f.write(str(i) + '\n')
    with open('settings.txt', 'w') as f:
        f.write(str(1 / (dt+0.005)) + '\n')
        f.write(str(3.3 / 256) + '\n')


    print('Продолжительность эксперимента:', t_0)
    print("Период одного измерения:", (dt+0.005))
    print("Средняя частота дискретизации:", (1 / (dt+0.005)))
    print('шаг квантования:', (3.3 / 256))


finally:
    gpio.output(leds, 0)
    gpio.output(dac, 0)
    gpio.cleanup()
