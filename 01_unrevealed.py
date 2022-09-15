import json
 
TOKEN_SIZE = 1000
START_ID = 0
OUTPUT_DIR = '01_unrevealed'

NAME = "The Merge"
DESC = "This collection is created on 2022/09/15 to celebrate Ethereum PoS -- The Merge"
IMG = "https://diewland.github.io/jigsaw-launchpad/assets/31868f886e0c.png"
ATTRS = [
    {
      "trait_type": "Artwork",
      "value": "Unrevealed", 
    },
]
ENGINE = "Jigsaw Engine"

metadata = {
  "name": "***",
  "description": DESC,
  "image": IMG,
  "attributes": ATTRS,
  "compiler": ENGINE,
}

for id in range(0, TOKEN_SIZE):
    metadata["name"] = "{} #{}".format(NAME, id)
    with open("./{}/{}.json".format(OUTPUT_DIR, START_ID + id), "w") as f:
        json.dump(metadata, f)
