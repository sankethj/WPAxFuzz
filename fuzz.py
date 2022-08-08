import subprocess
from Frame_types.Beacon import Beacon
from Frame_types.AssoReq import AssoReq
from Frame_types.AssoResp import AssoResp
from Frame_types.Authentication import Authentication
from Frame_types.Probe_request import ProbeReq
from Frame_types.Probe_response import Proberesp
from Frame_types.ReassoReq import ReassoReq
from Frame_types.ReassoResp import ReassoResp
from Connection_monitors.DeauthMonitor import DeauthMon
from Connection_monitors.AlivenessCheck import AllvCheck
from Frame_types.Construct_frame_fields import bcolors
from ControlFrames import ControlFrames
from fuzzer_init import *
from time import sleep
import threading
import settings
import sys
import os
import ascii_art


print(ascii_art.logo)
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n\n')
print('\t\tThis tool is capable of fuzzing either any management frame of the 802.11 protocol\n\t\tor the SAE exchange. For the management frames, you can choose either the "standard"\n\t\tmode where all of the frames transmitted have valid size values or the "random" mode\n\t\twhere the size value is random. The SAE fuzzing operation requires an AP that supports\n\t\tWPA3. Management frame fuzzing can be executed against any AP (WPA2 or WPA3).\n\t\tFinally, a DoS attack vector is implemented, which exploits the findings of the\n\t\tmanagement frames fuzzing.\n')
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n\n')
                            
print('1) Fuzz Management Frames')
print('2) Fuzz SAE exchange')
print('3) Fuzz Control Frames')
print('4) DoS attack module\n\n')
try:
    choice = int(input('Enter a choice: '))
except:
    print('\n' + bcolors.FAIL + 'Only integer inputs accepted' + bcolors.ENDC)
    os._exit(0)
