# HCU Quality Audit — Online Umrah Taxi
**Date:** February 2026 | **Auditor:** koray-auditor-agent
**Scoring:** 0–100. Ship-ready threshold: ≥ 80.

---

## Scoring Rubric (applies to all pages)

| Component | Max points | Weight |
| --------- | ---------- | ------ |
| Task completion (user can act after reading) | 25 | 25% |
| E-E-A-T signals (trust, identity, claims sourced) | 20 | 20% |
| Content integrity (no overpromises, numeric precision) | 15 | 15% |
| Koray writing rules compliance (42 rules) | 15 | 15% |
| Conversion UX (CTA placement, booking clarity) | 10 | 10% |
| Internal linking (hub/spoke compliance) | 10 | 10% |
| Structured data readiness (schema defined) | 5 | 5% |

---

## Page 00 — Main Service Page

**HCU Score: 87 / 100 ✅ SHIP-READY**

| Component | Score | Notes |
| --------- | ----- | ----- |
| Task completion | 23/25 | Answers: Can I book? How? What happens next? Pricing table present. Missing: explicit confirmation of what the pilgrim receives after booking (a WhatsApp message? Email? PDF?) |
| E-E-A-T signals | 17/20 | MOT permit mention, 24/7 availability, driver language coverage. Missing: company founding year, physical address, number of completed journeys |
| Content integrity | 14/15 | All prices sourced to Feb 2026 market data. Travel times sourced to Saudi road data. No overpromises. Minor: "fastest route" language absent (good). One phrase to fix: "confirmation within 15 minutes" — qualify as "during business hours (06:00–22:00 AST)" |
| Koray rules | 13/15 | Answer-first H1 ✓, EAV triples ✓, source context on prices ✓, no negative phrases ✓, entity in subject position ✓. Tables have purpose ✓. Lists < 7 items ✓. Missing: H2 headings should more precisely match query intent ("Airport Transfers" → "Private Airport Transfers from JED, MED, and RUH") |
| Conversion UX | 9/10 | CTA above fold ✓, WhatsApp + form both present ✓, booking fields listed ✓. Minor: WhatsApp number is placeholder [+966 XXX XXXX] — must be filled before launch |
| Internal linking | 8/10 | Links to /booking/, /pricing/, /fleet/, /intercity-transfers/, /airport-transfers/, /trust-and-policies/ ✓. Missing outbound link to /ziyarat/ hub from Ziyarat section |
| Schema readiness | 4/5 | LocalBusiness + FAQPage called for in brief ✓. FAQ questions are in the page ✓. Schema JSON not yet generated |

**Priority fixes before launch:**
1. Fill placeholder WhatsApp number
2. Add company founding year and journey count to Trust section
3. Add link to /ziyarat/ hub
4. Specify business hours alongside the 15-minute confirmation promise

---

## Page 01 — Jeddah Airport to Makkah

**HCU Score: 91 / 100 ✅ SHIP-READY**

| Component | Score | Notes |
| --------- | ----- | ----- |
| Task completion | 25/25 | Covers: price, booking flow, terminal meeting point (Terminal 1 + Terminal 2 with exact column reference), vehicle selection, travel time by condition, Miqat stop, prayer stop, flight delay policy, FAQ. User has everything needed to book confidently |
| E-E-A-T signals | 18/20 | Source context on prices (Feb 2026 market rates) ✓, source context on travel time (Saudi Ministry of Roads, 2024) ✓, MOT permits mentioned ✓. Missing: company identity detail (operating since year, team size) |
| Content integrity | 15/15 | Precise km distance (90 km) ✓, price as range not fixed guarantee ✓, travel time given with conditions ✓, flight delay policy clearly defined (90 min free, SAR 30/hr after) ✓, Miqat presented with scholarly caveat ✓ |
| Koray rules | 14/15 | Answer-first ✓, entity in subject position ✓, EAV triples throughout ✓, source context ✓, no negative phrases ✓, positive framing ✓, lists < 7 items ✓, tables with purpose ✓. Minor: the "Pickup Instructions" H2 could be more query-intent specific ("How to Find Your Driver at King Abdulaziz Airport") |
| Conversion UX | 9/10 | CTA in first paragraph + booking fields listed ✓. Minor: WhatsApp number is a placeholder |
| Internal linking | 9/10 | Links to /booking/, /pricing/, /fleet/, /airport-transfers/, /jeddah-airport-to-madinah-taxi/ ✓. Related links at bottom ✓. Missing: link to /women-travelers-umrah-taxi/ from the "women solo travelers" FAQ answer |
| Schema readiness | 5/5 | Service + FAQPage schema viable; 6 FAQ Q&A pairs identified and in the page |

**Priority fixes before launch:**
1. Fill placeholder WhatsApp number
2. Update H2 "Pickup Instructions" → "How to Find Your Driver at King Abdulaziz Airport"
3. Add link to women travelers page (once written) in FAQ answer

---

## Page 02 — Makkah to Madinah

**HCU Score: 89 / 100 ✅ SHIP-READY**

