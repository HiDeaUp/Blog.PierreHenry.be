+++
title = "What Building an Open-Source Dating Platform Taught Me"
slug = "what-building-an-open-source-dating-platform-taught-me"
date = "2026-08-22T03:00:00+10:00"
draft = false
description = "What I learned from building pH7CMS, an open-source dating and social platform, about architecture, trust, maintenance, and product decisions."
summary = "Building pH7CMS taught me that a community platform is not a list of features. Trust, operations, and maintainable boundaries matter as much as the code."
tags = ["open source", "software architecture", "PHP", "dating platforms", "product engineering", "maintainability"]
priority = true
priority_topics = ["tech", "entrepreneurship"]
original_title = "pH7CMS : Le nouveau CMS révolutionnaire !"
source_01script = "https://01script.com/cms-rencontre-open-source-gratuit/"
+++

In 2014, I introduced pH7CMS with a long list of modules: profiles, messaging, geolocation, forums, moderation, internationalisation, and many other features.

That list explained what the software could do. It did not explain what building it taught me.

pH7CMS, now called [pH7Builder](https://github.com/pH7Software/pH7-Social-Dating-CMS), is an open-source PHP project for dating services and online communities. Building it forced me to think beyond one page or one isolated feature.

{{< figure src="/images/blog/ph7cms/ph7cms-2014-interface.webp" alt="pH7CMS registration interface in 2014" title="The pH7CMS Interface in 2014" caption="A pH7CMS interface published with my original article in 2014. The design is dated, but it records a real stage of the project." >}}

## A Platform Is a System of Connected Decisions

A profile does not work on its own. It depends on registration, permissions, search, messages, notifications, blocking, and data deletion.

A local change can therefore affect several other flows. Adding a profile field looks simple until I need to decide who can see it, how it can be searched, how it is translated, whether it appears in an export, and how it is deleted.

This taught me to review complete journeys. I no longer ask only whether a page works. I check what happens before it, after it, and when the user changes their mind.

## A Custom Framework Creates a Long Responsibility

I built pH7Framework for the needs of the CMS. It gave me direct experience with routing, controllers, models, views, caching, and application security.

It also taught me the cost of an internal framework. Every component becomes a maintenance commitment. It needs documentation, compatibility work, tests, upgrades, and security fixes.

Today, I would not build a complete framework by default. I would begin with a maintained framework and add an internal abstraction only for a product-specific need. The experience was valuable, but it made me more careful about code that only a small team knows how to maintain.

## Modules Need Real Boundaries

pH7CMS contained many modules. The number was not the important part. The real test was whether one feature could be disabled without breaking the rest of the application.

A useful module has a clear responsibility, visible dependencies, and a stable interface. If it reads several other modules' tables directly, edits their files, or assumes they are always installed, it is independent in name only.

This lesson applies to a modular monolith and to distributed systems. A technical boundary is useful only when it makes a part of the system easier to understand, test, and replace.

## Trust Is Core Product Work

A dating platform receives photos, private messages, preferences, and sometimes location data. Reporting, blocking, permissions, and moderation are not secondary features.

The system must also account for abuse: fake profiles, spam, harassment, compromised accounts, and third-party data collection. A written rule is not enough. The team needs a review flow, useful evidence, and a way to correct a decision.

I now include security and moderation in the initial design. The [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/) provides a testable base for technical controls. The risks of the specific community need to extend that base.

## Open Source Changes How I Communicate

Publishing code exposes design decisions, inconsistencies, and gaps in documentation. A difficult installation or an implicit convention quickly becomes a contributor problem.

The public repository taught me to write for someone who does not share my context. A clear issue, reproducible steps, and a small contribution can move the project further than a broad discussion.

It also taught me to protect maintenance time. Accepting every request creates a larger product, not necessarily a more useful one. Refusing a feature can be an architecture decision and a product decision at the same time.

## Deployment Is Part of the Product

Self-hosted software does not end at the source code. Installation, configuration, migrations, backups, and upgrades are part of the experience.

A feature that works on my machine but complicates every upgrade is not finished. I now prefer a repeatable setup, explicit dependencies, and a tested upgrade path.

Operations also affect architecture. A background job, media processor, or search service may be technically attractive, but each one adds monitoring, failure states, and recovery work.

## What I Would Do Today

I would begin with a smaller core: accounts, profiles, discovery, messaging, reporting, blocking, and administration. I would test those journeys with one specific community before adding dozens of modules.

I would keep a modular monolith until the team and load justified a more expensive split. I would use maintained components for common infrastructure. I would document decisions about personal data and moderation before the first production release.

Building pH7CMS taught me that a community product is a living system. Code starts the service. Maintenance, trust, and decisions made over several years determine whether it remains useful.
