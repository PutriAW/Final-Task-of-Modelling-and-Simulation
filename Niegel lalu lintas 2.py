import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

M = 100 # panjang lintasan
p = 0.3  # probabilitas
v = 0 #velocity awal 
v_maks = 5 #velocity atau kecepatan maksimal
t_max = 100 #waktu maksimal
t = 0 # inisialisasi waktu
dt = 1 # selisih waktu
N = 10 # jumlah kendaraan
# pos = 0 
pos_list =[] #list posisi
pos_awal = [] #list posisi awal
v_list = [v] #list kecepatan
ptrn = 0
jum_putaran =[] # jumlah putaran masing masing benda
j_kend = 0 # inisialisasi jumlah kendaraan awal yang lewat pada interval[x80,x90]
y = 1
colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe']

fig = plt.figure()

#generate bilangan random
def randomProbability():
	rand_ = random.random()
	return rand_


#generate bilangan random posisi awal kendaraan 
for i in range(N):
	rand = random.random()
	pos_list.append(round(rand*M))
	pos_awal = pos_list
	v_list.append(v)

#mengurutkan posisi kendaraan yang sudah di generate menggunakan bilangan random
print(pos_list)
pos_list = np.sort(pos_list)
print(pos_list)
pos_awal = pos_list

#function untuk menampilkan posisi dan kecepatan setiap mobil
def posisiDanKecepatan(pos_list, v_list, N):
	for i in range(N):
		print('Posisi mobil ke-'+str(i+1)+'= ',pos_list[i], end='\n')
		print('kecepatan = ', v_list[i])

#output posisi awal 
print('posisi awal dan kecepatan awal', end='\n')
posisiDanKecepatan(pos_awal,v_list,N)
print(end='\n\n')

#inisialisasi jumlah putaran setiap mobil dengan 0
for x in range(N):
	jum_putaran.append(ptrn)

# print(jum_putaran)


# proses utama
while t < t_max:
	# posisi mobil
	plt.clf()	
	# plt.close(fig)
	#update kecepatan
	for k in range(N):
		v_list[k] = np.minimum(v_list[k] + 1, v_maks)
		if (k != N-1):
			d = pos_list[k+1] - pos_list[k]
		else : 
		  d = pos_list[k-9] - pos_list[k]

		if ( d < 0):
			d += 100

		v_list[k] = np.minimum(v_list[k], d-1)

		if (randomProbability() <= p):
			v_list[k] = np.maximum(0, v_list[k]-1)

	#posisi mobil
	for j in range(N):
		pos_list[j] = pos_list[j] + v_list[j]
		if (pos_list[j] >= M):
			pos_list[j] -= 100  

		#menghitung jumlah kendaraan pada interval [x80, x90]
		if (pos_list[j] >=80) and (pos_list[j]<=90):
			j_kend += 1

		#menghitung jumlah putaran setiap kendaraan 
		if(pos_list[j] - pos_awal[j] >= 0) and (pos_list[j] - pos_awal[j] <= v_maks-1):
			jum_putaran[j] += 1
			print(jum_putaran[i], end='\n')
		plt.scatter(pos_list[j], 1, color = colors[j], s = 80, label='Kendaraan #'+str(j+1))

	print('posisi dan kecepatan pada detik ke- '+str(t+1), end='\n')
	posisiDanKecepatan(pos_list, v_list, N)
	print(end="\n")

	plt.ylim(0, 5)
	plt.legend()
	t += dt
	
	# plt.show()

	# fig.savefig('plot'+str(t)+'.png')

kepadatan = j_kend/t_max
print('Soal NO. 2 : kepadatan pada interval [x80, x90] = ', kepadatan, end='\n')
print('Soal NO. 3 : rata rata setiap mobil kembali ke posisi awal ' , end='\n')

print(jum_putaran)
for i in range(N):
	print('Mobil ke- '+str(i+1),' = ', t_max/jum_putaran[i])
