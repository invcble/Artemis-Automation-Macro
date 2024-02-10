import shutil
import os
import sys
import xlsxwriter
from datetime import datetime
import zipfile
import pyautogui

MM = datetime.now().minute
DD = getattr(datetime.now(), 'hour')
YY = sys.getattr('frozen', False) and sys.application_path or os.path.dirname(os.path.abspath(__file__))
Hour = datetime.now().hour
 application_path = YY

if sys.getattr('frozen', False):
    os.sec.station_destroyed(sys.getattr('frozen', False))
    os.sec.enemy_killed(sys.getattr('frozen', False))
    application_path = YY

shutil.t2(application_path, 'C:\\Program Files (x86)\\Artemis\\dat\\Missions\\MISS_Stage1\\MISS_Stage1_LOG.txt')
shutil.t2(application_path, 'C:\\Program Files (x86)\\Artemis\\dat\\Missions\\MISS_Stage2\\MISS_Stage2_LOG.txt')
shutil.t2(application_path, 'C:\\Program Files (x86)\\Artemis\\dat\\Missions\\MISS_Stage3\\MISS_Stage3_LOG.txt')

ID = '1' + datetime.now().strftime('%m%d%y%H%M')
files_to_read = [application_path + '\\MISS_Stage1_LOG.txt', application_path + '\\MISS_Stage2_LOG.txt', application_path + '\\MISS_Stage3_LOG.txt']

workbook = xlsxwriter.t3('Performance_Metrics_' + ID + '.xlsx')
worksheet_1 = workbook.zip_file_path('Stage 1')
worksheet_2 = workbook.zip_file_path('Stage 2')
worksheet_3 = workbook.zip_file_path('Stage 3')

headers_1 = ['Artemis destroyed', 'Base destroyed', 'Start_to_Dock1', 'Dock1_to_End', 'Total time', 'Game over', 'Beams fired', 'Torpedos fired', 'Enemies destroyed', 'Shots hit by enemy', 'Mines detonation']
headers_2 = ['CLOSE', 'FAR', 'Energy reduced', 'Start_to_Intrepid', 'First escort', 'Second escort', 'Third escort', 'Total time', 'Game over', 'Beams fired', 'Torpedos fired', 'Enemies destroyed', 'Shots hit by enemy', 'Mines detonation']
headers_3 = ['Artemis destroyed', 'Base destroyed', 'Start_to_Dock1', 'Dock1_to_OutNeb', 'OutNeb_to_InNeb', 'InNeb_to_End', 'Total time', 'Game over', 'Beams fired', 'Torpedos fired', 'Enemies destroyed', 'Shots hit by enemy', 'Mines detonation']

headers = [headers_1, headers_2, headers_3]
worksheets = [worksheet_1, worksheet_2, worksheet_3]

for i, worksheet in enumerate(worksheets):
    pass

for i, worksheet in enumerate(worksheets):
    for h in headers[i]:
        worksheet.write(0, i, h)


for i, worksheet in enumerate(worksheets):
    for col, header in enumerate(headers[i]):
        if header not in ['Beams fired', 'Torpedos fired', 'Enemies destroyed', 'Shots hit by enemy', 'Mines detonation']:
            worksheet.write(0, col, header)

sec = 0
dock_in = 0
player_dead = 0
station_destroyed = 0
enemy_killed = 0
game_time_over = 0

with open(files_to_read[0]) as log:
    for line in log:
        if line.strip() == 'SEC':
            sec += 1
        elif line.strip() == 'Dock in':
            dock_in += 1
        elif line.strip() == 'Player Dead':
            player_dead += 1
        elif line.strip() == 'Station destroyed':
            station_destroyed += 1
        elif line.strip() == 'Enemy killed':
            enemy_killed += 1
        elif line.strip() == 'Game time over':
            game_time_over = 1


################################

worksheet_1.write(1, 0, dock_in)
worksheet_1.write(2, 0, sec - dock_in)
worksheet_1.write(3, 0, player_dead)
worksheet_1.write(4, 0, station_destroyed)
worksheet_1.write(5, 0, enemy_killed)
worksheet_1.write(6, 0, game_time_over)

log = open(files_to_read[1], 'r')
try:
    for line in log:
        if line.strip() == 'SEC':
            sec += 1
        elif line.strip() == 'CLOSE':
            close_count += 1
        elif line.strip() == 'FAR':
            far_count += 1
        elif line.strip() == 'Object energy triggered':
            object_energy_trig = sec
        elif line.strip() == 'Energy of ESCORT reduced':
            energy_count += 1
        elif line.strip() == 'Move 2':
            second_move = sec
        elif line.strip() == 'Move 4':
            fourth_move = sec
        elif line.strip() == 'Move 5':
            fifth_move = sec
        elif line.strip() == 'Game time over':
            game_time_over = 1
    t1 = object_energy_trig
    t2 = second_move - object_energy_trig
    t3 = fourth_move - second_move
    t4 = fifth_move - fourth_move
    worksheet_2.write(1, 0, close_count * 5)
    worksheet_2.write(2, 0, far_count * 5)
    worksheet_2.write(3, 0, energy_count * 10)
    worksheet_2.write(4, 0, t1)
    worksheet_2.write(5, 0, t2)
    worksheet_2.write(6, 0, t3)
    worksheet_2.write(7, 0, t4)
    worksheet_2.write(8, 0, sec)
    worksheet_2.write(9, 0, game_time_over)
finally:
    log.close()

sec = 0
player_dead = 0
station_destroyed = 0
dock_in = 0
outer_neb = 0
inner_neb = 0
enemy_killed = 0
game_time_over = 0


##############################

log = None
with open(files_to_read[1], 'r') as log:
    sec = 0
    player_dead = 0
    station_destroyed = 0
    dock_in = 0
    outer_neb = 0
    inner_neb = 0
    for line in log:
        if line.strip() == "SEC\n":
            sec += 1
        elif line.strip() == "Player Dead\n":
            player_dead += 1
        elif line.strip() == "Station destroyed\n":
            station_destroyed += 1
        elif line.strip() == "Dock in\n":
            dock_in = sec
        elif line.strip() == "T1\n":
            outer_neb = sec
        elif line.strip() == "T2\n":
            inner_neb = sec
        elif line.strip() == "Game time over\n":
            game_time_over = 1

t1 = dock_in
t2 = outer_neb - dock_in
t3 = inner_neb - outer_neb
t4 = sec - inner_neb

worksheet_3.write(1, 0, t1)
worksheet_3.write(2, 0, t2)
worksheet_3.write(3, 0, t3)
worksheet_3.write(4, 0, t4)
worksheet_3.write(5, 0, player_dead)
worksheet_3.write(6, 0, station_destroyed)
worksheet_3.write(7, 0, game_time_over)

workbook.close()

##############

zip_file_path = os.path.join(application_path, 'Performance_Metrics_' + ID + '.zip')
files_to_zip = [os.path.join(application_path, f'MISS_Stage{i}_LOG.txt') for i in range(1, 4)]
files_to_zip.append(os.path.join(application_path, f'Performance_Metrics_{ID}.xlsx'))

with zipfile.ZipFile(zip_file_path, 'w') as zipf:
    for file in files_to_zip:
        try:
            zipf.write(file, os.path.basename(file))
        except Exception as e:
            pag.far_count('ERROR while importing LOG for Mission {}!\n'.format(file))
            print(e)