if choice == 1:
    subprocess.call(['clear'], shell=True)
    print(ascii_art.mngmt_frames) 
    print('Type "standard" for the standard mode')
    print('Type "random" for the random mode\n\n')
    mode = input('Enter a choice: ').lower()
    if mode == 'standard' or mode == 'random':
        Aliveness = AllvCheck(targeted_STA, 'fuzzing')
        Aliveness.start()
        while not settings.retrieving_IP:
            if settings.IP_not_alive:
                os._exit(0)
        sleep(10)
        subprocess.call(['clear'], shell=True)
    else:
        print(bcolors.FAIL + '\nNo such mode :(' + bcolors.ENDC)
        os._exit(0)
    subprocess.call(['clear'], shell=True)
    print(ascii_art.mngmt_frames)
    print('Which frames would you like to fuzz?')
    print('1) Beacon frames')
    print('2) Probe request frames')
    print('3) Probe response frames')
    print('4) Association request frames')
    print('5) Association response frames')
    print('6) Reassociation request frames')
    print('7) Reassociation response frames')
    print('8) Authentication frames\n\n')
    try:
        choice2 = int(input('Select a frame to fuzz: '))
    except:
        print('\n' + bcolors.FAIL + 'Only integer inputs accepted' + bcolors.ENDC)
        os._exit(0)
    Deauth_monitor = DeauthMon(targeted_AP, targeted_STA, att_interface)
    Deauth_monitor.start()
    if choice2 == 1:
        if mode == 'random':
            subprocess.call(['clear'], shell=True)
            print(ascii_art.beacon)        
            print(ascii_art.wifi)
            print("1) Target the STA and impersonate the AP")
            print("2) Target the AP and impersonate the STA\n\n")
            try:
                direction = int(input('Select a frame to fuzz: '))
            except:
                print('\n' + bcolors.FAIL + 'Only integer inputs accepted' + bcolors.ENDC)
                os._exit(0)
            if direction in {1, 2}:
                pass
            else:
                print(bcolors.FAIL + '\nNo such mode :(' + bcolors.ENDC)
                os._exit(0)
        else:
            direction = 1
        fuzz_beacons = Beacon(mode, "beacon", targeted_STA, targeted_AP, att_interface, real_ap_ssid, direction)
        subprocess.call(['clear'], shell=True)
        print(ascii_art.beacon)        
        print(ascii_art.wifi)
        print("Fasten your seatbelts and grab a coffee. Fuzzing is about to begin!")
        sleep(5)
        fuzz_beacons.fuzz_beacon()  
    elif choice2 == 2:
        fuzz_probe_reqs = ProbeReq(mode, "probe request", targeted_AP, targeted_STA, att_interface, real_ap_ssid)
        subprocess.call(['clear'], shell=True)
        print(ascii_art.probe_req)      
        print(ascii_art.wifi)
        print("Fasten your seatbelts and grab a coffee. Fuzzing is about to begin!")
        sleep(5)
        fuzz_probe_reqs.fuzz_probe_req()
    elif choice2 == 3:
        if mode == 'random':
            subprocess.call(['clear'], shell=True)
            print(ascii_art.probe_resp)        
            print(ascii_art.wifi)
            print("1) Target the STA and impersonate the AP")
            print("2) Target the AP and impersonate the STA\n\n")
            try:
                direction = int(input('Select a frame to fuzz: '))
            except:
                print('\n' + bcolors.FAIL + 'Only integer inputs accepted' + bcolors.ENDC)
                os._exit(0)
            if direction in {1, 2}:
                pass
            else:
                print(bcolors.FAIL + '\nNo such mode :(' + bcolors.ENDC)
                os._exit(0)
        else:
            direction = 1
        fuzz_probe_resp = Proberesp(mode, "probe response", targeted_STA, targeted_AP, att_interface, real_ap_ssid, direction)
        subprocess.call(['clear'], shell=True)
        print(ascii_art.probe_resp)    
        print(ascii_art.wifi)
        print("Fasten your seatbelts and grab a coffee. Fuzzing is about to begin!")
        sleep(5)
        fuzz_probe_resp.fuzz_probe_resp()
    elif choice2 == 4:
        fuzz_asso_reqs = AssoReq(mode, "association request", targeted_AP, targeted_STA, att_interface, real_ap_ssid)
        subprocess.call(['clear'], shell=True)
        print(ascii_art.asso_req)
        print(ascii_art.wifi)
        print("Fasten your seatbelts and grab a coffee. Fuzzing is about to begin!")
        sleep(5)
        fuzz_asso_reqs.fuzz_asso_req()
    elif choice2 == 5:
        if mode == 'random':
            subprocess.call(['clear'], shell=True)
            print(ascii_art.asso_resp)        
            print(ascii_art.wifi)
            print("1) Target the STA and impersonate the AP")
            print("2) Target the AP and impersonate the STA\n\n")
            try:
                direction = int(input('Select a frame to fuzz: '))
            except:
                print('\n' + bcolors.FAIL + 'Only integer inputs accepted' + bcolors.ENDC)
                os._exit(0)
            if direction in {1, 2}:
                pass
            else:
                print(bcolors.FAIL + '\nNo such mode :(' + bcolors.ENDC)
                os._exit(0)
        else:
            direction = 1
        fuzz_asso_resp = AssoResp(mode, "association response", targeted_STA, targeted_AP, att_interface, direction)
        subprocess.call(['clear'], shell=True)
        print(ascii_art.asso_resp)     
        print(ascii_art.wifi)
        print("Fasten your seatbelts and grab a coffee. Fuzzing is about to begin!")
        sleep(5)
        fuzz_asso_resp.fuzz_asso_resp()
    elif choice2 == 6:
        fuzz_reasso_reqs = ReassoReq(mode, "reassociation request", targeted_AP, targeted_STA, att_interface, real_ap_ssid)
        subprocess.call(['clear'], shell=True)
        print(ascii_art.reasso_req) 
        print(ascii_art.wifi)
        print("Fasten your seatbelts and grab a coffee. Fuzzing is about to begin!")
        sleep(5)
        fuzz_reasso_reqs.fuzz_reasso_req()
    elif choice2 == 7:
        if mode == 'random':
            subprocess.call(['clear'], shell=True)
            print(ascii_art.reasso_resp)        
            print(ascii_art.wifi)
            print("1) Target the STA and impersonate the AP")
            print("2) Target the AP and impersonate the STA\n\n")
            try:
                direction = int(input('Select a frame to fuzz: '))
            except:
                print('\n' + bcolors.FAIL + 'Only integer inputs accepted' + bcolors.ENDC)
                os._exit(0)
            if direction in {1, 2}:
                pass
            else:
                print(bcolors.FAIL + '\nNo such mode :(' + bcolors.ENDC)
                os._exit(0)
        else:
            direction = 1
        fuzz_asso_resp = ReassoResp(mode, "reassociation response", targeted_STA, targeted_AP, att_interface, direction)
        subprocess.call(['clear'], shell=True)
        print(ascii_art.reasso_resp)  
        print(ascii_art.wifi)
        print("Fasten your seatbelts and grab a coffee. Fuzzing is about to begin!")
        sleep(5)
        fuzz_asso_resp.fuzz_reasso_resp()
    elif choice2 == 8:
        fuzz_auth = Authentication(mode, "authentication", targeted_AP, targeted_STA, att_interface)
        subprocess.call(['clear'], shell=True)
        print(ascii_art.auth)  
        print(ascii_art.wifi)
        print("Fasten your seatbelts and grab a coffee. Fuzzing is about to begin!")
        sleep(5)
        fuzz_auth.fuzz_auth()
elif choice == 2:
    subprocess.call(['clear'], shell=True)
    subprocess.call(['sudo python3 dos-sae.py'], shell=True)
elif choice == 3:
    subprocess.call(['clear'], shell=True)
    print(ascii_art.control_frames)
    Aliveness = AllvCheck(targeted_STA, 'fuzzing')
    Aliveness.start()
    while not settings.retrieving_IP:
        if settings.IP_not_alive:
            os._exit(0)
    sleep(10)
    Deauth_monitor = DeauthMon(targeted_AP, targeted_STA, att_interface)
    Deauth_monitor.start()
    fuzz_ctrl = ControlFrames(targeted_AP, targeted_STA, att_interface)
    subprocess.call(['clear'], shell=True)
    print(ascii_art.control_frames)
    print(ascii_art.wifi)
    print("Fasten your seatbelts and grab a coffee. Fuzzing is about to begin!")
    sleep(5)
    fuzz_ctrl.fuzz_ctrl_frames()
elif choice == 4:
    subprocess.call(['clear'], shell=True)
    subprocess.call(['sudo python3 mage.py'], shell=True)
else:
    print(bcolors.FAIL + '\nNo such choice :(' + bcolors.ENDC)
