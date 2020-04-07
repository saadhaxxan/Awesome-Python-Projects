import os
import shutil
import sqlite3
import ssl
import time
import platform
from urllib.request import urlopen

try:
    import httplib
except:
    import http.client as httplib


# check whether the internet is working or not
def have_internet():
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False


# --------------------------------------------------------------------

def exit_gracefully():
    f.close()
    conn.commit()
    print("Exiting....")

    exit()


# --------------------------------------------------------------------


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

if __name__ == '__main__':

    target = 1000000

    if platform.system()=="Linux":
        download_dir = os.getcwd() + "/tmp/"
    else:
        download_dir = os.getcwd() + "\\tmp\\"

    database = "g_x_apps.sqlite"

    conn = sqlite3.connect(database)
    cur = conn.cursor()

    base_site = "http://app.mi.com/download/"

    # load the last id number from which to continue downloading
    f = open("ids_done.txt", "r")
    numbers = f.readlines()
    numbers = [a.rstrip() for a in numbers]
    curr_num = int(numbers[-1])
    f.close()

    f = open("ids_done.txt", "a")
    c = 1

    while curr_num != target:
        try:
            curr_num += 1

            c += 1
            # commit after every 500 iterations
            if c == 500:
                conn.commit()
                c = 0

            # check net connectivity
            if not have_internet():

                # save progress
                conn.commit()
                f.close()

                print("Internet disconnected.. waiting")
                while not have_internet():
                    time.sleep(5)

                f = open("ids_done.txt", "a")
                print("Connected!")

            print("------------------------------------------")
            print("Processing:", curr_num)

            # empty left over downloads
            if platform.system() == 'Linux':
                os.system("rm -f '" + download_dir + "{*,.*}'")
            else:
                os.system('del "' + download_dir + '*" /Q')

            # ------------------------------------------------------------------
            # check whether app on xiomi exists or not
            try:
                url = base_site + str(curr_num)
                html = urlopen(url, context=ctx)

                # check apk exists or not
                if html.url[-4:] != ".apk":
                    f.write(str(curr_num) + "\n")
                    print("No app against this ID on Xiaomi Store")
                    continue

                # if it exists
                package = html.url.split('/')[-1]
                package = package.split(".apk")[0]

                print("Found on Xiaomi:", package)
            except:
                f.write(str(curr_num) + "\n")
                print("No app against this ID on Xiaomi Store")
                continue
            # ------------------------------------------------------------------

            # ------------------------------------------------------------------
            # check if the same app exists on google
            try:
                url = "https://play.google.com/store/apps/details?id=" + package
                html = urlopen(url, context=ctx)

                if str(html.getcode()) != '200':
                    f.write(str(curr_num) + "\n")
                    print(package, " doesn't exist on Play Store")
                    continue

                # if it exists
                print("Found on PlayStore:", package)
            except:
                f.write(str(curr_num) + "\n")
                print(package, " doesn't exist on Play Store")
                continue
            # ------------------------------------------------------------------

            # ------------------------------------------------------------------
            # download google
            print("Downloading from Playstore")
            os.system('gplaycli -d ' + package + ' -f "' + 'google_apps"' + ' -p')

            # check if a file of that apk is created
            if platform.system() == "Linux":
                dir = os.getcwd() + "/google_apps/" + package + ".apk"
            else:
                dir = os.getcwd() + "\\google_apps\\" + package + ".apk"

            time.sleep(1)
            save = False

            # check if that directory exists
            if os.path.exists(dir):
                save = True

            if not save:
                f.write(str(curr_num) + "\n")
                print("App from playstore not downloaded (might be paid app or not available in your country).")
                continue

            print(package, ": Google Download Successful")
            # ------------------------------------------------------------------

            # ------------------------------------------------------------------
            # download xiomi
            print("Downloading from Xiaomi")
            os.system("wget -P tmp/ --content-disposition -q " + base_site + str(curr_num))

            # rename the file and move it to its folder
            for file in os.listdir(download_dir):
                if file.endswith(".apk"):
                    print('Moving Xiomi File...')
                    shutil.move(download_dir + file, "xiomi_apps/" + package + ".apk")

                    cur.execute("INSERT OR IGNORE INTO APPS VALUES (?,1,1,0)",
                                (package,))

                    print(package, ": Xiomi Download Successful")

                else:
                    error = 'Error in downloading'
                    print(error, package)
            # ------------------------------------------------------------------

            f.write(str(curr_num) + "\n")

        except KeyboardInterrupt:
            exit_gracefully()

        except:
            pass

    print("-----------------------------")
    print("Downloads Complete!!!")
    print("-----------------------------")

    print('\n\nProcess Successfully finished!!!!!\n\n')

    f.close()
    conn.commit()
