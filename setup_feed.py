# Source: https://github.com/MarshalX/bluesky-feed-generator/blob/main/publish_feed.py

#!/usr/bin/env python3
# YOU MUST INSTALL ATPROTO SDK
# pip3 install atproto

from atproto import Client, models
import os
from textwrap import dedent

# YOUR bluesky handle
# Ex: user.bsky.social
HANDLE: str = "amitness.com"

# YOUR bluesky password, or preferably an App Password (found in your client settings)
# Ex: abcd-1234-efgh-5678
PASSWORD = os.environ["BLUESKY_APP_PASSWORD"]


# The hostname of the server where feed server will be hosted
# Ex: feed.bsky.dev
HOSTNAME: str = "bluesky-1tj.pages.dev"

# A short name for the record that will show in urls
# Lowercase with no spaces.
# Ex: whats-hot
RECORD_NAME: str = "arxiv-feed"

# A display name for your feed
# Ex: What's Hot
DISPLAY_NAME: str = "Papers"

# (Optional) A description of your feed
# Ex: Top trending content from the whole network
DESCRIPTION: str = dedent(
    """
    Latest ML research papers and preprints from arxiv.org discussed on Bluesky.
    
    Logic:
    - Fetch arxiv preprints & filters out non-ML via arxiv API
    - Ranks the items using hackernews algorithm
    """
).strip()

# (Optional) The path to an image to be used as your feed's avatar
# Ex: ./path/to/avatar.jpeg
AVATAR_PATH: str = ""

# (Optional). Only use this if you want a service did different from did:web
SERVICE_DID: str = ""


# -------------------------------------
# NO NEED TO TOUCH ANYTHING BELOW HERE
# -------------------------------------


def main():
    client = Client()
    client.login(HANDLE, PASSWORD)

    feed_did = SERVICE_DID
    if not feed_did:
        feed_did = f"did:web:{HOSTNAME}"

    avatar_blob = None
    if AVATAR_PATH:
        with open(AVATAR_PATH, "rb") as f:
            avatar_data = f.read()
            avatar_blob = client.upload_blob(avatar_data).blob

    response = client.com.atproto.repo.put_record(
        models.ComAtprotoRepoPutRecord.Data(
            repo=client.me.did,
            collection=models.ids.AppBskyFeedGenerator,
            rkey=RECORD_NAME,
            record=models.AppBskyFeedGenerator.Record(
                did=feed_did,
                display_name=DISPLAY_NAME,
                description=DESCRIPTION,
                avatar=avatar_blob,
                created_at=client.get_current_time_iso(),
            ),
        )
    )

    print("Successfully published!")
    print('Feed URI (set in "FEED_URI" in `generate_feed.py`):', response.uri)


if __name__ == "__main__":
    main()
