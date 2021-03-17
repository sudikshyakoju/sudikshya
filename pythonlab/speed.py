'''You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way.
How long will the bus journey take? aternatively, you could run to the university. You jog the first mile at 7mph,
then run the next two at 15mph, before jogging the last at 7mph again. Will this be quicker or slower than the bus?'''

live_apart=4
bus_drives=25
time_taken=((live_apart/bus_drives)*60)
stop_time=20
total_time=time_taken+stop_time
print(f"total time taken by bus is {total_time}")

jog1=((1/7)*60)
jog2=((2/15)*60)
jog3=((1/7)*60)
total_jog=jog1+jog2+jog3
print(f"total jog time is {total_jog}")

if (total_time>total_jog):
    print('the bus is slower than jogging')
else:
    print('the bus is faster than jogging')
