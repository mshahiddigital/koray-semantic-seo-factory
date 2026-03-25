# Query Network — Online Umrah Taxi

## Cluster 1: Booking (transactional)
- book umrah taxi online
- umrah taxi booking whatsapp
- hajj taxi booking makkah
- private driver umrah taxi
- taxi service for pilgrims makkah

## Cluster 2: Airport transfers (commercial)
- jeddah airport to makkah taxi
- jeddah airport to madinah taxi
- madinah airport to makkah taxi
- airport pickup umrah taxi
- meet and greet airport transfer makkah

## Cluster 3: Intercity routes (commercial)
- makkah to madinah taxi
- makkah to jeddah taxi
- makkah to taif taxi
- jeddah to madinah taxi
- riyadh to makkah taxi

## Cluster 4: Pricing (commercial)
- umrah taxi price
- jeddah to makkah taxi fare
- makkah to madinah taxi cost
- umrah transport packages
- van taxi price for umrah

## Cluster 5: Ziyarat tours (commercial + informational)
- makkah ziyarat taxi
- madinah ziyarat taxi
- taif tour from makkah taxi
- ziyarat places in makkah with driver

## Cluster 6: Logistics & trust (informational that converts)
- how does airport pickup work in jeddah
- taxi for umrah pilgrims with luggage
- safe taxi service for women in saudi
- traveling with elderly umrah transport
- flight delay policy airport transfer

## Cluster 7: Location pages (local intent)
- umrah taxi makkah
- umrah taxi madinah
- umrah taxi jeddah
- umrah taxi taif
- umrah taxi riyadh

---

## Intent → page mapping rules
- If query includes a **route** (X to Y): route page (and link to booking + pricing)
- If query includes **airport**: airport route or airport hub; add meeting-point section
- If query includes **price/fare/cost**: pricing hub + embedded estimator; link back to relevant route pages
- If query includes **ziyarat**: ziyarat pages with itinerary + time blocks; link to booking
- If query includes **city only**: city service page; link to route hub(s)

---

## Suggested seed list file
Use `scripts/seed-queries.csv` if you later want to run `python-backend/query_clusterer.py`.
