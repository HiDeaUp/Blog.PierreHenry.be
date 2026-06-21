+++
title = "How to Write Less Code and Build Better Apps"
slug = "how-to-write-less-code-and-build-better-apps"
date = "2025-12-30T15:57:54.185187"
draft = false
description = "Something I wanted to share is that it's not because it's longer. It's not because you write a huge report. It's not because you code this 1,000 plus lines of code in each file and the function loo..."
summary = "Something I wanted to share is that it's not because it's longer. It's not because you write a huge report. It's not because you code this 1,000 plus lines of code in each file and the function loo..."
tags = ["code efficiency", "occams razor", "problem solving", "productivity", "simplicity", "software development", "tech"]
priority = true
priority_topics = ["tech", "productivity"]
original_title = "The SIMPLER ALWAYS WIN The Occam's Razor Principle"
source_medium = "https://medium.com/@phenrysay/5128ec9c3aa5"
+++

{{< figure src="https://images.unsplash.com/photo-1554306274-f23873d9a26c?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwxfHxPY2NhbXMlMjBSYXpvciUyMHNpbXBsaWNpdHklMjBzb2Z0d2FyZSUyMGRldmVsb3BtZW50fGVufDB8MHx8fDE3NjcwNzA2NzN8MA&ixlib=rb-4.1.0&q=80&w=1080" alt="Turned on macbook pro" title="How to Write Less Code and Build Better Apps" caption="How to Write Less Code and Build Better Apps - Photo by [Safar Safarov](https://unsplash.com/@safarslife) on [Unsplash](https://unsplash.com/photos/turned-on-macbook-pro-LKsHwgzyk7c)" >}}

Something I wanted to share is that it's not because it's longer. It's not because you write a huge report. It's not because you code this 1,000 plus lines of code in each file and the function looks giant. That is better. Of course not. And usually the simpler solution is the ideal one. The ideal one and it's the same for UX. It's the same for an app. It's the same in our day-to-day life. The simpler, the less, it's more.

So when you need to write a report, when you need to write something even for your performance review, what you have done, it's good to summarize. Writing too much, your manager will not read everything, but you have to mention everything you have done. You don't have to end up with 10 or 20 pages because then it will not be great.

And when we have to write code, an application, a program to solve a problem, it's not because it's more complex. It's not because it does so many, it handles so many cases, edge cases that will usually never happen, that it is better. No, the simpler solution is easier to maintain. It's easier to read. It's easier in the longer term. So yes, less is always more.

When we know, finally, that at school we were taught that a longer essay, something longer, when I need to write a capstone, when I need to write a paper, it has to be at least 2,000 words. But in our life as an adult and when we work, we finally realize that the less stories, the better, because people don't have the time to read everything. And complexity, it's very hard to maintain. Complexity will not end up well.

So when you end up with something super simple, very easy to maintain, it's also scalable. So less is always more. Learning how to decrease the complexity, learning how to make it smaller, it's actually something very important. The same when we refactor codebase, not having more code to handle more things. Of course, we do have to handle the things that happen quite often.

## Practical Example: Refactoring for Simplicity

{{< figure src="https://images.unsplash.com/photo-1610986603166-f78428624e76?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwyfHxPY2NhbXMlMjBSYXpvciUyMHNpbXBsaWNpdHklMjBzb2Z0d2FyZSUyMGRldmVsb3BtZW50fGVufDB8MHx8fDE3NjcwNzA2NzN8MA&ixlib=rb-4.1.0&q=80&w=1080" alt="Code example of CSS" title="How to Write Less Code and Build Better Apps" caption="How to Write Less Code and Build Better Apps - Photo by [Ferenc Almasi](https://unsplash.com/@flowforfrank) on [Unsplash](https://unsplash.com/photos/text-NzERTNpnaDw)" >}}

Let me give you a quick code example. Imagine you have a function that checks if a user is allowed to access a resource. The "complex" way might look like this:

```js
function canAccess(user, resource) {
    if (user && user.role) {
        if (user.role === 'admin') {
            return true;
        } else if (user.role === 'editor' && resource.type !== 'restricted') {
            return true;
        } else if (user.role === 'viewer' && resource.type === 'public') {
            return true;
        } else {
            return false;
        }
    } else {
        return false;
    }
}
```

But you can make it much simpler and easier to maintain:

```js
function canAccess(user, resource) {
    if (!user || !user.role) return false;
    if (user.role === 'admin') return true;
    if (user.role === 'editor') return resource.type !== 'restricted';
    if (user.role === 'viewer') return resource.type === 'public';
    return false;
}
```

See? Same logic, but way easier to read and update later. That's what I mean by "simpler always win."

## Why Simplicity Matters

When you keep things simple, you make your life easier. You make your teammates' lives easier. You make your future self's life easier. And honestly, you make your users happier, too. Whether it's code, documentation, or just explaining what you did in a project, less is more.

> "Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away."  
> — Antoine de Saint-Exupéry

{{< figure src="https://images.unsplash.com/photo-1649451844931-57e22fc82de3?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwzfHxPY2NhbXMlMjBSYXpvciUyMHNpbXBsaWNpdHklMjBzb2Z0d2FyZSUyMGRldmVsb3BtZW50fGVufDB8MHx8fDE3NjcwNzA2NzN8MA&ixlib=rb-4.1.0&q=80&w=1080" alt="A screen with a bunch of lines on it" title="How to Write Less Code and Build Better Apps" caption="How to Write Less Code and Build Better Apps - Photo by [Bernd 📷 Dittrich](https://unsplash.com/@hdbernd) on [Unsplash](https://unsplash.com/photos/a-computer-screen-with-a-bunch-of-lines-on-it-aYosQyFcC8k)" >}}

So next time you're tempted to add more, write more, or make something more complicated, ask yourself: can I make this simpler? Can I cut out the noise and just deliver what matters?

## Key Takeaways

- Simpler solutions are easier to maintain, read, and scale.
- Writing more code or longer reports doesn't make your work better.
- Focus on what matters and cut out unnecessary complexity.
- Refactoring is about reducing, not increasing, code.
- "Less is more" applies to code, UX, documentation, and communication.

---

🤔 [Learn more about me on Dev.to](https://dev.to/pierre)
