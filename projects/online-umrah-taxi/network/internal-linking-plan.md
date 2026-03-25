# Internal Linking Plan — Online Umrah Taxi

**Version 2.0** | February 2026 | 68 pages | Hub/Spoke Architecture

---

## Architecture Overview

The site follows a strict 4-level hub/spoke model. No page is more than 3 clicks from the homepage. Every route page is accessible from 2 hub pages minimum. Every outer page links back to at least 2 core pages.

```text
Level 0 — Homepage (/)
Level 1 — Master hub (/umrah-taxi-services) + city pages
Level 2 — Section hubs (airport / intercity / ziyarah / fleet / group)
Level 3 — Route, segment, and ziyarah spoke pages
Level 4 — Outer pages (guides, comparisons, legal)
```

---

## Level 0 — Homepage

**Page:** `/`

**Links out to (required):**

| Anchor text | Destination |
| ----------- | ----------- |
| Umrah Taxi Services | `/umrah-taxi-services` |
| Jeddah Airport to Makkah Taxi | `/jeddah-airport-to-makkah-taxi` |
| Makkah to Madinah Taxi | `/makkah-to-madinah-taxi` |
| Pricing & Packages | `/pricing` |
| Group & Family Packages | `/group-family-packages` |
| Female-Friendly Umrah Taxi | `/female-friendly-umrah-taxi` |
| About Us | `/about-us` |
| Contact Us | `/contact-us` |

**Receives links from:**

- All Level 2 hubs via breadcrumb (position 1)
- All Level 3 spoke pages via breadcrumb (position 1)

---

## Level 1 — Master Services Hub

**Page:** `/umrah-taxi-services`

**Links out to (required):**

| Anchor text | Destination |
| ----------- | ----------- |
| Airport Transfers | `/airport-transfers` |
| Inter-City Transfers | `/inter-city-transfers` |
| Ziyarah Tours | `/ziyarah-tours` |
| Vehicle Fleet | `/vehicle-fleet` |
| Group & Family Packages | `/group-family-packages` |
| Pricing & Packages | `/pricing` |

**Receives links from:**

- Homepage (main nav + body)
- All section hubs (breadcrumb position 2 or parent link)
- All city pages (contextual body link)

---

## Level 1 — City Pages

Each city page is linked from the homepage footer and from every route page where that city is the origin or destination.

### `/umrah-taxi-makkah`

**Links out to:**

| Anchor text | Destination |
| ----------- | ----------- |
| Jeddah Airport to Makkah Taxi | `/jeddah-airport-to-makkah-taxi` |
| Madinah Airport to Makkah Taxi | `/madinah-airport-to-makkah-taxi` |
| Riyadh Airport to Makkah Taxi | `/riyadh-airport-to-makkah-taxi` |
| Makkah to Madinah Taxi | `/makkah-to-madinah-taxi` |
| Makkah to Taif Taxi | `/makkah-to-taif-taxi` |
| Makkah Ziyarah Taxi Tours | `/makkah-ziyarah-taxi-tours` |
| Pricing & Packages | `/pricing` |
| Contact Us | `/contact-us` |

**Receives links from:** All pages where Makkah is origin or destination (route pages + ziyarah Makkah)

---

### `/umrah-taxi-madinah`

**Links out to:**

| Anchor text | Destination |
| ----------- | ----------- |
| Jeddah Airport to Madinah Taxi | `/jeddah-airport-to-madinah-taxi` |
| Madinah Airport to Madinah City Taxi | `/madinah-airport-to-madinah-taxi` |
| Riyadh Airport to Madinah Taxi | `/riyadh-airport-to-madinah-taxi` |
| Makkah to Madinah Taxi | `/makkah-to-madinah-taxi` |
| Madinah to Makkah Taxi | `/madinah-to-makkah-taxi` |
| Madinah Ziyarah Taxi Tours | `/madinah-ziyarah-taxi-tours` |
| Pricing & Packages | `/pricing` |
| Contact Us | `/contact-us` |

---

### `/umrah-taxi-jeddah`

**Links out to:**

