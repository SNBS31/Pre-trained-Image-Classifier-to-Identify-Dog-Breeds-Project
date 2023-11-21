## The current volume of our water resevoir(m**3)
resevoir_volume = 4.445e8
## The amount of rainfall from a storm(m**3)
rainfall = 5e6
## Decrease in the rainfall by 10%, so as to account of runnoff
rainfall *= 0.9
## Now adding our rainfall to our resevoir volume,
resevoir_volume += rainfall
## Now adding resevoir_volume by 5%, for the storm water flow
#  during storms within the days
resevoir_volume *= 1.05
## Decrease in resevoir_volume by 5% to account for evaporation
resevoir_volume *= 0.95
## Subtracting 2.5e5 cubic metres from the resevoir_volume to account
#  for the water piped to arid regions.
resevoir_volume -= 2.5e5