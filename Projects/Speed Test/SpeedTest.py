'''
This script is used to measure the internet connection speed. 
    It does this by using the speedtest module to run a series of tests 
    and then prints out the results in a nicely formatted table.
'''

# Import the necessary modules
import speedtest
from time import sleep
from tqdm import tqdm
from colorama import Fore, init

# Initialize the colorama module and reset the terminal's text color after each print statement
init(autoreset=True)

# Print a message indicating that the script is getting the best available servers and running the speed tests
print(Fore.GREEN + "GETTING BEST AVAILABLE SERVERS, UPLOADING & DOWNLOADING SPEED.....")

# Create an instance of the Speedtest class
WIFI = speedtest.Speedtest()

# Find the most optimal server for running the tests
WIFI.get_best_server()

# Display a progress bar while finding the optimal server
for i in tqdm(range(10), colour="green", desc="Finding Optimal Server"):
    sleep(0.1)

# Test the download speed
WIFI.download()

# Display a progress bar while testing the download speed
for i in tqdm(range(10), colour="cyan", desc="Getting Download Speed"):
    sleep(0.1)

# Test the upload speed
WIFI.upload()

# Display a progress bar while testing the upload speed
for i in tqdm(range(10), colour="red", desc="Getting Upload Speed"):
    sleep(0.1)

# Get a dictionary containing the results of the speed tests
WIFI_Dict = WIFI.results.dict()

# Format the download speed and assign it to the Download variable
Download = str(WIFI_Dict['download'])[:2] + "." + \
    str(WIFI_Dict['download'])[2:4]

# Format the upload speed and assign it to the Upload variable
Upload = str(WIFI_Dict['upload'])[:2] + "." + str(WIFI_Dict['upload'])[2:4]

# Print a blank line
print("")

# Print a line of magenta text as a divider
print(Fore.MAGENTA + "="*80)

# Print a line of green text containing the heading "INTERNET SPEED TEST RESULTS:"
print(Fore.GREEN + "INTERNET SPEED TEST RESULTS:".center(80))

# Print another line of magenta text as a divider
print(Fore.MAGENTA + "="*80)

# Print a line of yellow text containing the download and upload speeds, as well as the ping time
print(Fore.YELLOW +
      f"Download: {Download} Mbps({float(Download)*0.125:.2f}MBs) | Upload:{Upload} Mbps ({float(Upload)*0.125:.2f}MBs) | Ping: {WIFI_Dict['ping']:.2f}ms".center(80))

# Print another line of magenta text as a divider
print(Fore.MAGENTA + "-"*80)

# Print a line of cyan text containing the host name, sponsor, and latency of the server used for the tests
print(Fore.CYAN + f"HOST:{WIFI_Dict['server']['host']} | SPONSOR:{WIFI_Dict['server']['sponsor']} | LATENCY: {WIFI_Dict['server']['latency']:.2f}".center(80))