| Anchor text | Destination |
| ----------- | ----------- |
| Jeddah Airport to Makkah Taxi | `/jeddah-airport-to-makkah-taxi` |
| Jeddah Airport to Madinah Taxi | `/jeddah-airport-to-madinah-taxi` |
| Jeddah Airport to Taif Taxi | `/jeddah-airport-to-taif-taxi` |
| Jeddah Airport to Riyadh Taxi | `/jeddah-airport-to-riyadh-taxi` |
| Jeddah Ziyarah Taxi | `/jeddah-ziyarah-taxi` |
| Airport Transfers | `/airport-transfers` |
| Contact Us | `/contact-us` |

---

### `/umrah-taxi-taif`

**Links out to:**

| Anchor text | Destination |
| ----------- | ----------- |
| Jeddah Airport to Taif Taxi | `/jeddah-airport-to-taif-taxi` |
| Makkah to Taif Taxi | `/makkah-to-taif-taxi` |
| Taif to Makkah Taxi | `/taif-to-makkah-taxi` |
| Madinah to Taif Taxi | `/madinah-to-taif-taxi` |
| Taif Ziyarah Taxi | `/taif-ziyarah-taxi` |
| Pricing & Packages | `/pricing` |
| Contact Us | `/contact-us` |

---

### `/umrah-taxi-riyadh`

**Links out to:**

| Anchor text | Destination |
| ----------- | ----------- |
| Riyadh Airport to Makkah Taxi | `/riyadh-airport-to-makkah-taxi` |
| Riyadh Airport to Madinah Taxi | `/riyadh-airport-to-madinah-taxi` |
| Riyadh to Makkah Taxi | `/riyadh-to-makkah-taxi` |
| Riyadh to Madinah Taxi | `/riyadh-to-madinah-taxi` |
| Riyadh to Taif Taxi | `/riyadh-to-taif-taxi` |
| Riyadh Ziyarah Taxi | `/riyadh-ziyarah-taxi` |
| Contact Us | `/contact-us` |

---

## Level 2 — Airport Transfers Hub

**Page:** `/airport-transfers`

**Links out to (all 8 airport route spokes):**

| Anchor text | Destination |
| ----------- | ----------- |
| Jeddah Airport to Makkah Taxi | `/jeddah-airport-to-makkah-taxi` |
| Jeddah Airport to Madinah Taxi | `/jeddah-airport-to-madinah-taxi` |
| Madinah Airport to Makkah Taxi | `/madinah-airport-to-makkah-taxi` |
| Madinah Airport to Madinah City Taxi | `/madinah-airport-to-madinah-taxi` |
| Riyadh Airport to Makkah Taxi | `/riyadh-airport-to-makkah-taxi` |
| Riyadh Airport to Madinah Taxi | `/riyadh-airport-to-madinah-taxi` |
| Jeddah Airport to Taif Taxi | `/jeddah-airport-to-taif-taxi` |
| Jeddah Airport to Riyadh Taxi | `/jeddah-airport-to-riyadh-taxi` |
| How Airport Pickup Works | `/how-to-book-umrah-taxi-online` |
| Pricing & Packages | `/pricing` |

**Receives links from:** Homepage, /umrah-taxi-services, all 8 airport route pages (parent reference)

---

## Level 2 — Inter-City Transfers Hub

**Page:** `/inter-city-transfers`

**Links out to (all 10 intercity route spokes):**

| Anchor text | Destination |
| ----------- | ----------- |
| Makkah to Madinah Taxi | `/makkah-to-madinah-taxi` |
| Madinah to Makkah Taxi | `/madinah-to-makkah-taxi` |
| Makkah to Taif Taxi | `/makkah-to-taif-taxi` |
| Taif to Makkah Taxi | `/taif-to-makkah-taxi` |
| Makkah to Riyadh Taxi | `/makkah-to-riyadh-taxi` |
| Riyadh to Makkah Taxi | `/riyadh-to-makkah-taxi` |
| Madinah to Taif Taxi | `/madinah-to-taif-taxi` |
| Taif to Madinah Taxi | `/taif-to-madinah-taxi` |
| Riyadh to Madinah Taxi | `/riyadh-to-madinah-taxi` |
| Riyadh to Taif Taxi | `/riyadh-to-taif-taxi` |
| Pricing & Packages | `/pricing` |

**Receives links from:** Homepage, /umrah-taxi-services, all 10 intercity route pages

---

## Level 2 — Ziyarah Tours Hub

