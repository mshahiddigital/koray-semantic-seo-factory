# Brief: Frequently Asked Questions — Online Umrah Taxi

**Slug:** `/faq`
**Schema:** FAQPage | BreadcrumbList
**Phase:** P1 — launch-critical
**Primary query:** umrah taxi faq
**Word count target:** 1,800–2,200

---

## Central Entity

Online Umrah Taxi FAQ page — comprehensive answers to every pilgrim question about booking, pricing, routes, vehicle capacity, delays, cancellation, and safety for Umrah and Hajj taxi services in Saudi Arabia.

---

## Page Purpose

This page aggregates every high-frequency pilgrim question that route pages and outer guides cannot individually host. It serves as a trust anchor, an FAQ schema rich-result source, and a sitewide authority signal. Every question cluster must link back to the relevant core money page.

---

## EAV Triples (minimum 12)

| Entity | Attribute | Value | Source |
| ------ | --------- | ----- | ------ |
| Umrah taxi booking | Confirmation time | Within 15 minutes (business hours) / 60 minutes (overnight) | Business policy, February 2026 |
| Airport pickup waiting time | Free waiting period | 90 minutes after actual landing | Business policy, February 2026 |
| Umrah taxi pricing | Basis | Per vehicle, not per person | Business policy, February 2026 |
| Sedan taxi | Passenger capacity | 1–3 passengers, 2 large suitcases | Vehicle specification |
| SUV/MPV taxi | Passenger capacity | 4–6 passengers, 4 large suitcases | Vehicle specification |
| Toyota Hiace van | Passenger capacity | 7–9 passengers, 6 large suitcases | Vehicle specification |
| Cancellation policy | Free cancellation window | 48 hours or more before pickup | Business policy, February 2026 |
| Cancellation fee | Within 48 hours | 50% of quoted fare | Business policy, February 2026 |
| No-show fee | On the day of travel | Full fare charged | Business policy, February 2026 |
| Miqat stop | Availability | Available on request at booking; adds 20–30 minutes | Business policy, February 2026 |
| Driver language | Available languages | English, Arabic, Urdu | Service specification, February 2026 |
| Flight delay policy | Delay under 90 minutes | No additional charge; driver waits | Business policy, February 2026 |
| Zamzam water | Transport policy | Permitted in all vehicle types within standard luggage allowance | Business policy, February 2026 |
| Women travelers | Solo travel | Permitted; uniformed drivers; female companion available on request | Business policy, February 2026 |

---

## Query Clusters Addressed

Each cluster should map to an H2 section:

1. **Pricing & payment** — How much? Per person or per vehicle? What's included? Seasonal increases?
2. **Booking process** — How to book? How fast is confirmation? WhatsApp or form?
3. **Airport pickup** — Where does the driver meet me? What if my flight is delayed?
4. **Route & journey** — How long does it take? Can I make stops?
5. **Vehicle & capacity** — Which vehicle fits my group? Can I bring Zamzam?
6. **Cancellation & changes** — Can I cancel? What if my travel dates change?
7. **Special travelers** — Women solo, elderly, wheelchair users
8. **Religious & operational** — Miqat stop, prayer times, Haram zone pickup

---

## Paragraph Function Map

| Section | Function |
| ------- | -------- |
| Opening paragraph | State entity + macro purpose: this page answers the most common questions pilgrims ask before booking |
| Pricing cluster | Claim (per vehicle) → Evidence (sedan SAR 240–350, SUV SAR 350–480) → Implication (group of 5 in SUV pays SUV rate, not 5 fares) |
| Airport pickup cluster | Claim (driver meets you at arrivals hall) → Evidence (Terminal 1 international, Terminal 2 domestic; WhatsApp location share) → Implication (no waiting outside in heat) |
| Cancellation cluster | Claim (48-hour free window) → Evidence (50% within 48h, full no-show) → Implication (book early; cancel with notice if plans change) |
| Women + elderly cluster | Claim (safe, professional service) → Evidence (uniformed drivers, female companion option, Hiace wheelchair space) → Implication (specify requirements at booking) |

---

## Internal Links Required

| Anchor text | Destination |
| ----------- | ----------- |
| Pricing & Packages | `/pricing` |
| Airport Transfers | `/airport-transfers` |
| Inter-City Transfers | `/inter-city-transfers` |
| Vehicle Fleet | `/vehicle-fleet` |
| Contact Us | `/contact-us` |
| Female-Friendly Umrah Taxi | `/female-friendly-umrah-taxi` |
| Meeqat & Ihram Transfer Guide | `/meeqat-ihram-transfer-guide` |

---

## Schema

FAQPage with one Question/Answer pair per question in the page body. Every question visible on the page must appear in FAQPage schema. BreadcrumbList: Home → FAQ.

---

## Koray Writing Rules (key rules for this page)

- **Rule 1:** Answer first in every FAQ answer — state the direct answer in the opening sentence
- **Rule 4:** Use numeric qualifiers (90 minutes, 48 hours, SAR 240–350) in every answer containing a quantity
- **Rule 10:** Bold the answer, not the question keyword
- **Rule 16:** Each answer must be self-contained — readable without the question for passage ranking
- **Rule 24:** No overpromising — use "up to 90 minutes" not "we always wait"
- **Rule 26:** If using a list of included items, cap at 7 items with a purpose sentence introduction
