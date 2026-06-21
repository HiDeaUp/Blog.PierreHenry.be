+++
title = "How to Stay in Control When Coding With AI Copilot"
slug = "how-to-stay-in-control-when-coding-with-ai-copilot"
date = "2025-12-30T17:22:57.017821"
draft = false
description = "Alright, let’s get straight to it. Today, I want to talk about something that comes up all the time when you’re working with AI code assistants like Copilot. You’re writing code, you hit commit, an..."
summary = "Alright, let’s get straight to it. Today, I want to talk about something that comes up all the time when you’re working with AI code assistants like Copilot. You’re writing code, you hit commit, an..."
tags = ["ai coding assistants", "ai copilot", "code editors", "productivity", "productivity tips", "software development", "tasks", "tech"]
priority = true
priority_topics = ["tech", "tasks", "productivity"]
original_title = "Practical Tips to Use AI Copilot More Effectively in AI Driven Code Editors"
source_medium = "https://medium.com/@phenrysay/748cb389ddc0"
+++

{{< figure src="https://images.unsplash.com/photo-1561886362-a2b38ce83470?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwxfHxBSSUyMENvcGlsb3QlMjBjb2RlJTIwZWRpdG9ycyUyMHByb2R1Y3Rpdml0eSUyMHRpcHN8ZW58MHwwfHx8MTc2NzA3NTc3NXww&ixlib=rb-4.1.0&q=80&w=1080" alt="Macbook pro" title="How to Stay in Control When Coding With AI Copilot" caption="How to Stay in Control When Coding With AI Copilot - Photo by [Alfred Rowe](https://unsplash.com/@nukturnal) on [Unsplash](https://unsplash.com/photos/macbook-pro-w2dWzKL_t5E)" >}}

Alright, let’s get straight to it. Today, I want to talk about something that comes up all the time when you’re working with AI code assistants like Copilot. You’re writing code, you hit commit, and suddenly you’re staring at something weird in your diff. You’re thinking, “Wait, why did Copilot do this? I’m not silly—I’m the pilot here. Copilot is just the co-pilot.” And honestly, that’s exactly the mindset you need.

Let’s say Copilot resets an item count in your code. You might wonder, “Why are we resetting the item count? Do we really need to do that?” Here’s my advice: **never hesitate to ask, to question, and to challenge Copilot.** That’s super important. At the end of the day, you are the pilot. Copilot is your junior engineer, and you’re reviewing their code.

Of course, you want to help each other out, but you should always be thinking: “Why would you do that? Are you sure this is correct?” That’s not just about catching mistakes—it’s the best way to learn. If you just rely on AI and never dig deeper, you’re not going to learn anything. You’ll get bored, and eventually you’ll feel helpless, like all of this is pointless. But it’s not pointless. **Understanding what Copilot does helps you research, improve, and become a better engineer.** That’s the goal.

### Always Question, Always Learn

So, always question. That’s how you get better at what you do. Use AI to be more efficient and to level up, but don’t just accept everything Copilot spits out. Think of it as a conversation between you and Copilot. Ask yourself, “Do we need this?” Because if you just trust Copilot blindly, it’ll add a lot of code—sometimes too much. That’s when problems start. Your codebase becomes unmaintainable, bugs creep in, and you have no idea why. Well, it’s your fault if you didn’t review properly.

{{< figure src="https://images.unsplash.com/photo-1564931768730-7e4d8e240044?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwyfHxBSSUyMENvcGlsb3QlMjBjb2RlJTIwZWRpdG9ycyUyMHByb2R1Y3Rpdml0eSUyMHRpcHN8ZW58MHwwfHx8MTc2NzA3NTc3NXww&ixlib=rb-4.1.0&q=80&w=1080" alt="Debugging is a part of coding" title="How to Stay in Control When Coding With AI Copilot" caption="How to Stay in Control When Coding With AI Copilot - Photo by [Hitesh Choudhary](https://unsplash.com/@hiteshchoudhary) on [Unsplash](https://unsplash.com/photos/code-debug-vy7GOqb1M9s)" >}}

Copilot can also add redundant checks or unnecessary stuff. It’s your job to spot that and prevent it. You can even add rules for this. For example, you have Cursor rules, and you can set up instructions with Copilot in VS Code. Right now, the instructions aren’t as good as Cursor rules, but hopefully that’ll get better soon.

### Practical Example: Reviewing Copilot Suggestions

Let’s say Copilot suggests this:

```javascript
// Copilot adds this line
itemCount = 0;
```

Ask yourself: Do I really need to reset `itemCount` here? What’s the context? Is this introducing a bug or hiding a problem? Don’t just accept it. Sometimes Copilot will add things that seem logical but don’t fit your use case. That’s why you need to review every suggestion, just like you would with a junior developer’s pull request.

### Don’t Let Shortcuts Become Dead Ends

Here’s the thing: using AI is still pretty new. We’ve only had these tools for a few years, and we’re all still figuring out how to use them best. It takes time to adjust. But you want to use the latest and best technology to be quicker and better. Just remember, being quicker without reading or questioning Copilot won’t actually make you faster in the long run. It might feel like it, but eventually, you’ll hit a wall. That’s when the problems start.

{{< figure src="https://images.unsplash.com/photo-1600290239653-029f10d8b38d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwzfHxBSSUyMENvcGlsb3QlMjBjb2RlJTIwZWRpdG9ycyUyMHByb2R1Y3Rpdml0eSUyMHRpcHN8ZW58MHwwfHx8MTc2NzA3NTc3NXww&ixlib=rb-4.1.0&q=80&w=1080" alt="White and black ceramic mug beside black mouse" title="How to Stay in Control When Coding With AI Copilot" caption="How to Stay in Control When Coding With AI Copilot - Photo by [Srijan Tiwari](https://unsplash.com/@srijant) on [Unsplash](https://unsplash.com/photos/white-and-black-ceramic-mug-beside-black-computer-mouse-KUzd9yEFTAs)" >}}

**Don’t take the shortcut that leads to a dead end.** Use the right way, the right path. Step by step, you’ll become a better engineer—a better version of yourself.

---

## Key Takeaways

- **You are the pilot. Copilot is your junior engineer.**
- Always question and review Copilot’s suggestions.
- Use AI to be more efficient, but don’t rely on it blindly.
- Reviewing AI-generated code helps you learn and improve.
- Set up rules and instructions to guide Copilot, but always double-check.
- Don’t take shortcuts that lead to unmaintainable code.
- “Understanding what Copilot does helps you research, improve, and become a better engineer.”
- “Being quicker without reading or questioning Copilot won’t actually make you faster in the long run.”
