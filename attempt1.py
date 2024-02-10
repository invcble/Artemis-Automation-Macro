import shutil
import os
import sys
import xlsxwriter
from datetime import datetime
import zipfile
import pyautogui as pag

def collect_logs_and_generate_report():
    # Importing log files from specific locations
    log_files = [
        'C:\\Program Files (x86)\\Artemis\\dat\\Missions\\MISS_Stage1\\MISS_Stage1_LOG.txt',
        'C:\\Program Files (x86)\\Artemis\\dat\\Missions\\MISS_Stage2\\MISS_Stage2_LOG.txt',
        'C:\\Program Files (x86)\\Artemis\\dat\\Missions\\MISS_Stage3\\MISS_Stage3_LOG.txt'
    ]
    
    # Determine application path for frozen and non-frozen application
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    
    # Copy log files to application path
    for log_file in log_files:
        shutil.copy(log_file, application_path)
    
    # Generating unique ID based on date and time for file naming
    now = datetime.now()
    date_id = now.strftime("%Y%m%d_%H%M%S")
    
    # Create a new Excel file and add worksheets
    workbook = xlsxwriter.Workbook(f'{application_path}/Performance_Metrics_{date_id}.xlsx')
    worksheet1 = workbook.add_worksheet('Stage 1')
    worksheet2 = workbook.add_worksheet('Stage 2')
    worksheet3 = workbook.add_worksheet('Stage 3')
    
    # Example of writing headers to the first worksheet
    headers = ['Time', 'Event', 'Description']
    for col, header in enumerate(headers):
        worksheet1.write(0, col, header)
    
    # Assuming further data processing and Excel file generation logic here
    
    workbook.close()
    
    # Zipping log files and Excel report
    with zipfile.ZipFile(f'{application_path}/Report_{date_id}.zip', 'w') as zipf:
        for file_to_zip in log_files + [f'{application_path}/Performance_Metrics_{date_id}.xlsx']:
            zipf.write(file_to_zip, os.path.basename(file_to_zip))
            os.remove(file_to_zip)  # Assuming you want to clean up after zipping

if __name__ == "__main__":
    # Confirm from the user to proceed
    response = pag.confirm(text='Press OK to collect LOG files', title='Confirmation', buttons=['OK', 'Cancel'])
    if response == 'OK':
        try:
            collect_logs_and_generate_report()
        except Exception as e:
            pag.alert(text=f'Error occurred: {str(e)}', title='Error', button='OK')
    else:
        sys.exit("User cancelled the operation.")
