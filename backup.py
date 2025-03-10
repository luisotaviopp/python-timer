import schedule
import time
import subprocess
from datetime import datetime

def backup_job():
    print("Iniciando Backup ")
    print(datetime.now().strftime('%H:%M:%S | %d-%m-%Y'))
    subprocess.run(["php", "backup.php"])  # Chamando o backup.php todas as quartas feiras, 10 da manha.


print("Iniciou rotinas.")
schedule.every().wednesday.at("10:00").do(backup_job)

while True:
    schedule.run_pending()
    time.sleep(1)
