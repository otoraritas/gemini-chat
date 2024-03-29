#JANGAN RECODE AJG
import requests
import shutil
import os
from rich.panel import Panel
from rich import print as rprint
from rich.prompt import Prompt
from colorama import Fore as f
from datetime import datetime

now = datetime.now()

tahun = now.year
bulan = now.month
tanggal = now.strftime("%d")

hari_angka = now.weekday()
if hari_angka == 0:
    hari_nama = "Senin"
elif hari_angka == 1:
    hari_nama = "Selasa"
elif hari_angka == 2:
    hari_nama = "Rabu"
elif hari_angka == 3:
    hari_nama = "Kamis"
elif hari_angka == 4:
    hari_nama = "Jumat"
elif hari_angka == 5:
    hari_nama = "Sabtu"
else:
    hari_nama = "Minggu"

jam = now.hour
menit = now.minute
detik_awal = now.second

os.system("clear")

logo = f"""
{f.MAGENTA}╭━━━┳━━━┳━╮╭━┳━━┳━╮╱╭┳━━╮╱╭━━━┳╮╱╭┳━━━┳━━━━┳━━━┳━━━╮
{f.BLUE}┃╭━╮┃╭━━┫┃╰╯┃┣┫┣┫┃╰╮┃┣┫┣╯╱┃╭━╮┃┃╱┃┃╭━╮┃╭╮╭╮┃╭━╮┃╭━╮┃
{f.RED}┃┃╱╰┫╰━━┫╭╮╭╮┃┃┃┃╭╮╰╯┃┃┃╱╱┃┃╱╰┫╰━╯┃┃╱┃┣╯┃┃╰┫╰━╯┃╰━╯┃
{f.WHITE}┃┃╭━┫╭━━┫┃┃┃┃┃┃┃┃┃╰╮┃┃┃┣━━┫┃╱╭┫╭━╮┃╰━╯┃╱┃┃╱╰━━╮┣━━╮┃
{f.YELLOW}┃╰┻━┃╰━━┫┃┃┃┃┣┫┣┫┃╱┃┃┣┫┣┳━┫╰━╯┃┃╱┃┃╭━╮┃╱┃┃╱╭━━╯┣━━╯┃
{f.BLUE}╰━━━┻━━━┻╯╰╯╰┻━━┻╯╱╰━┻━━╯╱╰━━━┻╯╱╰┻╯╱╰╯╱╰╯╱╰━━━┻━━━╯
{f.GREEN}AUTHOR: ASIO
"""

def get_screen_width():
    columns, _ = shutil.get_terminal_size()
    return columns

screen_width = get_screen_width()

if screen_width != 70:
    print(f"Ukuran layar Anda ({screen_width}) tidak sama dengan 70. Silakan atur ukuran layar menjadi 70.")
    exit()

url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyALD_4lMsLnqlvXb3aOtLQ-eeYs6rhTaAY'

headers = {'Content-Type': 'application/json'}

print(logo)

while True:
    input_text = Prompt.ask("[bold yellow]Masukkan teks[/bold yellow]")

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": input_text
                    }
                ]
            }
        ]
    }

    detik_awal = now.second
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    detik_akhir = datetime.now().second

    for candidate in result['candidates']:
        content = candidate['content']
        if 'parts' in content:
            for part in content['parts']:
                if 'text' in part:
                    reply_text = part['text']
                    rprint(Panel(reply_text, title="[bold white]🤖 AI ASSISTAN CHAT 🤖[/bold white]", style="red"))
                    print(f"{f.WHITE}Riwayat: {tahun}/{bulan}/{tanggal}/{hari_nama}/{jam}:{menit} - Waktu Respon: {detik_akhir - detik_awal} detik")

                    os.system(f'espeak -s 190 -a 200 -p 60 -g 10 "{reply_text}"')

                    break
    print()
