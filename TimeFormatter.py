import psutil, os, sys
from datetime import datetime, timedelta

now = datetime.now()
print(f'系统时间 {now.strftime("%Y-%m-%d %H:%M:%S")}')
try:
    input_time = datetime.strptime(sys.argv[1], "%H%M")
    input_time = input_time.replace(year=now.year, month=now.month, day=now.day)
    if abs(now - input_time) <= timedelta(minutes=2):
        auto = True
    else:
        auto = False
except:
    auto = False

partitions = psutil.disk_partitions()
to_be_formatted = []
for partition in partitions:
    partition_path = partition.mountpoint
    if partition_path[0] != 'C' and partition_path[1:] == ':\\':
        to_be_formatted.append(partition_path[0:2])
print(f"即将格式化这些分区 {to_be_formatted}，")

if not auto:
    while input('要格式化请输入 format\n') != 'format':
        pass

all_success = True
for disk in to_be_formatted:
    ret = os.system(f'format {disk} /q /y')
    if ret == 0:
        print(f'{disk} 格式化完成\n')
    else:
        print(f'{disk} 格式化失败！失败！失败！\n')
        all_success = False
print('格式化结束，请自行检查格式化效果\n')
if all_success:
    print("""
 OOO   K   K
O   O  K  K
O   O  KKK
O   O  K  K
 OOO   K   K
    """)
while True:
    pass
