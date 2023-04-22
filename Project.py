import urllib.request
import os
from tqdm import tqdm


print("Welcome To Download Manager! Please Choose Option From Menu.")
print("\n 1-Download A File\n 2-Delete A Downloaded File \n 3-Exit From Tool")


while True:
    try:
        Selection = float(input("\n Please Choose An Option: "))
    except ValueError:
        print("You selected invalid value(s), Exiting From Tool ")
        break


    if Selection == 1:
        try:
            ProgramType = int(input("1-Programs for Coding\n2-Office Programs\n3-Games\n4-Other Programs\nPlease Select Type Of Programs That You Want to Install:"))
        except ValueError:
            print("You Selected İnvalid Value, Exiting From Tool ")
            break
        
        
        if ProgramType == 1:
            try:
                CodingPrograms = int(input("1-Python\n2-VSC\n3-Java\n4-Xampp(PHP)\n5-Node JS\n6-Visual Studio (Community Edition)\nPlease Select an App: "))
            
            except ValueError:
                print("Your Selection is Invalid. Exiting From Tool...")
                break

            if CodingPrograms == 1:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe'
                file_name = 'PythonSetup.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break

            if CodingPrograms == 2:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user'
                file_name = 'VSCodeSetupx64.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                
            if CodingPrograms == 3:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://javadl.oracle.com/webapps/download/AutoDL?BundleId=247917_0ae14417abb444ebb02b9815e2103550'
                file_name = 'JavaSetup.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                                
                
            if CodingPrograms == 4:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://sourceforge.net/projects/xampp/files/latest/download'
                file_name = 'XamppSetup.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                               
                
            if CodingPrograms == 5:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://nodejs.org/dist/v18.15.0/node-v18.15.0-x64.msi'
                file_name = 'NodeJS_Setup.msi'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                
            if CodingPrograms == 6:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://c2rsetup.officeapps.live.com/c2r/downloadVS.aspx?sku=community&channel=Release&version=VS2022&source=VSLandingPage&includeRecommended=true&cid=2030'
                file_name = 'VisualStudio_Setup.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                                
                
            if CodingPrograms > 6:
                print("WOW! You Found a Easter Egg! But Nothing Changed :/")
                break


        if ProgramType == 2:
            try:
                Office = int(input("1-Microsoft Office\n2-Libre Office (Offline Setup)\n3-SoftMaker FreeOffice\n\nPlease Select an App: "))
            except ValueError:
                print("Your Selection is Invalid. Exiting From Tool...")
                break
        

        
            if Office == 1:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://download.microsoft.com/download/D/4/4/D4458125-9BDC-4147-BE90-5D86CEA8C323/officesp2010-kb2687455-fullfile-x64-tr-tr.exe'
                file_name = 'Office_Setup.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                                   
                
            if Office == 2:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://sourceforge.net/projects/libreoffice/files/latest/download'
                file_name = 'LibreOffice_Setup.msi'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                  

            if Office == 3: 
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://www.freeoffice.com/download.php?filename=https://www.softmaker.net/down/freeoffice2021.msi'
                file_name = 'FreeOffice_Setup.msi'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                

            if Office > 3:
                print("You Selected İnvalid Value, Exiting From Tool ")
                break

        if ProgramType == 3:
            try:
                Games = int(input("1-Steam\n2-League Of Legends\n3-ETS 1\n4-ETS 2\n5-Epic Games Launcher\n6-Minecraft(Titan Launcher)\n7-GTA 5 (NON-ONLINE)\n8-Rocket League\n9-Apex Legends\n10-RDR\n11-NFS Most Wanted\n12-FIFA 22(with Emulator)\nPlease Select an App: "))
            except ValueError:
                print("Your Selection is Invalid. Exiting From Tool...")
                break


            if Games == 1:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe'
                file_name = 'SteamSetup.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
            
            if Games == 2:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://lol.secure.dyn.riotcdn.net/channels/public/x/installer/current/live.na.zip'
                file_name = 'LoL_Setup.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                  
                
            if Games == 3:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://drive.google.com/u/0/uc?id=1tcGI6iNDj31ZAH0PajLr2KEdFrP0chCD&export=download&confirm=t&uuid=d106295c-a5d5-4062-8643-9f84ac9931a9&at=ALgDtswS5HINQ-FWE0WHKd8Q0X1b:1679525253428'
                file_name = 'EuroTrucks_1_Setup.rar'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                
            if Games == 4:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://www.mediafire.com/file/8fe6exi8afttbd9/Euro.Truck.Simulator.2.Re.rar/file#'
                file_name = 'Ets2_FullDLC_Setup.rar'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                
            if Games == 5:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi?trackingId=27906a865a3a4050922257eaa60e0f8d'
                file_name = 'EpicGames_Setup.msi'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                
            if Games == 6:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://titan.mythicmc.org/Minecraft%20Launcher.exe'
                file_name = 'TitanLauncher.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                
            if Games == 7:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://www.bedavaoyunindir.com/indir/grand-theft-auto-v-gta-5/'
                file_name = 'Gta5_Setup.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                
            if Games == 8:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://downloader.disk.yandex.ru/disk/f17fb62d7642091c77ad6ac56afc9adff50011dda6466377f9bd46d2439c0d36/641bc61e/dkhvIAG1gA0s30MKr7syMFJLnWboJT5QlLO0xs8VXW3ffjqqDglaQHApdIhjE9YMiiM8Bt-R_IewxWUE0EsxgA%3D%3D?uid=0&filename=Rocket%20League-fp.rar&disposition=attachment&hash=07Sp1UQ3Q1K1kAyOSAe7O7gQsjPVCL18AR7KcDQreIvjOU4iC9UBySmk%2BPhifpvqq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=application%2Fx-rar&owner_uid=1586640062&fsize=5859896987&hid=a58d5dd1b6c1db356df68d7232c16d87&media_type=compressed&tknv=v2'
                file_name = 'RocketLeagueSetup.rar'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again. (I tested file on Wm)")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                
            if Games == 9:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://www.gezginler.net/indir/i/35625/'
                file_name = 'ApexLegendsSetup.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                
            if Games == 10:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://download2393.mediafire.com/tx6dw8c2ihrg1ZRyrAcyUv4eQ4OBQf2fk3RMvpGp6FHjrmJUgEPt-dhJUh46e5WKyjN4SbzDKMQBTPY0_uz1S5azQXBE/6pf4xfwtwazzhmb/Red+Dead+Redemption+T%C3%BCrk%C3%A7e.rar'
                file_name = 'RDR.rar'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                
            if Games == 11:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://download2354.mediafire.com/5r88mv0xs3igWvH9Xr0mY_bO7beDQgVWsboMVPStwcMMUbgsgXVa4rLzGcVCKi48yOhXWa076JjU3ebN6a24KzvdEj8K/sagkp2z686aitry/%5BFP%5D+Need+for+Speed+-+Most+Wanted.rar'
                file_name = 'NFS_MOST_WANTED.rar'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                
            if Games == 12:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://turbobit.net/download/started/ku6wbmejq9od'
                file_name = 'Fifa22.rar'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                
        if ProgramType == 4:
            try:
                Other = int(input("1-Spotify\n2-Discord\n3-Whatsapp (PC)\n4-Brave\n5-Quick CPU\n6-TeamSpeak3\n7-Adobe Photoshop\n8-Adobe After Effects\n9-WinRaR\n10-AVAST (Free)\n11-CClenaer\n12-Advanced SystemCare\n13-7 Zip\n14-EaseUS Partition Manager (Free)\n15-Rufus\n16-Google\n17-Opera GX\n18-VLC Media Player\n19-PhotoScape\n\nPlease Select an App: "))
            except ValueError:
                print("Your Selection is Invalid. Exiting From Tool...")
                break
            
            if Other < 1:
                print("Your Selection is Invalid. Exiting From Tool...")
                break                
            
            
            if Other == 1:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://download.scdn.co/SpotifySetup.exe'
                file_name = 'SpotifySetup.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                                

            if Other == 2:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86'
                file_name = 'DiscordSetup.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                                

            if Other == 3: #GEZGİNLER
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://www.gezginler.net/indir/i/34799/x64/'
                file_name = 'WhatsappSetup.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                                

            if Other == 4:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://laptop-updates.brave.com/latest/winx64'
                file_name = 'BraveSetup.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                                

            if Other == 5:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://coderbag.com/assets/downloads/cpm/currentversion/QuickCpuSetup64.zip'
                file_name = 'QuickCPU.zip'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                                
            
            if Other == 6:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://www.teamspeak.com/en/downloads/#'
                file_name = 'TeamSpeakSetup.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                

            if Other == 7:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://creativecloud.adobe.com/apps/download/photoshop?locale=tr#'
                file_name = 'Photoshop-Set-UP.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                                

            if Other == 8:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://pixeldrain.com/api/file/D3LDxowN?download'
                file_name = 'AfterEffects_Setup.rar'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                                

            if Other == 9:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://www.win-rar.com/postdownload.html?&L=5'
                file_name = 'WinRARSetup.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                               

            if Other == 10:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://www.avast.com/tr-tr/download-thank-you.php?product=FAV-ONLINE-FAD&locale=tr-tr&direct=1'
                file_name = 'AvastSetup.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                                

            if Other == 11:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://bits.avcdn.net/productfamily_CCLEANER/insttype_FREE/platform_WIN_PIR/installertype_ONLINE/build_RELEASE/cookie_mmm_ccl_003_999_a7c_dk'
                file_name = 'CCleanerSetup.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                                

            if Other == 12:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://www.iobit.com/en/advancedsystemcarefree.php#'
                file_name = 'AdvancedSystemCare_Setup.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                                

            if Other == 13:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://7-zip.org/a/7z2201-x64.exe'
                file_name = '7-Zip_Setup.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                                

            if Other == 14:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://www.gezginler.net/indir/i/19070/'
                file_name = 'EaseUsPartManager_Setup.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                                

            if Other == 15:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://github.com/pbatard/rufus/releases/download/v3.21/rufus-3.21.exe'
                file_name = 'Rufus-3.21.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                                

            if Other == 16:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://www.google.com/intl/tr_tr/chrome/thank-you.html?statcb=1&installdataindex=empty&defaultbrowser=0#'
                file_name = 'Chrome_Setup.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                                

            if Other == 17:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://www.opera.com/tr/computer/thanks?ni=eapgx&os=windows'
                file_name = 'OperaGX_Setup.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                                
            if Other == 18:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://get.videolan.org/vlc/3.0.18/win64/vlc-3.0.18-win64.exe'
                file_name = 'Vlc_Setup.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                                

            if Other == 19:
                folder_path = r'C:\Downloaded Files'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                url = 'https://www.gezginler.net/indir/i/4565/'
                file_name = 'Photoscape-Setup.exe'
                file_path = os.path.join(folder_path, file_name)

                if os.path.exists(file_path):
                    print(f"{file_name} Already Installed.\nIf You Want To Reinstall It, Delete The File With Tool And Try Again.")
                    break
                else:
                    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as progress_bar:
                        urllib.request.urlretrieve(url, file_path, reporthook=lambda b, bsize, tsize: progress_bar.update(bsize))
                    print(f"File is Successfully Installed\nYou Can Find {file_name} in C:/Downloaded Files.")
                    break                
                                

            if Other > 19:
                print("Your Selection is Invalid. Exiting From Tool...")
                break

        if ProgramType > 4:
            print("Your Selection is Invalid. Exiting From Tool...")
            break

        if ProgramType < 1:
            print("Your Selection is Invalid. Exiting From Tool...")
            break


    if Selection == 2:


        # Klasör yolu
        klasor_yolu = "C:/Downloaded Files"

        # Klasördeki dosyaları al
        dosyalar = os.listdir(klasor_yolu)

        # Dosyalara sayı atayarak yazdır
        for i, dosya in enumerate(dosyalar, 1):
            dosya_yolu = os.path.join(klasor_yolu, dosya)
            print(f"{i}){dosya_yolu}")
        try:
            silinecek_dosya = int(input("\n\nPlease İnput File Number Which You Want To Delete: "))
        except ValueError:
            print("Your Selection İs İnvalid. Exiting From Tool...")
            break

        secilen_dosya = dosyalar[silinecek_dosya - 1]
        secilen_dosya_yolu = os.path.join(klasor_yolu, secilen_dosya)
        os.remove(secilen_dosya_yolu)

    print(f"{secilen_dosya} dosyası silindi.")
    break



    if Selection == 3:
        print("You selected")

    if Selection > 3:
        print("You Selected İnvalid Value, Exiting From Tool...")
        break

Github = "Github.com/Eymenemen"
Sites = "https://Gezginler.net , https://sourceforge.net/ and https://oyunindir.vip/"
print("\n\nThank For Using My Tool! Follow Me On Github:",Github ,"\n\n*** Special Thanks For:",Sites , "***")