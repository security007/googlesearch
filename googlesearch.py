from mod.cari import Search
import argparse
import colorama
import time
import sys
import re
import requests


class Color:
    green = "["+colorama.Fore.GREEN+"+"+colorama.Fore.RESET+"] "
    red = "["+colorama.Fore.RED+"x"+colorama.Fore.RESET+"] "
    yellow = "["+colorama.Fore.YELLOW+"-"+colorama.Fore.RESET+"] "
    save = "["+colorama.Fore.BLUE+"✔"+colorama.Fore.RESET + "] "


class Judul:
    g = colorama.Fore.BLUE+"𝔾"+colorama.Fore.RESET
    o = colorama.Fore.RED+"𝕠"+colorama.Fore.RESET
    o2 = colorama.Fore.YELLOW+"𝕠"+colorama.Fore.RESET
    g2 = colorama.Fore.BLUE+"𝕘"+colorama.Fore.RESET
    l = colorama.Fore.GREEN+"𝕝"+colorama.Fore.RESET
    e = colorama.Fore.RED+"𝕖"+colorama.Fore.RESET
    text = g+o+o2+g2+l+e


def main():
    # set argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--query", type=str,
                        help="query to search", required=True)
    parser.add_argument("-l", "--limit", type=int,
                        help="limit of results, Default : 10", default=10)
    parser.add_argument("-s", "--save", type=str,
                        help="Save results to file", default=None)
    parser.add_argument(
        '-d', '--domain', help="Get only domain name", action='store_true')
    parser.add_argument(
        '--proxy', help="Set proxy, ip:port", default=None)
    args = parser.parse_args()

    # set query
    query = args.query
    # set limit
    limit = args.limit
    if args.domain:
        domain = True
    else:
        domain = False
    proxy = args.proxy
    save = args.save
    # start search
    # cek proxy format
    if proxy != None:
        print(Color.green+"Checking proxy ")
        # grep proxy
        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}$", proxy):
            # checking proxy
            setproxy = {
                'http': 'http://'+proxy,
                'https': 'https://'+proxy,
            }
            try:
                r = requests.get('https://www.google.com/',
                                 proxies=setproxy, timeout=10).status_code
                print(Color.green+"Proxy status "+str(r))
            except Exception as e:
                print(Color.red+"Proxy not working")
                sys.exit()

        else:
            print(Color.red+"Proxy format not valid")
            sys.exit()
    search = Search(query=query, limit=limit,
                    domain=domain, save=save, proxy=proxy)
    results = search.get_results()

    # print results
    for result in results:
        if result == "Captcha blocked":
            print(Color.red+"Captcha blocked")
            print(Color.green+"Sleeping for 10 seconds and exit")
            time.sleep(10)
            print(Color.red+"Exit...")
            sys.exit()
        elif result == "No results":
            print(Color.yellow+"No results")
        else:
            print(Color.green+str(result))
    if results[0] != "Captcha blocked" and results[0] != "No results":
        if save != None:
            print(Color.save+"Saved to "+save)


if __name__ == '__main__':
    print(Judul.text)
    main()