**Page:** `/ziyarah-tours`

**Links out to (all 8 ziyarah spokes):**

| Anchor text | Destination |
| ----------- | ----------- |
| Makkah Ziyarah Taxi Tours | `/makkah-ziyarah-taxi-tours` |
| Madinah Ziyarah Taxi Tours | `/madinah-ziyarah-taxi-tours` |
| Full Makkah–Madinah Ziyarah Package | `/full-makkah-madinah-ziyarah-package` |
| Jeddah Ziyarah Taxi | `/jeddah-ziyarah-taxi` |
| Taif Ziyarah Taxi | `/taif-ziyarah-taxi` |
| Riyadh Ziyarah Taxi | `/riyadh-ziyarah-taxi` |
| Private Ziyarah Taxi Package | `/private-ziyarah-taxi-package` |
| Group Ziyarah Taxi | `/group-ziyarah-taxi` |
| Pricing & Packages | `/pricing` |

**Receives links from:** Homepage, /umrah-taxi-services, all 8 ziyarah pages

---

## Level 2 — Vehicle Fleet Hub

**Page:** `/vehicle-fleet`

**Links out to (all 5 segment spokes + pricing):**

| Anchor text | Destination |
| ----------- | ----------- |
| Family Umrah Taxi | `/family-umrah-taxi` |
| Group Umrah Taxi (10+ Persons) | `/group-umrah-taxi-10-persons` |
| Female-Friendly Umrah Taxi | `/female-friendly-umrah-taxi` |
| Luxury Umrah Taxi | `/luxury-umrah-taxi` |
| Economy Umrah Taxi | `/economy-umrah-taxi` |
| Pricing & Packages | `/pricing` |

**Receives links from:** Homepage, /umrah-taxi-services, all segment pages, all route pages (via vehicle fit section)

---

## Level 2 — Group & Family Packages Hub

**Page:** `/group-family-packages`

**Links out to:**

| Anchor text | Destination |
| ----------- | ----------- |
| Group Umrah Taxi (10+ Persons) | `/group-umrah-taxi-10-persons` |
| Group Ziyarah Taxi | `/group-ziyarah-taxi` |
| Family Umrah Taxi | `/family-umrah-taxi` |
| Vehicle Fleet | `/vehicle-fleet` |
| Pricing & Packages | `/pricing` |
| Contact Us | `/contact-us` |

---

## Level 3 — Airport Transfer Spoke Pages

### Link rules for all 8 airport route pages

Every airport route page **must** link to:

1. `/airport-transfers` — parent hub (anchor: "Airport Transfers")
2. `/pricing` — pricing CTA (anchor: "Umrah taxi pricing")
3. `/vehicle-fleet` — vehicle fit context (anchor: "vehicle fleet and capacity")
4. Origin city page — e.g., `/umrah-taxi-jeddah` (anchor: city name + "Umrah taxi")
5. Destination city page — e.g., `/umrah-taxi-makkah` (anchor: city name + "Umrah taxi")
6. `/contact-us` — booking CTA (varied anchor — see anchor rotation table)

**Sibling cross-links (required where journey logic applies):**

| Route page | Cross-link to | Anchor text |
| ---------- | ------------- | ----------- |
| `/jeddah-airport-to-makkah-taxi` | `/makkah-to-madinah-taxi` | continue to Madinah by taxi |
| `/jeddah-airport-to-madinah-taxi` | `/madinah-ziyarah-taxi-tours` | Madinah Ziyarah taxi tours |
| `/madinah-airport-to-makkah-taxi` | `/meeqat-ihram-transfer-guide` | Miqat stop on the way to Makkah |
| `/madinah-airport-to-madinah-taxi` | `/madinah-to-makkah-taxi` | Madinah to Makkah taxi |
| `/riyadh-airport-to-makkah-taxi` | `/makkah-ziyarah-taxi-tours` | Makkah Ziyarah tours |
| `/jeddah-airport-to-makkah-taxi` | `/female-friendly-umrah-taxi` | female-friendly Umrah taxi |

---

## Level 3 — Inter-City Transfer Spoke Pages

### Link rules for all 10 intercity route pages

Every intercity route page **must** link to:

