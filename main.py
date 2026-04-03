HOSTS_FILE = "/etc/hosts"
from colorama import Fore, Style, init
import re
import sys

def main():
	print(Fore.CYAN + "╔════════════════════════════╗")
	print("║        LOGIN MENU          ║")
	print("╠════════════════════════════╣")
	print("║  " + Fore.WHITE + "[1] Add block to website" + Fore.CYAN + "  ║")
	print("║  " + Fore.WHITE + "[2] Restore file" + Fore.CYAN + "          ║")
	print("║  " + Fore.WHITE + "[3] Delete a block" + Fore.CYAN + "        ║")
	print("║  " + Fore.WHITE + "[4] Quit" + Fore.CYAN + "                  ║")
	print("╚════════════════════════════╝" + Style.RESET_ALL)

	choice = input("Choose between 1 and 4. ")
	
	match choice:
		case "1":
			web = input("what website you want to block? ")

			while check_url(web) == False:
				web = input("what website you want to block? ")

			if web.startswith("www."):
				web = web.removeprefix("www.")

			add_block(web)

		case "2":
			match input("Do you really want to restore the file (This will delete all of your websites blocked) ? "):
				case "yes" | "y":	
					restore_file()
				case "no" | "n":
					print("File not restored")
				case _:
					print("please respond by yes or no")

		case "3":
			web_name = input("What's the name of the website you want to unblock? (ex: youtube.com, instagram.com, ...) ")
			remove_block(web_name)

		case "4":
			sys.exit(0)

def check_website(website):
	if match := re.match(r"^(www\.)?[A-Za-z]+(\.com)?$", website):
		return (match.group(1), match.group(2))

def add_block(website_to_block):
	with open(HOSTS_FILE, "a") as file:
		website_to_block = website_to_block.lower().strip()
		line = f"127.0.0.1 {website_to_block}\n"
		file.write(line)
		line2 = f"127.0.0.1 www.{website_to_block}\n"
		file.write(line2)
			
def check_url(w):
	ws, domain = check_website(w)

	if not ws == "www." and ws is not None:
		return False

	if not re.match(r"^\..+", domain):
		return False

	return True

def restore_file():

	hosts_base_content = """127.0.0.1       localhost
127.0.1.1       daniel-deb-laptop.daniel-deb.org        daniel-deb-laptop

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
"""

	with open(HOSTS_FILE, "w+") as file:
		file.write(hosts_base_content)

def remove_block(web_name):
	target1 = "127.0.0.1 youtube.com"
	target2 = "127.0.0.1 www.youtube.com"

	with open(HOSTS_FILE, "r") as f:
		lines = f.readlines()

	filtered = []

	for line in lines:
		clean = line.strip()  # remove \n and spaces

		if clean != target1 and clean != target2:
			filtered.append(line)

	with open(HOSTS_FILE, "w") as f:
		f.writelines(filtered)

main()

# TO ADD tests and fix remove
