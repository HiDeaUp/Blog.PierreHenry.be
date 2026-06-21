+++
title = "How to Build an AI Audience Tracker Without Docker Headaches"
slug = "how-to-build-an-ai-audience-tracker-without-docker-headaches"
date = "2026-01-08T09:30:05.716777"
draft = false
description = "So, I continued working on our audience attention measurement system. If you missed the first part, we ran into a little snag with the API—turns out Postgres wasn’t installed locally. The quick win..."
summary = "So, I continued working on our audience attention measurement system. If you missed the first part, we ran into a little snag with the API—turns out Postgres wasn’t installed locally. The quick win..."
tags = ["ai engineering", "audience attention", "database setup", "debugging", "entrepreneurship", "productivity", "system development", "tech"]
priority = true
priority_topics = ["tech", "productivity", "entrepreneurship"]
original_title = "DAY 2: Build an audience attention measurement system from SCRATCH (AI Engineering)"
source_medium = "https://medium.com/@phenrysay/30c58326c981"
source_youtube = "https://www.youtube.com/watch?v=fpW4muqg76Y"
+++

{{< figure src="https://images.unsplash.com/photo-1646579886135-068c73800308?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwxfHxBSSUyMGVuZ2luZWVyaW5nJTIwYXVkaWVuY2UlMjBhdHRlbnRpb24lMjBzeXN0ZW0lMjBkZXZlbG9wbWVudHxlbnwwfDB8fHwxNzY3ODM1ODExfDA&ixlib=rb-4.1.0&q=80&w=1080" alt="A man in front of a group of people" title="How to Build an AI Audience Tracker Without Docker Headaches" caption="How to Build an AI Audience Tracker Without Docker Headaches - Photo by [Herlambang Tinasih Gusti](https://unsplash.com/@tinasihgusti) on [Unsplash](https://unsplash.com/photos/a-man-standing-in-front-of-a-group-of-people-3kc_75Rdgyk)" >}}

# DAY 2: Build an Audience Attention Measurement System from SCRATCH (AI Engineering)
## Debugging, Database Setup, and Admin Automation

---

So, I continued working on our audience attention measurement system. If you missed the first part, we ran into a little snag with the API—turns out Postgres wasn’t installed locally. The quick win here was just to install Postgres with Homebrew for now. Later, we’ll do it the proper way with Docker, especially for production. But for development, Homebrew gets us moving faster.

Once Postgres was up, it created a DB user for me—funny enough, it just grabbed my username from the `whoami` Unix command. If you’re not familiar, `whoami` simply spits out your current user in the terminal. That’s how the setup script picked my username for the DB user. After that, it created the database, updated the `.env` file, and we were good to go.

## API Troubleshooting: The Classic "Not Found" Headache

With the database sorted, I cd’d into the API directory and fired up the server. But when I hit the endpoint, I kept getting a "not found" response. I was scratching my head—why is it always not found? I double-checked with a POST request and realized, oh, the endpoint is POST, not GET. Classic mistake. I must have mixed up the docs or something. Once I switched to POST, boom—success response.

Here’s a quick example of the POST request payload I used:

```bash
curl -X POST http://localhost:3001/api/track \
  -H "Content-Type: application/json" \
  -d '{"userId": "123", "attention": 0.85}'
```

If you hit the GET endpoint (which is just for testing), you can do that in the browser at `/api/track/test`. It’s a bit slow to respond, but it works.

## Port Conflicts and the Mystery Process

Next, I ran into a port conflict—port 3001 was already in use. I couldn’t figure out what was using it. Checked everywhere in the terminal, no luck. The frontend is on 2000, so that’s fine. I switched the API to use 3100, and that solved it. No more timeouts or hanging requests.

Just a reminder: always check your ports. If something’s not responding, it might be a port issue, not your code.

## Database Setup: Why It Matters

The real issue was the database wasn’t set up properly. That’s why the endpoint wasn’t working. Once the DB was sorted, everything clicked into place. I wanted to make sure this doesn’t trip up anyone else, so I double-checked the setup and updated the docs. If you’re setting up this project, make sure your database is initialized before you start the API.

I also cleaned up some test users from the database:

```sql
DELETE FROM users WHERE email = 'test@example.com';
```

Just keeping things tidy.

## Automating Admin User Creation

We talked about this in part one, but I wanted to make sure there’s always an admin user created by default. The code now checks if an admin exists—if not, it inserts one with a hashed password. Super important: always hash your passwords. Never store them in plain text. Here’s a quick rundown:

- **Hashing**: Use a strong hashing algorithm (like bcrypt) to store passwords.
- **Salting**: Add a unique salt to each password before hashing for extra security.

In Node.js, you might use something like this:

```js
const bcrypt = require('bcrypt');
const password = 'admin123';
const saltRounds = 10;

bcrypt.hash(password, saltRounds, function(err, hash) {
  // Store hash in your database
});
```

And yes, the default admin password is `admin123`—but **change this immediately in production**. Don’t be that person who ships with default credentials.

> "Hashing and encryption can keep sensitive data safe. Never store plain text passwords—ever."

## Keeping the Repo Clean

I noticed some leftover setup and troubleshooting files in the repo. Cleaned those up with a quick `git rm` and commit. Sometimes, when you use integrations like Bit Kraken, it’s easy to commit stuff you didn’t mean to. Always double-check your commits.

```bash
git rm setup-troubleshooting.md
git commit -m "Remove setup troubleshooting docs"
```

## Wrapping Up

That’s it for this round. The API is running, the database is set up, admin user is automated, and the repo is clean. Honestly, building stuff like this is super rewarding. It’s always a pleasure to create meaningful applications, especially when you automate the boring stuff and focus on what matters.

If you want to fork the repo or raise a pull request, go for it. I look at all PRs. Can’t wait to see what you build on top of this.

---

## Key Takeaways

- **Install Postgres locally for quick dev setup; switch to Docker for production.**
- **Always check your API endpoints—POST vs GET matters.**
- **Port conflicts can cause mysterious issues. Double-check what’s running.**
- **Hash and salt all passwords. Never store them in plain text.**
- **Automate admin user creation, but never use default credentials in production.**
- **Keep your repo clean—remove leftover setup files and double-check commits.**

> "It’s not about never making mistakes—it’s about understanding why things break and making sure they don’t break the same way twice."

---
🤔 [Learn more about me on Dev.to](https://dev.to/pierre)
