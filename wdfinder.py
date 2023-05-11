import requests
import sys
import random
from colorama import Fore, Style
import readline
from prompt_toolkit import prompt

print(f'''{Fore.BLUE}
 ▄█     █▄     ▄████████ ▄██   ▄   ▀█████████▄     ▄████████  ▄████████    ▄█   ▄█▄      ███    █▄     ▄████████  ▄█               ▄████████  ▄█  ███▄▄▄▄   ████████▄     ▄████████    ▄████████ 
███     ███   ███    ███ ███   ██▄   ███    ███   ███    ███ ███    ███   ███ ▄███▀      ███    ███   ███    ███ ███              ███    ███ ███  ███▀▀▀██▄ ███   ▀███   ███    ███   ███    ███ 
███     ███   ███    ███ ███▄▄▄███   ███    ███   ███    ███ ███    █▀    ███▐██▀        ███    ███   ███    ███ ███              ███    █▀  ███▌ ███   ███ ███    ███   ███    █▀    ███    ███ 
███     ███   ███    ███ ▀▀▀▀▀▀███  ▄███▄▄▄██▀    ███    ███ ███         ▄█████▀         ███    ███  ▄███▄▄▄▄██▀ ███             ▄███▄▄▄     ███▌ ███   ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
███     ███ ▀███████████ ▄██   ███ ▀▀███▀▀▀██▄  ▀███████████ ███        ▀▀█████▄         ███    ███ ▀▀███▀▀▀▀▀   ███            ▀▀███▀▀▀     ███▌ ███   ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
███     ███   ███    ███ ███   ███   ███    ██▄   ███    ███ ███    █▄    ███▐██▄        ███    ███ ▀███████████ ███              ███        ███  ███   ███ ███    ███   ███    █▄  ▀███████████ 
███ ▄█▄ ███   ███    ███ ███   ███   ███    ███   ███    ███ ███    ███   ███ ▀███▄      ███    ███   ███    ███ ███▌    ▄        ███        ███  ███   ███ ███   ▄███   ███    ███   ███    ███ 
 ▀███▀███▀    ███    █▀   ▀█████▀  ▄█████████▀    ███    █▀  ████████▀    ███   ▀█▀      ████████▀    ███    ███ █████▄▄██        ███        █▀    ▀█   █▀  ████████▀    ██████████   ███    ███ 
                                                                          ▀                           ███    ███ ▀                                                                    ███    ███ 
---------------------------------------------------------------------------------c̶o̶d̶e̶d̶ b̶y̶ w̶h̶i̶t̶e̶d̶e̶v̶i̶l̶---------------------------------------------------------------------------------------------
''')
print(f'''{Fore.YELLOW} The order of command to be used:
 1. seturl <url>
 2. setbeg <yyyy>
 3. setend <yyyy>
 4. find
After execution of this commands you can see the output with help of command show_urls.''')

