Original Source: https://gist.github.com/bjmiller121/f93cd974ff709d2b968f

Making my own copy, because it's well useful, and things vanish from the internet all the time...

---------------------------------
Sometimes you need to keep two upstreams in sync with each other. For example, you might need to both push to your testing environment and your GitHub repo at the same time. In order to do this simultaneously in one git command, here's a little trick to add multiple push URLs to a single remote.

Once you have a remote set up for one of your upstreams, run these commands with:

```
git remote set-url --add --push [remote] [original repo URL]
git remote set-url --add --push [remote] [second repo URL]
```

Once set up, `git remote -v` should show two (push) URLs and one (fetch) URL. Something like this:

```
$ git remote -v
origin git@github.com:bjmiller121/original-repo.git (fetch)
origin git@github.com:bjmiller121/original-repo.git (push)
origin git@github.com:bjmiller121/second-repo.git (push)
```

Now, pushing to this remote will push to both upstreams simultaneiously. Fetch and pull from this remote will still pull from the original repo only.

**Tip:** If you always want to push to both upstreams simultaneously, you might want to use the `origin` remote. If you only sometimes want to push to both, you might use a remote name like `both` to indicate that it will push to multiple repos.
