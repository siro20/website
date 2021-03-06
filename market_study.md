# Homemade PV panel boost converter with MPPT

## Market analysis
List of currently available PV panels and it's maximum ratings.

```eval_rst
+-------------------------+----------+------+------+
| Name                    | Power    | Voc  |  Isc |
+-------------------------+----------+------+------+
| SolarFabrik 270Wp       | 270      | 38.5 | 9.25 |
+-------------------------+----------+------+------+
| Winaico WST-M6 PERC     | 310      | 40.2 | 10.0 |
+-------------------------+----------+------+------+
| SunPower 360W MAXEON 2  | 360      | 70.0 | 6.5  |
+-------------------------+----------+------+------+
| Panasonic VBHN 275 SJ46 | 275      | 38.2 | 9.3  |
+-------------------------+----------+------+------+
| Q.cells Q.peak-G5.1     | 310      | 40.3 | 9.33 |
+-------------------------+----------+------+------+
| GreenAkku ETFE          | 150      | 21.5 | 8.7  |
+-------------------------+----------+------+------+
| NoName 275W             | 275      | 39.1 | 9.1  |
+-------------------------+----------+------+------+
| BISOL BMO-360 XL        | 360      | 47.2 | 9.65 |
+-------------------------+----------+------+------+
| Panasonic VBHN 245 SJ25 | 245      | 53.0 | 5.86 |
+-------------------------+----------+------+------+
| BISOL BMO-265 transpar. | 265      | 34.7 | 9.2  |
+-------------------------+----------+------+------+
| Luxor ECO LINE M72 LX   | 200      | 36.4 | 5.8  |
+-------------------------+----------+------+------+
| ECO-WORTHY 100W Poly PV | 100      | 22.4 | 6.2  |
+-------------------------+----------+------+------+
| 160W 160-12 NoName PV   | 160      | 22.9 | 8.8  |
+-------------------------+----------+------+------+
| PANASONIC VBHN 325 SJ47 | 325      | 69   | 6.0  |
+-------------------------+----------+------+------+
```

## Graphical representation

![Graphical representation of above table](market_study_VW.png)

## Result
1. Modules below 200W have a low open collector voltage of 22V.
2. Modules between 200W and 300W have a voltage of around 40V.
3. Modules starting at 250W have a very high open collector voltage of 70V.

As power converters above 300W are difficult to build, and modules below
200W aren't worth attaching an expensive converter, the MPPT boost converter
will target 40V open collector voltage modules.
