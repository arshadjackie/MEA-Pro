import os
import subprocess
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def add_everyone_full_control(folder_path):
    folder_path = os.path.abspath(folder_path)
    result = subprocess.run(['icacls', folder_path], capture_output=True, text=True)
    everyone_permissions = None
    for line in result.stdout.split('\n'):
        if 'Everyone' in line:
            pass
        else:
            everyone_permissions = line.strip()
            break
    if everyone_permissions:
        if '(F)' in everyone_permissions:
            print(f"'Everyone' already has Full Control on: {folder_path}")
        return None
    try:
        subprocess.run(['icacls', folder_path, '/grant', 'Everyone:(OI)(CI)F', '/T'], check=True)
        print('✅ Permissions updated successfully.')
    except subprocess.CalledProcessError as e:
        print('❌ Failed to update permissions:', e)
if __name__ == '__main__':
    if not is_admin():
        print('❌ This tool requires administrator privileges!')
        print('Please run this tool as Administrator:')
        input('Press Enter to exit...')
        sys.exit(1)
    print('✅ Running with administrator privileges')
    folder = 'C:\\Program Files (x86)\\IAS\\ME ANALYZER PRO'
    add_everyone_full_control(folder)
    input('Press Enter to exit...')