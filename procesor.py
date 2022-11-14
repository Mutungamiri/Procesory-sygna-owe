from pydub import AudioSegment
from pydub.playback import play

def list():

    operation = input('''
Wybierz Opcję:
[1] Amplify
[2] Fade In
[3] Fade Out
[4] High and Low Pass filter
[5] Speedup
[6] Odtwarzanie

''')

    if operation == '1':
        print("Amplify-Zwiększ lub zmniejsz głośność pliku .wav ")
        print("Wybierz plik .wav (file.wav)")
        namei = input()
        song = AudioSegment.from_file(file = namei, format = "wav")
        print("Wpisz wartość amplify")
        ampvalue = input()
        ampsong = song + ampvalue
        print("Nazwij plik wyjściowy")
        nameo = input()
        ampsong.export(out_f = nameo, format = "wav")
    elif operation == '2':
        print("Fade In")
        print("Wybierz plik .wav (file.wav)")
        namei1 = input()
        song1 = AudioSegment.from_file(file = namei1, format = "wav")
        print("Wpisz czas trwania efektu Fade In (np. jeśli 2s to wpisz 2000)")
        fadeinvalue = int(input())
        fadeinsong = song1.fade_in(fadeinvalue)
        print("Nazwij plik wyjściowy")
        nameo1 = input()
        fadeinsong.export(out_f = nameo1, format = "wav")
    elif operation == '3':
        print("Fade Out")
        print("Wybierz plik .wav (file.wav)")
        namei2 = input()
        song2 = AudioSegment.from_file(file = namei2, format = "wav")
        print("Wpisz czas trwania efektu Fade Out (np. jeśli 2s to wpisz 2000)")
        fadeoutvalue = int(input())
        fadeoutsong = song2.fade_out(fadeoutvalue)
        print("Nazwij plik wyjściowy")
        nameo2 = input()
        fadeoutsong.export(out_f = nameo2, format = "wav")
    elif operation == '4':
        print("High Pass and Low Pass Filter")
        print("Wybierz plik .wav (file.wav)")
        namei3 = input()
        song3 = AudioSegment.from_file(file = namei3, format = "wav")
        print("Wybierz filtrowanie 1 - Dolnoprzepustowe, 2 - Górnoprzepustowe")
        choice = input()
        if choice == '1':
            print("Podaj częstotliwość:")
            lowvalue = input()
            passsong = song3.low_pass_filter(int(lowvalue))
        elif choice == '2':
            print("Podaj częstotliwość:")
            highvalue = input()
            passsong = song3.high_pass_filter(int(highvalue))
        print("Nazwij plik wyjściowy")
        nameo3 = input()
        passsong.export(out_f = nameo3, format = "wav")
    elif operation == '5':
        print("Speedup")
        print("Wybierz plik .wav (file.wav)")
        namei4 = input()
        song4 = AudioSegment.from_file(file = namei4, format = "wav")
        print("Wybierz przyspieszenie odtwarzania")
        td = input()
        speedsong = song4.speedup(int(td))
        print("Nazwij plik wyjściowy")
        nameo4 = input()
        speedsong.export(out_f = nameo4, format = "wav")
    elif operation == '6':
        print("Wpisz nazwę pliku który chcesz odtworzyć")
        wavesong = input()
        loadsong = AudioSegment.from_file(file = wavesong, format = "wav")
        play(loadsong)
    else:
        print('You have not chosen a valid operator, please run the program again.')

    again()

def again():
    list_again = input('''
Wrócić do Menu ? (Y/N)
''')

    if list_again.upper() == 'Y':
        list()
    elif list_again.upper() == 'N':
        print('Dowidzenia :)')
    else:
        again()

list()