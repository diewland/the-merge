import json
import random
from pprint import pprint as pp
 
DESC = "This collection is created on 2022/09/15 to celebrate Ethereum PoS -- The Merge"
ENGINE = "Jigsaw Engine"
OUTPUT_DIR = '02_revealed'
CONFIG = [
    # UR
    [ "ETH Merge Dayy",     1,      "https://diewland.github.io/jigsaw-launchpad/assets/the-merge/098fe0898606.png" ],
    # SR
    [ "15537393",           33,     "https://diewland.github.io/jigsaw-launchpad/assets/the-merge/40767b52265d.png" ],
    [ "The Merge",          33,     "https://diewland.github.io/jigsaw-launchpad/assets/the-merge/1212eeeb6ee0.png" ],
    [ "New Era",            33,     "https://diewland.github.io/jigsaw-launchpad/assets/the-merge/a227da0544e6.png" ],
    # R
    [ "Ethereum Pyramid",   100,    "https://diewland.github.io/jigsaw-launchpad/assets/the-merge/cf85e9c6402f.png" ],
    [ "Ethereum Tower",     100,    "https://diewland.github.io/jigsaw-launchpad/assets/the-merge/7ed96fcf3868.png" ],
    [ "Power of ETH",       100,    "https://diewland.github.io/jigsaw-launchpad/assets/the-merge/98c678818f93.png" ],
    # C
    [ "Ethereum in The Mist", 150,  "https://diewland.github.io/jigsaw-launchpad/assets/the-merge/c874e5725e27.png" ],
    [ "Ethereum City",      150,    "https://diewland.github.io/jigsaw-launchpad/assets/the-merge/819eeb07869d.png" ],
    [ "POW",                150,    "https://diewland.github.io/jigsaw-launchpad/assets/the-merge/bf2c257ecaf3.png" ],
    [ "The Day",            150,    "https://diewland.github.io/jigsaw-launchpad/assets/the-merge/3741b3c1ccab.png" ],
]

# bulk data
bulk = []

# append data to bulk
for (artwork, size, img) in CONFIG:
    for no in range(1, size+1):
        name = "{} #{}/{}".format(artwork, no, size)
        attrs = [
            {
              "trait_type": "Artwork",
              "value": artwork, 
            },
        ]
        metadata = {
          "name": name,
          "description": DESC,
          "image": img,
          "attributes": attrs,
          "compiler": ENGINE,
        }
        bulk.append(metadata)

# shuffle bulk 9999 round
for rnd in range(0, 9999):
    random.shuffle(bulk)

# write to file
for (idx, data) in enumerate(bulk):
    out = "./{}/{}.json".format(OUTPUT_DIR, idx)
    # write file
    with open(out, "w") as f:
        json.dump(data, f)
    # write log
    print("{}\t{}\t{}".format(out, data["name"], data["image"]))
