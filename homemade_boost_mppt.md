# Homemade PV panel boost converter with MPPT

This site is about building a homemade PV panel boost converter.
The schematics can be found on [GitHub].

## Index

* [market analysis]

## Market analysis

The [market analysis] shows the overal used voltage and current on currently
available PV panels. The homemade PV boost converter should cover
about 90% of the panels available. The study showed that modules in the range
of 200W-300W with 40Voc should be used.

As telecom power supply usually operate on 48V, those can be used as reference
design.

## Output voltage

The SMPS should output a voltage that can be used to drive arbitrary SMPS in
the household. I first thought about using 400VDC, to be able to connect
DC-AC sine inverter to AC mains, but a voltage of 240VDC would allow the use
of resistive consumers, like heatings, too.

As design choice the MPPT should generate 240VDC.

Feeding power back to AC main grid can still be achieved using series
connection of the SMPS outputs, which would result in 480VDC.

## SMPS converter choice
As the output voltage is way higher than the input voltage, galvanic isolation
should be used to prevent damage to the panel on failing parts (like a boost
diode).

It also might be desireable to completly shutdown the SMPS, which isn't possible
for a boost converter design.

Using a Push-Pull approach, which is galvanic isolated, also reduces the
input current ripple, compared to a boost converter, and thus reduces EMI.


[market analysis]: market_study.md
[GitHub]: https://github.com/siro20/mppt


