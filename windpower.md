# Harvesting energy from wind


## Math
In 2014 a wind sensor was installed and measured the winespeed for almost
 month.

The power that wind flowing through an rotor carries can be calculated as
```eval_rst
:math:`P = \frac{1}{2} A \rho v^3`
```

where
```eval_rst
:math:`A` is the rotor area,

:math:`\rho \approx 1.2041 \frac{kg}{m^3}` is the air density,

:math:`v` the speed of the wind.
```

According to Betz Law, the rotor coefficient is always less than
```eval_rst
:math:`c_{betz} < \frac{16}{27}` .
```

For a real fast-running wind turbine the rotor coefficient is
```eval_rst
:math:`c_{rotor} = 0.45` .
```

Assuming the generator and power converter have a combined efficiency of
```eval_rst
:math:`c_{generator} = 0.95`
```
then, the maximum electrical energy that can be harvested is:

```eval_rst
:math:`P_{electr} = \frac{1}{2} A \rho v^3 c_{rotor} c_{generator} \approx 0.26 A v^3`
```

## Measuring the wind distribution
To find out how much energy one could harvest you have to measure the wind over a long
time frame. The windsensor was positioned near the house, which isn't a good place !

Place it in the open field to get better results!

![][Eltako-WS-Sensor-small]

[Eltako-WS-Sensor-small]: Eltako-WS-Sensor-small.jpg

## Wind histogram

The histogram was made out of 11531906 samples, sampled at 1Hz.
That are about 133 days.

Half of the time there was zero wind (not shown in the chart).

![][windspeed_histogram]

[windspeed_histogram]: windspeed_histogram.svg


Converting the windspeed and occurence to kW/h, assuming 1qm of rotor area at 25°C.

![][windspeed_power]

[windspeed_power]: windspeed_power.svg

As you can see the most energy can be harvested between 2 m/s and 13 m/s windspeed.
From the above chart you see that 13 m/s is very unlikely and a significant amount
of energy is produced in a very short time.

## Total power

Over the whole measuring period, with one square meter of rotor area, the rotor
would have seen a total wind power of

```eval_rst
:math:`P_{wind} = 56.6 KWh` .
```

Due to betz law and the losses in the generator and inverter the electrical power
produced in one year would be:

```eval_rst
:math:`P_{electr} = P_{wind} c_{rotor} c_{generator} \frac{365}{133} \approx 66.4 kWh` .
```

## Operating area
The inverter needs to power itself from wind turbine. To use common technology, that
is available on the market, the generator would have a maximum voltage of 240Vac.

We could use an ATX power supply, with secondary side power regulation, to power
12V battery/lamps. It would measure the windspeed and regulate the load on the
12V rail.

Thoose ATX power supplies usually operates from 80Vac to 240Vac. As windspeed,
rotor RPMs and voltage on the generator are linear coupled, the inverter operating
region sets also the limits for the windspeed.

We choose 80Vac to 240Vac (3m/s to 12m/s) to be the operating region.

As we cannot use the power of windspeed below 3m/s and beyond 12m/s, a new
coefficient is introduced. The operating region coefficient is about 80% of
the total power seen in the histogram.

```eval_rst
:math:`c_{op} = 0.8` .
```

With the new coefficient the estimated electrical power in one year would be:

```eval_rst
:math:`P_{electr} = P_{wind} c_{rotor} c_{generator} c_{op} \frac{365}{133} \approx 53.1 kWh` .
```

## Wind continuity
The histogram shows that the windspeed was between 3m/s and 12m/s for *1804288* seconds,
over a sampling period of *11531906* seconds. That's

```eval_rst
:math:`\frac{1804288}{11531906} = 15.6 \%` of the time.
```

The energy is produced only on one day a week. The spot close to the house isn't
good to install a wind turbine.
