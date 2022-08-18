import winreg
import win32api
from winreg import QueryValueEx
import winshell
from pathlib import Path
import time
import os
import win32gui
import win32con
import win32com.client
import py3nvml.nvidia_smi as smi
import psutil
from datetime import datetime
def current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S:%U")
    return current_time
log_name = fr"\rndr_watchdog_log.txt"
path_name = fr"\rndr_watchdog_log"
last_error = False
rndr_log_path = os.environ['USERPROFILE'] + fr"\AppData\Local\OtoyRndrNetwork\rndr_log.txt"
miner_program_name = "PhoenixMiner"
key_to_send = "c"


def getTasks(name):
    r = os.popen('tasklist /v').read().strip().split('\n')
    print('# of tasks is %s' % (len(r)))
    for i in range(len(r)):
        s = r[i]
        if name in r[i]:
            print('%s in r[i]' % (name))
            return r[i]
    return []


def isresponding(name):
    if __name__ == '__main__':
        '''
        This code checks tasklist, and will print the status of a code
        '''

        notResponding = 'Not Responding'

        r = getTasks(name)

        if not r:
            print('%s - No such process' % (name))
            return True
        elif 'Not Responding' in r:
            print('%s is Not responding' % (name))
            writing_log_file(f"{name} is Not responding", f"{desktop}", log_name, path_name)
            return False
        else:
            print('%s is Running or Unknown' % (name))
            writing_log_file(f"{name} is running or unknown", f"{desktop}", log_name, path_name)
            return True

def send_keystroke(process, key):
    try:
        win32api.PostMessage(process, win32con.WM_CHAR, ord(f'{key}'), 0)
    except ValueError:
        writing_log_file(f"no {miner_program_name} window found", f"{desktop}", log_name, path_name)


def search_for_errors_in_rndr_logs(rndr_log_path):
    writing_log_file(f"search_for_errors_in_rndr_logs", f"{desktop}", log_name, path_name)
    with open(f"{rndr_log_path}", 'r') as f:
        last_line = f.readlines()[-1]
        f.close()
        if "ERROR" in last_line:
            return True
        else:
            return False



def change_config_file(is_started):
    try:
        config_file = open(fr"{desktop}\{miner_program_name}_4.0b_Windows\config.txt", 'w')
        config_exit = open(fr"{desktop}\{miner_program_name}_4.0b_Windows\config_exit.txt", 'r')
        config_start = open(fr"{desktop}\{miner_program_name}_4.0b_Windows\config_start.txt", 'r')
    except ValueError:
        writing_log_file("config file/s is missing", f"{desktop}", log_name, path_name)
        return

    if is_started:
        with config_exit as f:
            lines = f.readlines()
            lines_string = ''.join(lines)
            config_file.write(lines_string)
    else:
        with config_start as f:
            lines = f.readlines()
            lines_string = ''.join(lines)
            config_file.write(lines_string)

    config_file.close()
    config_exit.close()
    config_start.close()
    return


def writing_log_file(text, desktop_path, log_name, path_name):
    desktop_contents = os.listdir(f"{desktop_path}")
    if path_name.replace("\\", '') in desktop_contents:
        print(f"{current_time()}: Path already exist")
        pass
    else:
        try:
            os.makedirs(desktop_path + path_name)
            print(f"{current_time()}: Folder created")
        except OSError:
            print(f"{current_time()}: Creation of the directory has failed")
            return
    file = open(f"{desktop_path + path_name + log_name}", "a+")
    file.write(f"{current_time()}: {text}\n")
    file.close()
    return


def search_pid_in_unused_rndr_process():
    writing_log_file(f"search_pid_in_unused_rndr_process", f"{desktop}", log_name, path_name)
    smi_info = smi.XmlDeviceQuery().split("\n")
    for i, data in enumerate(smi_info):
        if "TCPSVCS.EXE" in data:
            process_id_for_kill = smi_info[i-1].strip().\
                replace("<pid>", "").\
                replace("</pid>", "")
            print(process_id_for_kill)
            return process_id_for_kill
    return "no process found"

def terminate_pid_1(pid):
    p = psutil.Process(int(pid))
    p.terminate()
    writing_log_file("TCP Process Terminated", f"{desktop}", log_name, path_name)

def check_pid_by_process_name(name):
    process_name = name
    pid = None
    for proc in psutil.process_iter():
        if process_name in proc.name():
            pid = proc.pid
            terminate_pid_1(pid)

def terminate_pid():
    writing_log_file(f"terminate_pid", f"{desktop}", log_name, path_name)
    if search_pid_in_unused_rndr_process() == "no process found":
        writing_log_file("No process for termination", f"{desktop}", log_name, path_name)
        pass
    else:
        p = psutil.Process(int(search_pid_in_unused_rndr_process()))
        p.terminate()
        writing_log_file("TCP Process Terminated", f"{desktop}", log_name, path_name)
    return
os.system("mode con cols=50")