class wdfind():
    def __init__(self):
        self.url = ""
        self.count = 0
        self.beg = ""
        self.end = ""
        self.timestamp = []
        self.rl = []
        self.urls = []
        self.filename = "archive_url.txt"

    def set_url(self, url):
        if len(url.split()) > 1:
            print(f"{Fore.RED}[!] More than 1 URL!! Please enter only one URL{Style.RESET_ALL}")
        else:
            self.url = url.split()[0]
            print(f"{Fore.GREEN}[+] URL set to {self.url}{Style.RESET_ALL}")
            
    def validate(self):
    	if self.beg<=self.end:
    		self.find()
    	else:
    	    print(f"{Fore.RED}[!]Error the ending can't be before the begining")
    def set_beg(self, beg):
        if len(beg.split()) > 1:
            print(f"{Fore.RED}[!] More than 1 timestamp!! Please enter only one timestamp{Style.RESET_ALL}")
        else:
            self.beg = beg.split()[0]
            print(f"{Fore.GREEN}[+] Beginning timestamp set to {self.beg}{Style.RESET_ALL}")

    def set_end(self, end):
        if len(end.split()) > 1:
            print(f"{Fore.RED}[!] More than 1 timestamp!! Please enter only one timestamp{Style.RESET_ALL}")
        else:
            self.end = end.split()[0]
            print(f"{Fore.GREEN}[+] End timestamp set to {self.end}{Style.RESET_ALL}")

    def find(self):
        r = requests.get(f"http://web.archive.org/cdx/search/cdx?url={self.url}&from={self.beg}&to={self.end}")
        if r.status_code == 200:
            print(f"{Fore.GREEN}[+] Data Retrieved{Style.RESET_ALL}")
            self.rl = r.text.split()
        else:
            print(f"{Fore.RED}[!] Error Status Code: -->" + str(r.status_code) + Style.RESET_ALL)
        return self.rl

    def find_timestamp(self):
        i = 1
        while i < len(self.rl):
            ts = self.rl[i]
            self.timestamp.append(ts)
            i += 7
            self.count = self.count + 1
        print(self.count)

    def print_timestamp(self):
        print(f"{Fore.GREEN}[+] Timestamps{Style.RESET_ALL}")
        print("\n".join(self.timestamp))

    @staticmethod
    def help():
    	print(f'''{Fore.YELLOW} The order of command to be used:
    			1. seturl <url>
    			2. setbeg <yyyy>
    			3. setend <yyyy>
    			4. find
    			5. findts
    		After execution of this commands you can see the output with help of command show_urls.
    	''')
    	print(f"{Fore.YELLOW}Wayback URL Finder Commands:{Style.RESET_ALL}")
    	print(f"{Fore.YELLOW}  seturl <url>        - Set the URL to search for{Style.RESET_ALL}")
    	print(f"{Fore.YELLOW}  setbeg <timestamp>  - Set the beginning timestamp (format: yyyy){Style.RESET_ALL}")
    	print(f"{Fore.YELLOW}  setend <timestamp>  - Set the end timestamp (format: yyyy){Style.RESET_ALL}")
    	print(f"{Fore.YELLOW}  find                - Perform the search and retrieve the data{Style.RESET_ALL}")
    	print(f"{Fore.YELLOW}  findts              - Extract the timestamps from the retrieved data{Style.RESET_ALL}")
    	print(f"{Fore.YELLOW}  printts             - Print the extracted timestamps{Style.RESET_ALL}")
    	print(f"{Fore.YELLOW}  showurls            - Display the URLs with their corresponding timestamps{Style.RESET_ALL}")
    	print(f"{Fore.YELLOW}  save <filename>     - Save the URLs and timestamps to a text file{Style.RESET_ALL}")
    	print(f"{Fore.YELLOW}  help                - Show available commands and their descriptions{Style.RESET_ALL}")
    	print(f"{Fore.YELLOW}  exit                - Exit the program{Style.RESET_ALL}")
	
    @staticmethod
    def exit():
    	quotes = [
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "The way to get started is to quit talking and begin doing. - Walt Disney",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "If life were predictable it would cease to be life, and be without flavor. - Eleanor Roosevelt",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
        "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "The harder I work, the luckier I get. - Samuel Goldwyn",
        "You miss 100% of the shots you don't take. - Wayne Gretzky",
        "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson",
        "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
        "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
        "The secret of success is to know something nobody else knows. - Aristotle Onassis",
        ]
    	quote = random.choice(quotes)
    	print(f"{Fore.GREEN}Exiting...{Style.RESET_ALL}")
    	print(f"{Fore.GREEN}Remember, hacking is a mindset.{Style.RESET_ALL}")
    	print(f"{Fore.GREEN}Before you go, here's a random hacking quote:{Style.RESET_ALL}")
    	print(f"{Fore.CYAN}[-]{quote}")
    	sys.exit(0)

    def show_urls(self):
        for time in self.timestamp:
            t = list(time)
            y = t[:4]
            m = t[4:6]
            d = t[6:8]
            hr = t[8:10]
            mi = t[10:12]
            sec = t[12:14]

            date_str = f"{Fore.GREEN}Date: {''.join(d)}/{''.join(m)}/{''.join(y)}{Style.RESET_ALL}"
            time_str = f"{Fore.GREEN}Time: {''.join(hr)}:{''.join(mi)}:{''.join(sec)}{Style.RESET_ALL}"
            url_str = f"{Fore.GREEN}URL: https://web.archive.org/web/{time}/{self.url}{Style.RESET_ALL}"
            
            url_info = f"{date_str} {time_str} | {url_str}"
            self.urls.append(url_info)

            y.clear()
            d.clear()
            m.clear()
            hr.clear()
            mi.clear()
            sec.clear()

    def print_urls(self):
        if self.urls == [] and self.url == "":
                print(f"{Fore.RED}[!]Error: Set url ")
        print(f"{Fore.GREEN}[+] URLs:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[+] Total Urls: {len(self.urls)}")
        for url in self.urls:          	
            	print(url)

    def show_options(self):
    	print(f"URl         -  {self.url}")
    	print(f"From Year   -  {self.beg}")
    	print(f"End Year    -  {self.end}")
    def save(self, filename):
        try:
            with open(filename, 'w') as file:
                for url in self.urls:
                    file.write(url + '\n')
        
            print(f"{Fore.GREEN}[+] URLs and timestamps saved to {filename}{Style.RESET_ALL}")
        except IOError:
            print(f"{Fore.RED}[!] Error: Failed to write to file{Style.RESET_ALL}")


def main():
    wdfinder = wdfind()  # Create an instance of the wdfind class

    while True:
        command = prompt(">>>")

        # Split the command into command and arguments
        parts = command.split(" ")
        cmd = parts[0]
        args = parts[1:]

        if cmd == "seturl":
            if args:
                url = args[0]
                wdfinder.set_url(url)
            else:
                print(f"{Fore.RED}[!] URL not provided. Usage: seturl <url>{Style.RESET_ALL}")

        elif cmd == "setbeg":
            if args:
                timestamp = args[0]
                wdfinder.set_beg(timestamp)
            else:
                print(f"{Fore.RED}[!] Beginning timestamp not provided. Usage: setbeg <timestamp>{Style.RESET_ALL}")

        elif cmd == "setend":
            if args:
                timestamp = args[0]
                wdfinder.set_end(timestamp)
            else:
                print(f"{Fore.RED}[!] End timestamp not provided. Usage: setend <timestamp>{Style.RESET_ALL}")

        elif cmd == "find":
            wdfinder.validate()

        elif cmd == "findts":
            wdfinder.find_timestamp()
        elif cmd == "options":
            wdfinder.show_options()

        elif cmd == "printts":
            wdfinder.print_timestamp()

        elif cmd == "showurls":
            wdfinder.show_urls()
            wdfinder.print_urls()

        elif cmd == "save":
            if args:
                filename = args[0]
                wdfinder.save(filename)
            else:
                filename = wdfinder.filename 
                wdfinder.save(filename)

        elif cmd == "help":
            wdfind.help()

        elif cmd == "exit":
            wdfinder.exit()

        else:
            print(f"{Fore.RED}[!] Invalid command. Type 'help' for available commands.{Style.RESET_ALL}")

if __name__ == "__main__":
	try:
	    main()
	except KeyboardInterrupt:
	    print(f"{Fore.RED}\n[-]Bye Bye.....")
