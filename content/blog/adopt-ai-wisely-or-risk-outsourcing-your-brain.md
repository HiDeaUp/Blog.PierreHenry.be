+++
title = "Adopt AI Wisely or Risk Outsourcing Your Brain"
slug = "adopt-ai-wisely-or-risk-outsourcing-your-brain"
date = "2025-12-30T10:36:47.082175"
draft = false
description = "Let’s get real about using AI in software development. As an AI engineer today, you know the drill: when you prompt and work with large language models, you have to think first—always, always, alwa..."
summary = "Let’s get real about using AI in software development. As an AI engineer today, you know the drill: when you prompt and work with large language models, you have to think first—always, always, alwa..."
tags = ["ai risks", "ai safety", "developer awareness", "large language models", "productivity", "software engineering", "tasks", "tech"]
priority = true
priority_topics = ["tech", "tasks", "productivity"]
original_title = "Hidden AI Risks Every Software Engineer Should Know"
source_medium = "https://medium.com/@phenrysay/4e8e9213dfe3"
+++

![C plus plus code in an coloured editor square strongly foreshortened](https://images.unsplash.com/photo-1568716353609-12ddc5c67f04?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwxfHxBSSUyMHJpc2tzJTIwc29mdHdhcmUlMjBlbmdpbmVlcmluZyUyMGxhcmdlJTIwbGFuZ3VhZ2UlMjBtb2RlbHN8ZW58MHwwfHx8MTc2NzA1MTQwNXww&ixlib=rb-4.1.0&q=80&w=1080 "Adopt AI Wisely or Risk Outsourcing Your Brain")
*Adopt AI Wisely or Risk Outsourcing Your Brain - Photo by [Patrick Martin](https://unsplash.com/@patrickmmartin) on [Unsplash](https://unsplash.com/photos/a-close-up-of-a-computer-screen-with-code-on-it-UMlT0bviaek)*

Let’s get real about using AI in software development. As an AI engineer today, you know the drill: when you prompt and work with large language models, you have to think first—always, always, always. Then, you review your code last. The AI models? You use them only to outsource what needs to be built, not what needs to be thought through.

It’s like being a product owner. You need a clear vision. You know exactly what has to be done. You plan the work, you specify a very clear prototype, you have a solid idea, and then you go from there. You outsource the execution to AI, and then you review everything else. But if you start outsourcing your brain instead, that’s where the problems creep in. Trust me, that’s when things go sideways.

### The Dangers of Blindly Trusting AI

Let’s talk about maintenance. If you ask AI to do everything—say, you have an existing codebase and you just tell it, “Clean up everything, this is a mess”—it will very likely, especially these days (hopefully not in a year or two, but for now), create bugs and problems you didn’t expect. Or it’ll just remove functionalities. I’ve seen a time zone option disappear for no reason. Literally had a similar issue yesterday. So yes, this is still happening now, even with the latest models.

You have to be super careful, super vigilant about what AI does. You don’t want surprises. You want something stable. When AI removes functionalities from your codebase, that can be extremely bad.

Same goes for automation tests. Automation is amazing. But if you ask AI to refactor everything, sometimes it’ll remove some automation tests too. You might believe your automation tests, your end-to-end tests, your whole testing pyramid is safe—but it’s not always the case.

### The Testing Pyramid: Don’t Let AI Knock It Down

Let me break down the testing pyramid for you. Normally, you have:

- Unit tests
- Functional tests
- System tests
- Integration tests
- UAT (User Acceptance Tests)

![An artist’s illustration of artificial intelligence (AI). This illustration depicts language models which generate text. It was created by Wes Cockx as part of the Visualising AI project launched by Google DeepMind.](https://images.unsplash.com/photo-1692607431225-5f4564c8f132?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwyfHxBSSUyMHJpc2tzJTIwc29mdHdhcmUlMjBlbmdpbmVlcmluZyUyMGxhcmdlJTIwbGFuZ3VhZ2UlMjBtb2RlbHN8ZW58MHwwfHx8MTc2NzA1MTQwNXww&ixlib=rb-4.1.0&q=80&w=1080 "Adopt AI Wisely or Risk Outsourcing Your Brain")
*Adopt AI Wisely or Risk Outsourcing Your Brain - Photo by [Google DeepMind](https://unsplash.com/@googledeepmind) on [Unsplash](https://unsplash.com/photos/a-close-up-of-a-piece-of-luggage-with-text-on-it-LuzT78A1g7M)*

UAT is basically what a user would do—clicking buttons, logging in, the whole acceptance flow. For example, with PHP, you might use a framework that’s conceptual for UAT.

If AI updates your code and removes some UAT tests, what’s the point? That’s why it’s crucial to review everything and make sure the behavior is still right.

**Never outsource your brain to AI.** Always think. Always be the master. AI is secondary. AI is the one you outsource the execution to, but not the thinking. That’s the whole difference.

### Trust, But Verify—With AI and With People

It’s easy to trust too much. Same with colleagues. Sometimes we trust someone because we believe they can do it, but everyone has blind spots. We all have days where we’re just not at our best—maybe we’re tired, maybe it’s just a bad day. That’s normal.

That’s why we ask colleagues to review our code and why we carefully test everything. That’s why we have QA automation teams. But if we just trust and don’t check, don’t be surprised if there’s a bug. It’s not magic. If the process isn’t strict enough, things will break. We need to keep everything robust.

### Use AI to Be Better, Not to Think for You

Of course, you have to use AI to be efficient, to be quicker, to be better. But you always need to remember why something has to be built, why you’re doing it, what kind of feature you’re working on. Then, review if what you did is correct before shipping anything to production.

If AI doesn’t work out, try a drastically different approach. It’s the same in life—when something doesn’t work, try something completely different. If you don’t try, you don’t know. Chances are, it’ll work.

Let’s go. Let’s do it. Let’s be better.

![Digital code web source code development. Leica R7 (1994), Summilux-R 1.4 50mm (1983). Hi-Res analog scan by www.totallyinfocus.com – Lomo 200 (expired)](https://images.unsplash.com/photo-1638602612226-55fd638475c9?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwzfHxBSSUyMHJpc2tzJTIwc29mdHdhcmUlMjBlbmdpbmVlcmluZyUyMGxhcmdlJTIwbGFuZ3VhZ2UlMjBtb2RlbHN8ZW58MHwwfHx8MTc2NzA1MTQwNXww&ixlib=rb-4.1.0&q=80&w=1080 "Adopt AI Wisely or Risk Outsourcing Your Brain")
*Adopt AI Wisely or Risk Outsourcing Your Brain - Photo by [Markus Spiske](https://unsplash.com/@markusspiske) on [Unsplash](https://unsplash.com/photos/a-computer-screen-with-a-lot-of-text-on-it-fN6HM1hrgxk)*

---

## Key Takeaways

- **Never outsource your thinking to AI.** Use AI to execute, not to decide.
- Always review AI-generated code, especially after big changes or refactors.
- Be vigilant about lost functionality and missing tests after AI-driven code changes.
- Maintain a strict, robust process—trust, but always verify.
- If something doesn’t work, don’t be afraid to try a completely different approach.

> “AI is the one you outsource the execution to, but not the thinking. That’s the whole difference.”

> “If we just trust and don’t check, don’t be surprised if there’s a bug.”

---

🤔 [Learn more about me on Dev.to](https://dev.to/pierre)

---

#