| Component | Score | Notes |
| --------- | ----- | ----- |
| Task completion | 24/25 | Covers: price by vehicle + season, travel time by condition (including congestion at Makkah exit), prayer stop locations with names, hotel pickup rules for Haram zone, drop-off in Madinah, luggage guidance, Zamzam water guidance, Bir Ali Miqat stop, FAQ. Slight gap: does not mention what documents/confirmation the pilgrim should have ready when the driver arrives |
| E-E-A-T signals | 17/20 | Source context on prices ✓, source on route distance (Saudi MoR, 2024) ✓, named prayer stop locations (Al-Safra, Al-Hanakiyah) ✓. Missing: company identity detail |
| Content integrity | 15/15 | SAR ranges, not exact guarantees ✓, seasonal surcharge stated as % range with source ✓, route km stated (430 km) ✓, no overpromise language ✓ |
| Koray rules | 13/15 | Answer-first ✓, EAV triples ✓, source context ✓. Two issues: (1) "Best departure times" section uses instructional tone but could be framed as positive recommendation more clearly; (2) the Haram pedestrian zone pickup section could open with the entity ("Pilgrims staying in hotels within the restricted Haram perimeter…") not a description |
| Conversion UX | 9/10 | Booking fields listed ✓, CTA in opening section ✓. WhatsApp number still placeholder |
| Internal linking | 8/10 | Links to /booking/, /pricing/, /fleet/, /intercity-transfers/, /madinah-ziyarat-taxi/, /makkah-to-jeddah-taxi/ ✓. Missing: link to /how-airport-pickup-works/ from the section about Madinah Airport drop-off |
| Schema readiness | 5/5 | Service + FAQPage schema viable; 6 FAQ Q&A pairs in the page |

**Priority fixes before launch:**
1. Fill placeholder WhatsApp number
2. Reframe the Haram pickup section opening sentence to entity-first
3. Add link to /how-airport-pickup-works/ in the Madinah Airport drop-off section

---

## Page 05 — Pricing & Packages

**HCU Score: 86 / 100 ✅ SHIP-READY**

| Component | Score | Notes |
| --------- | ----- | ----- |
| Task completion | 22/25 | Covers: all major route prices, Ziyarat prices, what's included/excluded, seasonal pricing, per-vehicle vs per-seat explanation, large group pricing, how to get a quote, cancellation fee, FAQ. Gap: Coaster bus pricing for RUH routes not stated |
| E-E-A-T signals | 16/20 | Source context on prices ✓ (Feb 2026 market rates). Missing: physical business detail, company age, regulatory reference for SAR pricing |
| Content integrity | 14/15 | All prices as ranges ✓, seasonal increases stated as % ranges ✓, cancellation policy defined ✓. Minor: the "Hajj season route management checkpoints" reference in the travel time section (page 02) is repeated implicitly here — cite same source |
| Koray rules | 13/15 | Tables throughout ✓, answer-first ✓, entity-first sentences ✓. Issues: (1) the "Frequently Asked Questions" section heading is generic — rename to "Umrah Taxi Pricing FAQs"; (2) the "Can I negotiate the price" FAQ begins with "The ranges listed reflect…" — put the actual answer first: "Multi-vehicle and repeat-group bookings qualify for package discounts." |
| Conversion UX | 9/10 | Step-by-step booking flow ✓, WhatsApp CTA ✓. WhatsApp number is placeholder |
| Internal linking | 8/10 | Links to /booking/, /trust-and-policies/ ✓. Missing: links to /fleet/ from the vehicle capacity table, and to /airport-transfers/ and /intercity-transfers/ hubs |
| Schema readiness | 4/5 | Service schema viable. No FAQPage schema on this page — pricing FAQ section has 4 Q&A pairs; add FAQPage schema |

**Priority fixes before launch:**
1. Fill placeholder WhatsApp number
2. Rename FAQ heading to "Umrah Taxi Pricing FAQs"
3. Fix "Can I negotiate" FAQ — put answer first
4. Add links to /fleet/, /airport-transfers/, /intercity-transfers/
5. Add RUH route Coaster pricing

---

## Summary Table

| Page | HCU Score | Status | Critical fix |
| ---- | --------- | ------ | ------------ |
| 00 Main service page | 87/100 | ✅ Ship-ready | Fill WhatsApp number |
| 01 Jeddah Airport → Makkah | 91/100 | ✅ Ship-ready | Fill WhatsApp number |
| 02 Makkah → Madinah | 89/100 | ✅ Ship-ready | Fill WhatsApp number |
| 05 Pricing & Packages | 86/100 | ✅ Ship-ready | Fill WhatsApp number + fix FAQ opening |

**All 4 pages pass the ≥ 80 threshold. One universal blocker: the WhatsApp number placeholder must be replaced with the real number before any page goes live.**

---

## Pages Still To Write (remaining 20 briefs)

| Priority | Brief | Estimated HCU risk |
| -------- | ----- | ------------------ |
| P1 | 07-booking-contact.md | Low (straightforward) |
| P1 | 06-fleet-capacity.md | Low |
| P1 | 09-how-airport-pickup-works.md | Low (content is partially covered in page 01) |
| P2 | 10-airport-transfers-hub.md | Low |
| P2 | 11-intercity-transfers-hub.md | Low |
| P2 | 03-makkah-ziyarat.md | Medium (religious sensitivity) |
| P2 | 04-madinah-ziyarat.md | Medium (religious sensitivity) |
| P3 | 19-23 city pages (5) | Low-medium |
| P4 | 12-hajj-taxi-service.md | High (Hajj restricted zones — needs careful claims) |
| P4 | 13-18 remaining routes | Low-medium |
