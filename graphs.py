import matplotlib.pyplot as plt
import csv

Time = []
AllocationRate = []
PromotionRate = []

with open('output.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:

        Time.append(float(row['Time Duration']))
        AllocationRate.append(float(row['Allocation Rate']))
        PromotionRate.append(float(row['Promotion Rate']))


plt.scatter(Time, AllocationRate, color = 'g',s = 100)
plt.xticks(rotation = 25)
plt.xlabel('Time(sec)')
plt.ylabel('Allocation Rate(Mb/sec)')
plt.title('Allocation Rate over time', fontsize = 20)
plt.plot(Time, AllocationRate)
plt.savefig('AllocationRate.png')
plt.show()

plt.scatter(Time, PromotionRate, color = 'g',s = 100)
plt.xticks(rotation = 25)
plt.xlabel('Time(sec)')
plt.ylabel('Promotion Rate vs Allocation Rate(Mb/sec)')
plt.title('Promotion Rate vs Allocation Rate over time', fontsize = 20)
plt.plot(Time, PromotionRate)
plt.savefig('PromotionRate.png')
plt.show()
