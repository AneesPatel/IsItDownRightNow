import os

def main():
    try:
        website_url = input("Enter Website URL: ")

        response = os.system("ping " + website_url)

        if response == 0:
            down = True
        else:
            down = False
        #print("\033[1;32m This text is Bright Green \n")

        print("Website URL: \u001b[37m {}".format(website_url))
        if down:
            print("Connectivity:" + "\033[1;32m Site is working.")
        else:
            print("Connectivity:" + "\u001b[31m Site is NOT working.")
    except:
        print("An error occured. Try Again in a moment...")

if __name__ == '__main__':
    main()