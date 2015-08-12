ALL             = "ALL"

UGC_PLATINUM    = "UGC Platinum"
UGC_GOLD        = "UGC Gold"
UGC_SILVER      = "UGC Silver"
UGC_STEEL       = "UGC Steel"
UGC_IRON        = "UGC Iron"
UGC_ASIA_GOLD   = "UGC Asia Gold"
UGC_ASIA_STEEL  = "UGC Asia Steel"

ETF_PREMIERSHIP = "ETF2L Premiership"
ETF_OPEN  = "ETF2L Open"
ETF_MID  = "ETF2L Mid"
ETF_HIGH  = "ETF2L High"

AUSTRALIA_NEWZ  = "Australia/New Zealand"

HIGHLANDER_OPEN = "Highlander Open"
ESEA_OPEN = "ESEA Open"
ESEA_INTER = "ESEA Intermediate"
ESEA_INV = "ESEA Invite"

CHOICES_TEAM_TYPE = [("4v4","4v4"),("6v6","6v6"),("9v9","9v9")]
FILTER_TEAM_TYPE = [(ALL, ALL)]
FILTER_TEAM_TYPE.extend(CHOICES_TEAM_TYPE)

CHOICES_CLASSES = [("Medic","Medic"),("Heavy","Heavy"),("Demoman","Demoman"),("Soldier","Soldier"),("Scout","Scout"),("Pyro","Pyro"),("Engineer","Engineer"),("Spy","Spy"),("Sniper","Sniper")]


CHOICES_SKILLS = [
    (UGC_PLATINUM,UGC_PLATINUM),
    (UGC_GOLD,UGC_GOLD),
    (UGC_SILVER,UGC_SILVER),
    (UGC_STEEL,UGC_STEEL),
    (UGC_IRON,UGC_IRON),
    (UGC_ASIA_GOLD,UGC_ASIA_GOLD),
    (UGC_ASIA_STEEL,UGC_ASIA_STEEL),
    (ETF_PREMIERSHIP,ETF_PREMIERSHIP),
    (ETF_OPEN,ETF_OPEN),
    (ETF_MID,ETF_MID),
    (ETF_HIGH,ETF_HIGH),
    (HIGHLANDER_OPEN, HIGHLANDER_OPEN),
    (ESEA_OPEN,ESEA_OPEN),
    (ESEA_INTER,ESEA_INTER),
    (ESEA_INV,ESEA_INV),
    (AUSTRALIA_NEWZ,AUSTRALIA_NEWZ)
]

FILTER_SKILLS = [(ALL, ALL)]
FILTER_SKILLS.extend(CHOICES_SKILLS)

