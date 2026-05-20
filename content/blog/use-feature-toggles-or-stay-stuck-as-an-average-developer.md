+++
title = "Use Feature Toggles or Stay Stuck as an Average Developer"
slug = "use-feature-toggles-or-stay-stuck-as-an-average-developer"
date = "2025-12-14T00:46:10.785088"
draft = false
description = "Let’s talk about something that gets overlooked way too often: how you ship features and handle mistakes in production. I see a lot of teams just rolling with the default, average approach—deploy,..."
summary = "Let’s talk about something that gets overlooked way too often: how you ship features and handle mistakes in production. I see a lot of teams just rolling with the default, average approach—deploy,..."
tags = ["career growth", "development best practices", "feature toggles", "money", "production deployment", "software engineering", "tech"]
priority = true
priority_topics = ["tech", "money"]
original_title = "Stop Being Average #softwareengineerjob"
source_medium = "https://medium.com/@phenrysay/b2a863728edd"
+++

![Photo by Nguyen Dang Hoang Nhu](https://images.unsplash.com/photo-1621036579842-9080c7119f67?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwxfHxzb2Z0d2FyZSUyMGVuZ2luZWVyaW5nJTIwZmVhdHVyZSUyMHRvZ2dsZXMlMjBkZXZlbG9wbWVudCUyMGJlc3QlMjBwcmFjdGljZXN8ZW58MHwwfHx8MTc2NTYzMzU2OXww&ixlib=rb-4.1.0&q=80&w=1080 "Use Feature Toggles or Stay Stuck as an Average Developer")
*Use Feature Toggles or Stay Stuck as an Average Developer - Photo by [Nguyen Dang Hoang Nhu](https://unsplash.com/@nguyendhn) on [Unsplash](https://unsplash.com/photos/boy-in-blue-t-shirt-sitting-on-black-office-rolling-chair-in-front-of-computer-F-5UxARmads)*

Let’s talk about something that gets overlooked way too often: how you ship features and handle mistakes in production. I see a lot of teams just rolling with the default, average approach—deploy, cross your fingers, and if something breaks, scramble to roll back. But there’s a smarter way, and it starts with thinking outside the box.

### Feature Toggles: Your Secret Weapon

Here’s the deal: when you’re shipping a new feature, it shouldn’t be live for everyone right away. It should be encapsulated inside a sandbox, hidden behind a feature toggle. This gives you control. You can move faster, test in production with real data, and if something goes sideways, you just toggle the feature off. No need to roll back the whole deployment.

Why is this better? Imagine you ship Feature A, and right after, someone else ships Feature B. If you have to roll back because of a bug in your code, you might accidentally roll back Feature B too. That’s a mess nobody wants. With feature toggles, you avoid that headache entirely.

Here’s a quick example in pseudo-code:

```python
if feature_toggle_enabled("new_dashboard"):
    render_new_dashboard()
else:
    render_old_dashboard()
```

Simple, right? But it’s powerful. You can ship, test, and iterate without putting everything at risk.

![Photo by Ofspace LLC](https://images.unsplash.com/photo-1681164315430-6159b2361615?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwyfHxzb2Z0d2FyZSUyMGVuZ2luZWVyaW5nJTIwZmVhdHVyZSUyMHRvZ2dsZXMlMjBkZXZlbG9wbWVudCUyMGJlc3QlMjBwcmFjdGljZXN8ZW58MHwwfHx8MTc2NTYzMzU2OXww&ixlib=rb-4.1.0&q=80&w=1080 "Use Feature Toggles or Stay Stuck as an Average Developer")
*Use Feature Toggles or Stay Stuck as an Average Developer - Photo by [Ofspace LLC](https://unsplash.com/@ofspace) on [Unsplash](https://unsplash.com/photos/a-man-sitting-at-a-desk-using-a-computer-5CFy4V-7WzU)*

### The Only Limit Is You

Most people stick to what’s average. They do what everyone else does, and the result is usually mediocre. But when you start asking, “Is there another solution?” you open up a whole new world of possibilities. The only real limit is the one you set in your own head.

I’ve seen teams build extremely scalable software, but it always starts with someone willing to challenge themselves. You have to be eager—not just to learn, but to teach what you learn. That’s how you level up, and that’s how you help your whole team get better.

### Pay It Forward

Here’s something I love: sharing what you’ve learned. Maybe you do it on Fridays, maybe you do it in a Slack channel, whatever works. The point is, you learn something, you teach it, and then someone else teaches you something back. That’s how you create a real community of growth.

**“We are the only limit. The only limit that exists is the one we set in our heads.”**

So next time you’re about to ship something, ask yourself: am I just doing what’s average, or am I finding a better way?

---

![Working on new project on Crumble Office in Prishtina, Kosovo.](https://images.unsplash.com/photo-1517148815978-75f6acaaf32c?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwzfHxzb2Z0d2FyZSUyMGVuZ2luZWVyaW5nJTIwZmVhdHVyZSUyMHRvZ2dsZXMlMjBkZXZlbG9wbWVudCUyMGJlc3QlMjBwcmFjdGljZXN8ZW58MHwwfHx8MTc2NTYzMzU2OXww&ixlib=rb-4.1.0&q=80&w=1080 "Use Feature Toggles or Stay Stuck as an Average Developer")
*Use Feature Toggles or Stay Stuck as an Average Developer - Photo by [Fatos Bytyqi](https://unsplash.com/@fatosi) on [Unsplash](https://unsplash.com/photos/gray-laptop-computer-on-brown-wooden-desk-Agx5_TLsIf4)*

## Key Takeaways

- Use feature toggles to encapsulate new features and avoid risky rollbacks
- Don’t settle for average—challenge yourself to find better solutions
- The only real limit is the one you set for yourself
- Share what you learn and build a culture of teaching and learning

**“We can build amazing, extremely scalable software, but we need to have that eagerness to challenge ourselves and pay it forward.”**

---
🤔 [Learn more about me on Dev.to](https://dev.to/pierre)

---

## Don’t just ship code—ship better ideas.
