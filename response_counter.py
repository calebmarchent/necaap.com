import requests
import json

base_url="https://cwwtprproposals.commonplace.is/schemes/proposals/"\
         "2-provide-your-feedback-on-the-site-area-options/comments.json"


def preferred_sites():
    idx = 0
    batch_size = 5
    while batch_size:
        r = requests.get(
            base_url,
            params={"from": str(idx),
                    "pageSize": str(batch_size)})
        j = json.loads(r.text)
        batch_size = len(j["data"])
        for f in j["data"]:
            yield [x["value"] for x in f["fields"] if x["name"]
                   == "whichSiteAreaDoYouThinkIsTheMostSuitableForTheRelocationProject"]
        idx = idx + batch_size

g = preferred_sites()

responses = 0
for v in g:
    responses += 1
    print(v)

print(f"{responses} responses counted")