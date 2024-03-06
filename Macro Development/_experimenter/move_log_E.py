import shutil
import xlsxwriter
import sys

passed_variable = sys.argv[1]
# passed_variable = str(99)

source = "C:\\Program Files (x86)\\Artemis\\dat\\Missions\\"
destination = "C:\\ARTEMIS\\" + passed_variable + "\\"

shutil.copy( source + "MISS_Stage1\\MISS_Stage1_LOG.txt", destination + "MISS_Stage1_LOG.txt")
shutil.copy( source + "MISS_Stage2\\MISS_Stage2_LOG.txt", destination + "MISS_Stage2_LOG.txt")
shutil.copy( source + "MISS_Stage3\\MISS_Stage3_LOG.txt", destination + "MISS_Stage3_LOG.txt")

files_to_read = ["MISS_Stage1_LOG.txt" , "MISS_Stage2_LOG.txt", "MISS_Stage3_LOG.txt"]

workbook = xlsxwriter.Workbook( destination + "Performance_Metrics_" + passed_variable + ".xlsx")
worksheet_1 = workbook.add_worksheet("Stage 1")
worksheet_2 = workbook.add_worksheet("Stage 2")
worksheet_3 = workbook.add_worksheet("Stage 3")

headers_1 = ['Artemis destroyed', 'Base destroyed', 'Start_to_Dock1', 'Dock1_to_End', 'Total time', 'Game over', 'Beams fired', 'Torpedos fired', 'Enemies destroyed', 'Shots hit by enemy', 'Mines detonation']
headers_2 = ['CLOSE', 'FAR', 'Energy reduced', 'Start_to_Intrepid', 'First escort', 'Second escort', 'Third escort', 'Total time', 'Game over', 'Beams fired', 'Torpedos fired', 'Enemies destroyed', 'Shots hit by enemy', 'Mines detonation']
headers_3 = ['Artemis destroyed', 'Base destroyed', 'Start_to_Dock1', 'Dock1_to_OutNeb', 'OutNeb_to_InNeb', 'InNeb_to_End', 'Total time', 'Game over', 'Beams fired', 'Torpedos fired', 'Enemies destroyed', 'Shots hit by enemy', 'Mines detonation']

headers = [headers_1, headers_2, headers_3]
worksheets = [worksheet_1, worksheet_2, worksheet_3]

for i, worksheet in enumerate(worksheets):
    for col, header in enumerate(headers[i]):
        worksheet.write(0, col, header)

        if header not in ['Beams fired', 'Torpedos fired', 'Enemies destroyed', 'Shots hit by enemy', 'Mines detonation']:
            worksheet.write(1, col, 0)


#---------------First sheet---------------#

sec = 0
dock_in = 0
player_dead = 0
station_destroyed = 0
game_time_over = 0

with open(destination + files_to_read[0]) as log:
    for line in log:
        if line.strip() == 'SEC':
            sec += 1
        elif line.strip() == 'Dock in':
            dock_in = sec
        elif line.strip() == 'Player Dead':
            player_dead += 1
        elif line.strip() == 'Station destroyed':
            station_destroyed += 1
        elif line.strip() == 'Game time over':
            game_time_over = 1

t1 = dock_in
t2 = sec - dock_in

worksheet_1.write(1, 0, player_dead)
worksheet_1.write(1, 1, station_destroyed)
worksheet_1.write(1, 2, t1)
worksheet_1.write(1, 3, t2)
worksheet_1.write(1, 4, sec)
worksheet_1.write(1, 5, game_time_over)


#---------------Second sheet---------------#

sec = 0
close_count = 0
far_count = 0
object_energy_trig = 0
energy_count = 0
second_move = 0
fourth_move = 0
fifth_move = 0
game_time_over = 0

with open(destination + files_to_read[1]) as log:
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
worksheet_2.write(1, 1, far_count * 5)
worksheet_2.write(1, 2, energy_count * 10)
worksheet_2.write(1, 3, t1)
worksheet_2.write(1, 4, t2)
worksheet_2.write(1, 5, t3)
worksheet_2.write(1, 6, t4)
worksheet_2.write(1, 7, sec)
worksheet_2.write(1, 8, game_time_over)


#---------------Third sheet---------------#

sec = 0
player_dead = 0
station_destroyed = 0
dock_in = 0
outer_neb = 0
inner_neb = 0
enemy_killed = 0
game_time_over = 0

with open(destination + files_to_read[2]) as log:
    for line in log:
        if line.strip() == "SEC":
            sec += 1
        elif line.strip() == "Player Dead":
            player_dead += 1
        elif line.strip() == "Station destroyed":
            station_destroyed += 1
        elif line.strip() == "Dock in":
            dock_in = sec
        elif line.strip() == "T1":
            outer_neb = sec
        elif line.strip() == "T2":
            inner_neb = sec
        elif line.strip() == "Game time over":
            game_time_over = 1

t1 = dock_in
t2 = outer_neb - dock_in
t3 = inner_neb - outer_neb
t4 = sec - inner_neb

worksheet_3.write(1, 0, player_dead)
worksheet_3.write(1, 1, station_destroyed)
worksheet_3.write(1, 2, t1)
worksheet_3.write(1, 3, t2)
worksheet_3.write(1, 4, t3)
worksheet_3.write(1, 5, t4)
worksheet_3.write(1, 6, sec)
worksheet_3.write(1, 7, game_time_over)


workbook.close()