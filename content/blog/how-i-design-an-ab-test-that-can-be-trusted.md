+++
title = "How I Design an A/B Test That Can Be Trusted"
slug = "how-i-design-an-ab-test-that-can-be-trusted"
date = "2015-02-17T08:28:00+01:00"
draft = false
description = "How I define a hypothesis, assign stable cohorts, and measure real exposure before using the result of an A/B test."
summary = "Showing a different page on each day is not a reliable A/B test. Cohorts, metrics, and stopping rules need to exist before launch."
tags = ["product experiments", "experimentation", "product", "analytics", "TypeScript", "SEO"]
priority = true
priority_topics = ["tech", "entrepreneurship"]
original_title = "Afficher aléatoirement une page Wordpress - Split Testing"
source_01script = "https://01script.com/page-aleatoire-wordpress-split-testing/"
+++

In my 2015 article, I proposed showing a different page on each day of the week. The mechanism alternated between two pages, but it did not produce a reliable comparison.

Tuesday's audience may differ from Sunday's audience. A campaign, news event, or price change may also affect the result. The variation is then mixed with time.

I would now build the test around a hypothesis, stable cohorts, and events measured in the same way.

## I Write the Hypothesis Before the Code

I use a statement that can be tested:

> For new visitors to the pricing page, explaining the trial limit next to the button will increase trial creation without increasing early cancellations.

This identifies the audience, change, primary metric, and a risk to monitor.

I change one important decision at a time. If the text, price, layout, and flow all change together, the result cannot explain what mattered.

## I Keep Each Person in the Same Cohort

Someone should not see version A in the morning and version B that evening. I use an account identifier when they are signed in. For a public flow, I can use an anonymous experiment identifier managed under the site's consent and privacy rules.

Assignment needs to be deterministic. This is a small TypeScript example:

```ts
type Variant = "control" | "variant";

export function assignVariant(
  experimentId: string,
  subjectId: string,
): Variant {
  const value = `${experimentId}:${subjectId}`;
  let hash = 2166136261;

  for (const character of value) {
    hash ^= character.codePointAt(0) ?? 0;
    hash = Math.imul(hash, 16777619);
  }

  return (hash >>> 0) % 2 === 0 ? "control" : "variant";
}
```

This function is not a security mechanism. It only keeps the same subject in the same variant while the experiment identifier remains unchanged.

## I Measure Exposure, Not Only Assignment

I do not record exposure when the server chooses a variant. The person may leave before seeing the tested element.

The exposure event is sent when the element becomes visible or usable. It includes the experiment identifier, variant, and the pseudonymous subject expected by the measurement system.

The conversion event needs the same dimensions. Without that connection, I may count conversions from people who never saw the test.

## I Define the Metrics Before Launch

I select one primary metric that matches the hypothesis. I add a small number of guardrails such as errors, flow abandonment, refunds, or another important product consequence.

I define exclusions too. Internal accounts, automated tests, and people exposed to an earlier version can distort the comparison.

The required duration and volume depend on traffic and conversion rate. I do not declare a win after a few favorable results. I define the analysis method and stopping rule before checking daily variation.

## I Protect Search Behavior on Public Pages

For a test using multiple URLs, Google recommends a canonical URL pointing to the original page and a temporary `302` redirect instead of a permanent `301`. The site must not give Googlebot one version and people another.

The [Google Search documentation for website tests](https://developers.google.com/search/docs/crawling-indexing/website-testing?hl=en) also recommends removing test URLs, scripts, and markup after the experiment ends.

## I Plan the End Before the Start

An experiment needs an owner, a review date, and an available decision: retain the control, adopt the variant, continue under the predefined rule, or stop because of a risk.

I then remove the experiment code. A winning variant should not remain hidden behind a forgotten flag for years.

A useful A/B test is not just a changing page. It isolates a decision, keeps comparable cohorts, and measures a result the team can use.