1. `/inter-city-transfers` — parent hub (anchor: "Inter-City Transfers")
2. `/pricing` — pricing CTA (anchor: "intercity taxi pricing")
3. `/vehicle-fleet` — vehicle fit (anchor: "vehicle capacity and fleet")
4. Origin city page (anchor: city name + "Umrah taxi")
5. Destination city page (anchor: city name + "Umrah taxi")
6. `/contact-us` — booking CTA (varied anchor)

**Route-pair cross-links (mandatory for reverse-route pairs):**

| Route page | Must link to reverse | Anchor text |
| ---------- | -------------------- | ----------- |
| `/makkah-to-madinah-taxi` | `/madinah-to-makkah-taxi` | Madinah to Makkah taxi |
| `/madinah-to-makkah-taxi` | `/makkah-to-madinah-taxi` | Makkah to Madinah taxi |
| `/makkah-to-taif-taxi` | `/taif-to-makkah-taxi` | Taif to Makkah taxi |
| `/taif-to-makkah-taxi` | `/makkah-to-taif-taxi` | Makkah to Taif taxi |
| `/makkah-to-riyadh-taxi` | `/riyadh-to-makkah-taxi` | Riyadh to Makkah taxi |
| `/riyadh-to-makkah-taxi` | `/makkah-to-riyadh-taxi` | Makkah to Riyadh taxi |
| `/madinah-to-taif-taxi` | `/taif-to-madinah-taxi` | Taif to Madinah taxi |
| `/taif-to-madinah-taxi` | `/madinah-to-taif-taxi` | Madinah to Taif taxi |
| `/riyadh-to-madinah-taxi` | `/riyadh-to-taif-taxi` | Riyadh to Taif taxi |
| `/riyadh-to-taif-taxi` | `/riyadh-to-madinah-taxi` | Riyadh to Madinah taxi |

**Journey continuation cross-links:**

| From | To | Anchor text |
| ---- | -- | ----------- |
| `/makkah-to-madinah-taxi` | `/madinah-ziyarah-taxi-tours` | Madinah Ziyarah taxi tours |
| `/madinah-to-makkah-taxi` | `/makkah-ziyarah-taxi-tours` | Makkah Ziyarah taxi tours |
| `/makkah-to-madinah-taxi` | `/meeqat-ihram-transfer-guide` | Miqat stop before Madinah |
| `/makkah-to-taif-taxi` | `/taif-ziyarah-taxi` | Taif Ziyarah taxi tours |
| `/riyadh-to-makkah-taxi` | `/group-umrah-taxi-10-persons` | group Umrah taxi for large parties |

---

## Level 3 — Ziyarah Tour Spoke Pages

### Link rules for all 8 ziyarah pages

Every ziyarah page **must** link to:

1. `/ziyarah-tours` — parent hub (anchor: "Ziyarah Tours")
2. `/pricing` — pricing CTA
3. The city page matching the ziyarah city (e.g., `/umrah-taxi-makkah`)
4. The relevant arrival route (e.g., `/jeddah-airport-to-makkah-taxi` for Makkah ziyarah pages)
5. `/contact-us` — booking CTA

**Ziyarah cross-links:**

| Ziyarah page | Cross-links to |
| ------------ | -------------- |
| `/makkah-ziyarah-taxi-tours` | `/full-makkah-madinah-ziyarah-package`, `/private-ziyarah-taxi-package` |
| `/madinah-ziyarah-taxi-tours` | `/full-makkah-madinah-ziyarah-package`, `/group-ziyarah-taxi` |
| `/full-makkah-madinah-ziyarah-package` | `/makkah-ziyarah-taxi-tours`, `/madinah-ziyarah-taxi-tours`, `/makkah-to-madinah-taxi` |
| `/group-ziyarah-taxi` | `/group-umrah-taxi-10-persons`, `/group-family-packages` |
| `/private-ziyarah-taxi-package` | `/luxury-umrah-taxi`, `/vehicle-fleet` |

---

## Level 3 — Vehicle & Segment Pages

### Link rules for all 5 audience segment pages

Every segment page **must** link to:

1. `/vehicle-fleet` — parent hub (anchor: "Umrah taxi vehicle fleet")
2. `/pricing` — pricing CTA
3. The primary route this segment uses most (e.g., `/jeddah-airport-to-makkah-taxi` for family/women pages)
4. `/contact-us` — booking CTA

