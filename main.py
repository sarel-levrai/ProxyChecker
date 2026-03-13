import requests
from pystyle import Colors, Colorate, Center, System
from concurrent.futures import ThreadPoolExecutor
import time

working_file = open("working.txt", "w")
dead_file = open("dead.txt", "w")

working = 0
dead = 0


def check_proxy(proxy):
    global working, dead

    try:
        proxies = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}"
        }

        r = requests.get(
            "http://httpbin.org/ip",
            proxies=proxies,
            timeout=2
        )

        if r.status_code == 200:
            print(Colors.green + f"[+] {proxy}")
            working_file.write(proxy + "\n")
            working += 1
            return

    except:
        pass

    print(Colors.red + f"[-] {proxy}")
    dead_file.write(proxy + "\n")
    dead += 1


def main():
    System.Title("ProxyChecker ^| Made By Sarel from SEC.")
    print(Center.XCenter(Colorate.Horizontal(Colors.black_to_blue , """ ██▓███   ██▀███   ▒█████  ▒██   ██▒▓██   ██▓ ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  
▓██░  ██▒▓██ ▒ ██▒▒██▒  ██▒▒▒ █ █ ▒░ ▒██  ██▒▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒▓██ ░▄█ ▒▒██░  ██▒░░  █   ░  ▒██ ██░▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒▒██▀▀█▄  ▒██   ██░ ░ █ █ ▒   ░ ▐██▓░▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ░  ░░██▓ ▒██▒░ ████▓▒░▒██▒ ▒██▒  ░ ██▒▓░▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
▒▓▒░ ░  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒▒ ░ ░▓ ░   ██▒▒▒ ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
░▒ ░       ░▒ ░ ▒░  ░ ▒ ▒░ ░░   ░▒ ░ ▓██ ░▒░   ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
░░         ░░   ░ ░ ░ ░ ▒   ░    ░   ▒ ▒ ░░  ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ 
            ░         ░ ░   ░    ░   ░ ░     ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░     
                                     ░ ░     ░                       ░                               
""", 1)))
    print(Colors.red + "Made By Sarel | S/O to Sarel-Edstine Corporation©")
    time.sleep(5)
    start_time = time.time()  # ← start timer
    with open("proxies.txt", "r") as f:
        proxies = [line.strip() for line in f if line.strip()]

    total = len(proxies)

    threads = 300  # ⬅ you can edit the threads rate.

    with ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(check_proxy, proxies)

    print(Colors.white+ f"\n===== END =====")
    print(Colors.white+ f"Total: {total}")
    print(Colors.white+ f"Working: {working}")
    print(Colors.white+ f"Dead: {dead}")

    end_time = time.time()
    elapsed = int(end_time - start_time)
    print(Colors.white + f"{elapsed} sec elapsed in total")
    working_file.close()
    dead_file.close()

    input("\nPress ⏎ to exit...")


if __name__ == "__main__":
    main()