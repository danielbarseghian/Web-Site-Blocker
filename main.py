HOSTS_FILE = "/etc/hosts"

def main():
	match input("1-4 "):
		case "1":
			add_block(input("website? "))
		case "2":
			restore_file()
		case "3":
			remove_block(input("web name? "))


def add_block(website_to_block):
	with open(HOSTS_FILE, "a") as file:
			website_to_block = website_to_block.lower().strip()
			line = f"127.0.0.1 {website_to_block}\n"
			file.write(line)
			line2 = f"127.0.0.1 www.{website_to_block}"
			file.write(line2)
			

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
	with open(HOSTS_FILE, "r") as file:
		filtered_lines = [line for line in file if web_name not in line]

	with open(HOSTS_FILE, "w") as file:
		file.writelines(filtered_lines)

main()