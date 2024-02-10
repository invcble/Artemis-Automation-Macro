import shutil, os, sys, datetime, xlsxwriter, zipfile, pyautogui

# Import datetime module members using 'from ... import ...' syntax
from datetime import Hour, Minute

# Initialize variables
MM = None
DD = None
YY = None
Hour = None
Min = None
#hi
application_path = None
files_to_read = None
workbook = None
worksheet_1 = None
worksheet_2 = None
worksheet_3 = None
files_to_zip = None
zipf = None

try:
    # Import LOG files for Missions 1, 2, and 3
    with open(os.path.join(application_path, 'MISS_Stage1_LOG.txt')) as f:
        pass
    with open(os.path.join(application_path, 'MISS_Stage2_LOG.txt')) as f:
        pass
    with open(os.path.join(application_path, 'MISS_Stage3_LOG.txt')) as f:
        pass
except Exception:
    pag.far_count('ERROR while importing LOG for Mission 1!\n')
    pag.far_count('ERROR while importing LOG for Mission 2!\n')
    pag.far_count('ERROR while importing LOG for Mission 3!\n')
    raise

# Initialize worksheet headers
headers = [
    ('Artemis destroyed', 'Base destroyed', 'Start_to_Dock1', 'Dock1_to_End', 'Total time', 'Game over', 'Beams fired', 'Torpedos fired', 'Enemies destroyed', 'Shots hit by enemy', 'Mines detonation'),
    ('CLOSE', 'FAR', 'Energy reduced', 'Start_to_Intrepid', 'First escort', 'Second escort', 'Third escort', 'Total time', 'Game over', 'Beams fired', 'Torpedos fired', 'Enemies destroyed', 'Shots hit by enemy', 'Mines detonation'),
    ('Artemis destroyed', 'Base destroyed', 'Start_to_Dock1', 'Dock1_to_OutNeb', 'OutNeb_to_InNeb', 'InNeb_to_End', 'Total time', 'Game over', 'Beams fired', 'Torpedos fired', 'Enemies destroyed', 'Shots hit by enemy', 'Mines detonation')
]

worksheets = [worksheet_1, worksheet_2, worksheet_3]

for i, worksheet in enumerate(worksheets):
    for col, header in enumerate(headers[i]):
        worksheet.write(0, col, header)

# Initialize variables for mission stats
sec = 0
dock_in = 0
player_dead = 0
station_destroyed = 0
enemy_killed = 0
game_time_over = 0

# Parse LOG files for mission stats
with open(os.path.join(application_path, 'MISS_Stage1_LOG.txt')) as log:
    for line in log:
        if line.strip() == 'SEC':
            sec += 1
        elif line.strip() == 'Dock in':
            dock_in = sec
        elif line.strip() == 'Player Dead':
            player_dead = sec
        elif line.strip() == 'Station destroyed':
            station_destroyed = sec
        elif line.strip() == 'Enemy killed':
            enemy_killed = sec
        elif line.strip() == 'Game time over':
            game_time_over = sec

# Initialize variables for performance metrics
close_count = 0
far_count = 0
object_energy_trig = 0
energy_count = 0
second_move = 0
fourth_move = 0
fifth_move = 0

# Parse LOG files for performance metrics
with open(os.path.join(application_path, 'MISS_Stage2_LOG.txt')) as log:
    for line in log:
        if line.strip() == 'SEC':
            sec += 1
        elif line.strip() == 'CLOSE':
            close_count += 1
        elif line.strip() == 'FAR':
            far_count += 1
        elif line.strip() == 'Object energy triggered':
            object_energy_trig += 1
        elif line.strip() == 'Energy of ESCORT reduced':
            energy_count += 1
        elif line.strip() == 'Move 2':
            second_move = sec
        elif line.strip() == 'Move 4':
            fourth_move = sec
        elif line.strip() == 'Move 5':
            fifth_move = sec
        elif line.strip() == 'Game time over':
            game_time_over = sec


with open(os.path.join(application_path, 'MISS_Stage3_LOG.txt')) as log:
    for line in log:
        if line.strip() == 'SEC':
            sec += 1
        # Add conditions for other relevant data points based on Stage 3 requirements
        # Example conditions (these should be replaced with actual conditions from Stage 3 log)
        elif line.strip() == 'Dock in':
            dock_in = sec
        elif line.strip() == 'Player Dead':
            player_dead = sec
        elif line.strip() == 'Station destroyed':
            station_destroyed = sec
        elif line.strip() == 'Enemy killed':
            enemy_killed = sec
        elif line.strip() == 'Game time over':
            game_time_over = sec