def terminate_app_by_name(name):
    os.system(f"taskkill /im {name}.exe")
    writing_log_file(f"Function terminate_app_by_name was executed for: {name}", f"{desktop}", log_name, path_name)


def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
def state(num):
    if num == "1":
        return f"Not Rendering"
    else:
        return f"Rendering"

def check_for_memory_error_window():
    writing_log_file("check_for_memory_error_window", f"{desktop}", log_name, path_name)
    if __name__ == "__main__":
        results = []
        top_windows = []
    try:
        win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    except Exception as e:
        print("type error: " + str(e))
    for i in top_windows:
        if "error" in i[1].lower():
            writing_log_file("Memory fail RNDR", f"{desktop}", log_name, path_name)
            win32gui.ShowWindow(i[0], 5)
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('enter')
            win32gui.SetForegroundWindow(i[0])

            win32gui.PostMessage(i[0], win32con.WM_CLOSE, 0, 0)
            time.sleep(0.5)
            break

    return


desktop = Path(winshell.desktop())
flag_started = False
flag_stopped = False
count = 0
os.startfile(fr"C:\rndr-master\start.bat")
print("RNDR Started")
time.sleep(1)


while True:

    check_for_memory_error_window()

    root = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    policy_key = winreg.OpenKeyEx(root, r"SOFTWARE\OTOY")
    print(policy_key)
    value_key = QueryValueEx(policy_key, "RNDR_IDLE")
    if value_key[0] == "1":
        if not flag_started:
            if count != 0:
                time.sleep(2)
                if value_key[0] == "1":
                    try:
                        os.startfile(fr"{desktop}\{miner_program_name}_4.0b_Windows\{miner_program_name}.exe")
                    except Exception as e:
                        print("type error: " + str(e))
            # subprocess.call([fr"{desktop}\{miner_program_name}_4.0b_Windows\PM.bat"])
                else:
                    """TEST PART_temp"""
                    winreg.CloseKey(policy_key)
                    print(f"State of Render Node: {state(value_key[0])}")
                    # print(f"Current run in secs: {floor(time.perf_counter())}")
                    print(f"Current time: {current_time()}")
                    if search_for_errors_in_rndr_logs(f"{rndr_log_path}"):
                        if not last_error:
                            text = smi_info = smi.XmlDeviceQuery()
                            writing_log_file(text, f"{desktop}", log_name, path_name)
                            print(f"{current_time()}: writing error log")
                            last_error = True
                    else:
                        last_error = False
                    """END OF TEST PART_temp"""
                    continue
            else:
                try:
                    terminate_app_by_name(miner_program_name)
                    os.startfile(fr"{desktop}\{miner_program_name}_4.0b_Windows\{miner_program_name}.exe")
                except Exception as e:
                    print("type error: " + str(e))
            flag_started = True
            flag_stopped = False
    elif value_key[0] == "0":
        if not flag_stopped:
            if __name__ == "__main__":
                results = []
                top_windows = []
            win32gui.EnumWindows(windowEnumerationHandler, top_windows)
            for i in top_windows:
                if miner_program_name.lower() in i[1].lower():
                    process_windows_number = i[0]
                    win32gui.ShowWindow(process_windows_number, 5)
                    shell = win32com.client.Dispatch("WScript.Shell")
                    shell.SendKeys('%')
                    win32gui.SetForegroundWindow(process_windows_number)
                    change_config_file(True)
                    writing_log_file("config file changed to exit version", f"{desktop}", log_name, path_name  )
                    send_keystroke(process_windows_number, key_to_send)
                    time.sleep(5)
                    win32gui.PostMessage(process_windows_number, win32con.WM_CLOSE, 0, 0)
                    writing_log_file("trying to close miner program", f"{desktop}", log_name, path_name)
                    change_config_file(False)
                    writing_log_file("config file changed to start version", f"{desktop}", log_name, path_name)
                    time.sleep(0.5)
                    if __name__ == "__main__":
                        results = []
                        top_windows = []
                    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
                    for windows in top_windows:
                        if miner_program_name.lower() in windows[1].lower():
                            os.system(f"taskkill /im {miner_program_name}.exe")
                            writing_log_file("Miner program was killed", f"{desktop}", log_name, path_name)

                    writing_log_file("Miner program successfully closed", f"{desktop}", log_name, path_name)
                    break

            flag_stopped = True
            flag_started = False
    winreg.CloseKey(policy_key)
    print(f"State of Render Node: {state(value_key[0])}")
    #print(f"Current run in secs: {floor(time.perf_counter())}")
    print(f"Current time: {current_time()}")
    if search_for_errors_in_rndr_logs(f"{rndr_log_path}"):
        if not last_error:
            text = smi_info = smi.XmlDeviceQuery()
            writing_log_file(text, f"{desktop}", log_name, path_name)
            print(f"{current_time()}: writing error log")
            last_error = True
    else:
        last_error = False

    time.sleep(0.5)

    count += 1
