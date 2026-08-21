+++
title = "How I Internationalize a Web Product Without a Translation Widget"
slug = "how-i-internationalize-a-web-product-without-a-translation-widget"
date = "2026-08-22T03:30:00+10:00"
draft = false
description = "How I build multilingual web products with stable URLs, translation resources, Intl formatting, language metadata, hreflang, and human review."
summary = "A translation widget does not create a multilingual product. URLs, content, formats, accessibility, and search discovery need one coherent implementation."
tags = ["internationalization", "i18n", "localization", "technical SEO", "accessibility", "web development"]
priority = true
priority_topics = ["tech"]
original_title = "Internationalisez votre site grâce aux outils de Google"
source_01script = "https://01script.com/script-internationalisation-pour-webmasters/"
+++

My original 2010 article recommended several Google tools and a widget that translated a page in the browser. Those services are no longer a sound foundation for a multilingual website.

Visible translation is only one part of the work. An internationalised product needs stable URLs, correct formats, accessible language metadata, and a way for search engines to find every version.

## I Separate Interface Text From Code

I begin by moving interface text out of components. A button should not contain its English or French sentence directly in the implementation.

I give it a stable key such as `account.delete.confirm`, then store a value for each supported language. Keys should describe intent, not screen position. `header.button.2` stops making sense as soon as the interface changes.

Editorial content needs a separate decision. An article, product page, or legal document has its own translation and review cycle. I do not mix that material with short application messages.

This separation also makes missing translations visible during testing instead of hiding them in source files.

## Every Language Gets a Stable URL

Each version needs to be opened, linked, and shared without depending on a cookie:

```text
https://example.com/en/products
https://example.com/fr/produits
```

Google recommends [different URLs for different language versions](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites) and warns against relying only on redirects based on browser language.

I can suggest a likely version on the first visit, but I keep a visible selector and remember the person's choice. A forced redirect becomes frustrating for travellers, translators, and people who prefer a language different from the browser default.

URL design also needs to remain stable. Changing translated slugs in every editorial revision creates redirects and broken links without helping the reader.

## I Declare Language in the Document

An English page should include:

```html
<html lang="en">
```

The [W3C recommends the `lang` attribute](https://www.w3.org/International/questions/qa-html-language-declarations.html) on the `html` element. Screen readers, spelling tools, and other software can then process the text with the correct rules.

If a passage uses another language, I mark that element separately. I also account for `dir="rtl"` when supporting right-to-left writing and test layouts with text longer than the English source.

## I Format Data for the Locale

Internationalisation is not only about words. Dates, numbers, currencies, lists, and plurals vary by locale.

In JavaScript, [`Intl`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Intl) provides browser implementations of those rules:

```js
const amount = new Intl.NumberFormat("fr-FR", {
  style: "currency",
  currency: "EUR",
}).format(1250.5);
```

I store data in a neutral form, then format it for display. I do not store `1 250,50 €` as the value used for calculations.

Language, country, and currency are separate settings. Someone can read French in Australia and pay in Australian dollars. One locale code should not silently decide the entire experience.

## I Connect Localised Pages for Search

When pages are translated equivalents, I add reciprocal `hreflang` links in the HTML or sitemap. [Google's documentation](https://developers.google.com/search/docs/specialty/international/localized-versions) states that each version should reference itself and the corresponding alternatives.

I also check that:

- each page has a title and description in its own language;
- internal links remain in the selected language;
- the canonical points to the correct URL for that version;
- the sitemap contains only real pages;
- an incomplete language does not publish nearly empty pages.

`hreflang` does not repair poor translation. It only connects pages that already exist.

## Machine Translation Is an Input, Not the Release

Machine translation can create a draft, identify forgotten strings, or help a team understand feedback. I do not publish it without review for important content.

Sales pages, legal terms, security messages, and sensitive user journeys need human review. I give the reviewer context for each string, a screenshot of the interface, and any useful length constraint.

I also maintain a glossary. The same concept should use the same term in navigation, help text, and error messages.

## I Test Each Language as a Complete Product

Before release, I go through registration, login, email, errors, payment, and account deletion in every supported language.

I look for untranslated strings, clipped text, ambiguous dates, and links that return to the default language. Where possible, I add these checks to automated tests.

Internationalising a website is not the act of placing a translation button on a page. It means treating content, URLs, formatting, discovery, and maintenance as part of the product.
