from mod.cari import Search
import argparse
import colorama
import time


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
    args = parser.parse_args()

    # set query
    query = args.query
    # set limit
    limit = args.limit
    if args.domain:
        domain = True
    else:
        domain = False
    save = args.save
    # start search
    search = Search(query=query, limit=limit, domain=domain, save=save)
    results = search.get_results()

    # print results
    for result in results:
        if result == "Captcha blocked":
            print(Color.red+"Captcha blocked")
            print(Color.green+"Sleeping for 10 seconds and exit")
            time.sleep(10)
        elif result == "No results":
            print(Color.yellow+"No results")
        else:
            print(Color.green+result)
    if results[0] != "Captcha blocked" and results[0] != "No results":
        if save != None:
            print(Color.save+"Saved to "+save)


if __name__ == '__main__':
    print(Judul.text)
    main()
