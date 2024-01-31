from configparser import ConfigParser

config = ConfigParser()

config["DEFAULT"] = {
    "numberdigits": 6,
    "numbertries": 9,
    "playername": "PLAYER"
    
}

config["SUDO"] = {
    "numberdigits": 12,
    "numbertries": 8,
    "playername": "JILLIAN"
    
}

config["DAMIAN"] = {
    "numberdigits": 9,
    "numbertries": 6,
    "playername": "CHEATER",
    "cheats": "on"
    
}
config.add_section('account')
config.set('account', 'name', 'pin')

with open("game_geussing.ini", "w") as f:
    config.write(f)

