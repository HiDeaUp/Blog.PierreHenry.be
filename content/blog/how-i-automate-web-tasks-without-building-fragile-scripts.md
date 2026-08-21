+++
title = "How I Automate Web Tasks Without Building Fragile Scripts"
slug = "how-i-automate-web-tasks-without-building-fragile-scripts"
date = "2026-08-21T22:10:00+10:00"
draft = false
description = "How I choose between APIs, Playwright, Selenium, and scheduled jobs when automating repetitive web work without creating a maintenance burden."
summary = "A practical method for automating useful web tasks with resilient locators, limited permissions, clear logs, and a recovery path."
tags = ["automation", "playwright", "selenium", "software testing", "github actions", "web development"]
priority = true
priority_topics = ["tech", "productivity"]
original_title = "Comment automatiser ses tâches Web"
source_01script = "https://01script.com/automatiser-taches-web/"
+++

I wrote the original version of this article around a Firefox extension based on Selenium IDE. The central idea still holds: when I repeat the same browser task, I ask whether a small automation can remove the repetition.

The old tool list no longer helps. The better question is whether the browser should be involved at all.

## I Look for an API First

Clicks are tied to a page. An API is tied to a contract. If a service lets me export a report, create a record, or update data through an API, I normally use it.

I automate the browser when I need to test the path a person actually follows or when no suitable API exists. I also check the service terms before writing the script. Automation does not make fake accounts, unsolicited messages, or limit avoidance acceptable.

This distinction matters because a browser script has more ways to fail. Text changes, a modal appears, authentication expires, or a button moves behind a different state. I accept that cost only when the browser provides evidence or access that I cannot get another way.

## Playwright and Selenium Solve Different Starting Problems

For a new JavaScript or TypeScript project, I often begin with [Playwright](https://playwright.dev/docs/intro). Its locators can target roles, labels, and visible text. It also checks whether an element is ready before acting on it.

[Selenium WebDriver](https://www.selenium.dev/documentation/webdriver/) remains a sound choice for an existing Selenium suite, teams working across several programming languages, or infrastructure already built around Selenium Grid. Selenium IDE can still record a first scenario, but I treat the recording as a draft. The final automation belongs in readable, reviewed code.

## A Small Playwright Example

This test exports a report from a test environment:

```ts
import { test, expect } from "@playwright/test";

test("exports a report", async ({ page }) => {
  await page.goto(process.env.APP_URL!);

  await page.getByLabel("Email address").fill(process.env.TEST_EMAIL!);
  await page.getByLabel("Password").fill(process.env.TEST_PASSWORD!);
  await page.getByRole("button", { name: "Sign in" }).click();

  await expect(page.getByRole("heading", { name: "Reports" })).toBeVisible();

  const download = page.waitForEvent("download");
  await page.getByRole("button", { name: "Export" }).click();
  await download;
});
```

I do not target "the third button" or copy a long CSS path from the browser inspector. I target the control as a user understands it. The [Playwright locator guide](https://playwright.dev/docs/locators) recommends the same preference for user-facing attributes and explicit contracts.

Credentials stay in a secret store. The test account receives only the permissions required for this scenario.

## Scheduling Is the Easy Part

A test can run on every pull request. A business task may run on a schedule. In both cases, I want the code to be safe when it runs twice.

[GitHub Actions workflows](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows) can run on repository events, manually, or on a schedule. For an important job, I keep a manual trigger as a recovery option and record enough context to understand every run:

- when it started and finished;
- which input it processed;
- what output it produced;
- whether a retry occurred;
- why it failed.

I also define an owner. A scheduled script without an owner becomes a hidden service that everyone depends on and nobody maintains.

## My Release Checklist for an Automation

Before letting a task run unattended, I verify that:

1. a retry will not create an unwanted duplicate;
2. a changed page causes a clear failure rather than a wrong action;
3. permissions and secrets are limited;
4. logs explain the result without exposing sensitive data;
5. someone can stop, inspect, and resume the job;
6. the automation saves more time than it consumes in maintenance.

The first recording rarely creates the real value. The value comes from a small script that another engineer can read, test, and repair without guessing what I intended.