**Segment-specific cross-links:**

| Segment page | Cross-links to | Anchor text |
| ------------ | -------------- | ----------- |
| `/family-umrah-taxi` | `/group-family-packages` | group and family packages |
| `/family-umrah-taxi` | `/elderly-umrah-taxi-guide` | elderly and mobility support |
| `/group-umrah-taxi-10-persons` | `/group-family-packages`, `/group-ziyarah-taxi` | group Ziyarah taxi |
| `/female-friendly-umrah-taxi` | `/women-umrah-taxi-guide` | Women's Umrah taxi guide |
| `/luxury-umrah-taxi` | `/private-ziyarah-taxi-package` | private Ziyarah taxi package |
| `/economy-umrah-taxi` | `/pricing` | economy Umrah taxi pricing |

---

## Level 4 — Outer Pages

### 4.1 Pilgrim Guide link rules (12 pages)

Every outer guide page **must** link to at least 2 core money pages contextually. Outer pages do **not** appear in the main nav.

| Outer page | Required core links | Anchor text examples |
| ---------- | ------------------- | -------------------- |
| `/umrah-season-2026-guide` | `/airport-transfers`, `/inter-city-transfers` | airport transfer booking, intercity taxi for Umrah season |
| `/hajj-2026-taxi-guide` | `/airport-transfers`, `/group-family-packages` | Hajj airport transfers, group Hajj taxi |
| `/pilgrim-tips-for-pakistani-umrah` | `/jeddah-airport-to-makkah-taxi`, `/contact-us` | Jeddah airport to Makkah taxi booking |
| `/how-to-book-umrah-taxi-online` | `/contact-us`, `/pricing` | Umrah taxi pricing, WhatsApp booking |
| `/meeqat-ihram-transfer-guide` | `/jeddah-airport-to-makkah-taxi`, `/madinah-to-makkah-taxi` | Jeddah airport to Makkah taxi, Madinah to Makkah route |
| `/heat-safety-for-pilgrims-2026` | `/vehicle-fleet`, `/contact-us` | air-conditioned Umrah taxi fleet |
| `/umrah-visa-taxi-guide` | `/airport-transfers`, `/jeddah-airport-to-makkah-taxi` | airport transfer on arrival, Jeddah Airport to Makkah |
| `/women-umrah-taxi-guide` | `/female-friendly-umrah-taxi`, `/contact-us` | female-friendly Umrah taxi, book via WhatsApp |
| `/elderly-umrah-taxi-guide` | `/family-umrah-taxi`, `/vehicle-fleet` | family Umrah taxi with assistance, Hiace van capacity |
| `/group-umrah-taxi-guide` | `/group-umrah-taxi-10-persons`, `/group-family-packages` | group Umrah taxi for 10+, group package pricing |
| `/prayer-times-taxi-schedule` | `/makkah-to-madinah-taxi`, `/contact-us` | Makkah to Madinah taxi schedule |
| `/umrah-taxi-booking-tips-2026` | `/pricing`, `/how-to-book-umrah-taxi-online` | Umrah taxi pricing, how to book Umrah taxi |

---

### 4.2 Comparison & Trust page link rules (4 pages)

| Outer page | Required core links | Anchor text examples |
| ---------- | ------------------- | -------------------- |
| `/umrah-taxi-vs-careem-uber` | `/umrah-taxi-services`, `/pricing` | private Umrah taxi service, fixed Umrah taxi prices |
| `/why-choose-online-umrah-taxi` | `/umrah-taxi-services`, `/contact-us` | book an Umrah taxi, all Umrah taxi services |
| `/umrah-taxi-testimonials` | `/contact-us`, `/pricing` | book your Umrah taxi |
| `/pakistani-pilgrim-umrah-taxi-stories` | `/jeddah-airport-to-makkah-taxi`, `/contact-us` | Jeddah Airport to Makkah taxi |

---

### 4.3 About & Legal page link rules (8 pages)

