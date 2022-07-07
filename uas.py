from turtle import speed


print('\n================================================')
print('implementasi logika fuzzy menggunakan python, studi kasus seberapa cepat berkendara tergantung 2 variabel temp dan cloud')
print('================================================')
x_temp = input('Masukan nilai temp dalam (F) = ')
y_cloud = input('Masukan nilai cloud cover (%) = ')

# refactor string to int
temp = int(x_temp)
cloud = int(y_cloud)


# proses fuzzyfikasi temp
if temp <= 30 :
    val_freezing = 1
    val_cool = 0
    val_warm = 0
    val_hot = 0
if temp > 30 and temp < 50 :
    val_freezing = (50 - temp) / (50 - 30)
    val_cool = (temp - 30) / (50 - 30)
    val_warm = 0
    val_hot = 0
if temp == 50 :
    val_freezing = 0
    val_cool = 1
    val_warm = 0
    val_hot = 0
if temp > 50 and temp < 70 :
    val_freezing = 0
    val_cool = (70 - temp) / (70 - 50)
    val_warm = (temp - 50) / (70 - 50)
    val_hot = 0
if temp == 50 :
    val_freezing = 0
    val_cool = 0
    val_warm = 1
    val_hot = 0
if temp > 70 and temp < 90 :
    val_freezing = 0
    val_cool =  (90 - temp) / (90 - 70)
    val_warm = (temp - 70) / (90 - 70)
    val_hot = 0
if temp >= 90 :
    val_freezing = 0
    val_cool = 0
    val_warm = 0
    val_hot = 1

print('================================================')
print('\nMaka temp dalam variabel linguistik, derajat ke anggotaan adalah')
print('Freezing = ', val_freezing)
print('cool = ', val_cool)
print('warm = ', val_warm)
print('hot = ', val_hot)

# proses fuzzyfikasi cloud
if cloud <= 20 :
    val_sunny = 1
    val_party_cloudy = 0
    val_overcast = 0
if cloud > 20 and cloud <40 :
    val_sunny = (40 - cloud) / (40 - 20)
    # val_party_cloudy = 0
    val_overcast = 0
if cloud > 20 and cloud <50 :
    # val_sunny = (40 - cloud) / (40 - 20)
    val_party_cloudy = (cloud - 20 ) / (50 - 20)
    # val_overcast = (cloud - 20 ) / (50 - 20)
if cloud == 50 :
    val_sunny = 0
    val_party_cloudy = 1
    val_overcast = 0
if cloud > 50 and cloud <80 :
    val_sunny = 0
    val_party_cloudy = (80 - cloud) / (80 - 50)
    # val_overcast = 0
if cloud > 60 and cloud <80 :
    val_sunny = 0
    # val_party_cloudy = (80 - cloud) / (80 - 50)
    val_overcast = (cloud - 60) / (80 - 60)
if cloud >= 80 :
    val_sunny = 0
    val_party_cloudy = 0
    val_overcast = 1

print('================================================')
print('\nMaka Cloud Cover dalam variabel linguistik, derajat keanggotaannya adalah')
print('Sunny = ', val_sunny)
print('Party Cloudy = ',val_party_cloudy)
print('Overcast = ', val_overcast)

# proses inferensi
speed=[]
def InferensiSlow(temp,cloud) :
    if temp != 0 :
        if cloud != 0 :
            hasil = min(temp, cloud)
            speed.append([hasil, 25])

def InferensiFast(temp,cloud) :
    if temp != 0 :
        if cloud != 0 :
            hasil = min(temp, cloud)
            speed.append([hasil, 75])

InferensiSlow(val_freezing, val_sunny)
InferensiSlow(val_freezing, val_party_cloudy)
InferensiSlow(val_freezing, val_overcast)
InferensiSlow(val_cool, val_sunny)
InferensiSlow(val_cool, val_party_cloudy)
InferensiSlow(val_cool, val_overcast)

InferensiFast(val_warm, val_sunny)
InferensiFast(val_warm, val_party_cloudy)
InferensiFast(val_warm, val_overcast)
InferensiFast(val_hot, val_sunny)
InferensiFast(val_hot, val_party_cloudy)
InferensiFast(val_hot, val_overcast)

print('\n================================================')
print('\nMaka Speed Adalah = ', speed)

perkalian = 0
pembagian = 0

for i in range (0, len(speed)):
    a = speed[i][0] * speed[i][1]
    b = speed[i][0]
    perkalian = perkalian + a
    pembagian = pembagian + b

z = perkalian / pembagian
print('================================================')
print('\nKecepatan Mobile adalah : ',z,'Mph')