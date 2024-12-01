# bluesky-arxiv

<p align="center">
<img src="https://amitness.com/posts/bluesky-custom-feed/paper-feed-screenshot.png" width="650"/><br>
Feed: https://bsky.app/profile/amitness.com/feed/arxiv-feed
</p>

A simple stack for generating custom feeds for Bluesky programmatically without a backend server

**Blog**: https://amitness.com/posts/bluesky-custom-feed/

## High-level Overview

We first use Skyfeed to filter the entire network of posts on Bluesky using a regular expression for posts with links for **arxiv.org** papers. 

Then, the resulting feed is filtered using Bluesky's atproto library through Python. Here, we iterate through each paper and check if the paper belongs to the arxiv categories for Machine Learning, NLP, and Computer Vision via the [pyarxiv](https://github.com/thechrisu/pyarxiv) library. From the filtered list of papers, we generate the JSON data format required by Bluesky for reading feeds and push that to Cloudflare pages as a static site.

![](https://amitness.com/posts/bluesky-custom-feed/bluesky-stack-pipeline.png)

When the feed is loaded on the Bluesky app, the app will make a request to our static page on Cloudflare and get a list of the post IDs as a JSON response. The app will parse each post ID, render it in the app, and display the feed. This runs super quick.

![](https://amitness.com/posts/bluesky-custom-feed/bluesky-api-calls.png)
