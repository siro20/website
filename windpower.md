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

For a real fast running wind turbine the rotor coefficient is
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

