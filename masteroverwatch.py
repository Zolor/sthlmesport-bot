# -*- coding: utf-8 -*-
import bs4 as bs
import urllib.request


def masteroverwatch(battletag):
    hash_number = battletag.find("#") + 1
    test_battletag = battletag[hash_number:]
    try:
        int(test_battletag)
        try:
            url = "http://masteroverwatch.com/profile/pc/eu/" + battletag.replace("#","-")
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            url_read = urllib.request.urlopen(req).read()
            soup = bs.BeautifulSoup(url_read,'lxml')
            master_winrate_soup = soup.find("strong", class_="stats-kills").get_text()
            master_winrate_soup = master_winrate_soup.strip()
            master_mmr_soup = soup.find("div", class_="header-stat").get_text()
            master_mmr_soup = "".join(line.strip() for line in master_mmr_soup.split("\n"))
            master_mmr_soup = master_mmr_soup[:5]
            heroes_soup = soup.select(".summary-hero-name")
            hero1 = heroes_soup[0].get_text()
            hero2 = heroes_soup[1].get_text()
            hero3 = heroes_soup[2].get_text()
            if master_mmr_soup != "—Skil":
                msg = (battletag + " is " + master_mmr_soup + " MMR and has " + master_winrate_soup + 
                " winrate. Favorite heroes are " + hero1 + ", " + hero2 + " and " + hero3 + ".")
                return(msg)
            else:
                msg = battletag + " has not yet played competitive and has " + master_winrate_soup + " winrate"
                return msg
        except urllib.error.HTTPError as err:
            if err.code == 404:
                msg = battletag + " not found :( sure you exist?"
                return(msg)
    except:
        msg = "Not found :( sure you exist?"
        return(msg)