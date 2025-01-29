import requests
import argparse

def print_list(l: list):
    for x in l:
        print(x)
    print("\n")


def find_readme(refs: list):
    readme = ""
    for ref in refs:
        if ref.find("README") >= 0:
            readme = ref
            break
    return readme


def find_href(html: str, opt: dict):
    refs = []
    start = 0
    fin = 0
    if type(html) is not str:
        raise AssertionError("argument is not an integer")
    while 1:
        debut = html.find("<a", start)
        if (debut == -1):
            break
        fin = html.find('</a>', debut + 3)
        ref = html[debut:fin + 4]
        start = fin + 1
        debut = ref.find('href="')
        if (debut == -1):
            continue
        f2 = ref.find('"', debut + 6)
        ref = ref[debut + 6:f2]
        if ref.find('http') == -1:
            ref = opt['url'] + ref
        if ref.find('/../') == -1:
            refs.append(ref)
    return refs


def recurse_get(refs: list, checked_url: list, av: dict):
    refs = [x for x in refs if x not in checked_url]
    av['r'] = av['r'] - 1
    for url in refs:
        av['url'] = url
        # print(av['url'])
        checked_url.append(url)
        response = requests.get(url)
        assert response.status_code == 200, f"Error: get Statue code {response.status_code}"
        new_refs = find_href(response.text, av)
        readme = find_readme(new_refs)
        if readme != "":
            response = requests.get(readme)
            if (response.text[:3] != 'Non' and response.text[:2] != 'Tu' and response.text[:7] != 'Demande' and response.text[:8] != 'Toujours'):
                print("readme >>>> ", readme)
                print(response.text)
                return 
        if (av["r"] >= 0):
            recurse_get(new_refs, checked_url, av)
            av['r'] = av['r'] + 1


def main():
    parser = argparse.ArgumentParser(prog="scrapy")
    parser.add_argument('url', type=str, help="The URL of the website")
    parser.add_argument('-r', '--recursive', action='store_true', help="Recursively downloads the images in a URL received as a parameter.")
    parser.add_argument('-rl', '-r -l', '--depht_level', type=int, help='Indicates the maximum depth level of the recursive download.\nIf not indicated, it will be 5.')
    args = parser.parse_args()

    av = {'url':args.url , 'r': 0, 'p': './data/'}
    if (args.recursive == True):
        av['r'] = 5
    elif (args.depht_level != None):
        av['r'] = args.depht_level

    refs = list()
    refs.append(args.url)
    checked_urls = list()
    try:
        recurse_get(refs, checked_urls, av)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
