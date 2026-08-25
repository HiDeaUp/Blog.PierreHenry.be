+++
title = "Why I Document a Process Before I Automate It"
slug = "why-i-document-a-process-before-i-automate-it"
date = "2017-08-26T10:10:00+02:00"
draft = false
description = "How I observe, simplify, and secure a process before assigning it to software, an AI agent, or another person."
summary = "Automating work that is poorly understood repeats its mistakes faster. A tested procedure reveals the decisions, exceptions, and controls first."
tags = ["automation", "documentation", "operations", "AI agents", "reliability", "delegation"]
priority = true
priority_topics = ["tech", "entrepreneurship"]
original_title = "Automatisez votre Business"
source_01script = "https://01script.com/automatisez-votre-business/"
+++

My original article presented automation as the route to a business that could almost run itself. It also recommended platforms, compensation, and an organization without accounting for law, location, or context. I am removing that advice.

The idea I keep is simpler: before I assign work to software, an AI agent, or another person, I need to explain how that work produces a correct result.

Automating an unclear procedure does not remove its defects. It repeats them faster.

## I Observe the Real Work

I begin by doing the task and recording what actually happens. A procedure imagined away from the work often misses incomplete data, unusual requests, and decisions made without conscious thought.

I document six elements:

1. the trigger;
2. the required inputs;
3. the steps and decisions;
4. the expected output;
5. possible failures;
6. the person responsible for the result.

"Process the refund" is not enough. The procedure needs to explain how to identify the transaction, verify its state, prevent a second refund, record the decision, and inform the customer.

## I Simplify Before Adding a Tool

Some repetitive tasks exist only because two systems request the same information or because an old rule was never questioned.

I first look for work that can be removed, combined, or handled inside the product. The best script for copying data is still less reliable than one source of truth.

I then separate stable rules from decisions that depend on context. A stable rule can be automated. A rare and costly exception often deserves human review.

## I Write a Procedure Another Person Can Execute

A useful procedure contains specific verbs, examples, and a completion condition. It also says what must not happen.

I test it with someone who does not have my context. If they need to ask where to find data, how to choose between two options, or what to do after an error, the documentation is incomplete.

This step is not only for delegation. It turns implicit knowledge into an operational contract that I can translate into code and tests.

## I Choose What Deserves Automation

I prioritize tasks that are frequent, well-defined, and easy to verify. I avoid starting with rare operations that contain many exceptions or can cause damage that is hard to repair.

Automation needs measurable value: fewer errors, a shorter delay, consistent application of a rule, or the removal of repetitive work. Saving a few clicks does not always justify another system to maintain.

The Google SRE chapter on [automation](https://sre.google/sre-book/automation-at-google/) makes an important distinction. Automation can create consistency, but it can also centralize a mistake. Its domain must be defined and controlled.

## I Add Controls Before Automatic Execution

For a task that modifies data or contacts people, I check at least:

- idempotency, so a retry does not create a duplicate;
- a dry-run mode when possible;
- permissions limited to the actual need;
- a volume or rate limit;
- logs connecting the input, decision, and result;
- an alert that explains the problem;
- a method to stop, resume, or reverse the operation.

I also test missing inputs, network delays, and unexpected responses. The happy path proves that the script can work. Failure cases show whether it can be operated.

## I Apply the Same Rule to AI Agents

An agent that can read several tools and perform actions should not receive a vague objective with broad permissions.

I give it a limited scope, identified sources, a result that can be verified, and approval points before important external actions. I keep a record of the tools called and data changed.

If a person cannot explain how to check the result, the agent should not act alone yet.

## I Delegate Responsibility Without Losing Visibility

Delegation does not mean abandoning oversight. I define who decides, who executes, who verifies, and who intervenes after a failure. The person needs the context and authority required for the work, not only a list of clicks.

I retain a few simple measures: volume processed, errors, manual recovery, and completion time. They show whether the process remains useful as the product, team, or constraints change.

The sequence I use is observe, remove unnecessary work, document, test, instrument, then automate or delegate. The preparation takes time, but it prevents local confusion from becoming a recurring problem.