| Page | Links to |
| ---- | -------- |
| `/about-us` | `/umrah-taxi-services`, `/contact-us`, `/saudi-transport-license` |
| `/contact-us` | `/pricing`, `/how-to-book-umrah-taxi-online`, `/faq` |
| `/privacy-policy` | `/contact-us`, `/terms-and-conditions` |
| `/terms-and-conditions` | `/contact-us`, `/pricing`, `/cancellation-policy section in pricing` |
| `/saudi-transport-license` | `/about-us`, `/fleet-safety-standards`, `/umrah-taxi-services` |
| `/fleet-safety-standards` | `/vehicle-fleet`, `/about-us`, `/saudi-transport-license` |
| `/careers` | `/about-us`, `/contact-us` |
| `/faq` | `/pricing`, `/airport-transfers`, `/inter-city-transfers`, `/contact-us` |

---

## Global Link Rules (apply sitewide)

### 1 — Booking CTA placement

Every money page (route, segment, ziyarah) must have a booking CTA:

- **First CTA:** Above the fold (within first 150 words) — links to `/contact-us`
- **Second CTA:** Within or immediately after the price table
- **Third CTA:** At the end of the page (conclusion paragraph)

CTA anchors must rotate. Never use the same anchor text twice on the same page.

### 2 — Anchor text rotation table (booking CTAs)

Use different anchors across pages and within pages. Do not repeat the same anchor on the same page.

| Anchor variant | Use context |
| -------------- | ----------- |
| book your Umrah taxi | Generic CTA — open of page |
| check Umrah taxi availability | Near price table |
| WhatsApp to confirm your booking | WhatsApp-specific CTA |
| get a fixed-price quote | Mid-page inquiry CTA |
| book airport pickup for your group | Group-context CTA |
| reserve your transfer now | Near-journey CTA |

### 3 — Pricing link rule

Every route page and segment page must include at least one contextual link to `/pricing` using a varied anchor:

- "full Umrah taxi pricing"
- "Umrah taxi price list for all routes"
- "pricing by vehicle type"

### 4 — Fleet link rule

Route pages must link to `/vehicle-fleet` in the vehicle selection section using:

- "vehicle fleet and capacity"
- "sedan, SUV, and van options"
- "Hiace van for 7–9 passengers"

### 5 — No orphan pages

Every page must receive at least one incoming internal link from a hub or sibling before it is published. Validate with `/internal-linking-gap-finder` agent before deployment.

### 6 — Breadcrumb consistency

All pages must implement BreadcrumbList schema consistent with the page's URL hierarchy:

- Route pages: Home → Section Hub → Route Page
- Segment pages: Home → Vehicle Fleet → Segment Page
- Ziyarah pages: Home → Ziyarah Tours → Page
- City pages: Home → City Page
- Outer pages: Home → Page

### 7 — First-occurrence rule

Link a phrase on its first occurrence per page only. Do not link the same destination multiple times on the same page (except explicit CTA buttons which are supplementary to contextual links).

### 8 — Canonical protection

Each route has exactly one canonical page. Reverse-direction routes are separate pages (Makkah→Madinah ≠ Madinah→Makkah) but must cross-link to each other. No thin pages — every route page must carry unique EAV triples specific to that direction's pickup logistics.

---

## Internal Link Count Targets (per page type)

| Page type | Min outgoing links | Min incoming links |
| --------- | ------------------ | ------------------ |
| Homepage | 8 | All hubs + key routes |
| Master hub | 6 | Homepage + all section hubs |
| Section hub | 10–12 | Homepage, master hub, all spokes |
| Route page (airport) | 6–8 | Parent hub + city pages + siblings |
| Route page (intercity) | 7–9 | Parent hub + reverse pair + city pages |
| Ziyarah page | 5–7 | Ziyarah hub + city + arrival route |
| Segment page | 5–7 | Fleet hub + related routes + group hub |
| City page | 6–8 | Homepage + all routes to/from that city |
| Outer guide | 3–5 | Topically related outer pages only |
| About/legal | 3–5 | About Us + contact + related legal |

---

## Validation Checklist (run before each deploy batch)

- [ ] Every page in the batch has at least 1 incoming link from an already-published page
- [ ] No anchor text is used more than once on the same page
- [ ] Every route page links to its parent section hub
- [ ] Every outer page links to at least 2 core money pages
- [ ] BreadcrumbList schema matches the actual URL path
- [ ] Pricing page is linked from every money page at least once
- [ ] Contact Us is linked from every money page at least once
